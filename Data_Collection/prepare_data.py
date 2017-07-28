
# coding: utf-8

# In[1]:

from imdb import IMDb
import csv
import timeit

ia = IMDb()
movie_names = []
delim = '('
other_delim = ')'
mv = 'movie'
start_yr = 1990
end_yr = 2015
eng = 'English'
braces = '{'
tv = '(TV)'
video = '(V)'
slash = '/'
question = '?'
hyphen = '-'
cast_count = 4

def is_valid(movie):
    if 'year' not in movie.keys() or 'cast' not in movie.keys() or 'genres' not in movie.keys():
        return False
    if 'director' not in movie.keys() or 'title' not in movie.keys() or 'rating' not in movie.keys():
        return False
    year = int(movie['year'])
    if year < start_yr:
        return False
    if year > end_yr:
        return False
    kind = movie['kind']
    if kind!=mv:
        return False
    if 'languages' not in movie.keys():
        return False
    languages = movie['languages'] 
    if eng not in languages:
        return False
    else:
        return True

def get_top_cast(cast):
    top_cast = []
    cast = cast[:cast_count]
    for person in cast:
        top_cast.append(person.personID)
        top_cast.append(person['name'].encode('utf-8'))
    return top_cast
    
def get_top_person(persons):
    top_person = persons[0]
    return [top_person.personID,top_person['name'].encode('utf-8')]

def get_genres(genres):
    return [str(genre) for genre in genres]

def get_persons(persons):
    li = []
    for person in persons:
        li.append(person.personID)
        li.append(person['name'].encode('utf-8'))
    return li

def get_companies(companies):
    li = []
    for company in companies:
        li.append(company.companyID)
        li.append(company['name'].encode('utf-8'))
    return li

def get_list(movie):
    li = []
    li.append(movie.movieID)
    li.append(movie['title'].encode('utf-8'))
    li.append(movie['rating'])
    li.extend(get_top_cast(movie['cast']))
    li.extend(get_top_person(movie['director']))
    # Instead of individual producers we use production companies
    #li.extend(get_persons(movie['producer']))
    if 'production companies' in movie.keys():    
        li.append(len(movie['production companies']))
        li.extend(get_companies(movie['production companies']))
    else:
        li.append(0)
    # Have to check whether we wish to deal with one genre
    if 'genres' in movie.keys():
        li.append(len(movie['genres']))
        li.extend(get_genres(movie['genres']))
    else:
        li.append(0)
    # Have to check whether we wish to deal with one writer
    if 'writers' in movie.keys():
        li.append(len(get_persons(movie['writers'])))
        li.extend(get_persons(movie['writers']))
    else:
        li.append(0)
    if 'votes' in movie.keys():
        li.append(movie['votes'])
    else:
        li.append(0)
    return li
    
data_file = file('ids_set_1', 'r')
data_file_csv = csv.reader(data_file, delimiter=',')
data = []

#keys being written - movieId,title,rating,lead_cast((top 4) name,id),director(top),number of production companies, production companies,
#                     number of genres, genres,number of writers,writers, votes
fp = open('movie_set_1.csv','w')
cnt = 0
#Test purposes
#data_file_csv = data_file_csv[:10]
data = []
i=0
cnt = 0
start_t = timeit.default_timer()
prev_t = start_t
print 'Started Reading'
for row in data_file_csv:
    try:
        movie = ia.get_movie(row[0])
        if i%100 ==0:
            print 'read movie',i,timeit.default_timer() - prev_t
            prev_t = timeit.default_timer()
        if is_valid(movie):
            li = get_list(movie)
            for idx in range(len(li)-1):
                #print idx,li[idx],li[0],li[1]
                fp.write(str(li[idx])+',')
            fp.write(str(li[len(li)-1])+'\n')
            if cnt%50==0:
                print 'append movie',cnt
            cnt +=1
        i+=1
    except:
        pass
stop_t = timeit.default_timer()
fp.close()
print 'Done Reading File','Took ',stop_t-start_t,'secs'


# In[89]:

print len(data)
with open('movie_set_1.csv','wb') as out:
    csv_out=csv.writer(out)
    for row in data:
        csv_out.writerow(str(row))


# In[ ]:


#ia = IMDb(accessSystem='http')
movie = ia.get_movie('0022386')
if 'la'
print movie['title'],movie['languages'],movie['director'],movie['kind'],movie['rating'],movie['miscellaneous crew'],movie['genres']
print type(movie['director'][0]),'##',movie['producer'],'##', movie['production companies']


# In[34]:

print movie['director'][0].keys()


# In[35]:

print movie['director'],movie.movieID,movie['producer']


# In[38]:

print movie['director'][0].personID,movie['director'][0]['name']


# In[64]:

print movie['year'],movie['production companies'],movie['languages']


# In[65]:

movie = ia.get_movie('0848228')
print movie['title'],movie['languages'],movie['director'],movie['kind'],movie['rating'],movie['cast'][5],movie['genres']


# In[57]:

movie['genre'],movie['production companies']


# In[53]:

movie['sound crew'][0],movie['production companies'][0].companyID


# In[56]:

movie['editor'],'##',movie['writer'][0],'##',movie['producer']


# In[27]:

movie['votes']


# In[28]:

l = [u'English', u'French']
if 'English' in l:
    print 'YES'


# In[42]:

t=[]
t.append(1)
t.append(2)
t


# In[43]:

t.append([3,4])


# In[44]:

t


# In[45]:

t=[1,2]
t


# In[48]:

[(s+2,s+3) for s in t]


# In[ ]:



