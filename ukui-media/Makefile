
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build  clean

docker-builder:
	$(DOCKER) build -t docker.io/jenningsloy318/ukui-media-builder:f32  -f Dockerfile .

docker-build: 
	@echo ">> building rpms"
	$(DOCKER) run --ulimit=host  --privileged -v `pwd`:/root docker.io/jenningsloy318/ukui-media-builder:f32  bash  /root/build.sh 

deps:
	@echo ">> install dependencies"
	dnf install -y  intltool qt5-qtbase-devel libcanberra-devel gsettings-qt-devel glib2-devel gtk3-devel mate-desktop-devel libmatemixer-devel libxml2-devel mate-common qt5-qtsvg-devel qt5-qtmultimedia-devel qt5-qtx11extras-devel bamf-devel libXrandr-devel libXtst-devel libX11-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

build: | deps
	@echo ">> building rpms"
	rpmbuild -ba ukui-media.spec
clean:
	@echo ">> clean up"
	rm -rf rpmbuild
	$(DOCKER) container rm -a

.PHONY: build  clean