
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build  clean

docker-builder:
	$(DOCKER) build -t docker.io/jenningsloy318/ukwm-builder:f32  -f Dockerfile .

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run --ulimit=host  --privileged -v `pwd`:/root docker.io/jenningsloy318/ukwm-builder:f32  bash  /root/build.sh 

deps:
	@echo ">> install dependencies"
	dnf install -y  which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  gtk3-devel glib2-devel libcanberra-gtk3 libcanberra-devel gobject-introspection-devel gsettings-desktop-schemas-devel json-glib-devel mesa-libgbm-devel pango-devel cairo-devel mesa-libGL-devel libdrm-devel mesa-libEGL-devel gnome-desktop3-devel libgudev-devel libinput-devel startup-notification-devel systemd-devel upower-devel libwacom-devel libxcb-devel libXcomposite-devel libXi-devel libxkbfile-devel libxkbcommon-x11-devel libxkbcommon-devel libX11-xcb libXfixes-devel libXdamage-devel libXcursor-devel libXt-devel libX11-devel libXinerama-devel libXext-devel libXrandr-devel libSM-devel libICE-devel pam-devel wayland-devel wayland-protocols-devel libglvnd-devel libglvnd-core-devel

build: | deps 
	@echo ">> building rpms"
	rpmbuild -ba ukwm.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild
	$(DOCKER) container rm -a

.PHONY: build  clean