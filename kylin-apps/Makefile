DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)

all: build


docker-build:
	@echo ">> building rpms in container"
	$(DOCKER) run  --rm --privileged -v `pwd`:/root/  -w /root/ docker.io/library/fedora   /bin/bash -c "sudo dnf install -y dnf-plugins-core make curl rpm-build && dnf update -y  && make build &&  chmod -R 777 rpmbuild"


build:
	@echo ">> build ukui on fedora"
	dnf install -y git  https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$$(rpm -E %{fedora}).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$$(rpm -E %{fedora}).noarch.rpm dnf-plugins-core
	make -C indicator-china-weather
	make -C kylin-burner
	make -C kylin-ipmsg
	make -C kylin-screenshot
	make -C kylin-video
	make -C kylin-calculator
	make -C kylin-music
	make -C kylin-recorder
	make -C kylin-camera

clean:
	rm -rf ~/rpmbuild/{SOURCES,RPMS}


.PHONY:   docker-build build  clean
