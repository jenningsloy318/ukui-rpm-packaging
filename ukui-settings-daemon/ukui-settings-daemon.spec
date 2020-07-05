Name:           ukui-settings-daemon
Version:        master
Release:        1%{?dist}
Summary:        daemon handling the UKUI session settings

License:         GPL-2.0 License
URL:            https://github.com/ukui/ukui-settings-daemon
# %%Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0:        https://github.com/ukui/%{name}/archive/%{version}.zip#/%{name}-%{version}.zip

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
Requires: ukui-settings-daemon-common
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
%{make_build}


%install
%{make_install} INSTALL_ROOT=%{buildroot}

%files
%{_sysconfdir}/xrdb/
%{_sysconfdir}/xdg/autostart/ukui-settings-daemon.desktop
%{_sysconfdir}/ukui-settings-daemon/xrandr
%{_sysconfdir}/dbus-1/system.d/org.ukui.SettingsDaemon.DateTimeMechanism.conf
%{_libdir}/ukui-settings-daemon
%{_libexecdir}/ukui-settings-daemon
%{_libexecdir}/usd-datetime-mechanism
%{_libexecdir}/usd-locate-pointer
%{_datadir}/dbus-1/services/org.ukui.SettingsDaemon.service
%{_datadir}/dbus-1/system-services/org.ukui.SettingsDaemon.DateTimeMechanism.service
%{_datadir}/polkit-1/actions/org.ukui.settingsdaemon.datetimemechanism.policy

%files common
%doc debian/changelog debian/copyright
%{_datadir}/glib-2.0/schemas//org.ukui.SettingsDaemon.plugins.a11y-keyboard.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.SettingsDaemon.plugins.a11y-settings.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.SettingsDaemon.plugins.background.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.SettingsDaemon.plugins.clipboard.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.SettingsDaemon.plugins.datetime.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.SettingsDaemon.plugins.housekeeping.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.SettingsDaemon.plugins.keybindings.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.SettingsDaemon.plugins.keyboard.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.SettingsDaemon.plugins.media-keys.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.SettingsDaemon.plugins.mouse.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.SettingsDaemon.plugins.mpris.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.SettingsDaemon.plugins.smartcard.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.SettingsDaemon.plugins.sound.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.SettingsDaemon.plugins.typing-break.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.SettingsDaemon.plugins.xrandr.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.SettingsDaemon.plugins.xrdb.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.SettingsDaemon.plugins.xsettings.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.applications-at.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.font-rendering.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.peripherals-keyboard.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.peripherals-mouse.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.peripherals-smartcard.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.peripherals-touchpad.gschema.xml
%{_datadir}/glib-2.0/schemas//org.ukui.peripherals-touchscreen.gschema.xml
%{_datadir}/icons/
%{_datadir}/locale/af/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/am/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/ar/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/as/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/ast/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/az/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/be/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/bg/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/bn/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/bn_IN/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/bo/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/br/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/bs/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/ca/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/ca@valencia/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/cmn/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/crh/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/cs/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/cy/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/da/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/de/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/dz/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/el/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/en_AU/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/en_CA/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/en_GB/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/es/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/es_CO/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/et/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/eu/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/fa/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/fi/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/fr/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/frp/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/ga/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/gl/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/gu/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/he/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/hi/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/hr/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/hu/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/hy/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/id/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/is/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/it/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/ja/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/ka/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/kk/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/kn/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/ko/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/ku/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/ku_IQ/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/ky/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/lt/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/lv/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/mai/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/mg/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/mk/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/ml/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/mn/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/mr/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/ms/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/nb/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/nds/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/ne/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/nl/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/nn/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/nso/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/oc/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/or/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/pa/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/pl/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/pms/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/pt/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/ro/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/ru/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/rw/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/si/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/sk/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/sl/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/sq/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/sr/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/sr@latin/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/sv/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/ta/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/te/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/th/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/tr/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/uk/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/ur/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/uz/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/vi/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/wa/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/xh/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/zh_HK/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/zh_TW/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/locale/zu/LC_MESSAGES/ukui-settings-daemon.mo
%{_datadir}/ukui-settings-daemon/
%{_datadir}/man/man1/ukui-settings-daemon.1.gz
%{_datadir}/man/man1/usd-datetime-mechanism.1.gz
%{_datadir}/man/man1/usd-locate-pointer.1.gz

%files devel
%{_includedir}/ukui-settings-daemon/
%{_libdir}/pkgconfig/ukui-settings-daemon.pc
