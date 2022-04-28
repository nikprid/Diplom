import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing  import Normalizer
from sklearn.svm import OneClassSVM

def create_and_train_model(user):
    n_scaler = Normalizer()
    data = pd.read_csv(f'keystroke/userdata/processed_data/{user}_processed_data.csv')[:55]
    col_names = ['HD', 'PPD', 'RPD', 'RRD']
    data_s = n_scaler.fit_transform(data[col_names])
    data_s = pd.DataFrame(data_s, columns = col_names)
    data_s['keycode']=data.keycode.astype('str')

    clf = OneClassSVM(nu=0.03, kernel="rbf", gamma=0.9999)
    clf.fit(data_s)
    
    filename = f'keystroke/models/{user}_model.sav'
    joblib.dump(clf, filename)


def check_user(user, data):
    n_scaler = Normalizer()
    col_names = ['HD', 'PPD', 'RPD', 'RRD']
    data_s = n_scaler.fit_transform(data[col_names])
    data_s = pd.DataFrame(data_s, columns = col_names)
    data_s['keycode']=data.keycode.astype('str')

    filename = f'keystroke/models/{user}_model.sav'
    loaded_model = joblib.load(filename)
    pred = loaded_model.predict(data_s)
    _, counts = np.unique(pred, return_counts=True)
    if counts[1]/len(data)>0.49:
        return {'user':user, 'result': f'valid - {counts[1]/len(data)}'}
    else:
        return {'user':user, 'result': f'intruder - {counts[1]/len(data)}'}    
    




