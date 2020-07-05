
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := $(shell { grep  "Name" ukui-wallpapers.spec| awk  '{print $$2}'; } )
PKG_VERSION := $(shell { grep  "Version" ukui-wallpapers.spec| awk  '{print $$2}'; } )

all: build 

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/ukui-wallpapers  -w /root/ukui-wallpapers docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"

deps:
	@echo ">> install dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros ninja-build meson

download-source:
	@echo "download source code"
	mkdir -p ~/rpmbuild/SOURCES/
	curl -SL https://github.com/ukui/${PKG_NAME}/archive/${PKG_VERSION}.zip#/${PKG_NAME}-${PKG_VERSION}.zip -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.zip

build: | deps download-source
	@echo ">> building rpms"
	rpmbuild -ba ukui-wallpapers.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/ukui-wallpapers* rpmbuild/RPMS/x86_64/ukui-wallpapers* ~/rpmbuild/SOURCES/ukui-wallpapers* ~/rpmbuild/RPMS/x86_64/ukui-wallpapers* 

.PHONY: build  clean