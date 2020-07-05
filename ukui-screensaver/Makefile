
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := $(shell { grep  "Name" ukui-screensaver.spec| awk  '{print $$2}'; } )
PKG_VERSION := $(shell { grep  "Version" ukui-screensaver.spec| awk  '{print $$2}'; } )

all: build 

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/ukui-screensaver  -w /root/ukui-screensaver docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"


deps:
	@echo ">> install dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros   qt5-qtbase-devel qt5-qtx11extras-devel  pam-devel qt5-qttools-devel glib2-devel libX11-devel libXtst-devel gsettings-qt-devel 
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

download-source:
	@echo "download source code"
	mkdir -p ~/rpmbuild/SOURCES/
	curl -SL https://github.com/ukui/${PKG_NAME}/archive/${PKG_VERSION}.zip#/${PKG_NAME}-${PKG_VERSION}.zip -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.zip

build: | deps  download-source
	@echo ">> building rpms"
	cp ukui-screensaver-libexec-path.patch ~/rpmbuild/SOURCES
	rpmbuild -ba ukui-screensaver.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/ukui-screensaver* rpmbuild/RPMS/x86_64/ukui-screensaver* ~/rpmbuild/SOURCES/ukui-screensaver* ~/rpmbuild/RPMS/x86_64/ukui-screensaver* 
	$(DOCKER) container rm -a

.PHONY: build  clean