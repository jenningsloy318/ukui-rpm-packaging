
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build  clean

docker-builder:
	$(DOCKER) build -t docker.io/jenningsloy318/qt5-ukui-platformtheme-builder:f32  -f Dockerfile .

docker-build: 
	@echo ">> building rpms"
	$(DOCKER) run  --ulimit=host  --privileged -v `pwd`:/root docker.io/jenningsloy318/qt5-ukui-platformtheme-builder:f32  bash  /root/build.sh 

deps:
	@echo ">> install dependencies"
	dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  glib2-devel qt5-qtx11extras-devel kf5-kwindowsystem-devel gsettings-desktop-schemas-devel qt5-qtbase-devel qt5-qtbase-private-devel qt5-qttools-devel gsettings-qt-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

build: | deps
	@echo ">> building rpms"
	rpmbuild -ba qt5-ukui-platformtheme.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/qt5-ukui-platformtheme* rpmbuild/RPMS/x86_64/qt5-ukui-platformtheme* ~/rpmbuild/SOURCES/qt5-ukui-platformtheme* ~/rpmbuild/RPMS/x86_64/qt5-ukui-platformtheme* 
	$(DOCKER) container rm -a

.PHONY: build  clean