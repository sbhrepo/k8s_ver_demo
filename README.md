# k8s_ver_demo

## Build Docker image

```sh
make docker
```

## Run Docker Compose

```sh
docker-compose up
```

## use env file and selective pull of services

```sh
docker-compose --env-file .env.version up
docker-compose --env-file .env.version up --pull always k8s-ver-3 k8s-ver-4
```
