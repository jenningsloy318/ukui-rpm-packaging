
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build  clean

docker-builder:
	$(DOCKER) build -t docker.io/jenningsloy318/ukui-power-manager-builder:f32  -f Dockerfile .

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run --ulimit=host  --privileged -v `pwd`:/root docker.io/jenningsloy318/ukui-power-manager-builder:f32  bash  /root/build.sh 

deps:
	@echo ">> install dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  gtk3-devel libwnck3-devel qt5-qtbase-devel intltool libcanberra-devel libcanberra-gtk3 glib2-devel dbus-glib-devel libnotify-devel libtool libgcrypt-devel upower-devel libX11-devel libXext-devel libXrandr-devel perl-XML-Parser qt5-qtx11extras-devel gsettings-qt-devel mate-common mate-desktop-devel qt5-qtcharts-devel xmlto yelp-tools libgnome-keyring-devel 
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

build: | deps 
	@echo ">> building rpms"
	rpmbuild -ba ukui-power-manager.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/ukui-power-manager* rpmbuild/RPMS/x86_64/ukui-power-manager* ~/rpmbuild/SOURCES/ukui-power-manager* ~/rpmbuild/RPMS/x86_64/ukui-power-manager* 
	$(DOCKER) container rm -a

.PHONY: build  clean