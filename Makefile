.PHONY: install
install:
	pip install -r requirements.txt

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: run
run:
	python manage.py runserver

.PHONY: test
test:
	python manage.py test