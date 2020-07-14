
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
PKG_NAME := $(shell { grep  "Name" ukwm.spec| awk  '{print $$2}'; } )
PKG_VERSION := $(shell { grep  "Version" ukwm.spec| awk  '{print $$2}'; } )

all: build 

docker-build: 
	@echo ">> building ${PKG_NAME} rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/ukui-window-switch  -w /root/ukui-window-switch docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"

deps:
	@echo ">> install dependencies for ${PKG_NAME}"
	dnf install -y  which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  gtk3-devel glib2-devel libcanberra-gtk3 libcanberra-devel gobject-introspection-devel gsettings-desktop-schemas-devel json-glib-devel mesa-libgbm-devel pango-devel cairo-devel mesa-libGL-devel libdrm-devel mesa-libEGL-devel gnome-desktop3-devel libgudev-devel libinput-devel startup-notification-devel systemd-devel upower-devel libwacom-devel libxcb-devel libXcomposite-devel libXi-devel libxkbfile-devel libxkbcommon-x11-devel libxkbcommon-devel libX11-xcb libXfixes-devel libXdamage-devel libXcursor-devel libXt-devel libX11-devel libXinerama-devel libXext-devel libXrandr-devel libSM-devel libICE-devel pam-devel wayland-devel wayland-protocols-devel libglvnd-devel libglvnd-core-devel


download-source:
	@echo "download source code"
	mkdir -p ~/rpmbuild/SOURCES/
	curl -SL https://github.com/ukui/${PKG_NAME}/archive/${PKG_VERSION}.zip#/${PKG_NAME}-${PKG_VERSION}.zip -o ~/rpmbuild/SOURCES/${PKG_NAME}-${PKG_VERSION}.zip

build: | deps download-source
	@echo ">> building rpms"
	rpmbuild -ba ukui-window-switch.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/ukui-window-switch* rpmbuild/RPMS/x86_64/ukui-window-switch* ~/rpmbuild/SOURCES/ukui-window-switch* ~/rpmbuild/RPMS/x86_64/ukui-window-switch* 

.PHONY: build  clean