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

# Processing in Python
These files provide the steps for extracting informative features of each modality, generating a network per modality and performing Similarity Network Fusion (SNF). 

Prior to performing processing in python, each modality is required to be saved in the format `{modality}_preprocessed.pkl`. See [GettingStarted](./GettingStarted.md) for more. 

## Step 1 - Preprocessing
Create a folder called for the dataset called `data` and within this folder copy the preprocessed data into a folder name e.g. TCGA-BRCA.

Run `Preprocessing.ipynb` for each modality of interest. There are two options for the feature extraction at this stage. Either differential gene expression or elastic net regression. 

Save each modalities processed folder with naming convention `{modality}_processed.pkl` in the `data/raw`
Save each network with naming convention `{modality}_graph.graphml` in the `data/Network` folder

The options are \
BRCA : \
target = 'paper_paper_BRCA_Subtype_PAM50' 

LGG : \
target = 'paper_Grade' 

KIPAN :  \
target = 'subtype' 

## Step 2 - Similarity Network Fusion
Create a folder called Network outside data \

Specify the modalities of interest in the list `modalities` 

Point the SNF script to the new Network folder

Run the cell to perofrm SNF for the modalities of interest. 

## Example of directory structure for TCGA-BRCA
- data
  - TCGA-BRCA
     - mRNA
       - mRNA.pkl
     - miRNA
       - miRNA.pkl
  - raw
    - mRNA_processed.pkl
    - miRNA_processed.pkl
  - Network
    - mRNA_graph.graphml
    - miRNA_graph.graphml
    - mRNA_miRNA_graph.graphml
