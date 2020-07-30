DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
DIST := $(shell { rpm --eval "%{dist}";} 2>/dev/null)

all: build 


docker-build-fedora-32: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y dnf-plugins-core make curl rpm-build && make build"

docker-build-fedora-rawhide: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/fedora:rawhide   /bin/bash -c "sudo dnf install -y dnf-plugins-core make curl rpm-build && make build"

docker-build-centos-8: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/centos:8   /bin/bash -c "dnf install -y dnf-plugins-core make curl rpm-build && make build"



build:
ifneq (,$(filter .el%,$(DIST)))
	@echo ">> build ukui on centos/rhel"
	dnf install -y https://mirrors.tuna.tsinghua.edu.cn/epel/epel-release-latest-8.noarch.rpm https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm https://pkgs.dyn.su/el8/base/x86_64/raven-release-1.0-1.el8.noarch.rpm dnf-plugins-core make curl rpm-build  centos-release-stream python3 git 
	dnf config-manager --enable PowerTools
	dnf config-manager --enable Stream-PowerTools
	dnf install -y rpmfusion-free-release-tainted rpmfusion-nonfree-release-tainted 
	alternatives --set python /usr/bin/python3
	dnf copr enable -y neonman/MATE
	dnf copr enable -y neonman/MATE-Dependencies
	rpm -ivh https://mirrors.tuna.tsinghua.edu.cn/fedora/releases/32/Everything/source/tree/Packages/l/libX11-1.6.9-3.fc32.src.rpm
	dnf install -y xorg-x11-util-macros "pkgconfig(xproto)" xorg-x11-xtrans-devel libxcb-devel "pkgconfig(xau)" "perl(Pod::Usage)" "pkgconfig(xdmcp)"
	rpmbuild -ba /root/rpmbuild/SPECS/libX11.spec
	dnf install  -y /root/rpmbuild/RPMS/x86_64/libX11-1.6.9-3.el8.x86_64.rpm  /root/rpmbuild/RPMS/noarch/libX11-common-1.6.9-3.el8.noarch.rpm /root/rpmbuild/RPMS/x86_64/libX11-devel-1.6.9-3.el8.x86_64.rpm  /root/rpmbuild/RPMS/x86_64/libX11-xcb-1.6.9-3.el8.x86_64.rpm
	make 	build-on-centos
else 
	@echo ">> build ukui on fedora"
	dnf install -y git 
	make 	build-on-fedora
endif


build-on-fedora: 
	make -C kylin-display-switch 
	make -C kylin-nm
	make -C kylin-video
	make -C indicator-china-weather 
	make -C kylin-scanner
	make -C biometric-authentication
	make -C qt5-ukui-platformtheme
	make -C peony 
	make -C peony-extensions 
	make -C ukui-biometric-auth 
	make -C ukui-biometric-manager 
	make -C ukui-control-center
	make -C ukui-greeter
	make -C ukwm
	make -C ukui-kwin
	make -C ukui-menu 
	make -C ukui-panel 
	make -C ukui-power-manager
	make -C ukui-screensaver
	make -C ukui-session-manager
	make -C ukui-settings-daemon
	make -C ukui-sidebar
	make -C ukui-system-monitor
	make -C ukui-window-switch
	make -C ukui-wallpapers
	make -C ukui-themes
	make -C ukui-media


build-on-centos: 
	make -C kylin-display-switch 
	make -C kylin-nm
	make -C kylin-video
	make -C indicator-china-weather
	make -C kylin-scanner
	make -C biometric-authentication
	make -C qt5-ukui-platformtheme
	make -C peony 
	make -C peony-extensions 
	make -C ukui-biometric-auth 
	make -C ukui-biometric-manager 
	make -C ukui-control-center
	make -C ukui-greeter
	make -C ukui-kwin
	make -C ukui-menu 
	make -C ukui-panel 
	make -C ukui-power-manager
	make -C ukui-screensaver
	make -C ukui-session-manager
	make -C ukui-settings-daemon
	make -C ukui-sidebar
	make -C ukui-system-monitor
	make -C ukui-window-switch
	make -C ukui-wallpapers
	make -C ukui-themes
	make -C ukui-media
	
clean:
	rm -rf ~/rpmbuild/{SOURCES,RPMS}


.PHONY:   docker-build build build-on-fedora build-on-centos  clean
