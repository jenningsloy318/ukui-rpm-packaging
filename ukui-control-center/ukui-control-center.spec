Name:           ukui-control-center
Version:        3.0.0
Release:        1%{?dist}
Summary:        utilities to configure the UKUI desktop


License:         GPL-2.0 License
URL:            https://github.com/ukui/ukui-control-center
Source0:        %{name}-%{version}.tar.gz


BuildArch:      x86_64

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: gsettings-qt-devel
BuildRequires: glib2-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: libmatekbd-devel
BuildRequires: libxklavier-devel
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: dconf-devel
BuildRequires: edid-decode
BuildRequires: libmatemixer-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: libxml2-devel
BuildRequires: libkscreen-qt5-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: libcanberra-devel
BuildRequires: libXi-devel
BuildRequires: mate-desktop-devel
BuildRequires: libxkbcommon-devel 
BuildRequires: libxkbfile-devel
BuildRequires: qt5-linguist
BuildRequires: kf5-kwindowsystem-devel
BuildRequires: kf5-kguiaddons-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: boost-devel
BuildRequires: libxcb-devel
BuildRequires: xcb-util-devel

Requires: redhat-lsb-core
Requires: qt5-qtquickcontrols
Requires: qt5-qtgraphicaleffects

Recommends: redshift
Recommends: qt5-qtquickcontrols


Suggests: gsettings-desktop-schemas
Suggests: mate-common
Suggests: ukui-power-manager
Suggests: ukui-session-manager
Suggests: ukui-screensaver
Suggests: ukui-settings-daemon
Suggests: qt5-qtgraphicaleffects

%description
utilities to configure the UKUI desktop
 The UKUI control center contains configuration applets for the UKUI desktop,
 allowing to set accessibility configuration, desktop fonts, keyboard
 and mouse properties, sound setup, desktop theme and background, user
 interface properties, screen resolution, and other UKUI parameters.

%prep
%setup -q

%build
export PATH=%{_qt5_bindir}:$PATH
%if 0%{?rhel} == 8
if ! grep -q "qm_files.CONFIG" /usr/lib64/qt5/mkspecs/features/lrelease.prf; then
  sed -i '/qm_files.path/a qm_files.CONFIG = no_check_exist'  /usr/lib64/qt5/mkspecs/features/lrelease.prf
fi
%endif
mkdir qmake-build
pushd qmake-build
%{qmake_qt5} ..
%{make_build}
popd

%install
pushd qmake-build
%{make_install} INSTALL_ROOT=%{buildroot}
popd
install -d  %{buildroot}/usr/share/dbus-1/system-services/ %{buildroot}/etc/dbus-1/system.d/ 
install -m644 registeredQDbus/conf/com.control.center.qt.systemdbus.service %{buildroot}/usr/share/dbus-1/system-services/com.control.center.qt.systemdbus.service
install -m644 registeredQDbus/conf/com.control.center.qt.systemdbus.conf %{buildroot}/etc/dbus-1/system.d/com.control.center.qt.systemdbus.conf
%find_lang installer-timezones

%files -f installer-timezones.lang 
%doc debian/changelog
%license  debian/copyright 
%{_sysconfdir}/dbus-1/system.d/com.control.center.qt.systemdbus.conf
%{_bindir}/*
%{_libdir}/ukui-control-center/
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/applications/ukui-control-center.desktop
%{_datadir}/dbus-1/system-services/com.control.center.qt.systemdbus.service
%{_datadir}/ukui-control-center/
%{_datadir}/ukui/faces/*
