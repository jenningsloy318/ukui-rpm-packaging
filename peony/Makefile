
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
DIST := $(shell { rpm --eval "%{dist}";} 2>/dev/null)
PKG_NAME := peony
PKG_VERSION := 3.0.3
PKG_RELEASE :=$(shell { grep "Release" ${PKG_NAME}.spec| awk '{print $$2}'|sed "s/%{?dist}/${DIST}/g"; } )
EXT_PKG_NAME := peony-extensions
EXT_PKG_VERSION := 3.0.1



# set the git tag based on the version
ifneq (,$(filter master,$(PKG_VERSION)))
		GitTag=HEAD
else 
		GitTag=v${PKG_VERSION}
endif

all: build 

docker-build-f33: 
	@echo ">> building ${PKG_NAME} and  ${PKG_NAME}-extensions rpms in container"
	$(DOCKER) run    --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/fedora:33   /bin/bash -c "dnf install -y make curl rpm-build git  https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$$(rpm -E %{fedora}).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$$(rpm -E %{fedora}).noarch.rpm && make build "

docker-build-centos8: 
	@echo ">> building ${PKG_NAME} and  ${PKG_NAME}-extensions rpms in container"
	$(DOCKER) run    --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/centos:8   /bin/bash -c "dnf install -y make curl rpm-build https://mirrors.tuna.tsinghua.edu.cn/epel/epel-release-latest-8.noarch.rpm https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm && make build"

peony-deps:
	@echo ">> install dependencies for ${PKG_NAME}"
	dnf -y install git which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros qt5-qtbase-devel qt5-qttools-devel glib2-devel qt5-qtbase-devel gsettings-qt-devel kf5-kwindowsystem-devel poppler-qt5-devel qt5-qtx11extras-devel qt5-qtbase-private-devel  qt5-linguist libudisks2-devel libnotify-devel libcanberra-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

peony-extensions-deps:
	@echo ">> install dependencies for ${PKG_NAME}-extensions"
	dnf -y install git which gcc gcc-c++ make cmake cmake-rpm-macros kf5-rpm-macros autoconf automake intltool rpm-build qt5-qtsvg-devel qt5-qtx11extras-devel glib2-devel qt5-qtbase-devel qt5-qttools-devel poppler-qt5-devel gsettings-qt-devel peony-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

download-source-peony:
	@echo "download ${PKG_NAME} source code"
	mkdir -p ~/rpmbuild/SOURCES/
	rm -rf ${PKG_NAME} 
	git clone https://github.com/ukui/${PKG_NAME}
	cd ${PKG_NAME} && git archive  --format=tar.gz --prefix=${PKG_NAME}-${PKG_VERSION}/  -o  ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.tar.gz  HEAD
	rm -rf ${PKG_NAME}

download-source-peony-extensions:
	@echo "download ${EXT_PKG_NAME} source code"
	mkdir -p ~/rpmbuild/SOURCES/
	rm -rf ${EXT_PKG_NAME}
	git clone https://github.com/ukui/${PKG_NAME}-extensions
	cd ${EXT_PKG_NAME} && git archive  --format=tar.gz --prefix=${EXT_PKG_NAME}-${EXT_PKG_VERSION}/  -o  ~/rpmbuild/SOURCES/${EXT_PKG_NAME}-${EXT_PKG_VERSION}.tar.gz  HEAD 
	rm -rf ${EXT_PKG_NAME}



build-peony: | peony-deps download-source-peony
	@echo ">> building ${PKG_NAME} rpms"
	rpmbuild -ba ${PKG_NAME}.spec
	rpm -ihv --force  /root/rpmbuild/RPMS/x86_64/{${PKG_NAME}-common-${PKG_VERSION}-${PKG_RELEASE}.x86_64.rpm,${PKG_NAME}-devel-${PKG_VERSION}-${PKG_RELEASE}.x86_64.rpm,${PKG_NAME}-libs-${PKG_VERSION}-${PKG_RELEASE}.x86_64.rpm}


build-peony-extensions: | build-peony peony-extensions-deps download-source-peony-extensions
	@echo ">> building ${EXT_PKG_NAME} rpms"
	rpmbuild -ba ${EXT_PKG_NAME}.spec

build:
	make build-peony
	make build-peony-extensions

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/${PKG_NAME}* rpmbuild/RPMS/x86_64/${PKG_NAME}* ~/rpmbuild/SOURCES/${PKG_NAME}* ~/rpmbuild/RPMS/x86_64/${PKG_NAME}* 

.PHONY: build docker-build-f33 docker-build-centos8 peony-deps peony-extensions-deps  download-source-peony download-source-peony-extensions clean
