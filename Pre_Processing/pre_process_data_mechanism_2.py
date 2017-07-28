
# coding: utf-8

# In[19]:

import csv

COMMA = ','
NEWLINE = '\n'
QUOTE = '"'
avg_rating = 0
def get_average_rating():
    fp = open('data/movie_ratings.csv','w')    
    data_file = file('data/movie_data.csv', 'r')
    data = csv.reader(data_file, delimiter=',')
    cnt = 0
    avg_rating = 0
    for row in data:
        if len(row) > 0:
            rating = float(row[1])
            fp.write(row[0]+COMMA+str(rating)+NEWLINE)
            cnt +=1
            avg_rating +=rating
    avg_rating = avg_rating/cnt
    fp.close()
    print 'Prepared Movie Ids',cnt,avg_rating
    return avg_rating
prep_movie()


# In[20]:


# In[5]:
avg_rating = get_average_rating()
print avg_rating


# In[37]:

def prep_actors():
    fp = open('data/mechanism_2/actor_scores.csv','w')
    actor_ratings_with_count = {}
    actor_ratings = {}
    data_file = file('data/movie_data.csv', 'r')
    data = csv.reader(data_file, delimiter=',')
    for row in data:
        if len(row) > 0:
            rating = float(row[1])
            start_actor_index = 2
            for index in range(start_actor_index,start_actor_index+4):
                if row[index] in actor_ratings_with_count:
                    actor_ratings_with_count[row[index]] =  (actor_ratings_with_count[row[index]][0] + rating - avg_rating, actor_ratings_with_count[row[index]][1] + 1)  
                else:
                    actor_ratings_with_count[row[index]] = (rating - avg_rating , 1)
    print len(actor_ratings_with_count.keys())
    for key in actor_ratings_with_count.keys():
        fp.write(key+COMMA+ str(float(actor_ratings_with_count[key][0])/int(actor_ratings_with_count[key][1]))+NEWLINE)
        actor_ratings[key] = float(actor_ratings_with_count[key][0])/int(actor_ratings_with_count[key][1])
    fp.close()
    print 'Prepared Actor Scores'
    return actor_ratings_with_count,actor_ratings

actor_ratings_with_count,actor_ratings = prep_actors()
print type(actor_ratings)


# In[44]:

# Top actors with atleast thresh movies
def get_top_actors(thresh=15):
    top_actors=[]
    fp = open('data/mechanism_2/top_actors_'+str(thresh)+'.csv','w')
    desc_ratings = sorted(actor_ratings.items(),key=lambda x:x[1],reverse=True)
    cnt=0
    for tup in desc_ratings:
        if actor_ratings_with_count[tup[0]][1] >=thresh:
            top_actors.append(tup[0])
            fp.write(tup[0]+COMMA+str(tup[1])+COMMA+str(actor_ratings_with_count[tup[0]][1])+NEWLINE)
            cnt +=1
        if cnt>=20:
            break
    print 'Got Top Actors-',len(top_actors),'Threshold',thresh
    fp.close()
    return top_actors
top_actors = get_top_actors()


# In[45]:

top_actors_10 = get_top_actors(10)
top_actors_15 = get_top_actors()
top_actors_20 = get_top_actors(20)
top_actors_25 = get_top_actors(25)


# In[55]:

def prep_directors():
    fp = open('data/mechanism_2/director_scores.csv','w')
    director_ratings = {}
    director_ratings_with_count = {}
    data_file = file('data/movie_data.csv', 'r')
    data = csv.reader(data_file, delimiter=',')
    for row in data:
        if len(row) > 0:
            rating = float(row[1])
            director_index = 6           
            if row[director_index] in director_ratings_with_count:
                director_ratings_with_count[row[director_index]] =  (director_ratings_with_count[row[director_index]][0] + rating - avg_rating, director_ratings_with_count[row[director_index]][1] + 1)  
            else:
                director_ratings_with_count[row[director_index]] = (rating - avg_rating, 1)
    print len(director_ratings_with_count.keys())
    for key in director_ratings_with_count.keys():
        fp.write(key+COMMA+ str(float(director_ratings_with_count[key][0])/int(director_ratings_with_count[key][1]))+NEWLINE)
        director_ratings[key] = float(director_ratings_with_count[key][0])/int(director_ratings_with_count[key][1])
    fp.close()
    print 'Prepared Director ratings'
    return director_ratings_with_count,director_ratings
director_ratings_with_count,director_ratings = prep_directors()


# In[56]:

print len(director_ratings_with_count),len(director_ratings)
def top_directors(thresh=15):
    top_directors=[]
    fp = open('data/mechanism_2/top_directors_'+str(thresh)+'.csv','w')
    desc_ratings = sorted(director_ratings.items(),key=lambda x:x[1],reverse=True)
    print len(desc_ratings)
    cnt=0
    m=1
    for tup in desc_ratings:
        m= max(director_ratings_with_count[tup[0]][1],m)
        if director_ratings_with_count[tup[0]][1] >=thresh:
            top_directors.append(tup[0])
            fp.write(tup[0]+COMMA+str(tup[1])+COMMA+str(director_ratings_with_count[tup[0]][1])+NEWLINE)
            cnt +=1
        if cnt>=20:
            break
    print 'Got Top Directors-',len(top_directors),'Threshold',thresh,'Max',m
    fp.close()
    return top_directors


# In[57]:

top_directors_5 = top_directors(5)
top_directors_10 = top_directors(10)
top_directors_15 = top_directors()
top_directors_20 = top_directors(20)
top_directors_25 = top_directors(25)


# In[61]:

def prep_producers():
    fp = open('data/mechanism_2/producer_score.csv','w')
    producer_ratings_with_count = {}
    producer_ratings = {}
    data_file = file('data/movie_data.csv', 'r')
    data = csv.reader(data_file, delimiter=',')
    cnt = 0
    for row in data:
        if len(row) > 0:
            rating = float(row[1])
            n_prod = 7
            try:
                for index in range(int(row[n_prod])):
                    prod_index = index + n_prod + 1
                    if row[prod_index] in producer_ratings_with_count:
                        producer_ratings_with_count[row[prod_index]] =  (producer_ratings_with_count[row[prod_index]][0] + rating - avg_rating, producer_ratings_with_count[row[prod_index]][1] + 1)  
                    else:
                        producer_ratings_with_count[row[prod_index]] = (rating - avg_rating, 1)
            except:
                print row[0],len(row),prod_index,row
    print len(producer_ratings_with_count.keys())
    for key in producer_ratings_with_count.keys():
        fp.write(key+COMMA+ str(float(producer_ratings_with_count[key][0])/int(producer_ratings_with_count[key][1]))+NEWLINE)
        producer_ratings[key]=float(producer_ratings_with_count[key][0])/int(producer_ratings_with_count[key][1])
    fp.close()
    print 'Prepared Producer ratings',len(producer_ratings_with_count)
    return producer_ratings_with_count,producer_ratings

producer_ratings_with_count,producer_ratings = prep_producers()


# In[62]:

print len(producer_ratings_with_count),len(producer_ratings)
def top_producers(thresh=15):
    top_producers=[]
    fp = open('data/mechanism_2/top_producers_'+str(thresh)+'.csv','w')
    desc_ratings = sorted(producer_ratings.items(),key=lambda x:x[1],reverse=True)
    print len(desc_ratings)
    cnt=0
    m=1
    for tup in desc_ratings:
        m= max(producer_ratings_with_count[tup[0]][1],m)
        if producer_ratings_with_count[tup[0]][1] >=thresh:
            top_producers.append(tup[0])
            fp.write(tup[0]+COMMA+str(tup[1])+COMMA+str(producer_ratings_with_count[tup[0]][1])+NEWLINE)
            cnt +=1
        if cnt>=20:
            break
    print 'Got Top Producers-',len(top_producers),'Threshold',thresh,'Max',m
    fp.close()
    return top_producers


# In[63]:

top_producers_5 = top_producers(5)
top_producers_10 = top_producers(10)
top_producers_15 = top_producers()
top_producers_20 = top_producers(20)
top_producers_25 = top_producers(25)


# In[64]:


def prep_writers():
    fp = open('data/mechanism_2/writers_score.csv','w')
    writer_ratings = {}
    writer_ratings_with_count = {}
    data_file = file('data/movie_data.csv', 'r')
    data = csv.reader(data_file, delimiter=',')
    for row in data:
        if len(row) > 0:
            rating = float(row[1])
            n_writer = 7 + int(row[7]) + 1
            try:
                for index in range(int(row[n_writer])):
                    writer_index = index + n_writer + 1
                    if row[writer_index] in writer_ratings_with_count:
                        writer_ratings_with_count[row[writer_index]] =  (writer_ratings_with_count[row[writer_index]][0] + rating - avg_rating , writer_ratings_with_count[row[writer_index]][1] + 1)  
                    else:
                        writer_ratings_with_count[row[writer_index]] = ( rating - avg_rating, 1)
            except:
                print row[0],len(row),writer_index,row
    print len(writer_ratings_with_count.keys())
    for key in writer_ratings_with_count.keys():
        fp.write(key+COMMA+ str(float(writer_ratings_with_count[key][0])/int(writer_ratings_with_count[key][1]))+NEWLINE)
        writer_ratings[key] = float(writer_ratings_with_count[key][0])/int(writer_ratings_with_count[key][1])
    fp.close()
    print 'Prepared Writer ratings'
    return writer_ratings_with_count,writer_ratings
writer_ratings_with_count,writer_ratings = prep_writers()


# In[67]:

print len(writer_ratings_with_count),len(writer_ratings)
def top_writers(thresh=15):
    top_writers=[]
    fp = open('data/mechanism_2/top_writers_'+str(thresh)+'.csv','w')
    desc_ratings = sorted(writer_ratings.items(),key=lambda x:x[1],reverse=True)
    print len(desc_ratings)
    cnt=0
    m=1
    for tup in desc_ratings:
        m= max(writer_ratings_with_count[tup[0]][1],m)
        if writer_ratings_with_count[tup[0]][1] >=thresh:
            top_writers.append(tup[0])
            fp.write(tup[0]+COMMA+str(tup[1])+COMMA+str(writer_ratings_with_count[tup[0]][1])+NEWLINE)
            cnt +=1
        if cnt>=20:
            break
    print 'Got Top Writers-',len(top_writers),'Threshold',thresh,'Max',m
    fp.close()
    return top_writers


# In[68]:

top_writers_5 = top_writers(5)
top_writers_10 = top_writers(10)
top_writers_15 = top_writers()
top_writers_20 = top_writers(20)
top_writers_25 = top_writers(25)


# In[ ]:



