# Beender Service

Docker commands:

Build docker image:
```
docker build -t beender-service:latest .
```

Run docker container
```
docker run --name beender-service -it -p 5000:5000 beender-service
```