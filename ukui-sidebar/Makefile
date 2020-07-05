
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := $(shell { grep  "Name" ukui-sidebar.spec| awk  '{print $$2}'; } )
PKG_VERSION := $(shell { grep  "Version" ukui-sidebar.spec| awk  '{print $$2}'; } )

all: build 

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/ukui-sidebar  -w /root/ukui-sidebar docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"


deps:
	@echo ">> install dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  qt5-qtbase-devel qt5-qttools-devel glib2-devel qt5-qtbase-devel qt5-qtsvg-devel dconf-devel gsettings-qt-devel qt5-qtmultimedia-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

download-source:
	@echo "download source code"
	mkdir -p ~/rpmbuild/SOURCES/
	curl -SL https://github.com/ukui/${PKG_NAME}/archive/${PKG_VERSION}.zip#/${PKG_NAME}-${PKG_VERSION}.zip -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.zip

build: | deps  download-source
	@echo ">> building rpms"
	cp ukui-sidebar-plugin-libdir.patch ~/rpmbuild/SOURCES/
	rpmbuild -ba ukui-sidebar.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/ukui-sidebar* rpmbuild/RPMS/x86_64/ukui-sidebar* ~/rpmbuild/SOURCES/ukui-sidebar* ~/rpmbuild/RPMS/x86_64/ukui-sidebar* 

.PHONY: build  clean