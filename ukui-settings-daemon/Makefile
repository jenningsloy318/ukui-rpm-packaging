
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build  clean


docker-builder:
	$(DOCKER) build -t docker.io/jenningsloy318/ukui-settings-daemon-builder:f32  -f Dockerfile .

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run --ulimit=host  --privileged -v `pwd`:/root docker.io/jenningsloy318/ukui-settings-daemon-builder:f32  bash  /root/build.sh 

deps:
	@echo ">> install dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  libcanberra-devel dbus-glib-devel dconf-devel fontconfig-devel glib2-devel gtk3-devel mate-desktop-devel libmatekbd-devel libmatemixer-devel libnotify-devel polkit-devel nss-devel pulseaudio-libs-devel pulseaudio-qt-devel startup-notification-devel libX11-devel libXext-devel libXi-devel libxklavier-devel libXrandr-devel libXt-devel xorg-x11-proto-devel mate-desktop-devel mate-utils-devel mate-common 

build: | deps 
	@echo ">> building rpms"
	rpmbuild -ba ukui-settings-daemon.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild
	$(DOCKER) container rm -a

.PHONY: build  clean