
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build  clean

docker-builder:
	$(DOCKER) build -t docker.io/jenningsloy318/ukui-biometric-manager-builder:f32  -f Dockerfile .

docker-build: 
	@echo ">> building rpms"
	$(DOCKER) run --ulimit=host  --privileged -v `pwd`:/root docker.io/jenningsloy318/ukui-biometric-manager-builder:f32  bash  /root/build.sh 

deps:
	@echo ">> install dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros qt5-qtbase-devel qt5-qttools-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

build: | deps
	@echo ">> building rpms"
	rpmbuild -ba ukui-biometric-manager.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/ukui-biometric-manager* rpmbuild/RPMS/x86_64/ukui-biometric-manager* ~/rpmbuild/SOURCES/ukui-biometric-manager* ~/rpmbuild/RPMS/x86_64/ukui-biometric-manager* 
	$(DOCKER) container rm -a

.PHONY: build  clean