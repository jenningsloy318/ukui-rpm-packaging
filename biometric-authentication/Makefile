
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build 

builder:
	$(DOCKER) build -t docker.io/jenningsloy318/biometric-authentication-builder:f32  -f Dockerfile .

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --privileged -v `pwd`:/root docker.io/jenningsloy318/biometric-authentication-builder:f32  bash  /root/build.sh 

deps:
	@echo ">> install dependencies"
	dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros   automake python3-devel glib2-devel gtk3-devel libusb-devel sqlite-devel  polkit-devel libtool libuuid-devel  git gtk-doc meson glib2-devel libusb-devel nss-devel pixman-devel  libfprint-devel

build: | deps
	@echo ">> building rpms"
	rpmbuild  -ba biometric-authentication.spec
	
clean:
	@echo ">> clean up"
	rm -rf rpmbuild
	$(DOCKER) container rm -a

.PHONY: build  clean