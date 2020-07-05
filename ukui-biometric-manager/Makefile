
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := $(shell { grep  "Name" ukui-biometric-manager.spec| awk  '{print $$2}'; } )
PKG_VERSION := $(shell { grep  "Version" ukui-biometric-manager.spec| awk  '{print $$2}'; } )

all: build 

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/ukui-biometric-manager  -w /root/ukui-biometric-manager docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"

deps:
	@echo ">> install dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros qt5-qtbase-devel qt5-qttools-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

download-source:
	@echo "download source code"
	mkdir -p ~/rpmbuild/SOURCES/
	curl -SL https://github.com/ukui/${PKG_NAME}/archive/${PKG_VERSION}.zip#/${PKG_NAME}-${PKG_VERSION}.zip -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.zip

build: | deps download-source
	@echo ">> building rpms"
	rpmbuild -ba ukui-biometric-manager.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/ukui-biometric-manager* rpmbuild/RPMS/x86_64/ukui-biometric-manager* ~/rpmbuild/SOURCES/ukui-biometric-manager* ~/rpmbuild/RPMS/x86_64/ukui-biometric-manager* 

.PHONY: build  clean