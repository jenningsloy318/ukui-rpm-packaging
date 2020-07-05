
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := $(shell { grep  "Name" ukui-media.spec| awk  '{print $$2}'; } )
PKG_VERSION := $(shell { grep  "Version" ukui-media.spec| awk  '{print $$2}'; } )

all: build 

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/ukui-media  -w /root/ukui-media docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"


deps:
	@echo ">> install dependencies"
	dnf install -y  intltool qt5-qtbase-devel libcanberra-devel gsettings-qt-devel glib2-devel gtk3-devel mate-desktop-devel libmatemixer-devel libxml2-devel mate-common qt5-qtsvg-devel qt5-qtmultimedia-devel qt5-qtx11extras-devel bamf-devel libXrandr-devel libXtst-devel libX11-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5
	ln -s /usr/bin/lrelease-qt5 /usr/bin/lrelease

download-source:
	@echo "download source code"
	mkdir -p ~/rpmbuild/SOURCES/
	curl -SL https://github.com/ukui/${PKG_NAME}/archive/${PKG_VERSION}.zip#/${PKG_NAME}-${PKG_VERSION}.zip -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.zip

build: | deps download-source
	@echo ">> building rpms"
	rpmbuild -ba ukui-media.spec
clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/ukui-media* rpmbuild/RPMS/x86_64/ukui-media* ~/rpmbuild/SOURCES/ukui-media* ~/rpmbuild/RPMS/x86_64/ukui-media* 

.PHONY: build  clean