
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := $(shell { grep  "Name" ukui-biometric-auth.spec| awk  '{print $$2}'; } )
PKG_VERSION := $(shell { grep  "Version" ukui-biometric-auth.spec| awk  '{print $$2}'; } )

all: build 

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/ukui-biometric-auth  -w /root/ukui-biometric-auth docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"

deps:
	@echo ">> install dependencies"
	dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros qt5-qtbase-devel qt5-qttools-devel pam-devel polkit-qt5-1-devel 
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

download-source:
	@echo "download source code"
	mkdir -p ~/rpmbuild/SOURCES/
	curl -SL https://github.com/ukui/${PKG_NAME}/archive/${PKG_VERSION}.zip#/${PKG_NAME}-${PKG_VERSION}.zip -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.zip

build: | deps download-source
	@echo ">> building rpms"
	cp ukui-biometric-auth-libdir.patch ~/rpmbuild/SOURCES
	rpmbuild -ba ukui-biometric-auth.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/ukui-biometric-auth* rpmbuild/RPMS/x86_64/ukui-biometric-auth* ~/rpmbuild/SOURCES/ukui-biometric-auth* ~/rpmbuild/RPMS/x86_64/ukui-biometric-auth* 

.PHONY: build  clean