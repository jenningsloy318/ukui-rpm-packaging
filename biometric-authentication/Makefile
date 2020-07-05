
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
DIST := $(shell { rpm --eval "%{dist}";} 2>/dev/null)
PKG_NAME := $(shell { grep  "Name" biometric-authentication.spec| awk  '{print $$2}'; } )
PKG_VERSION := $(shell { grep  "Version" biometric-authentication.spec| awk  '{print $$2}'; } )

all: build 


docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/biometric-authentication  -w /root/biometric-authentication docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"

deps:
	@echo ">> install dependencies"
	dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros   automake python3-devel glib2-devel gtk3-devel libusb-devel sqlite-devel  polkit-devel libtool libuuid-devel  git gtk-doc meson glib2-devel libusb-devel nss-devel pixman-devel

build-libfprint:
	@echo ">> build libfprint-devel"
	rpm -ivh https://mirrors.tuna.tsinghua.edu.cn/fedora/releases/31/Everything/source/tree/Packages/l/libfprint-1.0-1.fc31.src.rpm  
	rpmbuild  -ba /root/rpmbuild/SPECS/libfprint.spec 
	rpm -ihv --force /root/rpmbuild/RPMS/x86_64/libfprint-1.0-1${DIST}.x86_64.rpm /root/rpmbuild/RPMS/x86_64/libfprint-devel-1.0-1${DIST}.x86_64.rpm

download-source:
	@echo "download source code"
	mkdir -p ~/rpmbuild/SOURCES/
	curl -SL https://github.com/ukui/${PKG_NAME}/archive/${PKG_VERSION}.zip#/${PKG_NAME}-${PKG_VERSION}.zip -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.zip

build: | deps build-libfprint download-source
	@echo ">> building rpms"
	cp biometric-authentication-unitdir.patch ~/rpmbuild/SOURCES
	rpmbuild  -ba biometric-authentication.spec
	
clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/biometric-authentication* rpmbuild/RPMS/x86_64/biometric-authentication* ~/rpmbuild/SOURCES/biometric-authentication* ~/rpmbuild/RPMS/x86_64/biometric-authentication* 

.PHONY: build  clean