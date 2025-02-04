---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# MOGDx Main Functions and Classes
We provide a description of the main functions and classes used to train a MOGDx model. 

## Graph Neural Network with Multi Modal Encoder (GNN-MME)
The GNN-MME is the main component in the architecture of MOGDx. It consists of a Multi-Modal Encoder (MME) to reduce the dimension of the input modalities and decodes all modalities to a shared latent space. 

Along with the MME there is a Graph Neural Network (GNN). Currently there are two GNN's implemented ; Graph Convolutional Network (GCN) for applications in the transductive setting and GraphSage for applications in the inductive setting. Both algorithms are implemented using the Deep Graph Library ([DGL](https://www.dgl.ai/)). 

```{image} ./images/gcn-mme.png
:alt: fishy
:width: 1200px
:align: left
```

### Multi Modal Encoder
The MME takes any number of modalities and compresses them to an arbitrary dimension, found through hyperparameter searching. The architecture for the MME has been established in similar research in {cite:p}`yang_subtype-gan_2021` and {cite:p}`xu_hierarchical_2019`. 

### Graph Convolutional Network (GCN)
GCN, developed by {cite:p}`kipf_semi-supervised_2017`, was implemented from the DGL. For a tutorial on the use of GCN's we refer you to the [DGL Tutorial Page](https://docs.dgl.ai/en/1.1.x/tutorials/blitz/1_introduction.html#sphx-glr-tutorials-blitz-1-introduction-py)

```{image} ./images/gcn.png
:alt: fishy
:width: 1200px
:align: left
```

### GraphSage
GraphSage, developed by {cite:p}`hamilton_inductive_2017`, was implemented from the DGL. For a tutorial on the use of GraphSage we refer you to the [DGL Tutorial Page](https://docs.dgl.ai/en/0.8.x/tutorials/blitz/4_link_predict.html)

```{image} ./images/gsage.png
:alt: fishy
:width: 1200px
:align: left
```

## Training
Functions used to train and evaluate the MOGDx model. The training implemented follows that outlined by {cite:p}`hamilton_graph_2020`.

The list of functions are : 
- train
- evaluate
- confusion_matrix
- AUROC

## Utility
Utility functions used to parse input data, load networks from csv or perform utility tasks. 

The list of functions are : 
- data_parsing_python
- data_parsing_R
- get_gpu_memory
- indices_removal_adjust
- network_from_csv

## Citations
```{bibliography}
:filter: docname in docnames
```
