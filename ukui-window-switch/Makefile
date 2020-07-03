
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build  clean

docker-builder:
	$(DOCKER) build -t docker.io/jenningsloy318/ukui-window-switch-builder:f32  -f Dockerfile .

docker-build:
	@echo ">> building rpms"
	$(DOCKER) run  --privileged -v `pwd`:/root docker.io/jenningsloy318/ukui-window-switch-builder:f32  bash  /root/build.sh 

deps:
	@echo ">> install dependencies"
	dnf install -y  which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  qt5-qtbase-devel qt5-qtx11extras-devel qt5-qtbase-private-devel gtk3-devel libwnck3-devel && \
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

build: | deps 
	@echo ">> building rpms"
	rpmbuild -ba ukui-window-switch.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/ukui-window-switch* rpmbuild/RPMS/x86_64/ukui-window-switch* ~/rpmbuild/SOURCES/ukui-window-switch* ~/rpmbuild/RPMS/x86_64/ukui-window-switch* 
	$(DOCKER) container rm -a

.PHONY: build  clean