
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := $(shell { grep  "Name" ukui-greeter.spec| awk  '{print $$2}'; } )
PKG_VERSION := $(shell { grep  "Version" ukui-greeter.spec| awk  '{print $$2}'; } )

all: build 

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/ukui-greeter  -w /root/ukui-greeter docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"

deps:
	@echo ">> install dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros qt5-qtbase-devel qt5-qtx11extras-devel qt5-qtsvg-devel lightdm-qt5-devel libX11-devel libXtst-devel libXrandr-devel qt5-qttools-devel imlib2-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

download-source:
	@echo "download source code"
	mkdir -p ~/rpmbuild/SOURCES/
	curl -SL https://github.com/ukui/${PKG_NAME}/archive/${PKG_VERSION}.zip#/${PKG_NAME}-${PKG_VERSION}.zip -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.zip

build: | deps download-source
	@echo ">> building rpms"
	rpmbuild -ba ukui-greeter.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/ukui-greeter* rpmbuild/RPMS/x86_64/ukui-greeter* ~/rpmbuild/SOURCES/ukui-greeter* ~/rpmbuild/RPMS/x86_64/ukui-greeter* 

.PHONY: build  clean