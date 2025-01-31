# Getting Started

## Introduction
Multi-omic Graph Diagnosis (MOGDx) is a tool for the integration of omic data and classification of heterogeneous diseases. MOGDx exploits a Patient Similarity Network (PSN) framework to integrate omic data using Similarity Network Fusion (SNF) {cite:p}`wang_similarity_2014`. A single PSN is built per modality. The PSN is built using the most informative features of that modality. The most informative features are found by performing a contrastive analysis between classification targets. For example, in mRNA, differentially expressed genes will be used to construct the PSN. Where suitable, Pearson correlation, otherwise Euclidean distance is measured between these informative features and the network is constructed using the K Nearest Neighbours (KNN) algorithm. SNF is used to combine individual PSN's into a single network. The fused PSN and the omic datasets are input into the Graph Convultional Network with Multi Modal Encoder, the architecture of which is shown in below. Each omic measure is compressed using a two layer encoder. The compressed encoded layer of each modality is then decoded to a shared latent space using mean pooling. This encourages each modality to learn the same latent space. The shared latent space is the node feature matrix, required for training the GCN, with each row forming a node feature vector. Classification is performed on the fused network using the Graph Convolutional Network (GCN) deep learning algorithm {cite:p}`kipf_semi-supervised_2017`. 

GCN is a novel paradigm for learning from both network structure and node features. Heterogeneity in diseases confounds clinical trials, treatments, genetic association and more. Accurate stratification of these diseases is therefore critical to optimize treatment strategies for patients with heterogeneous diseases. Previous research has shown that accurate classification of heterogenous diseases has been achieved by integrating and classifying multi-omic data {cite:p}`pai_netdx_2019,li_mogcn_2022,wang_mogonet_2021`. MOGDx improves upon this research. The advantages of MOGDx is that it can handle both a variable number of modalities and missing patient data in one or more modalities. Performance of MOGDx was benchmarked on the BRCA TCGA dataset with competitive performance compared to its counterparts. In summary, MOGDx combines patient similarity network integration with graph neural network learning for accurate disease classification. 

## Installation
A working version of R and Python is required. R version 4.2.2 and Python version 3.9.2 was used to obtain all results.

## Data Download
Create a folder called `data` and a folder for each dataset with naming convention 'TCGA-' e.g. 'TCGA-BRCA' inside this folder.

Use the R script `data_download.R` to download all data changing the project to BRCA/LGG/KICH/KIRC/KICH

Note : To create the KIPAN dataset, the KIRC, KICP and KICH datasets have to be combined. This can be achieved by copying the downloaded files 
from all three seperate datasets into a single dataset called KIPAN keeping the same naming structures. A column named 'subtype' specifying which dataset
the patient came from needs to be created in the Meta data file. A basic knowledge of R is required for this. 

## Accessing the data in Python
The downloaded data in its raw format will be in `.rda` format. It will be required to convert from this format to `.pkl` for processing in python. 

It is recommended to use the [pyreadr](https://pypi.org/project/pyreadr/) python package to do so and saving the preprocessed file with naming convention `{modality}_preprocessed.pkl`

## Citations
```{bibliography}
:filter: docname in docnames
```
