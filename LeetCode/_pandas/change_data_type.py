#https://leetcode.com/problems/change-data-type/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd


def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    return students.astype({'grade': int})
