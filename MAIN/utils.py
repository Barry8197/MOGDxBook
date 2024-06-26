import pandas as pd
import numpy as np
import torch
import os
import pickle
import networkx as nx

def data_parsing_R(DATA_PATH , MODALITIES ,TARGET , INDEX_COL) :
    """
    Parse data from multiple modalities and return the parsed data along with metadata.

    Args:
        DATA_PATH (str): The path to the data.
        MODALITIES (list): A list of modalities to be processed.
        TARGET (str): The target variable.
        INDEX_COL (str): The column to be used as the index.

    Returns:
        tuple: A tuple containing the parsed data for each modality and the metadata.
    """

    try : 
        META_DATA_PATH = [f'{DATA_PATH}/datMeta_{mod}.csv' for mod in MODALITIES]
    except : 
        print(f'Modalities listed not found in data path {DATA_PATH}')

    meta = pd.Series(dtype=str)
    for path in META_DATA_PATH : 
        meta_tmp = pd.read_csv(path , index_col=0)
        
        if INDEX_COL == '' :
            pass
        else :
            meta_tmp = meta_tmp.set_index(INDEX_COL)
            
        meta = pd.concat([meta , meta_tmp[TARGET]])

    meta = meta[~meta.index.duplicated(keep='first')] # Remove duplicated entries
    meta.index = [str(i) for i in meta.index] # Ensures the patient ids are strings

    try :
        TRAIN_DATA_PATH = [f'{DATA_PATH}/datExpr_{mod}.csv' for mod in MODALITIES] # Looks for all expr file names
    except : 
        print(f'Modalities listed not found in data path {DATA_PATH}')

    datModalities = {}
    for path in TRAIN_DATA_PATH : 
        print('Importing \t %s \n' % path)
        
        try : 
            dattmp = np.genfromtxt(path , delimiter=',' , dtype = str)
            if len(set(meta.index.astype(str)) & set(np.core.defchararray.strip(dattmp[1: , 0], '"'))) > 0 :
                dattmp = pd.DataFrame(dattmp[1: , 1:] , columns=np.core.defchararray.strip(dattmp[0 ,1:], '"') , index = [int(i.strip('"')) for i in dattmp[1: , 0]])
            else : 
                dattmp = pd.DataFrame(dattmp[1: , 1:] , columns=[int(i.strip('"')) for i in dattmp[0,1:]] , index = np.core.defchararray.strip(dattmp[1: , 0], '"'))
                dattmp = dattmp.T
        except : 
            dattmp = pd.read_csv(path , index_col=0)
            if len(set(meta.index) & set(dattmp.columns)) > 0 :
                dattmp = dattmp.T
                
        dattmp.index = [str(i) for i in dattmp.index] # Ensures the patient ids are strings
        dattmp.name = path.split('/')[-1].split('_')[-1][:-4] #Assumes there is no '.' in file name as per specified naming convention. Can lead to erros down stream. Files should be modality_datEXpr.csv e.g. mRNA_datExpr.csv
        datModalities[dattmp.name] = dattmp

    return datModalities , meta

def data_parsing_python(DATA_PATH , MODALITIES ,TARGET , INDEX_COL) :
    """
    Parse data from multiple modalities and return the parsed data along with metadata.

    Args:
        DATA_PATH (str): The path to the data.
        MODALITIES (list): A list of modalities to be processed.
        TARGET (str): The target variable.
        INDEX_COL (str): The column to be used as the index.

    Returns:
        tuple: A tuple containing the parsed data for each modality and the metadata.
    """

    datModalities = {}
    for i, mod in enumerate(modalities) : 
        try : 
            with open(f'{DATA_PATH}/{mod}_processed.pkl' , 'rb') as file : 
                loaded_data = pickle.load(file)
        except : 
            print(f'Modalities listed not found in data path {DATA_PATH}')

            
        if i == 0 : 
            datMeta = loaded_data['datMeta'].reset_index()[[INDEX_COL , TARGET]]
        else : 
            datMeta = pd.merge(datMeta , loaded_data['datMeta'].reset_index()[[INDEX_COL , TARGET]] , how = 'outer' , on = [INDEX_COL , TARGET] )
         
        datExpr = loaded_data['datExpr']
        if len(set(datExpr.index.astype(str)) & set(datMeta[INDEX_COL])) == 0 : 
            datExpr = datExpr.T
            
        if datExpr.isna().sum().sum() > 0 : 
            datExpr = datExpr.fillna(datExpr.mean())
        
        datModalities[mod] = datExpr.loc[sorted(datExpr.index)]
        
        meta = datMeta.set_index(INDEX_COL)[TARGET]

    return datModalities , meta

def get_gpu_memory():
    """
    Returns the total, reserved, and allocated GPU memory in gigabytes.
    
    Returns:
        Print statement with the total, reserved, and allocated GPU memory.
    """
    t = torch.cuda.get_device_properties(0).total_memory*(1*10**-9)             
    r = torch.cuda.memory_reserved(0)*(1*10**-9)
    a = torch.cuda.memory_allocated(0)*(1*10**-9)
    
    return print("Total = %1.1fGb \t Reserved = %1.1fGb \t Allocated = %1.1fGb" % (t,r,a))

def indices_removal_adjust(idx_to_swap, all_idx, new_idx):
    """
    Adjusts the indices based on the given parameters.

    Args:
        idx_to_swap (array-like): The indices to be swapped.
        all_idx (pandas.Series): All the indices.
        new_idx (array-like): The new indices.

    Returns:
        numpy.ndarray: The adjusted indices.

    """
    update_idx = all_idx[all_idx.isin(new_idx)].reset_index()['index']
    
    update_idx_swap = pd.Series(update_idx.index , index=update_idx.values)
    
    return update_idx_swap[list(set(update_idx) & set(idx_to_swap))].values
    

def network_from_csv(NETWORK_PATH, no_psn, weighted=False):
    '''
    Generate a networkx network from a as_long_data_frame() object from igraph in R.

    Args:
        NETWORK_PATH (str): The path to the CSV file containing the network data.
        no_psn (bool): If True, the function will not add any edges to the network.
        weighted (bool): If True, the function will add weighted edges to the network based on the 'weight' column in the CSV file.

    Returns:
        G (networkx.Graph): The networkx Graph object representing the network.

    '''

    # Open csv as pandas dataframe
    network = pd.read_csv(NETWORK_PATH, index_col=0)

    # Obtain node names (ids) and numbers
    node_from = network[['from', 'from_name']]
    node_from.columns = ['node', 'id']

    node_to = network[['to', 'to_name']]
    node_to.columns = ['node', 'id']

    # Create networkx Graph object and add nodes to network 
    G = nx.Graph()

    # Add nodes to Graph object, resetting index to begin from 0
    nodes = pd.concat([node_from, node_to]).drop_duplicates().reset_index(drop=True)
    nodes['id'] = [str(i) for i in nodes['id']] # Convert node names to strings

    G.add_nodes_from(nodes['id'])

    nx.set_node_attributes(G, nodes.reset_index().set_index('id')['index'], 'idx')

    # Add edges and weights (if applicable to network)
    edges = []
    if weighted == True:
        for edge1, edge2, weight in zip(network['from'], network['to'], network['weight']):
            edges.append((nodes[nodes['node'] == edge1].index[0], nodes[nodes['node'] == edge2].index[0], weight))

        G.add_weighted_edges_from(edges)
    elif no_psn == True:
        pass
    else:
        for edge1, edge2 in zip(network['from_name'], network['to_name']):
            edges.append((nodes[nodes['id'] == edge1]['id'].iloc[0], nodes[nodes['id'] == edge2]['id'].iloc[0]))

        G.add_edges_from(edges)

    return G
