
# coding: utf-8

# In[15]:

import csv, time
from imdb import IMDb


ia = IMDb()

COMMA = ','
NEWLINE = '\n'


def get_persons(persons):
    li = []
    for person in persons:
        li.append(person.personID)
        li.append(person['name'].encode('utf-8'))
    return li

def get_writer():
    start_t = timeit.default_timer()
    prev_t = start_t
    fp = file('writers_1.csv','w')
    data_file = file('ids_1.txt', 'r')
    data = csv.reader(data_file, delimiter=',')
    cnt = 0
    print 'Started Writing'
    for row in data:
        cnt +=1
        movie = ia.get_movie(row[0])
        if 'writer' in movie.keys():
        #print movie['writer'],row[0]
            fp.write(row[0]+COMMA)
            persons = get_persons(movie['writer'])
            fp.write(str(len(persons)/2))
            for person in persons:
                fp.write(COMMA+'"'+person+'"')
            fp.write(NEWLINE)
            if cnt%100==0:
                cur_t = timeit.default_timer()
                print 'Time taken:',cur_t-prev_t,'secs'
                prev_t = cur_t
    stop_t = timeit.default_timer()
    print 'Number of writers',cnt,' and time taken', str(stop_t-start_t),' secs'
    fp.close()


# In[ ]:

get_writer()


# In[ ]:



