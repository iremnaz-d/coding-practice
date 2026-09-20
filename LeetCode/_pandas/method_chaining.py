#https://leetcode.com/problems/method-chaining/description/

import pandas as pd


def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    new_animals = animals[animals['weight'] > 100].sort_values(ascending=False, by='weight')
    return new_animals[['name']]
