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

# Executing MOGDx
MOGDx can be executed either by running the `MOGDx.py` module on the command line, or interactively using the `MOGDx.ipynb` Jupyter Notebook. 

## Jupyter Notebook
The Jupyter Notebook is designed to train one model on a single network. This is a useful tool to become accustomed to the running, training and expected outputs of the model. It is also useful for debugging any small errors with network generation e.g. missing patient nodes or patient nodes with no edges. 

## Command Line
The command line interface is a single line command designed for execution on a cluster. The command can be run on either GPU or CPU and is designed for hyperparameter tuning, and flexible modalitiy integration. The command will train one model, with one set of parameters on a single network. The command is designed to be run concurrently with results formatted in an easy to read method so that the optimal model can be quickly distinguished. 