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
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  mate-desktop-devel
BuildRequires:  mate-utils-devel
BuildRequires:  mate-common

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

%package devel
Summary: daemon handling the UKUI session settings (development files)
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
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
 This package contains the development files for building
 ukui-settings-daemon plugins.


%prep
%setup -q
./autogen.sh --prefix=/usr --sysconfdir=/etc --libdir=/usr/lib64 --sysconfdir=/etc 

%build
%if 0%{?rhel} == 8
if ! grep -q "qm_files.CONFIG" /usr/lib64/qt5/mkspecs/features/lrelease.prf; then 
sed -i '/qm_files.path/a        qm_files.CONFIG = no_check_exist'  /usr/lib64/qt5/mkspecs/features/lrelease.prf
fi
%endif
%{make_build}


%install
%{make_install} INSTALL_ROOT=%{buildroot}

%find_lang %name

%files
%{_sysconfdir}/xrdb/
%{_sysconfdir}/xdg/autostart/ukui-settings-daemon.desktop
%{_sysconfdir}/ukui-settings-daemon/xrandr
%{_sysconfdir}/dbus-1/system.d/org.ukui.SettingsDaemon.DateTimeMechanism.conf
%{_libdir}/ukui-settings-daemon
%{_libexecdir}/ukui-settings-daemon
%{_libexecdir}/usd-datetime-mechanism
%{_libexecdir}/usd-locate-pointer
%{_libexecdir}/usd-usb-monitor
%{_datadir}/dbus-1/services/org.ukui.SettingsDaemon.service
%{_datadir}/dbus-1/system-services/org.ukui.SettingsDaemon.DateTimeMechanism.service
%{_datadir}/polkit-1/actions/org.ukui.settingsdaemon.datetimemechanism.policy

%files common -f %name.lang
%doc debian/changelog
%license  debian/copyright
%{_datadir}/glib-2.0/schemas/org.ukui.SettingsDaemon.plugins.a11y-keyboard.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.SettingsDaemon.plugins.a11y-settings.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.SettingsDaemon.plugins.background.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.SettingsDaemon.plugins.clipboard.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.SettingsDaemon.plugins.datetime.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.SettingsDaemon.plugins.housekeeping.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.SettingsDaemon.plugins.keybindings.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.SettingsDaemon.plugins.keyboard.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.SettingsDaemon.plugins.media-keys.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.SettingsDaemon.plugins.mouse.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.SettingsDaemon.plugins.mpris.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.SettingsDaemon.plugins.smartcard.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.SettingsDaemon.plugins.sound.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.SettingsDaemon.plugins.typing-break.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.SettingsDaemon.plugins.xrandr.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.SettingsDaemon.plugins.xrdb.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.SettingsDaemon.plugins.xsettings.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.applications-at.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.font-rendering.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.peripherals-keyboard.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.peripherals-mouse.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.peripherals-smartcard.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.peripherals-touchpad.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.peripherals-touchscreen.gschema.xml
%{_datadir}/icons/ukui/*/actions/*
%{_datadir}/icons/hicolor/*/apps/*
%{_datadir}/ukui-settings-daemon/
%{_datadir}/man/man1/ukui-settings-daemon.1.gz
%{_datadir}/man/man1/usd-datetime-mechanism.1.gz
%{_datadir}/man/man1/usd-locate-pointer.1.gz
%{_mandir}/man1/usd-usb-monitor.1.gz

%files devel
%{_includedir}/ukui-settings-daemon/
%{_libdir}/pkgconfig/ukui-settings-daemon.pc
