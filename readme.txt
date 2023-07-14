conda env create -f environment.yml
python data_generator.py
python ./script.py --batch-size 100 --hidden-dims 20 --num-layers 3 --dropout 0 --lr 0.01 --epochs 200 --exp-no 1 --k 2
