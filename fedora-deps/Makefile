
DIST := $(shell { rpm --eval "%{dist}";} 2>/dev/null)

all: build-libfprint 

build-libfprint:
		@echo ">> build libfprint-devel"
		rpm -ivh libfprint-1.0-1.fc31.src.rpm  
		dnf install -y meson gcc gcc-c++ git "pkgconfig(glib-2.0)" "pkgconfig(libusb-1.0)" "pkgconfig(nss)" "pkgconfig(pixman-1)" gtk-doc systemd
		rpmbuild  -ba /root/rpmbuild/SPECS/libfprint.spec 
		dnf install -y /root/rpmbuild/RPMS/x86_64/libfprint-1.0-1${DIST}.x86_64.rpm /root/rpmbuild/RPMS/x86_64/libfprint-devel-1.0-1${DIST}.x86_64.rpm

.PHONY: build-libfprint 
