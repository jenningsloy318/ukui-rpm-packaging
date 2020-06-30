
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
DIST := $(shell { grep "%dist" /etc/rpm/macros.dist |cut -d " " -f 2 ;} 2>/dev/null)

all: build 

docker-builder:
	$(DOCKER) build -t docker.io/jenningsloy318/biometric-authentication-builder:f32  -f Dockerfile .

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --privileged -v `pwd`:/root docker.io/jenningsloy318/biometric-authentication-builder:f32  bash  /root/build.sh 

deps:
	@echo ">> install dependencies"
	dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros   automake python3-devel glib2-devel gtk3-devel libusb-devel sqlite-devel  polkit-devel libtool libuuid-devel  git gtk-doc meson glib2-devel libusb-devel nss-devel pixman-devel

build-libfprint:
	@echo ">> build libfprint-devel"
	rpm -ivh https://mirrors.tuna.tsinghua.edu.cn/fedora/releases/31/Everything/source/tree/Packages/l/libfprint-1.0-1.fc31.src.rpm  
	rpmbuild  -ba /root/rpmbuild/SPECS/libfprint.spec 
	dnf install -y  /root/rpmbuild/RPMS/x86_64/libfprint-1.0-1${DIST}.x86_64.rpm /root/rpmbuild/RPMS/x86_64/libfprint-devel-1.0-1${DIST}.x86_64.rpm

build: | deps build-libfprint
	@echo ">> building rpms"
	cp biometric-authentication-unitdir.patch ~/rpmbuild/SOURCES
	rpmbuild  -ba biometric-authentication.spec
	
clean:
	@echo ">> clean up"
	rm -rf rpmbuild
	$(DOCKER) container rm -a

.PHONY: build  clean