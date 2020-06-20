
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build  clean

builder:
	$(DOCKER) build -t docker.io/jenningsloy318/ukui-system-monitor-builder:f32  -f Dockerfile .

build: 
	@echo ">> building rpms"
	$(DOCKER) run --ulimit=host  --privileged -v `pwd`:/root docker.io/jenningsloy318/ukui-system-monitor-builder:f32  bash  /root/build.sh 

clean:
	@echo ">> clean up containers"
	$(DOCKER) container rm -a

.PHONY: build  clean