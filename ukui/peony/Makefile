
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := peony
PKG_VERSION := 3.0.3
PKG_EXT_NAME := peony-extensions
PKG_EXT_VERSION := 3.0.1



# set the git tag based on the version
ifneq (,$(filter master,$(PKG_VERSION)))
		GitTag=HEAD
else 
		GitTag=v${PKG_VERSION}
endif

all: build 

docker-build: 
	@echo ">> building ${PKG_NAME} and  ${PKG_NAME}-extensions rpms in container"
	$(DOCKER) run    --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/fedora   /bin/bash -c "dnf install -y make curl rpm-build git  https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$$(rpm -E %{fedora}).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$$(rpm -E %{fedora}).noarch.rpm && make build "

peony-deps:
	@echo ">> install dependencies for ${PKG_NAME}"
	dnf -y builddep ${PKG_NAME}.spec
	export libQt5CoreFile=$$(rpm -ql qt5-qtbase|grep  libQt5Core.so.5.....);if file $${libQt5CoreFile} |grep "GNU/Linux"; then  strip --remove-section=.note.ABI-tag $${libQt5CoreFile}; else echo "already stripped";fi 

peony-extensions-deps:
	@echo ">> install dependencies for ${PKG_EXT_NAME}-extensions"
	dnf -y  builddep ${PKG_EXT_NAME}.spec
	export libQt5CoreFile=$$(rpm -ql qt5-qtbase|grep  libQt5Core.so.5.....)
	if file "$${libQt5CoreFile}" |grep   "for GNU/Linux" ; then strip --remove-section=.note.ABI-tag $${libQt5CoreFile}; else echo "already stripped";fi 

download-source-peony:
	@echo ">> download ${PKG_NAME} source code"
	mkdir -p ~/rpmbuild/SOURCES/
	rm -rf ${PKG_NAME} 
	git clone https://github.com/ukui/${PKG_NAME}
	cd ${PKG_NAME} && git archive  --format=tar.gz --prefix=${PKG_NAME}-${PKG_VERSION}/  -o  ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.tar.gz  HEAD
	rm -rf ${PKG_NAME}

download-source-peony-extensions:
	@echo ">> download ${PKG_EXT_NAME} source code"
	mkdir -p ~/rpmbuild/SOURCES/
	rm -rf ${PKG_EXT_NAME}
	git clone https://github.com/ukui/${PKG_EXT_NAME}
	cd ${PKG_EXT_NAME} && git archive  --format=tar.gz --prefix=${PKG_EXT_NAME}-${PKG_EXT_VERSION}/  -o  ~/rpmbuild/SOURCES/${PKG_EXT_NAME}-${PKG_EXT_VERSION}.tar.gz  HEAD 
	rm -rf ${PKG_EXT_NAME}



build-peony: | peony-deps download-source-peony
	@echo ">> building ${PKG_NAME} rpms"
	rpmbuild -ba ${PKG_NAME}.spec
	rpm -ihv --force $${HOME}/rpmbuild/RPMS/x86_64/{${PKG_NAME}-common-${PKG_VERSION}-1$$(rpm -E %{dist}).x86_64.rpm,${PKG_NAME}-devel-${PKG_VERSION}-1$$(rpm -E %{dist}).x86_64.rpm,${PKG_NAME}-libs-${PKG_VERSION}-1$$(rpm -E %{dist}).x86_64.rpm}


build-peony-extensions: | peony-extensions-deps download-source-peony-extensions
	@echo ">> building ${PKG_EXT_NAME} rpms"
	rpmbuild -ba ${PKG_EXT_NAME}.spec

build:
	make build-peony
	make build-peony-extensions

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/${PKG_NAME}* rpmbuild/RPMS/x86_64/${PKG_NAME}* ~/rpmbuild/SOURCES/${PKG_NAME}* ~/rpmbuild/RPMS/x86_64/${PKG_NAME}* 

.PHONY: build docker-build peony-deps peony-extensions-deps  download-source-peony download-source-peony-extensions clean
