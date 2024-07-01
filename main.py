import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

data_one_hot = pd.DataFrame()

for unique_value in data['whoAmI'].unique():
    data_one_hot[unique_value] = (data['whoAmI'] == unique_value).astype(int)

data_one_hot = pd.concat([data, data_one_hot], axis=1)

data_one_hot.head()
