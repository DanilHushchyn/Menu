MANAGE = python3 manage.py

run:
	$(MANAGE) runserver

m1:
	$(MANAGE) makemigrations

m2:
	$(MANAGE) migrate

superuser:
	$(MANAGE) createsuperuser

init:
	$(MANAGE) makemigrations
	$(MANAGE) migrate
	$(MANAGE) createsuperuser