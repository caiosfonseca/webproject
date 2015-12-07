import requests
from datetime import datetime
from core.models import Person
from core.models import Movie


def clean_people():

    for person in Person.objects.all():
        if "None" in person.profile_path:
            person.delete()


def request_data(person):

    api_key = '43a11d4a123a0d76d473e4f70abc1ce8'
    root_url = 'https://api.themoviedb.org/3/person/'

    person_url = '{0}{1}?api_key={2}'.format(
        root_url,
        person.tmdb_id,
        api_key
    )
    data = requests.get(person_url).json()
    return data


def update_person(person, data):

    try:
        if len(data['also_known_as']) > 0:
            person.nickname = data['also_known_as'][0]
        person.biography = data['biography']
        person.birthday = datetime.strptime(data['birthday'], '%Y-%m-%d')
        if data['deathday']:
            person.deathday = datetime.strptime(data['deathday'], '%Y-%m-%d')
        person.place_of_birth = data['place_of_birth']
        person.popularity = data['popularity']
        person.save()
    except:
        person.delete()


def get_people():

    clean_people()
    people = Person.objects.all()
    for person in people:
        data = request_data(person)
        update_person(person, data)
        print(person.name)


if __name__ == '__main__':
    get_people()
