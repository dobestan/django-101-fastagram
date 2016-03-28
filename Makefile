migrate:
	python fastagram/manage.py makemigrations users posts
	python fastagram/manage.py migrate