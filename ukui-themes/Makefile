
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
DIST := $(shell { rpm --eval "%{dist}";} 2>/dev/null)
PKG_NAME := $(shell { grep  "Name" ukui-themes.spec| awk  '{print $$2}'; } )
PKG_VERSION := $(shell { grep  "Version" ukui-themes.spec| awk  '{print $$2}'; } )

all: build 

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/ukui-themes  -w /root/ukui-themes docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"

deps:
ifneq (,$(filter .el%,$(DIST)))
	@echo ">> install dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros sassc
	ln -sf /usr/bin/sassc /usr/bin/sass
else 
	@echo ">> install dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros rubygem-sass
endif

download-source:
	@echo "download source code"
	mkdir -p ~/rpmbuild/SOURCES/
	curl -SL https://github.com/ukui/${PKG_NAME}/archive/${PKG_VERSION}.zip#/${PKG_NAME}-${PKG_VERSION}.zip -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.zip

build: | deps download-source
	@echo ">> building rpms"
	rpmbuild -ba ukui-themes.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/ukui-themes* rpmbuild/RPMS/x86_64/ukui-themes* ~/rpmbuild/SOURCES/ukui-themes* ~/rpmbuild/RPMS/x86_64/ukui-themes* 

.PHONY: build  clean