DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build-libfprint build-gsettings-qt build-redshift build-bamf build-lxqt-build-tools  build-libstatgrab build-libqtxdg build-sassc
docker-build:
	@echo ">> building rpms in container"
	$(DOCKER) run  --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/centos:8   /bin/bash -c "dnf install -y dnf-plugins-core make curl rpm-build && make build"
deps:
	@echo ">> install dependencies"
	dnf install -y https://mirrors.tuna.tsinghua.edu.cn/epel/epel-release-latest-8.noarch.rpm https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm  dnf-plugins-core make curl rpm-build  centos-release-stream python3 git
	dnf config-manager --enable PowerTools
	dnf config-manager --enable Stream-PowerTools
	dnf install -y rpmfusion-free-release-tainted rpmfusion-nonfree-release-tainted intltool

build: deps build-libfprint build-gsettings-qt build-redshift build-bamf build-lxqt-build-tools build-libstatgrab build-libqtxdg build-sassc

build-libfprint:
	@echo ">> build libfprint-devel"
	rpm -ivh libfprint-1.0-1.el8.src.rpm
	dnf install -y meson gcc gcc-c++ git "pkgconfig(glib-2.0)" "pkgconfig(libusb-1.0)" "pkgconfig(nss)" "pkgconfig(pixman-1)" gtk-doc systemd
	rpmbuild  -ba /root/rpmbuild/SPECS/libfprint.spec 
	dnf install -y /root/rpmbuild/RPMS/x86_64/libfprint-1.0-1.el8.x86_64.rpm /root/rpmbuild/RPMS/x86_64/libfprint-devel-1.0-1.el8.x86_64.rpm

build-gsettings-qt:
	@echo ">> build gsettings-qt"
	rpm -ivh gsettings-qt-0-0.21.20180723bzr85.el8.src.rpm
	dnf install -y qt5-qtbase-devel qt5-qtdeclarative-devel glib2-devel gcc-c++
	rpmbuild -ba ~/rpmbuild/SPECS/gsettings-qt.spec
	dnf install -y  /root/rpmbuild/RPMS/x86_64/gsettings-qt-0-0.21.20180723bzr85.el8.x86_64.rpm  /root/rpmbuild/RPMS/x86_64/gsettings-qt-devel-0-0.21.20180723bzr85.el8.x86_64.rpm

build-redshift:
	@echo ">> build redshift"
	rpm -ivh redshift-1.12-7.el8.src.rpm
	dnf install -y GConf2-devel geoclue2-devel  libXxf86vm-devel desktop-file-utils  gettext-devel intltool libXrandr-devel libdrm-devel libtool
	rpmbuild -ba ~/rpmbuild/SPECS/redshift.spec
	dnf install -y  /root/rpmbuild/RPMS/x86_64/redshift-1.12-7.el8.x86_64.rpm

build-bamf:
	@echo ">> build bamf"
	rpm -ivh bamf-0.5.4-4.el8.src.rpm
	dnf install -y gobject-introspection-devel python3-lxml vala "pkgconfig(libgtop-2.0)" "pkgconfig(libwnck-3.0)"
	rpmbuild -ba  ~/rpmbuild/SPECS/bamf.spec
	dnf install -y   /root/rpmbuild/RPMS/x86_64/bamf-0.5.4-4.el8.x86_64.rpm /root/rpmbuild/RPMS/x86_64/bamf-devel-0.5.4-4.el8.x86_64.rpm   /root/rpmbuild/RPMS/x86_64/bamf-daemon-0.5.4-4.el8.x86_64.rpm

build-lxqt-build-tools:
	@echo ">> build lxqt-build-tools"
	rpm -ivh lxqt-build-tools-0.7.0-1.el8.src.rpm
	dnf install -y gcc-c++ "pkgconfig(Qt5Core)" glib2-devel
	rpmbuild -ba ~/rpmbuild/SPECS/lxqt-build-tools.spec
	dnf install -y /root/rpmbuild/RPMS/noarch/lxqt-build-tools-0.7.0-1.el8.noarch.rpm


build-libstatgrab:
	@echo ">> build libstatgrab"
	rpm -ivh libstatgrab-0.92-3.el8.src.rpm
	dnf install -y log4cplus-devel ncurses-devel "perl(App::Prove)" "perl(IPC::Cmd)" "perl(Test::More)"  perl-generators
	rpmbuild -ba ~/rpmbuild/SPECS/libstatgrab.spec
	dnf install -y /root/rpmbuild/RPMS/x86_64/libstatgrab-0.92-3.el8.x86_64.rpm /root/rpmbuild/RPMS/x86_64/libstatgrab-devel-0.92-3.el8.x86_64.rpm

build-libqtxdg:
	@echo ">> build libqtxdg"
	rpm -ivh libqtxdg-3.5.0-1.el8.src.rpm
	dnf install -y qt5-qtwebkit-devel file-devel "pkgconfig(Qt5Help)" "pkgconfig(Qt5Svg)" qt5-qtbase-private-devel 
	rpmbuild -ba  ~/rpmbuild/SPECS/libqtxdg.spec
	dnf install -y  /root/rpmbuild/RPMS/x86_64/libqtxdg-3.5.0-1.el8.x86_64.rpm /root/rpmbuild/RPMS/x86_64/libqtxdg-devel-3.5.0-1.el8.x86_64.rpm

build-sassc:
	@echo ">> build sassc"
	rpm -ivh sassc-3.5.0-2.el8.src.rpm libsass-3.5.4-4.el8.src.rpm
	rpmbuild -ba ~/rpmbuild/SPECS/libsass.spec 
	dnf install -y /root/rpmbuild/RPMS/x86_64/libsass-3.5.4-4.el8.x86_64.rpm  /root/rpmbuild/RPMS/x86_64/libsass-devel-3.5.4-4.el8.x86_64.rpm
	dnf install -y  gcc-c++ rubygem-minitest ruby 
	rpmbuild -ba  ~/rpmbuild/SPECS/sassc.spec 
	dnf install -y /root/rpmbuild/RPMS/x86_64/sassc-3.5.0-2.el8.x86_64.rpm

.PHONY: deps build-libfprint build-gsettings-qt build-redshift build-bamf build-lxqt-build-tools build-libstatgrab build-libqtxdg build-sassc
