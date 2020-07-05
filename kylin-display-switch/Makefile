
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := $(shell { grep  "Name" kylin-display-switch.spec| awk  '{print $$2}'; } )
PKG_VERSION := $(shell { grep  "Version" kylin-display-switch.spec| awk  '{print $$2}'; } )

all: build 


docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/kylin-display-switch  -w /root/kylin-display-switch docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"


deps:
	@echo ">> install dependencies"
	dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros python3 python3-setuptools python3-distutils-extra python3-rpm-macros 

download-source:
	@echo "download source code"
	mkdir -p ~/rpmbuild/SOURCES/
	curl -SL https://github.com/ukui/${PKG_NAME}/archive/${PKG_VERSION}.zip#/${PKG_NAME}-${PKG_VERSION}.zip -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.zip

build: | deps download-source
	@echo ">> building rpms"
	rpmbuild  -ba kylin-display-switch.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/kylin-display-switch* rpmbuild/RPMS/x86_64/kylin-display-switch* ~/rpmbuild/SOURCES/kylin-display-switch* ~/rpmbuild/RPMS/x86_64/kylin-display-switch* 

.PHONY: build  clean