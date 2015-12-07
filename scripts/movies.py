import time
import requests
from datetime import datetime
from core.models import Movie
from core.models import Person
from core.models import Genre


def request_page(namespace, page_number):

    api_key = '43a11d4a123a0d76d473e4f70abc1ce8'
    root_url = 'https://api.themoviedb.org/3/'

    request_url = '{0}{1}?api_key={2}&page={3}'.format(
        root_url,
        namespace,
        api_key,
        page_number
    )
    print(request_url)
    response = requests.get(request_url)
    data = response.json()
    return data


def request_similar(id_req):
    api_key = '43a11d4a123a0d76d473e4f70abc1ce8'
    root_url = 'https://api.themoviedb.org/3/'

    # /movie/id/similar
    path = 'movie/{0}/similar'.format(
        id_req
    )
    request_url = '{0}{1}?api_key={2}'.format(
        root_url,
        path,
        api_key
    )

    # print("request similar url : " + request_url)
    response = requests.get(request_url)
    data = response.json()
    movie_ids = []
    for movie in data['results']:
        movie_ids.append(movie['id'])
    return movie_ids


def request_casting_and_crew(id_req):
    api_key = '43a11d4a123a0d76d473e4f70abc1ce8'
    root_url = 'https://api.themoviedb.org/3/'

    # /movie/id/credits
    path = 'movie/{0}/credits'.format(
        id_req
    )
    request_url = '{0}{1}?api_key={2}'.format(
        root_url,
        path,
        api_key
    )

    # print("request credits url : " + request_url)
    response = requests.get(request_url)
    data = response.json()

    crew = data['crew']
    producers = []
    directors = []

    for c in crew:
        if(c['job'] == "Producer"):
            # producer_info = {}
            # producer_info["name"] = c["name"]
            # producer_info["id"] = c["id"]
            producers.append(c)

        if(c['job'] == "Director"):
            # director_info = {}
            # director_info["name"] = c["name"]
            # director_info["id"] = c["id"]
            directors.append(c)

    return data['cast'], producers, directors


def request_directors_and_producers(movie_id):
    api_key = '43a11d4a123a0d76d473e4f70abc1ce8'
    root_url = 'https://api.themoviedb.org/3/'

    # /movie/id/credits
    path = 'movie/{0}/credits'.format(
        movie_id
    )
    request_url = '{0}{1}?api_key={2}'.format(
        root_url,
        path,
        api_key
    )

    # print("request credits url : " + request_url)
    response = requests.get(request_url)
    data = response.json()

    crew = data['crew']
    producers = []
    directors = []

    for c in crew:
        if(c['job'] == "Producer"):
            # producer_info = {}
            # producer_info["name"] = c["name"]
            # producer_info["id"] = c["id"]
            producers.append(c)

        if(c['job'] == "Director"):
            # director_info = {}
            # director_info["name"] = c["name"]
            # director_info["id"] = c["id"]
            directors.append(c)

    return directors, producers


def write_json(movie_list):

    for movie in movie_list:
        movie_id = movie['id']

        # chama request_similar e adiciona no json
        movie['similar'] = request_similar(movie_id)

        # chama request_casting e adiciona no json
        # = request_casting(movie_id)

        casting, producers, directors = request_casting_and_crew(movie_id)

        movie['casting'] = casting
        movie['directors'] = directors
        movie['producers'] = producers

        persist_data(movie)

        # filename = 'movie_list/{0}.json'.format(movie_id)
        # f = open(filename, 'w')
        # f.write(str(movie))
        # f.close()

        print("dormindo por 1s")
        time.sleep(1)
        print("acordando")


def persist_data(movie):

    actors = []
    directors = []
    producers = []

    movie_obj = create_movie(movie)

    for actor in movie['casting']:
        movie_obj.casting.add(create_person(actor))
    for director in movie['directors']:
        movie_obj.directors.add(create_person(director))
    for producer in movie['producers']:
        movie_obj.producers.add(create_person(producer))

    print(movie_obj.title)


def create_person(person):

    image_root = 'http://image.tmdb.org/t/p/w300'

    try:
        person_obj = Person.objects.get(tmdb_id=person['id'])
    except Person.DoesNotExist:
        person_obj = Person.objects.create(
            tmdb_id=person['id'],
            name=person['name'],
            profile_path='{0}{1}'.format(image_root, person['profile_path'])
        )
    return person_obj


def create_movie(movie):

    image_root = 'http://image.tmdb.org/t/p/w300'

    try:
        movie_obj = Movie.objects.get(tmdb_id=movie['id'])
    except Movie.DoesNotExist:
        release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')
        movie_obj = Movie.objects.create(
            tmdb_id=movie['id'],
            title=movie['title'],
            overview=movie['overview'],
            release_date=release_date,
            popularity=movie['popularity'],
            poster_path='{0}{1}'.format(image_root, movie['poster_path']),
            vote_count=movie['vote_count'],
            vote_average=movie['vote_average'],
            similars_ids=movie['similar']
        )

        for genre_id in movie['genre_ids']:
            genre = Genre.objects.get(tmdb_id=genre_id)
            movie_obj.genres.add(genre)
    return movie_obj


def parse_response(url, page_number):

    data = request_page(url, page_number)
    total_pages = int(data['total_pages'])
    write_json(data['results'])

    return total_pages


def get_movies():

    movies_urls = ['movie/popular']

    for url in movies_urls:
        total_pages = parse_response(url, 1)
        for next_page in range(2, total_pages+1):
            parse_response(url, next_page)


if __name__ == '__main__':
    get_movies()
