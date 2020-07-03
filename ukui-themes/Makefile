
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
DIST := $(shell { rpm --eval "%{dist}";} 2>/dev/null)

all: build  clean

docker-builder:
	$(DOCKER) build -t docker.io/jenningsloy318/ukui-themes-builder:f32  -f Dockerfile .

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host --privileged -v `pwd`:/root docker.io/jenningsloy318/ukui-themes-builder:f32  bash  /root/build.sh 

deps:
ifneq (,$(filter .el%,$(DIST)))
	@echo ">> install dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros sassc
	ln -sf /usr/bin/sassc /usr/bin/sass
else 
	@echo ">> install dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros rubygem-sass
endif

build: | deps 
	@echo ">> building rpms"
	rpmbuild -ba ukui-themes.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/ukui-themes* rpmbuild/RPMS/x86_64/ukui-themes* ~/rpmbuild/SOURCES/ukui-themes* ~/rpmbuild/RPMS/x86_64/ukui-themes* 
	$(DOCKER) container rm -a

.PHONY: build  clean