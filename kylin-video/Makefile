
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := kylin-video
PKG_VERSION := 2.1.0

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
	dnf -y install git qt5-qtbase-devel qt5-qtscript-devel qt5-qttools-devel qt5-linguist qt5-qtbase-private-devel qt5-qtx11extras-devel zlib-devel libX11-devel libcrystalhd-devel qt5-qtsvg-devel libXext-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

download-source:
	@echo "download ${PKG_NAME} source code"
	mkdir -p ~/rpmbuild/SOURCES/
	rm -rf ${PKG_NAME} 
	git clone https://github.com/UbuntuKylin/${PKG_NAME}
	cd ${PKG_NAME} && git archive  --format=tar.gz --prefix=${PKG_NAME}-${PKG_VERSION}/  -o  ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.tar.gz  HEAD
	rm -rf ${PKG_NAME} 

build: | deps download-source
	@echo ">> building rpms"
	rpmbuild -ba ${PKG_NAME}.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/${PKG_NAME}* rpmbuild/RPMS/x86_64/${PKG_NAME}* ~/rpmbuild/SOURCES/${PKG_NAME}* ~/rpmbuild/RPMS/x86_64/${PKG_NAME}* 

.PHONY: build docker-build deps download-source clean
