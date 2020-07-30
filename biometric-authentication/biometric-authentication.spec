Name:           biometric-authentication
Version:        master
Release:        1%{?dist}
Summary:        Biometric Authentication Service

License:        LGPL-3.0 License
URL:            https://github.com/ukui/biometric-authentication
Source0:        %{name}-%{version}.tar.gz
Patch0:					biometric-authentication-unitdir.patch
BuildArch:      x86_64


BuildRequires: automake
BuildRequires: python3-devel
BuildRequires: glib2-devel
BuildRequires: gtk3-devel 
BuildRequires: libusb-devel
BuildRequires: sqlite-devel
BuildRequires: libfprint-devel
BuildRequires: polkit-devel
BuildRequires: libtool
BuildRequires: libuuid-devel

Requires: systemd
Requires: %{name}-libs%{?_isa}  = %{version}-%{release}

%description
 The service layer of the biometric identification authentication framework.
 The service layer uses the DBus bus to provide the upper application with
 operation interfaces such as feature enroll, feature verify, feature identify,
 feature search, feature delete, etc. Meanwhile, it also provides notification
 of device status changes event and notification of USB device hotplug event.
 .
 This package contains a library for biometric authentication.



%package libs
Summary: Biometric Identification library
Requires: systemd


%description libs
 The core layer of biometric identification authentication framework.
 The core layer abstracts the common operation of all kinds of biometric
 recognition, constructs the underlying framework of biometric recognition,
 and provides the general function and unified data storage method.
 .
 This package contains a library for biometric identification.




%package  devel

Summary: Biometric Identification DRIVER API - development files

Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa}  = %{version}-%{release}
Requires: systemd
Requires: python3-prettytable
Requires: python3-dbus
Requires: python3-gobject

%description  devel
 It provides the development file for driver development based on biometric
 identification authentication framework.
 .
 This package contains the development files (headers, static libraries)


%package utils

Summary: Biometric authentication utils

Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa}  = %{version}-%{release}

%description utils
 Biometric authentication tools.
 This package provides the biometric-config-tool and biometric-device-discover
 tools:
  - biometric-auth-client: The command line client of the biometric
    identification framework service;
  - biometric-config-tool: add, remove, configure the biometric drivers;
  - biometric-device-discover: discover the devices supported by the biometric
    framework;

%package community-drivers
Summary: Biometric Authentication Driver (community multidevice)

Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa}  = %{version}-%{release}

%description community-drivers

 Community multi-device drivers for biometric authentication.
 Community multi-device drivers use libfprint for biometric identification.
 .
 This package supports following devices:
   upekts, uru4000, aes4000, aes2501, upektc, aes1610, fdu2000, vcom5s,
   upeksonly, vfs101, vfs301, aes2550, upeke2, aes1660, aes2660, aes3500,
   upektc_img, etes603, vfs5011, vfs0050, elan.


%prep
%setup -q
%patch0 -p0
./autogen.sh --prefix=/usr --sysconfdir=/etc --libdir=/usr/lib64 --unitdir=/usr/lib/system/systemd
%{configure} --disable-dependency-tracking  --with-bio-config-dir=/etc/biometric-auth/   --disable-silent-rules --with-bio-db-dir=/var/lib/biometric-auth/     --with-bio-db-name=biometric.db     --with-bio-config-dir=/etc/biometric-auth/     --with-bio-driver-dir=/usr/lib64/biometric-authentication/drivers    --with-bio-extra-dir=/usr/lib64/biometric-authentication/drivers/extra      --libexecdir=/usr/libexec/biometric-authentication

%build
%{make_build}

%install
rm -rf %{buildroot}
%{make_install} INSTALL_ROOT=%{buildroot}
install -d %{buildroot}/usr/share/man/{man1,man8}
gzip -c doc/man/biometric-auth-client.1	 > %{buildroot}/usr/share/man/man1/biometric-auth-client.1.gz
gzip -c doc/man/biometric-device-discover.1 > %{buildroot}/usr/share/man/man1/biometric-device-discover.1.gz
gzip -c doc/man/biometric-config-tool.8 >%{buildroot}/usr/share/man/man8/biometric-config-tool.8.gz

sed -i 's|/usr/lib/biometric-authentication/biometric-authenticationd|/usr/libexec/biometric-authentication/biometric-authenticationd|g' %{buildroot}/%{_unitdir}/biometric-authentication.service

%files
%doc debian/copyright debian/changelog 
%{_sysconfdir}/biometric-auth/biometric-drivers.conf
%{_sysconfdir}/dbus-1/system.d/org.ukui.Biometric.conf
%{_sysconfdir}/init.d/biometric-authentication
%{_libexecdir}/biometric-authentication
%{_datadir}/dbus-1/interfaces/org.ukui.Biometric.xml
%{_datadir}/polkit-1/actions/org.freedesktop.policykit.pkexec.biometric-authentication.policy
%{_datadir}/polkit-1/actions/org.ukui.biometric.policy
%{_unitdir}/biometric-authentication.service




%files devel 
%{_includedir}/libbiometric/
%{_libdir}/pkgconfig/libbiometric.pc
%{_libdir}/libbiometric.a
%{_libdir}/libbiometric.la

%files libs
%{_libdir}/libbiometric.so  
%{_libdir}/libbiometric.so.0  
%{_libdir}/libbiometric.so.0.0.0
%{_datadir}/locale/bo/LC_MESSAGES/biometric-authentication.mo
%{_datadir}/locale/es/LC_MESSAGES/biometric-authentication.mo
%{_datadir}/locale/fr/LC_MESSAGES/biometric-authentication.mo
%{_datadir}/locale/pt/LC_MESSAGES/biometric-authentication.mo
%{_datadir}/locale/ru/LC_MESSAGES/biometric-authentication.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/biometric-authentication.mo


%files community-drivers
%{_libdir}/biometric-authentication/drivers/
%{_libdir}/biometric-authentication/discover-tools/*

%files utils
%{_bindir}/biometric-auth-client
%{_bindir}/biometric-config-tool
%{_bindir}/biometric-device-discover
%{_mandir}/man1/*
%{_mandir}/man8/*



%post 
#!/bin/sh
set -e



if [ ! -f /etc/biometric-auth/biometric-drivers.conf ]; then
	mkdir -p /etc/biometric-auth
	cp /usr/share/biometric-auth/biometric-drivers.conf.template \
		/etc/biometric-auth/biometric-drivers.conf
fi

# In case this system is running systemd, we make systemd reload the unit files
# to pick up changes.
if [ -d /run/systemd/system ] ; then
	systemctl --system daemon-reload >/dev/null || true
fi
# End automatically added section


systemctl start biometric-authentication.service

systemctl enable biometric-authentication.service


%postun 
#!/bin/sh -e

set -e

BIO_DRIVER_CONF="/etc/biometric-auth/biometric-drivers.conf"
BIO_DATABASE="/var/lib/biometric-auth/biometric.db"
BIO_USERS=`ls /home`



systemctl stop biometric-authentication.service

systemctl disable biometric-authentication.service

# In case this system is running systemd, we make systemd reload the unit files
# to pick up changes.
if [ -d /run/systemd/system ] ; then
	systemctl --system daemon-reload >/dev/null || true
fi
# End automatically added section





%post community-drivers


#!/bin/sh
set -e


KEY_DIR="/etc/biometric-auth/key"
KEY_FILE="${KEY_DIR}/community-multidevice-aes.key"
KEY_LEN=32

if [ ! -f "/etc/biometric-auth/" ]
then
	mkdir -p /etc/biometric-auth/
	touch /etc/biometric-auth/biometric-drivers.conf
fi

if [ ! -f ${KEY_FILE} ]
then
	mkdir -p ${KEY_DIR}
	touch ${KEY_FILE}
	AES_KEY=`dd if=/dev/urandom bs=${KEY_LEN} count=1 2>/dev/null | base64 | head -c ${KEY_LEN}`
	echo -n ${AES_KEY} > ${KEY_FILE}
	chmod 0600 ${KEY_FILE}
fi

DRIVER_LIST="upekts uru4000 aes4000 aes2501 upektc aes1610 fdu2000 vcom5s 	upeksonly vfs101 vfs301 aes2550 upeke2 aes1660 aes2660 aes3500  	upektc_img etes603 vfs5011 vfs0050 elan"


for driver in ${DRIVER_LIST}; do
			biometric-config-tool add-driver -f ${driver} /usr/lib64/biometric-authentication/drivers/${driver}.so
			biometric-config-tool set-key -i ${driver} AESKey ${KEY_FILE}
done

exit 0

%preun community-drivers
#!/bin/sh
set -e

DRIVER_LIST="upekts uru4000 aes4000 aes2501 upektc aes1610 fdu2000 vcom5s 	upeksonly vfs101 vfs301 aes2550 upeke2 aes1660 aes2660 aes3500  	upektc_img etes603 vfs5011 vfs0050 elan"

for driver in ${DRIVER_LIST}; do
	biometric-config-tool remove-driver -i ${driver}
done

exit 0
