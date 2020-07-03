
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build  clean

docker-builder:
	$(DOCKER) build -t docker.io/jenningsloy318/peony-extensions-builder:f32  -f Dockerfile .

docker-build: 
	@echo ">> building rpms"
	$(DOCKER) run  --ulimit=host --privileged -v `pwd`:/root docker.io/jenningsloy318/peony-extensions-builder:f32  bash  /root/build.sh 

deps:
	@echo ">> install dependencies"
	dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-qtsvg-devel qt5-qtx11extras-devel glib2-devel qt5-qtbase-devel qt5-qttools-devel poppler-qt5-devel gsettings-qt-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

build: | deps
	@echo ">> building rpms"
	cp peony-extensions-libdir-and-qmake.patch ~/rpmbuild/SOURCES/peony-extensions-libdir-and-qmake.patch
	rpmbuild -ba peony-extensions.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/peony-extensions* rpmbuild/RPMS/x86_64/peony-extensions* ~/rpmbuild/SOURCES/peony-extensions* ~/rpmbuild/RPMS/x86_64/peony-extensions* 
	$(DOCKER) container rm -a

.PHONY: build  clean