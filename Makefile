.PHONY: docker

ifndef tag
override tag=latest
endif

docker:
	docker build --rm -t k8s_ver_demo:${tag} .