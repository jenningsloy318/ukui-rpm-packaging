
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build  clean

docker-builder:
	$(DOCKER) build -t docker.io/jenningsloy318/ukui-sidebar-builder:f32  -f Dockerfile .

docker-build: 
	@echo ">> building rpms"
	$(DOCKER) run  --ulimit=host --privileged -v `pwd`:/root docker.io/jenningsloy318/ukui-sidebar-builder:f32  bash  /root/build.sh 

deps:
	@echo ">> install dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  qt5-qtbase-devel qt5-qttools-devel glib2-devel qt5-qtbase-devel qt5-qtsvg-devel dconf-devel gsettings-qt-devel qt5-qtmultimedia-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

build: | deps 
	@echo ">> building rpms"
	cp ukui-sidebar-plugin-libdir.patch ~/rpmbuild/SOURCES/
	rpmbuild -ba ukui-sidebar.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/ukui-sidebar* rpmbuild/RPMS/x86_64/ukui-sidebar* ~/rpmbuild/SOURCES/ukui-sidebar* ~/rpmbuild/RPMS/x86_64/ukui-sidebar* 
	$(DOCKER) container rm -a

.PHONY: build  clean