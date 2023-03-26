import sys
import os

import numpy as np
import pandas as pd
import dill
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV

from src.exception import CustomException


def save_object(filepath,obj):
    try:
        dir_path=os.path.dirname(filepath)
        os.makedirs(dir_path,exist_ok=True)

        with open(filepath,"wb") as f:
            dill.dump(obj, f)

    except Exception as e:
        raise CustomException(e,sys)

def evaluate_model(X_train,y_train,X_test,y_test,models,params):
    try:
        report={}
        for i in range(len(list(models))):
            model= list(models.values())[i]
            param= params[list(models.keys())[i]]

            grid_search=GridSearchCV(model,param,cv=3)
            grid_search.fit(X_train,y_train)

            model.set_params(**grid_search.best_params_)




            model.fit(X_train,y_train)
            y_train_pred=model.predict(X_train)
            y_test_pred=model.predict(X_test)
            train_model_score=r2_score(y_train,y_train_pred)
            test_model_score=r2_score(y_test,y_test_pred)
            report[list(models.keys())[i]]=test_model_score

        return report




    except Exception as e:
        raise CustomException(e,sys)

