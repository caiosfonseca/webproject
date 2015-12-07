run:
	python manage.py runserver

new_db:
	dropdb minweb --if-exists
	createdb minweb
	python manage.py makemigrations
	python manage.py migrate

deps:
	pip install -r requirements.txt

shell:
	python manage.py shell

clean:
	find . -name '*.pyc' -delete

migrations:
	python manage.py makemigrations
	python manage.py migrate

create_user:
	python manage.py createsuperuser

dumpdata:
	python manage.py dumpdata core.Genre > core/fixtures/genres.json
	python manage.py dumpdata core.Person > core/fixtures/people.json
	python manage.py dumpdata core.Movie > core/fixtures/movies.json

loaddata:
	python manage.py loaddata core/fixtures/genres.json
	python manage.py loaddata core/fixtures/people.json
	python manage.py loaddata core/fixtures/movies.json

sync:
	make clean
	make new_db
	make loaddata
	make create_user
