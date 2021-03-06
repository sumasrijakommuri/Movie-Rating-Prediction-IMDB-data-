
# coding: utf-8

# In[14]:

import csv

from sklearn.linear_model import LogisticRegression
import numpy as np
from sklearn.metrics import mean_squared_error

import warnings
warnings.filterwarnings('ignore')

TEST_DATA_FILE_1 = "test_data_1.csv"
TEST_DATA_FILE_2 = "test_data_2.csv"
TRAIN_DATA_FILE_1 = "train_data_1.csv"
TRAIN_DATA_FILE_2 = "train_data_2.csv"
PROD_INDEX = 6
DIR_INDEX = 5
ERROR_THRESHOLD_1 = 0
ERROR_THRESHOLD_2 = 0.2
ERROR_THRESHOLD_3 = 0.4


# In[15]:

def read_data_file(filename):    
    data_file = file(filename, 'r')
    data = csv.reader(data_file, delimiter=',')
    labels = []
    values = []
    for row in data:
        value = []
        prod_value = 0
        writer_value = 0
        for index in range(1,PROD_INDEX):
            value.append(float(row[index]))
        for index in range(PROD_INDEX + 1,PROD_INDEX + int(row[PROD_INDEX]) + 1):
            prod_value = max(float(row[index]),prod_value)
        value.append(prod_value)
        WRITER_INDEX = PROD_INDEX + int(row[PROD_INDEX]) + 1
        for index in range(WRITER_INDEX+1,len(row)):
            writer_value = max(float(row[index]),writer_value)
        value.append(writer_value)
        labels.append(float(row[0]))
        values.append(value)
    print 'Done Reading File',filename
    return labels,values


# In[16]:

train_data_1_labels, train_data_1_values = read_data_file(TRAIN_DATA_FILE_1)
train_data_2_labels, train_data_2_values = read_data_file(TRAIN_DATA_FILE_2)

test_data_1_labels, test_data_1_values = read_data_file(TEST_DATA_FILE_1)
test_data_2_labels, test_data_2_values = read_data_file(TEST_DATA_FILE_2)


# In[37]:

def get_error_metric(threshold,actual_labels,predicted_labels):
    error_count = 0
    errors = np.zeros(len(actual_labels))
    for index in range(0,len(actual_labels)):
        errors[index] = (abs(float(actual_labels[index])-float(predicted_labels[index])))
        if abs(float(actual_labels[index])-float(predicted_labels[index])) > threshold:
            error_count +=1
    return error_count*100/len(actual_labels),np.mean(errors),np.std(errors)


# In[38]:

def get_predictions(classifier,val,data):
    if val==1:
        X = np.asarray(train_data_1_values)
        Y = np.asarray(train_data_1_labels,dtype='S6')
    else:
        X = np.asarray(train_data_2_values)
        Y = np.asarray(train_data_2_labels,dtype="S6")
    classifier.fit(X,Y)
    return classifier.predict(data)


# In[39]:

classifier = LogisticRegression(C=1e5)
obs_labels = get_predictions(classifier,1,test_data_1_values)


# In[40]:

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_1_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_1_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_1_labels,obs_labels)
print 'Errors for Mechanism-1: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors for Mechanism-1: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors for Mechanism-1: 0.2 Tolerance:',error_3,mean_3,std_3


# In[42]:

classifier = LogisticRegression(C=1e5)
obs_labels = get_predictions(classifier,2,test_data_2_values)


# In[43]:

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_2_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_2_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_2_labels,obs_labels)
print 'Errors for Mechanism-2: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors for Mechanism-2: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors for Mechanism-2: 0.2 Tolerance:',error_3,mean_3,std_3


# In[50]:

print 'l2,C:1e5'
classifier = LogisticRegression(penalty='l2',C=1e5)
obs_labels = get_predictions(classifier,1,test_data_1_values)

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_1_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_1_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_1_labels,obs_labels)
print 'Errors for Mechanism-1: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors for Mechanism-1: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors for Mechanism-1: 0.2 Tolerance:',error_3,mean_3,std_3  

print 'l2,C:1'
classifier = LogisticRegression(penalty='l2',C=1)
obs_labels = get_predictions(classifier,1,test_data_1_values)

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_1_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_1_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_1_labels,obs_labels)
print 'Errors for Mechanism-1: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors for Mechanism-1: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors for Mechanism-1: 0.2 Tolerance:',error_3,mean_3,std_3

print 'l1,C:1'
classifier = LogisticRegression(penalty='l1',C=1)
obs_labels = get_predictions(classifier,1,test_data_1_values)

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_1_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_1_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_1_labels,obs_labels)
print 'Errors for Mechanism-1: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors for Mechanism-1: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors for Mechanism-1: 0.2 Tolerance:',error_3,mean_3,std_3

print 'l1,C:1e5'
classifier = LogisticRegression(penalty='l1',C=1e5)
obs_labels = get_predictions(classifier,1,test_data_1_values)

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_1_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_1_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_1_labels,obs_labels)
print 'Errors for Mechanism-1: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors for Mechanism-1: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors for Mechanism-1: 0.2 Tolerance:',error_3,mean_3,std_3


# In[51]:

print 'l2,C:1e5'
classifier = LogisticRegression(penalty='l2',C=1e5)
obs_labels = get_predictions(classifier,2,test_data_2_values)

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_2_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_2_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_2_labels,obs_labels)
print 'Errors for Mechanism-2: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors for Mechanism-2: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors for Mechanism-2: 0.2 Tolerance:',error_3,mean_3,std_3  

print 'l2,C:1'
classifier = LogisticRegression(penalty='l2',C=1)
obs_labels = get_predictions(classifier,2,test_data_2_values)

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_2_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_2_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_2_labels,obs_labels)
print 'Errors for Mechanism-2: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors for Mechanism-2: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors for Mechanism-2: 0.2 Tolerance:',error_3,mean_3,std_3

print 'l1,C:1'
classifier = LogisticRegression(penalty='l1',C=1)
obs_labels = get_predictions(classifier,2,test_data_2_values)

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_2_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_2_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_2_labels,obs_labels)
print 'Errors for Mechanism-2: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors for Mechanism-2: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors for Mechanism-2: 0.2 Tolerance:',error_3,mean_3,std_3

print 'l1,C:1e5'
classifier = LogisticRegression(penalty='l1',C=1e5)
obs_labels = get_predictions(classifier,2,test_data_2_values)

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_2_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_2_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_2_labels,obs_labels)
print 'Errors for Mechanism-2: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors for Mechanism-2: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors for Mechanism-2: 0.2 Tolerance:',error_3,mean_3,std_3


# In[54]:

avg_rating = 6.031

def read_data_file_2(filename):    
    data_file = file(filename, 'r')
    data = csv.reader(data_file, delimiter=',')
    labels = []
    values = []
    for row in data:
        value = []
        prod_value = 0
        writer_value = 0
        for index in range(1,PROD_INDEX):
            value.append(float(row[index]))
        for index in range(PROD_INDEX + 1,PROD_INDEX + int(row[PROD_INDEX]) + 1):
            prod_value = max(float(row[index]),prod_value)
        value.append(prod_value)
        WRITER_INDEX = PROD_INDEX + int(row[PROD_INDEX]) + 1
        for index in range(WRITER_INDEX+1,len(row)):
            writer_value = max(float(row[index]),writer_value)
        value.append(writer_value)
        labels.append(float(row[0])-avg_rating)
        values.append(value)
    print 'Done Reading File',filename
    return labels,values

train_data_1_labels, train_data_1_values = read_data_file_2(TRAIN_DATA_FILE_1)
train_data_2_labels, train_data_2_values = read_data_file_2(TRAIN_DATA_FILE_2)

test_data_1_labels, test_data_1_values = read_data_file_2(TEST_DATA_FILE_1)
test_data_2_labels, test_data_2_values = read_data_file_2(TEST_DATA_FILE_2)


# In[56]:


classifier = LogisticRegression(C=1e5)
obs_labels = get_predictions(classifier,1,test_data_1_values)

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_1_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_1_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_1_labels,obs_labels)
print 'Errors(2) for Mechanism-1: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors(2) for Mechanism-1: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors(2) for Mechanism-1: 0.2 Tolerance:',error_3,mean_3,std_3


# In[57]:

classifier = LogisticRegression(C=1e5)
obs_labels = get_predictions(classifier,2,test_data_2_values)


# In[58]:

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_2_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_2_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_2_labels,obs_labels)
print 'Errors(2) for Mechanism-2: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors(2) for Mechanism-2: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors(2) for Mechanism-2: 0.2 Tolerance:',error_3,mean_3,std_3


# In[59]:

print 'l2,C:1e5'
classifier = LogisticRegression(penalty='l2',C=1e5)
obs_labels = get_predictions(classifier,1,test_data_1_values)

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_1_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_1_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_1_labels,obs_labels)
print 'Errors(2) for Mechanism-1: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors(2) for Mechanism-1: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors(2) for Mechanism-1: 0.2 Tolerance:',error_3,mean_3,std_3  

print 'l2,C:1'
classifier = LogisticRegression(penalty='l2',C=1)
obs_labels = get_predictions(classifier,1,test_data_1_values)

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_1_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_1_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_1_labels,obs_labels)
print 'Errors(2) for Mechanism-1: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors(2) for Mechanism-1: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors(2) for Mechanism-1: 0.2 Tolerance:',error_3,mean_3,std_3

print 'l1,C:1'
classifier = LogisticRegression(penalty='l1',C=1)
obs_labels = get_predictions(classifier,1,test_data_1_values)

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_1_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_1_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_1_labels,obs_labels)
print 'Errors(2) for Mechanism-1: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors(2) for Mechanism-1: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors(2) for Mechanism-1: 0.2 Tolerance:',error_3,mean_3,std_3

print 'l1,C:1e5'
classifier = LogisticRegression(penalty='l1',C=1e5)
obs_labels = get_predictions(classifier,1,test_data_1_values)

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_1_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_1_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_1_labels,obs_labels)
print 'Errors(2) for Mechanism-1: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors(2) for Mechanism-1: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors(2) for Mechanism-1: 0.2 Tolerance:',error_3,mean_3,std_3


# In[60]:

print 'l2,C:1e5'
classifier = LogisticRegression(penalty='l2',C=1e5)
obs_labels = get_predictions(classifier,2,test_data_2_values)

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_2_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_2_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_2_labels,obs_labels)
print 'Errors(2) for Mechanism-2: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors(2) for Mechanism-2: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors(2) for Mechanism-2: 0.2 Tolerance:',error_3,mean_3,std_3  

print 'l2,C:1'
classifier = LogisticRegression(penalty='l2',C=1)
obs_labels = get_predictions(classifier,2,test_data_2_values)

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_2_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_2_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_2_labels,obs_labels)
print 'Errors(2) for Mechanism-2: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors(2) for Mechanism-2: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors(2) for Mechanism-2: 0.2 Tolerance:',error_3,mean_3,std_3

print 'l1,C:1'
classifier = LogisticRegression(penalty='l1',C=1)
obs_labels = get_predictions(classifier,2,test_data_2_values)

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_2_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_2_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_2_labels,obs_labels)
print 'Errors(2) for Mechanism-2: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors(2) for Mechanism-2: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors(2) for Mechanism-2: 0.2 Tolerance:',error_3,mean_3,std_3

print 'l1,C:1e5'
classifier = LogisticRegression(penalty='l1',C=1e5)
obs_labels = get_predictions(classifier,2,test_data_2_values)

error_1,mean_1,std_1 = get_error_metric(ERROR_THRESHOLD_1,test_data_2_labels,obs_labels)
error_2,mean_2,std_2 = get_error_metric(ERROR_THRESHOLD_2,test_data_2_labels,obs_labels)
error_3,mean_3,std_3 = get_error_metric(ERROR_THRESHOLD_3,test_data_2_labels,obs_labels)
print 'Errors(2) for Mechanism-2: Zero Tolerance:',error_1,mean_1,std_1
print 'Errors(2) for Mechanism-2: 0.1 Tolerance:',error_2,mean_2,std_2
print 'Errors(2) for Mechanism-2: 0.2 Tolerance:',error_3,mean_3,std_3


# In[ ]:



