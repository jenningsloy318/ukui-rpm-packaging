
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := ukui-session-manager
PKG_VERSION := master

# set the git tag based on the version
ifneq (,$(filter master,$(PKG_VERSION)))
		GitTag=HEAD
else 
		GitTag=v${PKG_VERSION}
endif

all: build 

docker-build: 
	@echo ">> building ${PKG_NAME} rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"

deps:
	@echo ">> install dependencies for ${PKG_NAME}"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros   qt5-qtdeclarative-devel qt5-qtbase-devel qt5-qtmultimedia-devel qt5-qtx11extras-devel kf5-kidletime-devel qt5-qttools-devel qt5-qttools qt5-linguist gsettings-qt-devel libXtst-devel libqtxdg-devel systemd-devel 
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

download-source:
	@echo "download ${PKG_NAME} source code"
	mkdir -p ~/rpmbuild/SOURCES/
	git clone https://github.com/ukui/${PKG_NAME}
	cd ${PKG_NAME} && git archive  --format=tar.gz --prefix=${PKG_NAME}-${PKG_VERSION}/  -o  ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.tar.gz  ${GitTag}
	rm -rf ${PKG_NAME} 

build: | deps  download-source
	@echo ">> building ${PKG_NAME} rpms"
	rpmbuild -ba ${PKG_NAME}.spec

clean:
	rm -rf rpmbuild/SOURCES/${PKG_NAME}* rpmbuild/RPMS/x86_64/${PKG_NAME}* ~/rpmbuild/SOURCES/${PKG_NAME}* ~/rpmbuild/RPMS/x86_64/${PKG_NAME}* 

.PHONY: build docker-build deps download-source clean