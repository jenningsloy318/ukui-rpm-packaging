DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
DIST := $(shell { rpm --eval "%{dist}";} 2>/dev/null)

all: build 


docker-build-fedora-32: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y dnf-plugins-core make curl rpm-build && make build"

docker-build-fedora-rawhide: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/fedora:rawhide   /bin/bash -c "sudo dnf install -y dnf-plugins-core make curl rpm-build && make build"

docker-build-centos-8: 
	@echo ">> building rpms in container"
	docker run  --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/centos:8   /bin/bash -c "dnf install -y dnf-plugins-core make curl rpm-build && make build"



build:
ifneq (,$(filter .el%,$(DIST)))
	@echo ">> build ukui on centos/rhel"
	dnf install -y https://mirrors.tuna.tsinghua.edu.cn/epel/epel-release-latest-8.noarch.rpm https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm  dnf-plugins-core make curl rpm-build  centos-release-stream python3 git 
	dnf config-manager --enable PowerTools
	dnf config-manager --enable Stream-PowerTools
	dnf install -y rpmfusion-free-release-tainted rpmfusion-nonfree-release-tainted 
	alternatives --set python /usr/bin/python3
	dnf copr enable -y neonman/MATE
	dnf copr enable -y neonman/MATE-Dependencies
	make 	build-on-centos
	make build-apps
	
else 
	@echo ">> build ukui on fedora"
	dnf install -y git  https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$$(rpm -E %{fedora}).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$$(rpm -E %{fedora}).noarch.rpm
	make 	build-on-fedora
	make build-apps
endif


build-on-fedora: 
	make -C fedora-deps
	make -C libinput-touch-translator
	make -C biometric-authentication
	make -C qt5-ukui-platformtheme
	make -C peony 
	make -C peony-extensions 
	make -C time-shutdown
	make -C ukui-biometric-auth 
	make -C ukui-biometric-manager 
	make -C ukui-control-center
	make -C ukui-greeter
	make -C ukui-kwin
	make -C ukui-media
	make -C ukui-menu 
	make -C ukui-notification-daemon
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
	


build-on-centos: 
	make -C centos8-deps
	make -C libinput-touch-translator
	make -C biometric-authentication
	make -C qt5-ukui-platformtheme
	make -C peony 
	make -C peony-extensions 
	make -C time-shutdown
	make -C ukui-biometric-auth 
	make -C ukui-biometric-manager 
	make -C ukui-control-center
	make -C ukui-greeter
	make -C ukui-kwin
	make -C ukui-media
	make -C ukui-menu 
	make -C ukui-notification-daemon
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
	
build-apps:
	make -C indicator-china-weather
	make -C kylin-display-switch 
	make -C kylin-ipmsg
	make -C kylin-nm
	make -C kylin-scanner
	make -C kylin-screenshot
	make -C kylin-video
	make -C kylin-calculator
	make -C kylin-music
	make -C kylin-recording

clean:
	rm -rf ~/rpmbuild/{SOURCES,RPMS}


.PHONY:   docker-build build build-on-fedora build-on-centos build-apps  clean
