# enable download source
%undefine _disable_source_fetch

Name:           biometric-authentication
Version:        master
Release:        1%{?dist}
Summary:        Biometric Authentication Service

License:        LGPL-3.0 License
URL:            https://github.com/ukui/biometric-authentication
#Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0:        https://github.com/ukui/%{name}/archive/%{version}.zip#/%{name}-%{version}.zip
Patch0:					biometric-authentication-unitdir.patch
BuildArch:      x86_64


BuildRequires: automake
BuildRequires: python3-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel 
BuildRequires:  libusb-devel
BuildRequires: sqlite-devel
BuildRequires: libfprint-devel
BuildRequires: polkit-devel
BuildRequires: libtool
BuildRequires: libuuid-devel

Requires: systemd
Requires: biometric-authentication-libs

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

Requires: biometric-authentication-libs
Requires: systemd
Requires: biometric-authentication,
Requires: python3-prettytable,
Requires: python3-dbus,
Requires: python3-gobject

%description  devel
 It provides the development file for driver development based on biometric
 identification authentication framework.
 .
 This package contains the development files (headers, static libraries)


%package utils

Summary: Biometric authentication utils
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
%{configure} --disable-dependency-tracking  --with-bio-config-dir=/etc/biometric-auth/   --disable-silent-rules --with-bio-db-dir=/var/lib/biometric-auth/     --with-bio-db-name=biometric.db     --with-bio-config-dir=/etc/biometric-auth/     --with-bio-driver-dir=/usr/lib64/biometric-authentication/drivers    --with-bio-extra-dir=/usr/lib64/biometric-authentication/drivers/extra     

%build
%{make_build}

%install
rm -rf %{buildroot}
%{make_install}  INSTALL_ROOT=%{buildroot} 
mkdir -p %{buildroot}/usr/share/man/{man1,man8}
gzip -c doc/man/biometric-auth-client.1	 > %{buildroot}/usr/share/man/man1/biometric-auth-client.1.gz
gzip -c doc/man/biometric-device-discover.1 > %{buildroot}/usr/share/man/man1/biometric-device-discover.1.gz
gzip -c doc/man/biometric-config-tool.8 >%{buildroot}/usr/share/man/man8/biometric-config-tool.8.gz

%files
%doc debian/copyright debian/changelog 
%{_sysconfdir}/biometric-auth/biometric-drivers.conf
%{_sysconfdir}/dbus-1/system.d/org.ukui.Biometric.conf
%{_sysconfdir}/init.d/biometric-authentication
%{_libexecdir}/biometric-authenticationd
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

#DEBHELPER#

if [ ! -f /etc/biometric-auth/biometric-drivers.conf ]; then
	mkdir -p /etc/biometric-auth
	cp /usr/share/biometric-auth/biometric-drivers.conf.template \
		/etc/biometric-auth/biometric-drivers.conf
fi

# Automatically added by dh_systemd_enable/10.7.2ubuntu2
# This will only remove masks created by d-s-h on package removal.
deb-systemd-helper unmask biometric-authentication.service >/dev/null || true

# was-enabled defaults to true, so new installations run enable.
if deb-systemd-helper --quiet was-enabled biometric-authentication.service; then
	# Enables the unit on first installation, creates new
	# symlinks on upgrades if the unit file has changed.
	deb-systemd-helper enable biometric-authentication.service >/dev/null || true
else
	# Update the statefile to add new symlinks (if any), which need to be
	# cleaned up on purge. Also remove old symlinks.
	deb-systemd-helper update-state biometric-authentication.service >/dev/null || true
fi

if [ "$1" = "configure" ] || [ "$1" = "abort-upgrade" ] || [ "$1" = "abort-deconfigure" ] || [ "$1" = "abort-remove" ] ; then
        if [ -x "/etc/init.d/biometric-authentication" ]; then
                update-rc.d biometric-authentication defaults >/dev/null || exit 1
        fi
fi
# End automatically added section

exit 0


%postun 
#!/bin/sh -e

#DEBHELPER#

set -e

BIO_DRIVER_CONF="/etc/biometric-auth/biometric-drivers.conf"
BIO_DATABASE="/var/lib/biometric-auth/biometric.db"
BIO_USERS=`ls /home`

case "$1" in
	remove)
		;;

	purge)
		if [ -e $BIO_DRIVER_CONF ]; then
			rm -rf $BIO_DRIVER_CONF
		fi

		if [ -e $BIO_DATABASE ]; then
			rm -rf $BIO_DATABASE
		fi

		for user in $BIO_USERS;
		do
			user_uuid_file="/home/$user/.biometric_auth/UUID"
			if [ -e $user_uuid_file ]; then
				rm -rf $user_uuid_file
			fi
		done

		;;

	upgrade|failed-upgrade|abort-install|abort-upgrade|disappear)
		;;

	*)
		echo "postrm called with unknown argument '$1'" >&2
		exit 1
		;;
esac

# In case this system is running systemd, we make systemd reload the unit files
# to pick up changes.
if [ -d /run/systemd/system ] ; then
	systemctl --system daemon-reload >/dev/null || true
fi
# End automatically added section

# Automatically added by dh_systemd_enable/11.2.1ubuntu1
if [ "$1" = "remove" ]; then
	if [ -x "/usr/bin/deb-systemd-helper" ]; then
		deb-systemd-helper mask 'biometric-authentication.service' >/dev/null || true
	fi
fi

if [ "$1" = "purge" ]; then
	if [ -x "/usr/bin/deb-systemd-helper" ]; then
		deb-systemd-helper purge 'biometric-authentication.service' >/dev/null || true
		deb-systemd-helper unmask 'biometric-authentication.service' >/dev/null || true
	fi
	update-rc.d biometric-authentication remove >/dev/null
fi
# End automatically added section


%post community-drivers


#!/bin/sh
set -e

#DEBHELPER#

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

DRIVER_LIST="upekts uru4000 aes4000 aes2501 upektc aes1610 fdu2000 vcom5s \
	upeksonly vfs101 vfs301 aes2550 upeke2 aes1660 aes2660 aes3500  \
	upektc_img etes603 vfs5011 vfs0050 elan"

case "${1}" in
	configure)
		for driver in ${DRIVER_LIST}; do
			biometric-config-tool add-driver -f ${driver} \
				/usr/lib/biometric-authentication/drivers/${driver}.so
			biometric-config-tool set-key -i ${driver} AESKey ${KEY_FILE}
		done
		;;

	abort-upgrade|abort-remove|abort-deconfigure)
		;;

	*)
		echo "postinst called with unknown argument \`${1}'" >&2
		exit 1
		;;
esac

exit 0

%preun community-drivers
#!/bin/sh
set -e

#DEBHELPER#

DRIVER_LIST="upekts uru4000 aes4000 aes2501 upektc aes1610 fdu2000 vcom5s \
	upeksonly vfs101 vfs301 aes2550 upeke2 aes1660 aes2660 aes3500  \
	upektc_img etes603 vfs5011 vfs0050 elan"

for driver in ${DRIVER_LIST}; do
	biometric-config-tool remove-driver -i ${driver}
done

exit 0
