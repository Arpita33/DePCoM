import random
import os
import numpy as np
from sklearn.model_selection import KFold
import os
import shutil

demog_array = ['Gender', 'Race', 'Ethnicity','Age']
variable_array = ['HCT', 'WBC_NUM', 'BUN', 'CREAT', 'PLT', 'HGB',
       'BIL_TOT', 'ALT', 'ALKP', 'PROT_TOT', 'ALB_SER', 'AST',
       'FIBR', 'LDH', 'PROCALC', 'FERR', 'LYMPH_NUM', 'LYMPH_PERC',
       'BIL_DIR', 'Troponin T', 'LAC_SER', 'INR', 'PT', 'CK', 'CRP',
       'D-Dimer FEU', 'ESR', 'CRP_S', 'D-Dimer DDU', 'aPTT', 'Troponin I',
       'D-Dimer', 'IL6', 'FLU_TEST','C19_TEST', 'CORONA_TEST','AIDS/HIV', 'Any malignancy', 'Cerebrovascular disease',
       'Chronic pulmonary disease', 'Congestive heart failure', 'Dementia',
       'Diabetes with complications', 'Diabetes without complications',
       'Hemiplegia or paraplegia', 'Metastatic solid tumor',
       'Mild liver disease', 'Moderate or severe liver disease',
       'Myocardial infarction', 'Peptic ulcer disease',
       'Peripheral vascular disease', 'Renal disease', 'Rheumatic disease']

if not os.path.exists("./SampleDataset"):
    os.mkdir("./SampleDataset")

num_patients = 1000

    
for patient in range(1,num_patients+1):
    filename = "./SampleDataset/"+str(patient)+".txt"
    f = open(filename,"w")
    df = random.randint(0,1)
    f.write("DEATH_FLAG="+str(df)+"\n")
    f.write("Time, Parameter, Value\n")
    f.write("0.0,RecordID,"+str(patient)+"\n")
    gender = random.randint(0,2)
    f.write("0.0, Gender, "+str(gender)+"\n")
    race = random.randint(0,7)
    f.write("0.0, Race, "+str(race)+"\n")
    eth= random.randint(0,2)
    f.write("0.0, Ethnicity, "+str(eth)+"\n")
    age = random.uniform(1, 85.5)
    f.write("0.0, Age, "+str(age)+"\n")
    time = 0 
    num_records = random.randint(0,100)
    for line in range(num_records):
        time_inc_flag = random.randint(0,1)
        if time_inc_flag==1:
            time+=random.uniform(0, 50)
        len_var_array = len(variable_array)
        item_num = random.randint(0,len_var_array-1)
        item = variable_array[item_num]
        if item_num>35:
            f.write(str(time)+", "+item+", 1.0\n")
        elif item_num<33:
            val = random.uniform(0, 100)
            val = random.randint(0, 2)
            f.write(str(time)+", "+item+", "+str(val)+"\n")
        else:
            val = random.randint(0, 2)
            f.write(str(time)+", "+item+", "+str(val)+"\n")
            
    f.close()


#splitting data into k folds

X = [i for i in range(1,num_patients+1)]
kf = KFold(n_splits=5)
if not os.path.exists("k_folds/"):
    os.mkdir("k_folds/")
if not os.path.exists("k_folds/raw"):
    os.mkdir("k_folds/raw")

for i, (train_index, test_index) in enumerate(kf.split(X)):
    #print(f"Fold {i}:")
    if not os.path.exists("k_folds/raw/k_"+str(i+1)):
        os.mkdir("k_folds/raw/k_"+str(i+1))
    if not os.path.exists("k_folds/raw/k_"+str(i+1)+"/Train"):
        os.mkdir("k_folds/raw/k_"+str(i+1)+"/Train") 
    if not os.path.exists("k_folds/raw/k_"+str(i+1)+"/Validation"):
        os.mkdir("k_folds/raw/k_"+str(i+1)+"/Validation") 
    if not os.path.exists("k_folds/raw/k_"+str(i+1)+"/Test"):
        os.mkdir("k_folds/raw/k_"+str(i+1)+"/Test") 
    #print(f"  Train: index={train_index}")
    #print(f"  Test:  index={test_index}")
    for idx in train_index:
        origin = "./SampleDataset/"+str(idx+1)+".txt"
        target = "./k_folds/raw/k_"+str(i+1)+"/Train/"
        shutil.copy(origin, target)
    l = len(test_index)//2
    for idx in test_index[:l]:
        origin = "./SampleDataset/"+str(idx+1)+".txt"
        target = "./k_folds/raw/k_"+str(i+1)+"/Test/"
        shutil.copy(origin, target)
    for idx in test_index[l:]:
        origin = "./SampleDataset/"+str(idx+1)+".txt"
        target = "./k_folds/raw/k_"+str(i+1)+"/Validation/"
        shutil.copy(origin, target)
    
