
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := $(shell { grep  "Name" ukui-power-manager.spec| awk  '{print $$2}'; } )
PKG_VERSION := $(shell { grep  "Version" ukui-power-manager.spec| awk  '{print $$2}'; } )

all: build 

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/ukui-power-manager  -w /root/ukui-power-manager docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"


deps:
	@echo ">> install dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  gtk3-devel libwnck3-devel qt5-qtbase-devel intltool libcanberra-devel libcanberra-gtk3 glib2-devel dbus-glib-devel libnotify-devel libtool libgcrypt-devel upower-devel libX11-devel libXext-devel libXrandr-devel perl-XML-Parser qt5-qtx11extras-devel gsettings-qt-devel mate-common mate-desktop-devel qt5-qtcharts-devel xmlto yelp-tools libgnome-keyring-devel 
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

download-source:
	@echo "download source code"
	mkdir -p ~/rpmbuild/SOURCES/
	curl -SL https://github.com/ukui/${PKG_NAME}/archive/${PKG_VERSION}.zip#/${PKG_NAME}-${PKG_VERSION}.zip -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.zip

build: | deps  download-source
	@echo ">> building rpms"
	rpmbuild -ba ukui-power-manager.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/ukui-power-manager* rpmbuild/RPMS/x86_64/ukui-power-manager* ~/rpmbuild/SOURCES/ukui-power-manager* ~/rpmbuild/RPMS/x86_64/ukui-power-manager* 

.PHONY: build  clean