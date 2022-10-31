import pandas as pd
import numpy as np
from tgan.model import TGANModel
import time 

# replace the path to the input dataset

data = pd.read_csv('/bhome/ahznik/real_datasets/mimic-test.csv')

# we need to create 0-indexed list of columns indices considered to be continuous. In this example script, 
# the mimic-test dataset has 15 columns. For other datasets, a similar approach should be applied to specify
# continuous columns.  

cols = [i for i in range(14)]
data.columns = cols
continuous_columns = [8,9,10,11,12]

tgan = TGANModel(continuous_columns, max_epoch = 1, steps_per_epoch = 10 ,restore_session=False)



start_time = time.time()
tgan.fit(data)
end_time = time.time()
print('Finished training in',end_time-start_time," seconds.")

