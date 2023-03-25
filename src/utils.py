import sys
import os

import numpy as np
import pandas as pd
import dill

from src.exception import CustomException


def save_object(filepath,obj):
    try:
        dir_path=os.path.dirname(filepath)
        os.makedirs(dir_path,exist_ok=True)

        with open(filepath,"wb") as f:
            dill.dump(obj, f)

    except Exception as e:
        raise CustomException(e,sys)

