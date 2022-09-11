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

Run docker compose
    
SERVICE             PORT
- beender-service:    5000
- postgresql:         5432
- pgadmin:            5050
````
docker-compose up
```

pgadmin password: admin