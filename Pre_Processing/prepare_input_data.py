
# coding: utf-8

# In[1]:

import csv

def read_movie_ratings():
    movie_ratings = {}
    data_file = file('data/movie_ratings.csv', 'r')
    data = csv.reader(data_file, delimiter=',')
    for row in data:
        movie_ratings[row[0]] = float(row[1])
    return movie_ratings

def read_actor_ratings(val):
    actor_ratings = {}
    data_file = file('data/mechanism_'+str(val)+'/actor_scores.csv', 'r')
    data = csv.reader(data_file, delimiter=',')
    for row in data:
        actor_ratings[row[0]] = float(row[1])
    return actor_ratings

def read_director_ratings(val):
    director_ratings = {}
    data_file = file('data/mechanism_'+str(val)+'/director_scores.csv', 'r')
    data = csv.reader(data_file, delimiter=',')
    for row in data:
        director_ratings[row[0]] = float(row[1])
    return director_ratings


def read_producer_ratings(val):
    producer_ratings = {}
    data_file = file('data/mechanism_'+str(val)+'/producer_scores.csv', 'r')
    data = csv.reader(data_file, delimiter=',')
    for row in data:
        producer_ratings[row[0]] = float(row[1])
    return producer_ratings


def read_writer_ratings(val):
    writer_ratings = {}
    data_file = file('data/mechanism_'+str(val)+'/writer_scores.csv', 'r')
    data = csv.reader(data_file, delimiter=',')
    for row in data:
        writer_ratings[row[0]] = float(row[1])
    return writer_ratings


# In[2]:

movie_ratings = read_movie_ratings()


# In[12]:

COMMA = ','
NEWLINE = '\n'

def prep_data(val):
    actor_ratings = read_actor_ratings(val)
    director_ratings = read_director_ratings(val)
    producer_ratings = read_producer_ratings(val)
    writer_ratings = read_writer_ratings(val)
    fp = open('input_mechanism_'+str(val)+'.csv','w')
    data_file = file('data/movie_data.csv', 'r')
    data = csv.reader(data_file, delimiter=',')
    for row in data:
        fp.write(str(movie_ratings[row[0]]))
        start_actor_index = 2
        for index in range(start_actor_index,start_actor_index+4):
            fp.write(COMMA+str(actor_ratings[row[index]]))
        director_index = 6
        fp.write(COMMA+str(director_ratings[row[director_index]]))
        start_prod_index = 7
        fp.write(COMMA+str(row[start_prod_index]))
        for index in range(start_prod_index + 1, start_prod_index + int(row[start_prod_index]) + 1):
            fp.write(COMMA+str(producer_ratings[row[index]]))
        start_writer_index = start_prod_index + int(row[start_prod_index]) + 1
        fp.write(COMMA+str(row[start_prod_index]))
        for index in range(start_writer_index + 1, start_writer_index + int(row[start_writer_index]) + 1):
            fp.write(COMMA+str(writer_ratings[row[index]]))
        fp.write(NEWLINE)
    fp.close()
    print 'Prepared Data for Mechanism',val


# In[16]:

prep_data(1)
prep_data(2)


# In[23]:

from random import shuffle
def split_data():
    for i in range(1,3):
        data_file = file('input_mechanism_'+str(i)+'.csv', 'r')
        data = csv.reader(data_file, delimiter=',')
        rows = []
        for row in data:
            rows.append(row)
        shuffle(rows)
        print 'Done shuffling',i
        cnt = int(0.8*len(rows))
        train_data = rows[:cnt]
        test_data = rows[cnt:-1]
        print len(rows),len(train_data),len(test_data)
        fp = open('train_data_'+str(i)+'.csv','w')
        for row in train_data:
            fp.write(row[0])
            for index in range(1,len(row)):
                fp.write(COMMA+row[index])
            fp.write(NEWLINE)
        fp.close()
        print 'Done writing Train Data',i
        fp = open('test_data_'+str(i)+'.csv','w')
        print len(rows),len(train_data),len(test_data)
        for row in test_data:
            fp.write(row[0])
            for index in range(1,len(row)):
                fp.write(COMMA+row[index])
            fp.write(NEWLINE)
        fp.close()
        print 'Done writing Test Data',i
split_data()


# In[ ]:



