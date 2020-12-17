import pandas as pd
from datetime import datetime

from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error

def prepare_sprint_1(df):
    df = df.copy()
    
    columns_to_keep = ["Nature mutation","Code postal", "Code departement", 
                       "Valeur fonciere", "Type local", "Surface reelle bati", 
                       "Nombre pieces principales"]
    df = df[columns_to_keep]
    
    
    columns_to_be_categorical = ["Nature mutation", "Code postal", "Code departement", "Type local"]

    for column in columns_to_be_categorical:
        df[column] = df[column].astype('category')
        
        
    df['Valeur fonciere'] = df["Valeur fonciere"].str.replace(",",".")
    df['Valeur fonciere'] = df["Valeur fonciere"].astype('float64')
    df = df.dropna()

    df['Valeur fonciere'] = df["Valeur fonciere"].astype('uint64')

    mask_vente = df["Nature mutation"] == "Vente"
    df = df[mask_vente]
    
    return df

def prepare_sprint_2(df):
    df = df.copy()
    
    centile_25 = 1.07e+05
    centile_75 = 3.05e+05

    mask_sup_25 = df["Valeur fonciere"] > centile_25
    mask_inf_75 = df["Valeur fonciere"] < centile_75
    
    df = df[mask_sup_25 & mask_inf_75]
    
    return df


def fit_and_predict(Classifier, df, cols_features, col_target):
    
    start = datetime.now()

    df = df.copy()
    
    
    y = df[col_target]
    
    X = df[cols_features]    
    X = pd.get_dummies(X)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=31)
    
    clf = Classifier()
    clf = clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    
    error = mean_absolute_error(y_test, y_pred)
    

    
    end = datetime.now()
    duration =  end - start
    columns = X.columns
    
    return (error, duration, columns, clf)

from  datetime import datetime
import re, os, joblib

def save_model(clf, version):
 
    if not os.path.exists("models"):
        os.mkdir("models")
        
    filename = f"model-{version}.model"
    joblib.dump(clf, "./models/" + filename)