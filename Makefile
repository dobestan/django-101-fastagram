migrate:
	python fastagram/manage.py makemigrations users posts tags
	python fastagram/manage.py migrate