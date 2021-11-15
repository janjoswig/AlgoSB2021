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

We recommend to use a Python 3.8 based virtual environment for this exercise, e.g. managed by [conda](https://www.anaconda.com/products/individual). Create an environment like this:

`conda create --name AlgoSB python=3.8 -y`

Then activate your virtual environment:

`conda activate AlgoSB`.

Install the requirements:

`conda install matplotlib numpy scipy scikit-learn pyemma`

Please note that the `cnnclustering` package is only available on PyPi:

`pip install cnnclustering`

or directly from the [development repository on GitHub](https://github.com/janjoswig/CommonNNClustering):

`git clone https://github.com/janjoswig/CommonNNClustering.git`

`cd CommonNNClustering`

`pip install .`

You can also create a ready to use conda virtual environment with all the requirements installed using the provided `environment.yml` file:

`conda env create -f environment.yml`

If you prefer pip over conda to manage packages, you can instead install all requirements from the provided `requirements.txt` file:

`pip install -r requirements.txt`

If you want to read up on Python virtual environments, you could start with [Python Virtual Environments: A Primer](https://realpython.com/python-virtual-environments-a-primer/).
