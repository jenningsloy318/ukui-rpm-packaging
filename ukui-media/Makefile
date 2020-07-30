
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := ukui-media
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
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"


deps:
	@echo ">> install dependencies for ${PKG_NAME}"
	dnf install -y  intltool qt5-qtbase-devel libcanberra-devel gsettings-qt-devel glib2-devel gtk3-devel mate-desktop-devel libmatemixer-devel libxml2-devel mate-common qt5-qtsvg-devel qt5-qtmultimedia-devel qt5-qtx11extras-devel bamf-devel libXrandr-devel libXtst-devel libX11-devel kf5-kwindowsystem-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5
	ln -sf /usr/bin/lrelease-qt5 /usr/bin/lrelease

download-source:
	@echo "download ${PKG_NAME} source code"
	mkdir -p ~/rpmbuild/SOURCES/
	git clone https://github.com/ukui/${PKG_NAME}
	cd ${PKG_NAME} && git archive  --format=tar.gz --prefix=${PKG_NAME}-${PKG_VERSION}/  -o  ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.tar.gz  ${GitTag}
	rm -rf ${PKG_NAME} 

build: | deps download-source
	@echo ">> building ${PKG_NAME} rpms"
	rpmbuild -ba ${PKG_NAME}.spec
clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/${PKG_NAME}* rpmbuild/RPMS/x86_64/${PKG_NAME}* ~/rpmbuild/SOURCES/${PKG_NAME}* ~/rpmbuild/RPMS/x86_64/${PKG_NAME}* 


.PHONY: build docker-build deps download-source clean