
# coding: utf-8

# In[15]:

import csv

COMMA = ','
NEWLINE = '\n'
doc = 'Documentary'
short = 'Short'

def prep_data():
    fp = open('movie_data.csv','w')
    for i in range(1,8):
        print i
        data_file = file('movie_set_'+str(i)+'.csv', 'r')
        data = csv.reader(data_file, delimiter=',')
        for row in data:
            if len(row) > 0 and doc not in row and short not in row:
                for i in range(0,len(row)-1):
                    fp.write(row[i]+COMMA)
                fp.write(row[len(row)-1]+NEWLINE)
    fp.close()
    print 'Prepared Director ratings'


# In[16]:

prep_data()


# In[ ]:



