
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := ukui-control-center
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
	$(DOCKER) run    --rm --privileged -v `pwd`:/root  -w /root/ docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"

deps:
	@echo ">> install dependencies for ${PKG_NAME}"
	dnf install -y git which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros qt5-qtbase-devel qt5-qtsvg-devel gsettings-qt-devel glib2-devel qt5-qtx11extras-devel libmatekbd-devel libxklavier-devel kf5-kconfigwidgets-devel kf5-kconfig-devel qt5-qtdeclarative-devel dconf-devel edid-decode libmatemixer-devel  qt5-qtmultimedia-devel libxml2-devel libkscreen-qt5-devel kf5-ki18n-devel libcanberra-devel libXi-devel mate-desktop-devel libxkbcommon-devel libxkbfile-devel qt5-linguist kf5-kwindowsystem-devel kf5-kguiaddons-devel kf5-kcoreaddons-devel boost-devel libxcb-devel xcb-util-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

download-source:
	@echo "download ${PKG_NAME} source code"
	mkdir -p ~/rpmbuild/SOURCES/
	rm -rf ${PKG_NAME} 
	git clone https://github.com/ukui/${PKG_NAME}
	cd ${PKG_NAME} && git archive  --format=tar.gz --prefix=${PKG_NAME}-${PKG_VERSION}/  -o  ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.tar.gz HEAD
	rm -rf ${PKG_NAME} 

build: | deps download-source
	@echo ">> building ${PKG_NAME} rpms"
	rpmbuild -ba ${PKG_NAME}.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/${PKG_NAME}* rpmbuild/RPMS/x86_64/${PKG_NAME}* ~/rpmbuild/SOURCES/${PKG_NAME}* ~/rpmbuild/RPMS/x86_64/${PKG_NAME}* 

.PHONY: build docker-build deps download-source clean
