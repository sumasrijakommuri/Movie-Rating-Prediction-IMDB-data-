
# coding: utf-8

# In[3]:

import csv

writer_data={}
def prepare_writer_data():
    for i in range(1,5):
        data_file = file('writers_'+str(i)+'.csv','r')
        data = csv.reader(data_file, delimiter=',')
        for row in data:
            writer_data[row[0]]=row
    print len(writer_data)


# In[4]:

prepare_writer_data()


# In[5]:

COMMA = ','
NEWLINE = '\n'
QUOTE = '"'
def prepare_proper_data():
    fp = open('movie_data.csv','w')
    data_file = file('movie_data_with_quotes.csv','r')
    data = csv.reader(data_file,delimiter=',')
    for row in data:
        if row[0] in writer_data:
            for i in range(len(row)-2):
                fp.write(QUOTE+row[i]+QUOTE+COMMA)
            writer = writer_data[row[0]]
            for i in range(1,len(writer)):
                fp.write(QUOTE+writer[i]+QUOTE+COMMA)
            fp.write(QUOTE+row[len(row)-1]+QUOTE+NEWLINE)
    print 'Prepared New Data'


# In[6]:

prepare_proper_data()


# In[19]:

def remove_genres():
    data_file = file('movie_data_with_genres.csv','r')
    data = csv.reader(data_file,delimiter=',')
    fp = open('movie_data.csv','w')
    for row in data:
        try:
            s_genre_index = 13 + 2*int(row[13]) + 1
            n_genres = int(row[s_genre_index])
            for i in range(len(row)-1):
                if i < s_genre_index or i > s_genre_index + n_genres:
                    fp.write(QUOTE+row[i]+QUOTE+COMMA)
            fp.write(QUOTE+row[len(row)-1]+QUOTE+NEWLINE)
        except:
            print row[0],'#',s_genre_index,'#',row[s_genre_index]  
    print 'Removed Genres'


# In[20]:

remove_genres()


# In[10]:

import csv
COMMA = ','
NEWLINE = '\n'

outliers = ["0798817","3781762","3465074","0478087","1629439","0450385","1680045","0120577","0126765","0416449","0453562","0116635","1190080","1517177","2395385","0472033","0493101"," 0259822"]

def remove_names():
    data_file = file('movie_data_with_names.csv','r')
    data = csv.reader(data_file,delimiter=',')
    fp = open('data.csv','w')
    for row in data:
        fp.write(row[0])
        for i in range(1,len(row)):
            try:
                val = float(row[i])
                if val!=None and val!='':
                    if row[0] in outliers:
                        if i!=1:
                            fp.write(COMMA+row[i])
                    else:
                        fp.write(COMMA+row[i])
            except:
                pass
        fp.write(NEWLINE)
    print 'Done removing names'


# In[11]:

remove_names()


# In[ ]:



