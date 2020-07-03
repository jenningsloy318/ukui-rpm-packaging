
DIST := $(shell { rpm --eval "%{dist}";} 2>/dev/null)

all: build 


bio-auth:
ifneq (,$(filter .el%,$(DIST)))
	@echo ">> build biometric-authentication"
	cd biometric-authentication/ && make build && cd ..
else 
	@echo ">> don't build biometric-authentication on fedora"

endif



build: | bio-auth
	cd kylin-display-switch/ && make build && cd ..
	cd kylin-nm/ && make build && cd ..
	cd peony/ && make build && cd ..
	cd peony-extensions/ && make build && cd ..
	cd qt5-ukui-platformtheme/ && make build && cd ..
	cd ukui-biometric-auth/ && make build && cd ..
	cd ukui-biometric-manager/ && make build && cd ..
	cd ukui-control-center/ && make build && cd ..
	cd ukui-greeter/ && make build && cd ..
	cd ukui-kwin/ && make build && cd ..
	cd ukui-menu/ && make build && cd ..
	cd ukui-panel/ && make build && cd ..
	cd ukui-power-manager/ && make build && cd ..
	cd ukui-screensaver/ && make build && cd ..
	cd ukui-session-manager/ && make build && cd ..
	cd ukui-settings-daemon/ && make build && cd ..
	cd ukui-sidebar/ && make build && cd ..
	cd ukui-system-monitor/ && make build && cd ..
	cd ukui-themes/ && make build && cd ..
	cd ukui-wallpapers/ && make build && cd ..
	cd ukui-window-switch/ && make build && cd ..
	cd ukui-media/ && make build && cd ..

clean:
	rm -rf ~/rpmbuild/{SOURCES,RPMS}