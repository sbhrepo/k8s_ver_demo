.PHONY: docker

ifndef tag
override tag=latest
endif

docker:
	DOCKER_BUILDKIT=1 docker build --rm -t k8s_ver_demo:${tag} .