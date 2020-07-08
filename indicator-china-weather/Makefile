
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := $(shell { grep  "Name" indicator-china-weather.spec| awk  '{print $$2}'; } )
PKG_VERSION := $(shell { grep  "Version" indicator-china-weather.spec| awk  '{print $$2}'; } )

all: build 


docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/indicator-china-weather  -w /root/indicator-china-weather docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"


deps:
	@echo ">> install dependencies"
	dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-qtbase-devel  qt5-qtscript-devel qt5-qttools-devel GeoIP-devel

download-source:
	@echo "download source code"
	mkdir -p ~/rpmbuild/SOURCES/
	curl -SL https://github.com/UbuntuKylin/${PKG_NAME}/archive/${PKG_VERSION}.zip#/${PKG_NAME}-${PKG_VERSION}.zip -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.zip

build: | deps download-source
	@echo ">> building rpms"
	rpmbuild  -ba indicator-china-weather.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/indicator-china-weather* rpmbuild/RPMS/x86_64/indicator-china-weather* ~/rpmbuild/SOURCES/indicator-china-weather* ~/rpmbuild/RPMS/x86_64/indicator-china-weather* 

.PHONY: build  clean