# Algorithms in structural bioinformatics

__Machine learning methods to analyze and predict protein structure, dynamics and function__

## Exercise material for the practical afternoon session on Monday, 8th of November 2021

The content of this exercise aligns with the morning lecture "Learning models of complex dynamics from simulation data" held by Bettina Keller.

## Requirements

The exercise will make use of [Jupyter](https://jupyter.org/) notebooks and requires (a recent version of) the following Python packages:

   - matplotlib
   - numpy
   - scipy
   - sklearn
   - pyemma
   - nglview
   - cnnclustering

We recommend to use a Python 3.8 based (virtual) environment for this
exercise. Using [conda](https://www.anaconda.com/products/individual)
maybe the easiest solution here.

If you want to read up on Python virtual environments, you could start with [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/).

### conda

If you use conda, a ready to use conda virtual environment with all the requirements installed can be created using the provided `environment.yml` file:

```bash
conda env create -f environment.yml
```

Then activate the new environment:

```bash
conda activate AlgoSB
```

This is equivalent to a manual creation of a fresh environment
followed by an installation of the needed packages:

```bash
conda create --name AlgoSB python=3.8 -y
conda activate AlgoSB
conda install matplotlib numpy scipy scikit-learn pyemma nglview -c conda-forge
```

Please note that the `cnnclustering` package is only available on PyPi:

```bash
pip install cnnclustering
```

or directly from the [development repository on GitHub](https://github.com/janjoswig/CommonNNClustering):

```bash
git clone https://github.com/janjoswig/CommonNNClustering.git
cd CommonNNClustering
pip install .
```

### pip

If you genrally prefer pip over conda to manage packages, you can instead install all requirements from the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```
Please note, that the installation of `pyemma` via pip can be sometimes [problematic](http://www.emma-project.org/latest/INSTALL.html), though.

### Google Colab

If you like to use the notebook in Colab, consider installing the requirements via `condacolab`. Open the notebook in Colab and add the following:

```bash
!pip install -q condacolab
import condacolab
condacolab.install()
```

Then install only the still missing dependencies:

```bash
!conda install pyemma nglview -c conda-forge
!pip install cnnclustering
```

