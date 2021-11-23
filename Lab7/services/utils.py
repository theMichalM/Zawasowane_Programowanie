from klasy.Rating import Rating
from klasy.Tag import Tag
from klasy.Link import Link
from klasy.Movie import Movie


def read_file(sciezka:str, t:str):
    f = open(sciezka, encoding='utf8' )
    if(t=="movie"):
        dictio:__dict__ = read_movie(f)
    elif(t=="link"):
        dictio:__dict__ = read_link(f)
    elif(t=="tag"):
        dictio:__dict__ = read_tag(f)
    elif(t=="rating"):
        dictio:__dict__ = read_rating(f)
    f.close()
    return dictio

def read_movie(f):
    movies: Movie = {}
    i = 0
    f.readline()
    for line in f:
        data = line.split(",")
        type = data[len(data)-1]
        title:str = data[1]
        for j in range(2,len(data)-1):
            title += ',' + data[j]
        movies[i]= Movie(data[0],title,type[:-1]).__dict__
        i+=1
    return movies

def read_link(f):
    links: Link = {}
    i = 0
    f.readline()
    for line in f:
        data = line.split(",")
        type = data[len(data)-1]
        links[i]= Link(data[0],data[1],type[:-1]).__dict__
        i+=1
    return links

def read_tag(f):
    tags: Tag = {}
    i = 0
    f.readline()
    for line in f:
        data = line.split(",")
        type = data[len(data)-1]
        tags[i]= Tag(data[0],data[1],data[2],type[:-1]).__dict__
        i+=1
    return tags

def read_rating(f):
    ratings: Rating = {}
    i = 0
    f.readline()
    for line in f:
        data = line.split(",")
        type = data[len(data)-1]
        ratings[i]= Rating(data[0],data[1],data[2],type[:-1]).__dict__
        i+=1
    return ratings