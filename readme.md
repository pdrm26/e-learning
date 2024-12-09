## First of all run the memcached after that run the project
docker run -it --rm --name memcached -p 11211:11211 memcached:1.6.26 -m 64