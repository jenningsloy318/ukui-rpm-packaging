
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := $(shell { grep  "Name" kylin-video.spec| awk  '{print $$2}'; } )
PKG_VERSION := $(shell { grep  "Version" kylin-video.spec| awk  '{print $$2}'; } )

all: build 


docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/kylin-video  -w /root/kylin-video docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"

deps:
	@echo ">> install dependencies"
	dnf -y install  qt5-qtbase-devel qt5-qtscript-devel qt5-qttools-devel qt5-linguist qt5-qtbase-private-devel qt5-qtx11extras-devel zlib-devel libX11-devel libcrystalhd-devel qt5-qtsvg-devel libXext-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

download-source:
	@echo "download source code"
	mkdir -p ~/rpmbuild/SOURCES/
	curl -SL https://github.com/ukui/${PKG_NAME}/archive/${PKG_VERSION}.zip#/${PKG_NAME}-${PKG_VERSION}.zip -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.zip

build: | deps download-source
	@echo ">> building rpms"
	rpmbuild -ba kylin-video.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/kylin-video* rpmbuild/RPMS/x86_64/kylin-video* ~/rpmbuild/SOURCES/kylin-video* ~/rpmbuild/RPMS/x86_64/kylin-video* 

.PHONY: build  clean