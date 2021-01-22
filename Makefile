DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
DIST := $(shell { rpm --eval "%{dist}";} 2>/dev/null)

all: build


docker-build-fedora-32: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y dnf-plugins-core make curl rpm-build && dnf update -y  && make build &&  chmod -R 777 rpmbuild"

docker-build-fedora-33: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/fedora:33   /bin/bash -c "sudo dnf install -y dnf-plugins-core make curl rpm-build && dnf update -y && make build &&  chmod -R 777 rpmbuild"

docker-build-centos-8: 
	@echo ">> building rpms in container"
	docker run  --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/centos:8   /bin/bash -c "dnf install -y dnf-plugins-core make curl rpm-build && dnf update -y  && make build && chmod -R 777 rpmbuild"



build:
ifneq (,$(filter .el%,$(DIST)))
	@echo ">> build ukui on centos/rhel"
	dnf install centos-release-stream -y 
	dnf distro-sync -y
	dnf install --allowerasing -y https://mirrors.tuna.tsinghua.edu.cn/epel/epel-release-latest-8.noarch.rpm https://download1.rpmfusion.org/free/el/rpmfusion-free-release-8.noarch.rpm https://download1.rpmfusion.org/nonfree/el/rpmfusion-nonfree-release-8.noarch.rpm  https://pkgs.dyn.su/el8/base/x86_64/raven-release-1.0-1.el8.noarch.rpm https://mirrors.tuna.tsinghua.edu.cn/centos/8-stream/BaseOS/x86_64/os/Packages/centos-stream-release-8.4-1.el8.noarch.rpm https://mirrors.tuna.tsinghua.edu.cn/centos/8-stream/BaseOS/x86_64/os/Packages/centos-stream-repos-8-2.el8.noarch.rpm dnf-plugins-core make curl rpm-build  python3 git 
	dnf install -y rpmfusion-free-release-tainted rpmfusion-nonfree-release-tainted 
	sed -i 's/enabled=0/enabled=1/g' /etc/yum.repos.d/CentOS-Stream-PowerTools.repo
	alternatives --set python /usr/bin/python3
	dnf copr enable -y neonman/MATE
	dnf copr enable -y neonman/MATE-Dependencies
	make 	build-on-centos
	
else 
	@echo ">> build ukui on fedora"
	dnf install -y git  https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$$(rpm -E %{fedora}).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$$(rpm -E %{fedora}).noarch.rpm dnf-plugins-core
	make 	build-on-fedora
endif




build-on-centos: 
	make -C libinput-touch-translator
	make -C qt5-ukui-platformtheme
	make -C peony 
	make -C time-shutdown
	make -C ukui-biometric-auth
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
	make -C indicator-china-weather
	make -C kylin-burner
	make -C kylin-display-switch 
	make -C kylin-ipmsg
	make -C kylin-nm
	make -C kylin-screenshot
	make -C kylin-video
	make -C kylin-calculator
	make -C kylin-music
	make -C kylin-recorder
#	make -C kylin-camera



build-on-fedora: 
	make -C libinput-touch-translator
	make -C biometric-authentication
	make -C qt5-ukui-platformtheme
	make -C peony 
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
	make -C indicator-china-weather
	make -C kylin-burner
	make -C kylin-display-switch 
	make -C kylin-ipmsg
	make -C kylin-nm
	make -C kylin-scanner
	make -C kylin-screenshot
	make -C kylin-video
	make -C kylin-calculator
	make -C kylin-music
	make -C kylin-recorder
#	make -C kylin-camera

clean:
	rm -rf ~/rpmbuild/{SOURCES,RPMS}


.PHONY:   docker-build build build-on-fedora build-on-centos  clean
