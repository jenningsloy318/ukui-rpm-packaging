
DOCKER := $(shell { command -v podman || command -v docker; } 2>/dev/null)
all: build  clean

docker-builder:
	$(DOCKER) build -t docker.io/jenningsloy318/kylin-video-builder:f32  -f Dockerfile .

docker-build: 
	@echo ">> building rpms in container"
	$(DOCKER) run --ulimit=host  --privileged -v `pwd`:/root docker.io/jenningsloy318/kylin-video-builder:f32  bash  /root/build.sh 

deps:
	@echo ">> install dependencies"
	dnf -y install  qt5-qtbase-devel qt5-qtscript-devel qt5-qttools-devel qt5-linguist qt5-qtbase-private-devel qt5-qtx11extras-devel zlib-devel libX11-devel libcrystalhd-devel
	strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5
	ln -s /usr/bin/lrelease-qt5 /usr/bin/lrelease

build: | deps
	@echo ">> building rpms"
	rpmbuild -ba kylin-video.spec

clean:
	@echo ">> clean up"
	rm -rf rpmbuild/SOURCES/kylin-video* rpmbuild/RPMS/x86_64/kylin-video* ~/rpmbuild/SOURCES/kylin-video* ~/rpmbuild/RPMS/x86_64/kylin-video* 
	$(DOCKER) container rm -a

.PHONY: build  clean