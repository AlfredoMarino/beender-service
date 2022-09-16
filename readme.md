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

Run docker compose
    
SERVICE             PORT
- beender-service:    6060
- postgresql:         5432
- pgadmin:            5050
````
docker-compose up
```

pgadmin password: admin