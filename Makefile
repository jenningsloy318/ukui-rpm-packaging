DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
DIST := $(shell { rpm --eval "%{dist}";} 2>/dev/null)

all: build 


bio-auth:
ifneq (,$(filter .el%,$(DIST)))
	@echo ">> build biometric-authentication"
	cd biometric-authentication/ && make build && cd ..
else 
	@echo ">> don't build biometric-authentication on fedora"

endif

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run  --ulimit=host  --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/fedora:32   /bin/bash -c "sudo dnf install -y make curl rpm-build && make build"


build:
ifneq (,$(filter .el%,$(DIST)))
	@echo ">> build ukui on centos/rhel"
	make 	build-on-centos
else 
	@echo ">> build ukui on fedora"
	make 	build-on-fedora
endif


build-on-fedora: | bio-auth
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


build-on-centos: | bio-auth
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
	
clean:
	rm -rf ~/rpmbuild/{SOURCES,RPMS}


.PHONY:  bio-auth  docker-build build build-on-fedora build-on-centos  clean