
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := biometric-authentication
PKG_VERSION := 0.9.63

# set the git tag based on the version
ifneq (,$(filter master,$(PKG_VERSION)))
		GitTag=HEAD
else 
		GitTag=v${PKG_VERSION}
endif

all: build 


docker-build-f33: 
	@echo ">> building ${PKG_NAME} rpms in container"
	$(DOCKER) run    --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/fedora:33   /bin/bash -c "dnf install -y make curl rpm-build git  https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$$(rpm -E %{fedora}).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$$(rpm -E %{fedora}).noarch.rpm && make build"

docker-build-centos8: 
	@echo ">> building ${PKG_NAME} rpms in container"
	$(DOCKER) run    --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/centos:8   /bin/bash -c "dnf install -y make curl rpm-build dnf-plugins-core https://mirrors.tuna.tsinghua.edu.cn/epel/epel-release-latest-8.noarch.rpm https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm centos-stream-release &&	dnf config-manager --enable PowerTools && dnf config-manager --enable Stream-PowerTools && dnf install -y rpmfusion-free-release-tainted rpmfusion-nonfree-release-tainted && make build"

deps:
	@echo ">> install dependencies for ${PKG_NAME}"
	dnf -y install git which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros   automake python3-devel glib2-devel gtk3-devel libusb-devel sqlite-devel  polkit-devel libtool libuuid-devel  git gtk-doc meson glib2-devel libusb-devel nss-devel pixman-devel 

download-source:
	@echo "download ${PKG_NAME} source code"
	mkdir -p ~/rpmbuild/SOURCES/
	rm -rf ${PKG_NAME}
	git clone https://github.com/ukui/${PKG_NAME}
	cd ${PKG_NAME} && git archive  --format=tar.gz --prefix=${PKG_NAME}-${PKG_VERSION}/  -o  ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.tar.gz  HEAD
	rm -rf ${PKG_NAME} 

build-libfprint:
	@echo ">> build libfprint-devel"
	dnf install -y meson gcc gcc-c++ git "pkgconfig(glib-2.0)" "pkgconfig(libusb-1.0)" "pkgconfig(nss)" "pkgconfig(pixman-1)" gtk-doc systemd
	rpmbuild  -ba libfprint.spec
	dnf install -y /root/rpmbuild/RPMS/x86_64/libfprint-1.0-*.rpm /root/rpmbuild/RPMS/x86_64/libfprint-devel-1.0-*.x86_64.rpm

build: | deps  download-source build-libfprint
	@echo ">> building rpms"
	rpmbuild  -ba  ${PKG_NAME}.spec
	
clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/${PKG_NAME}* rpmbuild/RPMS/x86_64/${PKG_NAME}* ~/rpmbuild/SOURCES/${PKG_NAME}* ~/rpmbuild/RPMS/x86_64/${PKG_NAME}* 

.PHONY: build docker-build-f33 docker-build-centos8 deps download-source clean
