Create the conda environment using:
conda env create -f environment.yml
Create sample dataset using:
python data_generator.py
Run the model using:
python ./script.py --batch-size 100 --hidden-dims 20 --num-layers 3 --dropout 0 --lr 0.01 --epochs 50 --exp-no 1 --k 2
