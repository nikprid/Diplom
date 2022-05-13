import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing  import Normalizer
from sklearn.svm import OneClassSVM

def create_and_train_model(user):
    scaler = Normalizer()
    data = pd.read_csv(f'keystroke/userdata/processed_data/{user}_processed_data.csv')[:300]
    col_names = ['HD', 'PPD', 'RPD', 'RRD']
    data_s = scaler.fit_transform(data[col_names])
    data_s = pd.DataFrame(data_s, columns = col_names)
    data_s['keycode']=data.keycode.values.astype('str')

    clf = OneClassSVM(nu=0.04, kernel="rbf", gamma=0.0275)
    clf.fit(data_s)
    
    filename_norm = f'keystroke/models/{user}_norm.sav'
    filename_model = f'keystroke/models/{user}_model.sav'
    joblib.dump(scaler, filename_norm)
    joblib.dump(clf, filename_model)



def check_user(user, data):
    filename_norm = f'keystroke/models/{user}_norm.sav'
    scaler = joblib.load(filename_norm)
    col_names = ['HD', 'PPD', 'RPD', 'RRD']
    data_s = scaler.transform(data[col_names])
    data_s = pd.DataFrame(data_s, columns = col_names)
    data_s['keycode']=data.keycode.values.astype('str')

    filename_model = f'keystroke/models/{user}_model.sav'
    loaded_model = joblib.load(filename_model)
    pred = loaded_model.predict(data_s)
    _, counts = np.unique(pred, return_counts=True)
    return counts[1]/len(data)  
    




