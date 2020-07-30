
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
DIST := $(shell { rpm --eval "%{dist}";} 2>/dev/null)
SAASound := $(shell { dnf search -q SAASound-devel ;} 2>/dev/null)
PKG_NAME := ukui-panel
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


SAASound-build:
ifndef SAASound
		@echo ">> building SAASound-devel from source"
		rpm -ivh 	https://mirrors.tuna.tsinghua.edu.cn/fedora/releases/32/Everything/source/tree/Packages/s/SAASound-3.2-24.fc32.src.rpm
		rpmbuild -ba 	/root/rpmbuild/SPECS/SAASound.spec
		rpm -ihv --force  /root/rpmbuild/RPMS/x86_64/SAASound-3.2-24${DIST}.x86_64.rpm /root/rpmbuild/RPMS/x86_64/SAASound-devel-3.2-24${DIST}.x86_64.rpm
else 
		@echo ">> install SAASound-devel from repository"
		dnf install -y SAASound-devel
endif 

deps:
	@echo ">> install ${PKG_NAME} dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  dbusmenu-qt5-devel glib2-devel libicu-devel kf5-solid-devel kf5-kwindowsystem-devel pulseaudio-libs-devel pulseaudio-qt-devel qt5-qtsvg-devel qt5-qtx11extras-devel lm_sensors-devel libstatgrab-devel libX11-devel libxcb-devel xcb-util-devel xcb-util-keysyms-devel xcb-util-image-devel libXcomposite-devel libXdamage-devel libxkbcommon-devel libxkbcommon-x11-devel libXrandr-devel qt5-qtwebkit-devel libqtxdg-devel qt5-qttools-devel gsettings-qt-devel dconf-devel qt5-qtbase-devel qt5-qtbase-private-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

download-source:
	@echo "download ${PKG_NAME} source code"
	mkdir -p ~/rpmbuild/SOURCES/
	git clone https://github.com/ukui/${PKG_NAME}
	cd ${PKG_NAME} && git archive  --format=tar.gz --prefix=${PKG_NAME}-${PKG_VERSION}/  -o  ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.tar.gz  ${GitTag}
	rm -rf ${PKG_NAME} 

build: | deps  SAASound-build download-source
	@echo ">> building ${PKG_NAME} rpms"
	rpmbuild -ba ${PKG_NAME}.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/${PKG_NAME}* rpmbuild/RPMS/x86_64/${PKG_NAME}* ~/rpmbuild/SOURCES/${PKG_NAME}* ~/rpmbuild/RPMS/x86_64/${PKG_NAME}* 
	

.PHONY: build docker-build deps SAASound-build download-source clean