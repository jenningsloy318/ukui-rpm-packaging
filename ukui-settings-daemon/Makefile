
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := $(shell { grep  "Name" ukui-settings-daemon.spec| awk  '{print $$2}'; } )
PKG_VERSION := $(shell { grep  "Version" ukui-settings-daemon.spec| awk  '{print $$2}'; } )

all: build 

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/ukui-settings-daemon  -w /root/ukui-settings-daemon docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"

deps:
	@echo ">> install dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  libcanberra-devel dbus-glib-devel dconf-devel fontconfig-devel glib2-devel gtk3-devel mate-desktop-devel libmatekbd-devel libmatemixer-devel libnotify-devel polkit-devel nss-devel pulseaudio-libs-devel pulseaudio-qt-devel startup-notification-devel libX11-devel libXext-devel libXi-devel libxklavier-devel libXrandr-devel libXt-devel xorg-x11-proto-devel mate-desktop-devel mate-utils-devel mate-common 

download-source:
	@echo "download source code"
	mkdir -p ~/rpmbuild/SOURCES/
	curl -SL https://github.com/ukui/${PKG_NAME}/archive/${PKG_VERSION}.zip#/${PKG_NAME}-${PKG_VERSION}.zip -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.zip

build: | deps download-source
	@echo ">> building rpms"
	rpmbuild -ba ukui-settings-daemon.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/ukui-settings-daemon* rpmbuild/RPMS/x86_64/ukui-settings-daemon* ~/rpmbuild/SOURCES/ukui-settings-daemon* ~/rpmbuild/RPMS/x86_64/ukui-settings-daemon* 

.PHONY: build  clean