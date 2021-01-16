# Flask Starter
docker build . -t flask-app:v1

docker run -d -p 5000:5000 flask-app:v1

docker exec -it 406ed143918a bash