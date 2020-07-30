
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
DIST := $(shell { rpm --eval "%{dist}";} 2>/dev/null)
PKG_NAME := biometric-authentication
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
	dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros   automake python3-devel glib2-devel gtk3-devel libusb-devel sqlite-devel  polkit-devel libtool libuuid-devel  git gtk-doc meson glib2-devel libusb-devel nss-devel pixman-devel

build-libfprint:
	@echo ">> build libfprint-devel"
	rpm -ivh https://mirrors.tuna.tsinghua.edu.cn/fedora/releases/31/Everything/source/tree/Packages/l/libfprint-1.0-1.fc31.src.rpm  
	rpmbuild  -ba /root/rpmbuild/SPECS/libfprint.spec 
	rpm -ihv --force /root/rpmbuild/RPMS/x86_64/libfprint-1.0-1${DIST}.x86_64.rpm /root/rpmbuild/RPMS/x86_64/libfprint-devel-1.0-1${DIST}.x86_64.rpm

download-source:
	@echo "download ${PKG_NAME} source code"
	mkdir -p ~/rpmbuild/SOURCES/
	git clone https://github.com/ukui/${PKG_NAME}
	cd ${PKG_NAME} && git archive  --format=tar.gz --prefix=${PKG_NAME}-${PKG_VERSION}/  -o  ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.tar.gz  ${GitTag}
	rm -rf ${PKG_NAME} 

build: | deps build-libfprint download-source
	@echo ">> building rpms"
	cp biometric-authentication-unitdir.patch ~/rpmbuild/SOURCES
	rpmbuild  -ba  ${PKG_NAME}.spec
	
clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/${PKG_NAME}* rpmbuild/RPMS/x86_64/${PKG_NAME}* ~/rpmbuild/SOURCES/${PKG_NAME}* ~/rpmbuild/RPMS/x86_64/${PKG_NAME}* 

.PHONY: build docker-build deps download-source clean