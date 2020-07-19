DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
DIST := $(shell { rpm --eval "%{dist}";} 2>/dev/null)

all: build 


docker-build-fedora: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"

docker-build-centos8: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/centos:8   /bin/bash -c "dnf install -y https://mirrors.tuna.tsinghua.edu.cn/epel/epel-release-latest-8.noarch.rpm https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm https://pkgs.dyn.su/el8/base/x86_64/raven-release-1.0-1.el8.noarch.rpm make curl rpm-build && sed -i 's|enabled=0|enabled=1|g' /etc/yum.repos.d/CentOS-PowerTools.repo && dnf install -y  python3 rpmfusion-free-release-tainted rpmfusion-nonfree-release-tainted  && alternatives --set python /usr/bin/python3 && make build"



build:
ifneq (,$(filter .el%,$(DIST)))
	@echo ">> build ukui on centos/rhel"
	make 	build-on-centos
else 
	@echo ">> build ukui on fedora"
	make 	build-on-fedora
endif


build-on-fedora: 
	make -C kylin-display-switch 
	make -C kylin-nm
	make -C kylin-video
	make -C indicator-china-weather 
	make -C qt5-ukui-platformtheme
	make -C peony 
	make -C peony-extensions 
	make -C ukui-biometric-auth 
	make -C ukui-biometric-manager 
	make -C ukui-control-center
	make -C ukui-greeter
	make -C ukwm
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
