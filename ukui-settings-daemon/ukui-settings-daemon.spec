# disable debug package
%define debug_package %{nil}

Name:           ukui-settings-daemon
Version:        3.0.0
Release:        1%{?dist}
Summary:        daemon handling the UKUI session settings

License:         GPL-2.0 License
URL:            https://github.com/ukui/ukui-settings-daemon
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64

BuildRequires:  libcanberra-devel
BuildRequires:  dbus-glib-devel
BuildRequires:  dconf-devel
BuildRequires:  fontconfig-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  mate-desktop-devel
BuildRequires:  libmatekbd-devel
BuildRequires:  libmatemixer-devel
BuildRequires:  libnotify-devel
BuildRequires:  polkit-devel
BuildRequires:  nss-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  pulseaudio-qt-devel
BuildRequires:  startup-notification-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXi-devel
BuildRequires:  libxklavier-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXt-devel
BuildRequires:  libusb-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-utils-devel
BuildRequires:  mate-common
BuildRequires:  colord-devel
BuildRequires:  gnome-desktop3-devel
BuildRequires:  lcms2-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtsensors-devel
BuildRequires:  kf5-kconfig-devel

BuildRequires: qt5-qtsvg-devel
Requires: mate-common
Requires: ukui-polkit
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Requires: xorg-x11-server-utils




%description
 This package contains the daemon which is responsible for setting the
 various parameters of a UKUI session and the applications that run
 under it. It handles the following kinds of settings:
 .
  * Keyboard: layout, accessibility options, shortcuts, media keys
  * Clipboard management
  * Theming: background, icons, GTK+ applications
  * Cleanup of unused files
  * Mouse: cursors, speed, accessibility options
  * Startup of other daemons: screensaver, sound daemon
  * Typing break
 .
 It also sets various application settings through X resources and
 freedesktop.org XSETTINGS.

%package common
Summary: daemon handling the UKUI session settings (common files)

%description common
 This package contains the daemon which is responsible for setting the
 various parameters of a UKUI session and the applications that run
 under it. It handles the following kinds of settings:
 .
  * Keyboard: layout, accessibility options, shortcuts, media keys
  * Clipboard management
  * Theming: background, icons, GTK+ applications
  * Cleanup of unused files
  * Mouse: cursors, speed, accessibility options
  * Startup of other daemons: screensaver, sound daemon
  * Typing break
 .
 It also sets various application settings through X resources and
 freedesktop.org XSETTINGS.
 .
 This package contains the architecture independent files.



%prep
%setup -q

%build
export PATH=%{_qt5_bindir}:$PATH
mkdir qmake-build
pushd qmake-build
%if 0%{?rhel} == 8
if ! grep -q "qm_files.CONFIG" /usr/lib64/qt5/mkspecs/features/lrelease.prf; then 
sed -i '/qm_files.path/a qm_files.CONFIG = no_check_exist'  /usr/lib64/qt5/mkspecs/features/lrelease.prf
fi
%endif
%{qmake_qt5} ..
%{make_build}
popd

%install
pushd qmake-build
%{make_install} INSTALL_ROOT=%{buildroot}
popd 
mkdir -p %{buildroot}/usr/share/man/man1/
gzip -c man/ukui-settings-daemon.1	 > %{buildroot}/usr/share/man/man1/ukui-settings-daemon.1.gz
gzip -c man/usd-locate-pointer.1	 > %{buildroot}/usr/share/man/man1/usd-locate-pointer.1.gz
%find_lang %name

%files
%{_sysconfdir}/xdg/autostart/ukui-settings-daemon.desktop
%{_sysconfdir}/udev/rules.d/01-touchpad-state-onmouse.rules
%{_bindir}/*
%{_libdir}/ukui-settings-daemon
%{_datadir}/dbus-1/services/org.ukui.SettingsDaemon.service

%files common -f %name.lang
%doc debian/changelog
%license  debian/copyright
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/ukui-settings-daemon/
%{_mandir}/man1/*


%post 
glib-compile-schemas /usr/share/glib-2.0/schemas
