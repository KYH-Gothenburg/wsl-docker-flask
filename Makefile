start:
	docker-compose up -d
	watchman-make -p '**/*.py' -s 1 --run 'touch ./flask/uwsgi-reload'
stop:
	docker-compose stop