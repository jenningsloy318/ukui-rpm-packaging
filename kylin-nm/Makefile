
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := $(shell { grep  "Name" kylin-nm.spec| awk  '{print $$2}'; } )
PKG_VERSION := $(shell { grep  "Version" kylin-nm.spec| awk  '{print $$2}'; } )

all: build 


docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/kylin-nm  -w /root/kylin-nm docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"


deps:
	@echo ">> install dependencies"
	dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros qt5-qtbase-devel  qt5-qtscript-devel qt5-qttools-devel qt5-qtx11extras-devel gsettings-qt-devel kf5-kwindowsystem-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

download-source:
	@echo "download source code"
	mkdir -p ~/rpmbuild/SOURCES/
#	curl -SL https://github.com/ukui/${PKG_NAME}/archive/${PKG_VERSION}.zip#/${PKG_NAME}-${PKG_VERSION}.zip -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.zip
	curl -SL https://github.com/ukui/${PKG_NAME}/archive/v${PKG_VERSION}.tar.gz#/${PKG_NAME}-${PKG_VERSION}.tar.gz -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.tar.gz

build: | deps download-source
	@echo ">> building rpms"
	rpmbuild -ba kylin-nm.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/kylin-nm* rpmbuild/RPMS/x86_64/kylin-nm* ~/rpmbuild/SOURCES/kylin-nm* ~/rpmbuild/RPMS/x86_64/kylin-nm* 

.PHONY: build  clean