.PHONY: docker

ifndef tag
override tag=latest
endif

docker:
	DOCKER_BUILDKIT=1 docker build --rm -t sbh69/k8s-ver-demo:${tag} .