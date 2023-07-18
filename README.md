## Installation guide

Create a conda environment using:

```
conda env create -f environment.yml
```

Activate the conda environment using:

```
conda activate mGRU_CP
```

## Data Availability

The original dataset is available at https://data-dictionary.regenstrief.org/iadc/catalog/showDataset/REGENSTRIEF%20DATA%20RESOURCES/7. However, in order to get access to the data, researchers need to submit a data request through https://www.regenstrief.org/data-request/ at Regenstrief Institute. 

Therefore here we provide a script to generate sample dummy data that looks like the original data.

Use this code to generate the sample data:

```
python data_generator.py

```
## Training and testing the model

The script.py file contains code for training and testing the model. 

```
python ./script.py --batch-size 100 --hidden-dims 20 --num-layers 3 --dropout 0 --lr 0.01 --epochs 50 --exp-no 1 --k 2

'''



