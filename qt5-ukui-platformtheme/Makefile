
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := $(shell { grep  "Name" qt5-ukui-platformtheme.spec| awk  '{print $$2}'; } )
PKG_VERSION := $(shell { grep  "Version" qt5-ukui-platformtheme.spec| awk  '{print $$2}'; } )

all: build 


docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/qt5-ukui-platformtheme  -w /root/qt5-ukui-platformtheme docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"

deps:
	@echo ">> install dependencies"
	dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  glib2-devel qt5-qtx11extras-devel kf5-kwindowsystem-devel gsettings-desktop-schemas-devel qt5-qtbase-devel qt5-qtbase-private-devel qt5-qttools-devel gsettings-qt-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

download-source:
	@echo "download source code"
	mkdir -p ~/rpmbuild/SOURCES/
	curl -SL https://github.com/ukui/${PKG_NAME}/archive/${PKG_VERSION}.zip#/${PKG_NAME}-${PKG_VERSION}.zip -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.zip

build: | deps download-source
	@echo ">> building rpms"
	cp qt5-ukui-platformtheme-libdir-and-qmake.patch ~/rpmbuild/SOURCES/qt5-ukui-platformtheme-libdir-and-qmake.patch
	rpmbuild -ba qt5-ukui-platformtheme.spec

build: | deps
	@echo ">> building rpms"
	rpmbuild -ba qt5-ukui-platformtheme.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/qt5-ukui-platformtheme* rpmbuild/RPMS/x86_64/qt5-ukui-platformtheme* ~/rpmbuild/SOURCES/qt5-ukui-platformtheme* ~/rpmbuild/RPMS/x86_64/qt5-ukui-platformtheme* 

.PHONY: build  clean