from model.ctabgan import CTABGAN
import numpy as np
import pandas as pd

# Specifying the path of the dataset used 
real_path = "Real_Datasets/diabetic.csv" 
# Specifying the root directory for storing generated data
fake_path = "C:\\Users\\47405\\Desktop\\Implementations\\Models\\CTAB-GAN\\Fake_Datasets" 

print('script started')

synthesizer =  CTABGAN(raw_csv_path = real_path,
                 test_ratio = 0.10,  
                 categorical_columns = ['race', 'gender', 'age', 'admission_type_id',
                                        'max_glu_serum', 'A1Cresult', 'metformin','repaglinide','nateglinide',
                                       'glimepiride','glipizide','glyburide','pioglitazone','rosiglitazone','insulin',
                                       'change','diabetesMed','readmitted'], 
                 log_columns = [],
                 mixed_columns= {}, 
                 integer_columns =  ['num_lab_procedures', 'num_medications','time_in_hospital','number_outpatient',
                                    'number_emergency', 'number_inpatient','number_diagnoses', 'num_procedures'],
                 problem_type= {"Classification": 'readmitted'},
                 epochs = 3)


print('fitting started')
synthesizer.fit()
print('fitting finished')

syn = synthesizer.generate_samples()
syn.to_csv(fake_path, index= False)
print('script finished')


