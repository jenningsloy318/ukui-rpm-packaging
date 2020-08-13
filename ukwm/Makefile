
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := ukwm
PKG_VERSION := 1.2.0

# set the git tag based on the version
ifneq (,$(filter master,$(PKG_VERSION)))
		GitTag=HEAD
else 
		GitTag=v${PKG_VERSION}
endif

all: build 

docker-build: 
	@echo ">> building ${PKG_NAME} rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/ukui-window-switch  -w /root/ukui-window-switch docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"

deps:
	@echo ">> install dependencies for ${PKG_NAME}"
	dnf install -y git which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  gtk3-devel glib2-devel libcanberra-gtk3 libcanberra-devel gobject-introspection-devel gsettings-desktop-schemas-devel json-glib-devel mesa-libgbm-devel pango-devel cairo-devel mesa-libGL-devel libdrm-devel mesa-libEGL-devel gnome-desktop3-devel libgudev-devel libinput-devel startup-notification-devel systemd-devel upower-devel libwacom-devel libxcb-devel libXcomposite-devel libXi-devel libxkbfile-devel libxkbcommon-x11-devel libxkbcommon-devel libX11-xcb libXfixes-devel libXdamage-devel libXcursor-devel libXt-devel libX11-devel libXinerama-devel libXext-devel libXrandr-devel libSM-devel libICE-devel pam-devel wayland-devel wayland-protocols-devel libglvnd-devel libglvnd-core-devel


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
