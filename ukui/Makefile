DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)

all: build


docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/fedora  /bin/bash -c "sudo dnf install -y dnf-plugins-core make curl rpm-build && dnf update -y  && make build &&  chmod -R 777 rpmbuild"

build:
	@echo ">> build ukui on fedora"
	dnf install -y git  https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$$(rpm -E %{fedora}).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$$(rpm -E %{fedora}).noarch.rpm dnf-plugins-core
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
	make -C kylin-nm
	make -C kylin-display-switch
clean:
	rm -rf ~/rpmbuild/{SOURCES,RPMS}


.PHONY:   docker-build build  clean
