#https://leetcode.com/problems/drop-missing-data/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd


def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(axis=0, subset = 'name')
