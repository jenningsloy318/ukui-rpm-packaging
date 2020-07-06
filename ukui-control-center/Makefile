
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := $(shell { grep  "Name" ukui-control-center.spec| awk  '{print $$2}'; } )
PKG_VERSION := $(shell { grep  "Version" ukui-control-center.spec| awk  '{print $$2}'; } )

all: build 

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/ukui-control-center  -w /root/ukui-control-center docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"

deps:
	@echo ">> install dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros qt5-qtbase-devel qt5-qtsvg-devel gsettings-qt-devel glib2-devel qt5-qtx11extras-devel libmatekbd-devel libxklavier-devel kf5-kconfigwidgets-devel kf5-kconfig-devel qt5-qtdeclarative-devel dconf-devel redshift edid-decode libmatemixer-devel libqtxdg-devel qt5-qtmultimedia-devel libxml2-devel libkscreen-qt5-devel kf5-ki18n-devel libcanberra-devel libXi-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

download-source:
	@echo "download source code"
	mkdir -p ~/rpmbuild/SOURCES/
	curl -SL https://github.com/ukui/${PKG_NAME}/archive/${PKG_VERSION}.zip#/${PKG_NAME}-${PKG_VERSION}.zip -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.zip

build: | deps download-source
	@echo ">> building rpms"
	cp ukui-control-center-libdir.patch ~/rpmbuild/SOURCES
	rpmbuild -ba ukui-control-center.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/ukui-control-center* rpmbuild/RPMS/x86_64/ukui-control-center* ~/rpmbuild/SOURCES/ukui-control-center* ~/rpmbuild/RPMS/x86_64/ukui-control-center* 

.PHONY: build  clean