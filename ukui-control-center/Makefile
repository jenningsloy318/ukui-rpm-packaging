
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build  clean

docker-builder:
	$(DOCKER) build -t docker.io/jenningsloy318/ukui-control-center-builder:f32  -f Dockerfile .

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run --ulimit=host  --privileged -v `pwd`:/root docker.io/jenningsloy318/ukui-control-center-builder:f32  bash  /root/build.sh 

deps:
	@echo ">> install dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros qt5-qtbase-devel qt5-qtsvg-devel gsettings-qt-devel glib2-devel qt5-qtx11extras-devel libmatekbd-devel libxklavier-devel kf5-kconfigwidgets-devel kf5-kconfig-devel qt5-qtdeclarative-devel dconf-devel redshift edid-decode libmatemixer-devel libqtxdg-devel qt5-qtmultimedia-devel libxml2-devel libkscreen-qt5-devel kf5-ki18n-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

build: | deps
	@echo ">> building rpms"
	cp ukui-control-center-libdir.patch ~/rpmbuild/SOURCES
	rpmbuild -ba ukui-control-center.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild
	$(DOCKER) container rm -a

.PHONY: build  clean