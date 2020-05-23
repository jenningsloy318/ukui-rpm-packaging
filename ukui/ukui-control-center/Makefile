
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build  clean

build: 
	@echo ">> building rpms"
	$(DOCKER) run  --privileged -v `pwd`:/root docker.io/jenningsloy318/ukui-builder:f32  bash  /root/build.sh 

clean:
	@echo ">> clean up containers"
	$(DOCKER) container rm -a

.PHONY: build  clean