
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build  clean

docker-builder:
	$(DOCKER) build -t docker.io/jenningsloy318/ukui-kwin-builder:f32  -f Dockerfile .

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host --privileged -v `pwd`:/root docker.io/jenningsloy318/ukui-kwin-builder:f32  bash  /root/build.sh 

deps:
	@echo ">> install dependencies"
	dnf install -y which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  extra-cmake-modules glib2-devel qt5-qtsvg-devel qt5-qtx11extras-devel qt5-qtbase-devel qt5-qttools-devel qt5-qtmultimedia-devel qt5-qtdeclarative-devel qt5-qtscript-devel qt5-qtsensors-devel qt5-qttools-static gsettings-qt-devel poppler-qt5-devel qt5-qtbase-static qt5-qtbase-private-devel kf5-kconfigwidgets-devel kf5-kcrash-devel kf5-kglobalaccel-devel kf5-ki18n-devel kf5-kiconthemes-devel kf5-kidletime-devel kf5-kinit-devel kf5-knotifications-devel kf5-kpackage-devel kf5-plasma-devel kf5-kwayland-devel kf5-kwidgetsaddons-devel kf5-kcompletion-devel kf5-kdeclarative-devel kf5-kcmutils-devel kf5-kio-devel kf5-knewstuff-devel kf5-kservice-devel kf5-ktextwidgets-devel kf5-kxmlgui-devel kf5-kactivities-devel kf5-kdoctools-devel kf5-kirigami2-devel kf5-kconfig-devel kf5-kcoreaddons-devel kf5-kwindowsystem-devel libxcb-devel xcb-util-devel xcb-util-cursor-devel xcb-util-keysyms-devel xcb-util-image-devel xcb-util-wm-devel xcb-util-renderutil-devel libxkbcommon-devel libxkbcommon-x11-devel libinput-devel systemd-devel libdrm-devel mesa-libgbm-devel libepoxy-devel libICE-devel libSM-devel mesa-libEGL-devel wayland-devel libwayland-client-devel libwayland-server-devel libwayland-cursor-devel kdecoration-devel kscreenlocker-devel libcap-devel xorg-x11-server-Xwayland  qt5-qtvirtualkeyboard-devel  libXi-devel  qt5-qtquickcontrols plasma-breeze-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5

build: | deps
	@echo ">> building rpms"
	rpmbuild -ba ukui-kwin.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild
	$(DOCKER) container rm -a

.PHONY: build  clean