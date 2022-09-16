# Beender Service

Docker commands:

Build docker image:
```
docker build -t beender-service:latest .
```

Run docker container
```
docker run --name beender-service -it -p 6060:6060 beender-service
```