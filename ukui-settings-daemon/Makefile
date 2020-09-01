
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := ukui-settings-daemon
PKG_VERSION := 3.0.0

# set the git tag based on the version
ifneq (,$(filter master,$(PKG_VERSION)))
		GitTag=HEAD
else 
		GitTag=v${PKG_VERSION}
endif

all: build 

docker-build: 
	@echo ">> building ${PKG_NAME} rpms in container"
	$(DOCKER) run    --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"

deps:
	@echo ">> install dependencies for ${PKG_NAME}"
	dnf install -y git which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  libcanberra-devel dbus-glib-devel dconf-devel fontconfig-devel glib2-devel gtk3-devel mate-desktop-devel libmatekbd-devel libmatemixer-devel libnotify-devel polkit-devel nss-devel pulseaudio-libs-devel pulseaudio-qt-devel startup-notification-devel libX11-devel libXext-devel libXi-devel libxklavier-devel libXrandr-devel libXt-devel xorg-x11-proto-devel mate-desktop-devel mate-utils-devel mate-common 

download-source:
	@echo "download ${PKG_NAME} source code"
	mkdir -p ~/rpmbuild/SOURCES/
	rm -rf ${PKG_NAME} 
	git clone https://github.com/ukui/${PKG_NAME}
	cd ${PKG_NAME} && git archive  --format=tar.gz --prefix=${PKG_NAME}-${PKG_VERSION}/  -o  ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.tar.gz  HEAD
	rm -rf ${PKG_NAME} 
	
build: | deps download-source
	@echo ">> building ${PKG_NAME} rpms"
	rpmbuild -ba ${PKG_NAME}.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/${PKG_NAME}* rpmbuild/RPMS/x86_64/${PKG_NAME}* ~/rpmbuild/SOURCES/${PKG_NAME}* ~/rpmbuild/RPMS/x86_64/${PKG_NAME}* 

.PHONY: build docker-build deps download-source clean
