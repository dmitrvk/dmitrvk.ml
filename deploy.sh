docker build --build-arg API_URL='https://dmitrvk.ml/api' --tag dmitrvkml_frontend --file Dockerfile.prod .
docker build --tag dmitrvkml_backend --file ./api/Dockerfile.prod ./api
docker-compose --file docker-compose.prod.yml up -d
