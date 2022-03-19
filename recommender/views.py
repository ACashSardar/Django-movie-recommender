from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
import requests
# from Recommend_movie import recommend_movie


# Create your views here.
import pandas as pd
import numpy as np
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

ps=PorterStemmer()

def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)
    
new_df=pd.read_csv('./staticfiles/clean_data.csv')
movies=pd.read_csv('./staticfiles/movie_data.csv')


def fetch_poster(movie_id):
    url="https://api.themoviedb.org/3/movie/{}?api_key=7529d26771e710b99bf8c7deda5db2f6&language=en-US".format(movie_id)
    response=requests.get(url)
    movie_info=response.json()
    return ("http://image.tmdb.org/t/p/w500/"+movie_info['poster_path'])
    

def recommend_movie(movie_name):

    new_df['tag']=new_df['tag'].apply(lambda x: stem(x))
    
    cv=CountVectorizer(max_features=5000,stop_words='english')
    vectors=cv.fit_transform(new_df['tag']).toarray()
    similarity=cosine_similarity(vectors)

    indx=movies[movies['title']==movie_name].index[0]
    cos_sim=similarity[indx]
    enum_list=list(enumerate(cos_sim))
    score_list=sorted(enum_list,reverse=True,key=lambda x:x[1])
    score_list=score_list[1:11]

    rec_mov_name=[]
    rec_mov_poster=[]
    for i in score_list:
        rec_mov_name.append((movies['title'].iloc[i[0]]))
        rec_mov_poster.append(fetch_poster(movies['id'].iloc[i[0]]))
        print(movies['title'].iloc[i[0]])
    return rec_mov_name,rec_mov_poster
    
def firstpage(request):
    from register import views as v
    return v.register(request)

def home(request):
    return render(request,'Homepage.html')


def output(request):
    movie_name=str(request.POST.get('movie_name'))
    
    try:
        name,poster=recommend_movie(movie_name)
        My_dict={name[i]:poster[i] for i in range(len(name))}
        # print(My_dict.keys(),My_dict.values())
        return render(request,'Output.html',{'result':My_dict, 'movie_name':movie_name})    
    except:
        return render(request,'Warning.html',{'movie_name':movie_name})


if __name__=="__main__":
    recommend_movie('The Amazing Spider-Man 2')