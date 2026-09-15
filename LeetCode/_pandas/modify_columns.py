#https://leetcode.com/problems/modify-columns/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = employees['salary']*2
    return employees