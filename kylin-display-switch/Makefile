
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build  clean

docker-builder:
	$(DOCKER) build -t docker.io/jenningsloy318/kylin-display-switch-builder:f32  -f Dockerfile .

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host --privileged -v `pwd`:/root docker.io/jenningsloy318/kylin-display-switch-builder:f32  bash  /root/build.sh 

deps:
	@echo ">> install dependencies"
	dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros python3 python3-setuptools python3-distutils-extra python3-rpm-macros 

build: | deps 
	@echo ">> building rpms"
	rpmbuild  -ba kylin-display-switch.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/kylin-display-switch* rpmbuild/RPMS/x86_64/kylin-display-switch* ~/rpmbuild/SOURCES/kylin-display-switch* ~/rpmbuild/RPMS/x86_64/kylin-display-switch* 
	$(DOCKER) container rm -a

.PHONY: build  clean