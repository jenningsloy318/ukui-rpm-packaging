
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
DIST := $(shell { rpm --eval "%{dist}";} 2>/dev/null)
PKG_NAME := $(shell { grep  "Name" peony.spec| awk  '{print $$2}'; } )
PKG_VERSION := $(shell { grep  "Version" peony.spec| awk  '{print $$2}'; } )
PKG_RELEASE :=$(shell { grep "Release" peony.spec| awk '{print $$2}'|sed "s/%{?dist}/${DIST}/g"; } )

all: build 


docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/peony  -w /root/peony docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"

deps:
	@echo ">> install dependencies"
	dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros   qt5-qtbase-devel qt5-qttools-devel glib2-devel qt5-qtbase-devel gsettings-qt-devel kf5-kwindowsystem-devel poppler-qt5-devel qt5-qtx11extras-devel qt5-qtbase-private-devel 
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

download-source:
	@echo "download source code"
	mkdir -p ~/rpmbuild/SOURCES/
	curl -SL https://github.com/ukui/${PKG_NAME}/archive/${PKG_VERSION}.zip#/${PKG_NAME}-${PKG_VERSION}.zip -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.zip

build: | deps download-source
	@echo ">> building rpms"
	cp peony-libdir.patch ~/rpmbuild/SOURCES/peony-libdir.patch
	rpmbuild -ba peony.spec
	rpm -ihv --force  /root/rpmbuild/RPMS/x86_64/{peony-common-${PKG_VERSION}-${PKG_RELEASE}.x86_64.rpm,peony-devel-${PKG_VERSION}-${PKG_RELEASE}.x86_64.rpm,peony-libs-${PKG_VERSION}-${PKG_RELEASE}.x86_64.rpm}

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/peony* rpmbuild/RPMS/x86_64/peony* ~/rpmbuild/SOURCES/peony* ~/rpmbuild/RPMS/x86_64/peony* 

.PHONY: build  clean