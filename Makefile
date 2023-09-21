dev-start:
	python3 manage.py runserver --settings=config.settings.dev

dev-install:
	pip install -r requirements/dev.txt

prod-start:
	python3 manage.py runserver --settings=config.settings.prod

prod-install:
	pip install -r requirements/prod.txt

dev-migrate:
	python3 manage.py migrate --settings=config.settings.dev

dev-makemigrations:
	python3 manage.py makemigrations --settings=config.settings.dev

prod-migrate:
	python3 manage.py migrate --settings=config.settings.prod

prod-makemigrations:
	python3 manage.py makemigrations --settings=config.settings.prod

dev-showmigrations:
	python3 manage.py showmigrations --settings=config.settings.dev

dev-sqlmigrate:
	python3 manage.py sqlmigrate $(app) $(migration) --settings=config.settings.dev

dev-createsuperuser:
	python3 manage.py createsuperuser --settings=config.settings.dev

dev-shell:
	python3 manage.py shell --settings=config.settings.dev

prod-shell:
	python3 manage.py shell --settings=config.settings.prod

dev-rollback:
	python3 manage.py migrate $(app) $(migration) --settings=config.settings.dev

dev-test:
	python3 manage.py test -v 2 --traceback --settings=config.settings.dev