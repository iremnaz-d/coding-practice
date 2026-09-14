#https://leetcode.com/problems/get-the-size-of-a-dataframe/?envType=study-plan-v2&envId=introduction-to-pandas&lang=pythondata

import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> list[int]:
    rows, cols = players.shape
    return [rows, cols]
