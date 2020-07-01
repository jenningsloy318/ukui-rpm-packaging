
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
DIST := $(shell { rpm --eval "%{dist}";} 2>/dev/null)
PKG_VERSION := $(shell { grep  "Version" peony.spec| awk  '{print $$2}'; } )
PKG_RELEASE :=$(shell { grep "Release" peony.spec| awk '{print $$2}'|sed "s/%{?dist}/${DIST}/g"; } )

all: build  clean

docker-builder:
	$(DOCKER) build -t docker.io/jenningsloy318/peony-builder:f32  -f Dockerfile .

docker-build: 
	@echo ">> building rpms"
	$(DOCKER) run --ulimit=host  --privileged -v `pwd`:/root docker.io/jenningsloy318/peony-builder:f32  bash  /root/build.sh 

deps:
	@echo ">> install dependencies"
	dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros   qt5-qtbase-devel qt5-qttools-devel glib2-devel qt5-qtbase-devel gsettings-qt-devel kf5-kwindowsystem-devel poppler-qt5-devel qt5-qtx11extras-devel qt5-qtbase-private-devel 
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

build: | deps
	@echo ">> building rpms"
	cp peony-libdir.patch ~/rpmbuild/SOURCES/peony-libdir.patch
	rpmbuild -ba peony.spec
	dnf install -y  /root/rpmbuild/RPMS/x86_64/{peony-common-${PKG_VERSION}-${PKG_RELEASE}.x86_64.rpm,peony-devel-${PKG_VERSION}-${PKG_RELEASE}.x86_64.rpm,peony-libs-${PKG_VERSION}-${PKG_RELEASE}.x86_64.rpm}

clean:
	@echo ">> clean up"
	rm -rf rpmbuild
	$(DOCKER) container rm -a

.PHONY: build  clean