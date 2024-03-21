# GIHP: Graph convolutional neural network based Interpretable pan-specific Hla-Peptide binding affinity prediction

## Framework
![Overall Framework of GIHP](https://github.com/sdustSu/GIHP/blob/main/Framework.jpg?raw=true)


## Requirements  

matplotlib==3.2.2  
pandas==1.2.4  
torch_geometric==1.7.0  
CairoSVG==2.5.2  
torch==1.7.1  
tqdm==4.51.0  
opencv_python==4.5.1.48  
networkx==2.5.1  
numpy==1.20.1  
ipython==7.24.1  
rdkit==2009.Q1-1  
scikit_learn==0.24.2  


## Step-by-step running:  

### 1. Train/test GIHP

#### 1.1 filtered_davis folder

- First, cd MGraphDTA/filtered_davis, and run preprocessing.py using  
  `python preprocessing.py`  

  Running preprocessing.py convert the raw data into graph format.

- Second, run train.py using 
  `python train.py --fold 0 --save_model` 

  to train MGraphDTA. The training record can be found in save/ folder.

  Explanation of parameters

  - --fold: k-th fold, from 0 to 4
  - --save_model: whether save model or not
  - --lr: learning rate, default =  5e-4
  - --batch_size: default = 512

- To test a trained model please run test.py using

  `python test.py --model_path model_path`

  This will return the RMSE, CI, and  Spearm performance in the test set.

  For example, running

  `python test.py --model_path '/home/yang/project/MGraphDTA/filtered_davis/save/20211127_040602_filtered_davis/model/epoch-149, loss-0.1245, cindex-0.9016, test_loss-0.4863.pt'`

  will output results as follows

  `Reading fold_0 from data/filtered_davis
  test_rmse:0.6973, test_cindex:0.7438, test_spearm:0.6642`

* To train MGraphDTA in your own datasets, please organize your data as the format shown in data/filtered_davis/raw/data.csv and provide a data/filtered_davis/warm.kfold file to describle the train/val/test split index.



### Visualization using Grad-WAM


- First, copy you own data into MGraphDTA/visualization/data.  
- Second, cd GIHP/visualization, and run preprocessing.py using  
  `python preprocessing.py`  
- Third, run visualization_wam.py using  
  `python visualization_wam.py`  
If you want to test Grad-WAM in your own model, please replace this pre-trained model with your own one and modify the path in the visualization_wam.py file.

