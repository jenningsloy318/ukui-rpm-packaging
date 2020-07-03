
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build  clean

docker-builder:
	$(DOCKER) build -t docker.io/jenningsloy318/ukui-wallpapers-builder:f32  -f Dockerfile .

docker-build: 
	@echo ">> building rpms"
	$(DOCKER) run  --ulimit=host --privileged -v `pwd`:/root docker.io/jenningsloy318/ukui-wallpapers-builder:f32  bash  /root/build.sh 


deps:
	@echo ">> install dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros ninja-build meson

build: | deps 
	@echo ">> building rpms"
	rpmbuild -ba ukui-wallpapers.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/ukui-wallpapers* rpmbuild/RPMS/x86_64/ukui-wallpapers* ~/rpmbuild/SOURCES/ukui-wallpapers* ~/rpmbuild/RPMS/x86_64/ukui-wallpapers* 
	$(DOCKER) container rm -a

.PHONY: build  clean