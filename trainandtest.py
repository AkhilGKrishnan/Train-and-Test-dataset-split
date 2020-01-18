import random
import os
import subprocess
import sys

def split_data_set(Data):

    f_val = open("smokimg_test.txt", 'w')
    f_train = open("smoking_train.txt", 'w')
    
    path, dirs, files = next(os.walk(Data))
    data_size = len(files)

    ind = 0
    data_test_size = int(0.1 * data_size)
    test_array = random.sample(range(data_size), k=data_test_size)
    
    for f in os.listdir(Data):
        if(f.split(".")[1] == "jpg"):
            ind += 1
            
            if ind in test_array:
                f_val.write(Data+'/'+f+'\n')
            else:
                f_train.write(Data+'/'+f+'\n')
split_data_set(sys.argv[1])