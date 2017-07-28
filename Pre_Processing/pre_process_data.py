
# coding: utf-8

# In[1]:

import csv

COMMA = ','
NEWLINE = '\n'
QUOTE = '"'
def prep_movie():
    fp = open('movie_ratings.csv','w')    
    data_file = file('movie_data.csv', 'r')
    data = csv.reader(data_file, delimiter=',')
    cnt = 0
    for row in data:
        if len(row) > 0:
            rating = float(row[2])
            name = row[1]
        fp.write(row[0]+COMMA+QUOTE+name+QUOTE+COMMA+str(rating)+NEWLINE)
        cnt +=1
    fp.close()
    print 'Prepared Movie Ids',cnt
prep_movie()


# In[2]:


# In[5]:

def prep_actors():
    fp = open('actor_scores.csv','w')
    actor_ratings = {}
    data_file = file('movie_data.csv', 'r')
    data = csv.reader(data_file, delimiter=',')
    for row in data:
        if len(row) > 0:
            rating = float(row[2])
            start_actor_index = 3
            for index in range(start_actor_index,start_actor_index+8,2):
                if row[index] in actor_ratings:
                    actor_ratings[row[index]] =  (actor_ratings[row[index]][0], actor_ratings[row[index]][1] + rating, actor_ratings[row[index]][2] + 1)  
                else:
                    actor_ratings[row[index]] = (row[index+1], rating, 1)
    print len(actor_ratings.keys())
    for key in actor_ratings.keys():
        fp.write(key+COMMA+QUOTE+actor_ratings[key][0]+QUOTE+COMMA+ str(float(actor_ratings[key][1])/int(actor_ratings[key][2]))+NEWLINE)
    fp.close()
    print 'Prepared Actor Ids'


# In[3]:

prep_actors()


# In[4]:

def prep_directors():
    fp = open('director_score.csv','w')
    director_ratings = {}
    data_file = file('movie_data.csv', 'r')
    data = csv.reader(data_file, delimiter=',')
    for row in data:
        if len(row) > 0:
            rating = float(row[2])
            director_index = 11            
            if row[director_index] in director_ratings:
                director_ratings[row[director_index]] =  (director_ratings[row[director_index]][0], director_ratings[row[director_index]][1] + rating, director_ratings[row[director_index]][2] + 1)  
            else:
                director_ratings[row[director_index]] = (row[director_index+1], rating, 1)
    print len(director_ratings.keys())
    for key in director_ratings.keys():
        fp.write(key+COMMA+QUOTE+director_ratings[key][0]+QUOTE+COMMA+ str(float(director_ratings[key][1])/int(director_ratings[key][2]))+NEWLINE)
    fp.close()
    print 'Prepared Director ratings'


# In[5]:

prep_directors()


# In[21]:

def prep_producers():
    fp = open('producer_score.csv','w')
    producer_ratings = {}
    data_file = file('movie_data.csv', 'r')
    data = csv.reader(data_file, delimiter=',')
    cnt = 0
    for row in data:
        if len(row) > 0:
            rating = float(row[2])
            n_prod = 13
            try:
                for index in range(int(row[n_prod])):
                    prod_index = 2*index + n_prod + 1
                    if row[prod_index] in producer_ratings:
                        producer_ratings[row[prod_index]] =  (producer_ratings[row[prod_index]][0], producer_ratings[row[prod_index]][1] + rating, producer_ratings[row[prod_index]][2] + 1)  
                    else:
                        producer_ratings[row[prod_index]] = (row[prod_index+1], rating, 1)
                    if cnt < 10:
                        print '#',row[0],'#',prod_index,'#',row[n_prod],'#',row[prod_index],'#',row[prod_index+1]
                        cnt += 1
            except:
                print row[0],len(row),prod_index,row
    print len(producer_ratings.keys())
    for key in producer_ratings.keys():
        fp.write(key+COMMA+QUOTE+producer_ratings[key][0]+QUOTE+COMMA+ str(float(producer_ratings[key][1])/int(producer_ratings[key][2]))+NEWLINE)
    fp.close()
    print 'Prepared Producer ratings'


# In[22]:

prep_producers()


# In[23]:

def prep_writers():
    fp = open('writers_score.csv','w')
    writer_ratings = {}
    data_file = file('movie_data.csv', 'r')
    data = csv.reader(data_file, delimiter=',')
    for row in data:
        if len(row) > 0:
            rating = float(row[2])
            n_writer = 13 + 2*int(row[13]) + 1
            try:
                for index in range(int(row[n_writer])):
                    writer_index = 2*index + n_writer + 1
                    if row[writer_index] in writer_ratings:
                        writer_ratings[row[writer_index]] =  (writer_ratings[row[writer_index]][0], writer_ratings[row[writer_index]][1] + rating, writer_ratings[row[writer_index]][2] + 1)  
                    else:
                        writer_ratings[row[writer_index]] = (row[writer_index+1], rating, 1)
            except:
                print row[0],len(row),writer_index,row
    print len(writer_ratings.keys())
    for key in writer_ratings.keys():
        fp.write(key+COMMA+QUOTE+writer_ratings[key][0]+QUOTE+COMMA+ str(float(writer_ratings[key][1])/int(writer_ratings[key][2]))+NEWLINE)
    fp.close()
    print 'Prepared Writer ratings'


# In[24]:

prep_writers()


# In[ ]:




# In[ ]:



