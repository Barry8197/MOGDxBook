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
# Processing in R

## Step 1 - Preprocessing
Create a folder called for the dataset e.g. TCGA, and within this folder create a folder for each project.

Run the R script `Preprocessing.R` specifying the phenotypical trait and project, checking to ensure the paths point to the created `data` folder. 

Save each modalities processed folder with naming convention `modality_processed.RData`.

The options are \
BRCA : \
project = 'BRCA' \
trait = 'paper_paper_BRCA_Subtype_PAM50' 

LGG : \
project = 'LGG' \
trait = 'paper_Grade' 

KIPAN :  \
project = 'KIPAN' \
trait = 'subtype' 

## Step 2 - Graph Generation
Point the knn_graph_generation.R to the project folder containing the processed modalities.

Create a folder called raw. This is the folder from which MOGDx will be run.

Use the R script `knn_graph_generation.R` specifying the phenotypical trait, project and modalities downloaded in the for loop.

## Step 3 - SNF
Create a folder called Network outside data \
Copy each modalities `modality_graph.csv` to this folder \

Specify the modalities of interest in the list `mod_list` 

Point the SNF script to the new Network folder

Run the R script `SNF.R` 

## Example of directory structure for TCGA
- data
  - TCGA-BRCA
     - mRNA
       - mRNA.rda
     - miRNA
       - miRNA.rda
    - processed
      - mRNA_processed.RData
      - miRNA_processed.RData
  - raw
    - datExpr_mRNA.csv
    - datMeta_mRNA.csv
    - datExpr_miRNA.csv
    - datMeta_miRNA.csv
  - Network
    - mRNA_graph.csv
    - miRNA_graph.csv
    - mRNA_miRNA_graph.csv
