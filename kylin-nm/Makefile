
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build  clean

docker-builder:
	$(DOCKER) build -t docker.io/jenningsloy318/kylin-nm-builder:f32  -f Dockerfile .

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run --ulimit=host  --privileged -v `pwd`:/root docker.io/jenningsloy318/kylin-nm-builder:f32  bash  /root/build.sh 

deps:
	@echo ">> install dependencies"
	dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros qt5-qtbase-devel  qt5-qtscript-devel qt5-qttools-devel qt5-qtx11extras-devel gsettings-qt-devel kf5-kwindowsystem-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

build: | deps
	@echo ">> building rpms"
	rpmbuild -ba kylin-nm.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild
	$(DOCKER) container rm -a

.PHONY: build  clean