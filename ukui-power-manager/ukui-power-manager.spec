Name:           ukui-power-manager
Version:        master
Release:        1%{?dist}
Summary:        power management tool for the UKUI desktop




License:        GPL-2.0 License
URL:            https://github.com/ukui/ukui-power-manager
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64




BuildRequires: gtk3-devel
BuildRequires: libwnck3-devel

BuildRequires: qt5-qtbase-devel
BuildRequires: intltool
BuildRequires: libcanberra-devel
BuildRequires: libcanberra-gtk3
BuildRequires: glib2-devel
BuildRequires: dbus-glib-devel
BuildRequires:  libnotify-devel
BuildRequires:  libtool
BuildRequires:  libgcrypt-devel
BuildRequires:  upower-devel
BuildRequires: libX11-devel
BuildRequires:  libXext-devel
BuildRequires: libXrandr-devel
BuildRequires: perl-XML-Parser
BuildRequires: qt5-qtx11extras-devel
BuildRequires: gsettings-qt-devel
BuildRequires: mate-common
BuildRequires: mate-desktop-devel
BuildRequires: qt5-qtcharts-devel
BuildRequires: xmlto
BuildRequires: yelp-tools
BuildRequires: libgnome-keyring-devel

Requires: dbus-x11
Requires: mate-notification-daemon
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Requires: systemd
Requires: ukui-polkit
Requires: upower

%description
 UKUI Power Manager is a session daemon for the UKUI desktop
 that takes care of system or desktop events related to power, and
 triggers actions accordingly. Its philosophy is to completely hide
 these complex tasks and only show some settings important to the user.
 .
 The UKUI power manager displays and manages battery status, power plug
 events, display brightness, CPU, graphics card and hard disk drive
 power saving, and can trigger suspend-to-RAM, hibernate or shutdown
 events, all integrated to other components of the UKUI desktop.


%package common
Summary:  power management tool for the UKUI desktop (common files)

%description common
 UKUI Power Manager is a session daemon for the UKUI desktop
 that takes care of system or desktop events related to power, and
 triggers actions accordingly. Its philosophy is to completely hide
 these complex tasks and only show some settings important to the user.
 .
 The UKUI power manager displays and manages battery status, power plug
 events, display brightness, CPU, graphics card and hard disk drive
 power saving, and can trigger suspend-to-RAM, hibernate or shutdown
 events, all integrated to other components of the UKUI desktop.
 .
 This package contains the architecture independent files.


%prep

%setup -q
 ./autogen.sh --prefix=/usr --sysconfdir=/etc --libdir=/usr/lib64 -enable-introspection --enable-compile-warnings=yes  --enable-egl-device     --enable-wayland        --enable-native-backend

%build
%{make_build}

%install
%{make_install} INSTALL_ROOT=%{buildroot}

%files
%doc debian/copyright debian/changelog
%{_sysconfdir}/xdg/autostart/ukui-power-manager-tray.desktop
%{_sysconfdir}/xdg/autostart/ukui-power-manager.desktop
%{_bindir}/ukui-power-manager
%{_bindir}/ukui-power-preferences
%{_sbindir}/ukui-power-backlight-helper
%{_datadir}/applications/ukui-power-preferences.desktop
%{_datadir}/applications/ukui-power-statistics.desktop
%{_datadir}/dbus-1/services/org.ukui.PowerManager.service
%{_datadir}/polkit-1/actions/org.ukui.power.policy



%files common
%{_datadir}/doc/ukui-power-manager
%{_datadir}/ukui-power-manager/
%{_datadir}/locale/am/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/ar/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/as/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/ast/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/be/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/bg/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/bn/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/bn_IN/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/br/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/ca/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/ca@valencia/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/cmn/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/cs/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/cy/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/da/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/de/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/dz/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/el/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/en_AU/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/en_CA/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/en_GB/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/es/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/es_CO/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/es_MX/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/et/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/eu/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/fa/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/fi/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/fr/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/ga/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/gl/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/gu/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/he/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/hi/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/hr/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/hu/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/hy/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/id/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/is/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/it/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/ja/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/ka/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/kk/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/kn/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/ko/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/ku/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/ku_IQ/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/ky/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/lt/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/lv/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/mai/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/mg/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/mk/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/ml/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/mr/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/ms/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/nb/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/nl/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/nn/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/oc/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/or/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/pa/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/pl/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/pms/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/pt/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/ro/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/ru/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/si/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/sk/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/sl/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/sq/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/sr/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/sr@latin/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/sv/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/ta/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/te/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/th/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/tr/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/uk/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/ur/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/uz/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/vi/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/zh_HK/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/locale/zh_TW/LC_MESSAGES/ukui-power-manager.mo
%{_datadir}/glib-2.0/schemas/org.ukui.power-manager.gschema.xml
%{_datadir}/man/man1/ukui-power-backlight-helper.1.gz
%{_datadir}/man/man1/ukui-power-manager-tray.1.gz
%{_datadir}/man/man1/ukui-power-manager.1.gz
%{_datadir}/man/man1/ukui-power-preferences.1.gz
%{_datadir}/man/man1/ukui-power-statistics.1.gz
%{_datadir}/help/C/ukui-power-manager/figures/applet-brightness.png
%{_datadir}/help/C/ukui-power-manager/figures/applet-inhibit.png
%{_datadir}/help/C/ukui-power-manager/figures/gpm-cell-capacity.png
%{_datadir}/help/C/ukui-power-manager/figures/gpm-charged.png
%{_datadir}/help/C/ukui-power-manager/figures/gpm-critical.png
%{_datadir}/help/C/ukui-power-manager/figures/gpm-low.png
%{_datadir}/help/C/ukui-power-manager/figures/gpm-prefs-ac.png
%{_datadir}/help/C/ukui-power-manager/figures/gpm-prefs-battery.png
%{_datadir}/help/C/ukui-power-manager/figures/gpm-prefs-general.png
%{_datadir}/help/C/ukui-power-manager/figures/gpm-stats-graph.png
%{_datadir}/help/C/ukui-power-manager/figures/gpm-suspend-problem.png
%{_datadir}/help/C/ukui-power-manager/figures/gpm-unplugged.png
%{_datadir}/help/C/ukui-power-manager/figures/gs-prefs.png
%{_datadir}/help/C/ukui-power-manager/index.docbook
%{_datadir}/help/C/ukui-power-manager/legal.xml
%{_datadir}/help/ca/ukui-power-manager/figures/applet-brightness.png
%{_datadir}/help/ca/ukui-power-manager/figures/applet-inhibit.png
%{_datadir}/help/ca/ukui-power-manager/figures/gpm-cell-capacity.png
%{_datadir}/help/ca/ukui-power-manager/figures/gpm-charged.png
%{_datadir}/help/ca/ukui-power-manager/figures/gpm-critical.png
%{_datadir}/help/ca/ukui-power-manager/figures/gpm-low.png
%{_datadir}/help/ca/ukui-power-manager/figures/gpm-prefs-ac.png
%{_datadir}/help/ca/ukui-power-manager/figures/gpm-prefs-battery.png
%{_datadir}/help/ca/ukui-power-manager/figures/gpm-prefs-general.png
%{_datadir}/help/ca/ukui-power-manager/figures/gpm-stats-graph.png
%{_datadir}/help/ca/ukui-power-manager/figures/gpm-suspend-problem.png
%{_datadir}/help/ca/ukui-power-manager/figures/gpm-unplugged.png
%{_datadir}/help/ca/ukui-power-manager/figures/gs-prefs.png
%{_datadir}/help/ca/ukui-power-manager/index.docbook
%{_datadir}/help/ca/ukui-power-manager/legal.xml
%{_datadir}/help/de/ukui-power-manager/figures/applet-brightness.png
%{_datadir}/help/de/ukui-power-manager/figures/applet-inhibit.png
%{_datadir}/help/de/ukui-power-manager/figures/gpm-cell-capacity.png
%{_datadir}/help/de/ukui-power-manager/figures/gpm-charged.png
%{_datadir}/help/de/ukui-power-manager/figures/gpm-critical.png
%{_datadir}/help/de/ukui-power-manager/figures/gpm-low.png
%{_datadir}/help/de/ukui-power-manager/figures/gpm-prefs-ac.png
%{_datadir}/help/de/ukui-power-manager/figures/gpm-prefs-battery.png
%{_datadir}/help/de/ukui-power-manager/figures/gpm-prefs-general.png
%{_datadir}/help/de/ukui-power-manager/figures/gpm-stats-graph.png
%{_datadir}/help/de/ukui-power-manager/figures/gpm-suspend-problem.png
%{_datadir}/help/de/ukui-power-manager/figures/gpm-unplugged.png
%{_datadir}/help/de/ukui-power-manager/figures/gs-prefs.png
%{_datadir}/help/de/ukui-power-manager/index.docbook
%{_datadir}/help/de/ukui-power-manager/legal.xml
%{_datadir}/help/el/ukui-power-manager/figures/applet-brightness.png
%{_datadir}/help/el/ukui-power-manager/figures/applet-inhibit.png
%{_datadir}/help/el/ukui-power-manager/figures/gpm-cell-capacity.png
%{_datadir}/help/el/ukui-power-manager/figures/gpm-charged.png
%{_datadir}/help/el/ukui-power-manager/figures/gpm-critical.png
%{_datadir}/help/el/ukui-power-manager/figures/gpm-low.png
%{_datadir}/help/el/ukui-power-manager/figures/gpm-prefs-ac.png
%{_datadir}/help/el/ukui-power-manager/figures/gpm-prefs-battery.png
%{_datadir}/help/el/ukui-power-manager/figures/gpm-prefs-general.png
%{_datadir}/help/el/ukui-power-manager/figures/gpm-stats-graph.png
%{_datadir}/help/el/ukui-power-manager/figures/gpm-suspend-problem.png
%{_datadir}/help/el/ukui-power-manager/figures/gpm-unplugged.png
%{_datadir}/help/el/ukui-power-manager/figures/gs-prefs.png
%{_datadir}/help/el/ukui-power-manager/index.docbook
%{_datadir}/help/el/ukui-power-manager/legal.xml
%{_datadir}/help/en_GB/ukui-power-manager/figures/applet-brightness.png
%{_datadir}/help/en_GB/ukui-power-manager/figures/applet-inhibit.png
%{_datadir}/help/en_GB/ukui-power-manager/figures/gpm-cell-capacity.png
%{_datadir}/help/en_GB/ukui-power-manager/figures/gpm-charged.png
%{_datadir}/help/en_GB/ukui-power-manager/figures/gpm-critical.png
%{_datadir}/help/en_GB/ukui-power-manager/figures/gpm-low.png
%{_datadir}/help/en_GB/ukui-power-manager/figures/gpm-prefs-ac.png
%{_datadir}/help/en_GB/ukui-power-manager/figures/gpm-prefs-battery.png
%{_datadir}/help/en_GB/ukui-power-manager/figures/gpm-prefs-general.png
%{_datadir}/help/en_GB/ukui-power-manager/figures/gpm-stats-graph.png
%{_datadir}/help/en_GB/ukui-power-manager/figures/gpm-suspend-problem.png
%{_datadir}/help/en_GB/ukui-power-manager/figures/gpm-unplugged.png
%{_datadir}/help/en_GB/ukui-power-manager/figures/gs-prefs.png
%{_datadir}/help/en_GB/ukui-power-manager/index.docbook
%{_datadir}/help/en_GB/ukui-power-manager/legal.xml
%{_datadir}/help/es/ukui-power-manager/figures/applet-brightness.png
%{_datadir}/help/es/ukui-power-manager/figures/applet-inhibit.png
%{_datadir}/help/es/ukui-power-manager/figures/gpm-cell-capacity.png
%{_datadir}/help/es/ukui-power-manager/figures/gpm-charged.png
%{_datadir}/help/es/ukui-power-manager/figures/gpm-critical.png
%{_datadir}/help/es/ukui-power-manager/figures/gpm-low.png
%{_datadir}/help/es/ukui-power-manager/figures/gpm-prefs-ac.png
%{_datadir}/help/es/ukui-power-manager/figures/gpm-prefs-battery.png
%{_datadir}/help/es/ukui-power-manager/figures/gpm-prefs-general.png
%{_datadir}/help/es/ukui-power-manager/figures/gpm-stats-graph.png
%{_datadir}/help/es/ukui-power-manager/figures/gpm-suspend-problem.png
%{_datadir}/help/es/ukui-power-manager/figures/gpm-unplugged.png
%{_datadir}/help/es/ukui-power-manager/figures/gs-prefs.png
%{_datadir}/help/es/ukui-power-manager/index.docbook
%{_datadir}/help/es/ukui-power-manager/legal.xml
%{_datadir}/help/eu/ukui-power-manager/figures/applet-brightness.png
%{_datadir}/help/eu/ukui-power-manager/figures/applet-inhibit.png
%{_datadir}/help/eu/ukui-power-manager/figures/gpm-cell-capacity.png
%{_datadir}/help/eu/ukui-power-manager/figures/gpm-charged.png
%{_datadir}/help/eu/ukui-power-manager/figures/gpm-critical.png
%{_datadir}/help/eu/ukui-power-manager/figures/gpm-low.png
%{_datadir}/help/eu/ukui-power-manager/figures/gpm-prefs-ac.png
%{_datadir}/help/eu/ukui-power-manager/figures/gpm-prefs-battery.png
%{_datadir}/help/eu/ukui-power-manager/figures/gpm-prefs-general.png
%{_datadir}/help/eu/ukui-power-manager/figures/gpm-stats-graph.png
%{_datadir}/help/eu/ukui-power-manager/figures/gpm-suspend-problem.png
%{_datadir}/help/eu/ukui-power-manager/figures/gpm-unplugged.png
%{_datadir}/help/eu/ukui-power-manager/figures/gs-prefs.png
%{_datadir}/help/eu/ukui-power-manager/index.docbook
%{_datadir}/help/eu/ukui-power-manager/legal.xml
%{_datadir}/help/fi/ukui-power-manager/figures/applet-brightness.png
%{_datadir}/help/fi/ukui-power-manager/figures/applet-inhibit.png
%{_datadir}/help/fi/ukui-power-manager/figures/gpm-cell-capacity.png
%{_datadir}/help/fi/ukui-power-manager/figures/gpm-charged.png
%{_datadir}/help/fi/ukui-power-manager/figures/gpm-critical.png
%{_datadir}/help/fi/ukui-power-manager/figures/gpm-low.png
%{_datadir}/help/fi/ukui-power-manager/figures/gpm-prefs-ac.png
%{_datadir}/help/fi/ukui-power-manager/figures/gpm-prefs-battery.png
%{_datadir}/help/fi/ukui-power-manager/figures/gpm-prefs-general.png
%{_datadir}/help/fi/ukui-power-manager/figures/gpm-stats-graph.png
%{_datadir}/help/fi/ukui-power-manager/figures/gpm-suspend-problem.png
%{_datadir}/help/fi/ukui-power-manager/figures/gpm-unplugged.png
%{_datadir}/help/fi/ukui-power-manager/figures/gs-prefs.png
%{_datadir}/help/fi/ukui-power-manager/index.docbook
%{_datadir}/help/fi/ukui-power-manager/legal.xml
%{_datadir}/help/fr/ukui-power-manager/figures/applet-brightness.png
%{_datadir}/help/fr/ukui-power-manager/figures/applet-inhibit.png
%{_datadir}/help/fr/ukui-power-manager/figures/gpm-cell-capacity.png
%{_datadir}/help/fr/ukui-power-manager/figures/gpm-charged.png
%{_datadir}/help/fr/ukui-power-manager/figures/gpm-critical.png
%{_datadir}/help/fr/ukui-power-manager/figures/gpm-low.png
%{_datadir}/help/fr/ukui-power-manager/figures/gpm-prefs-ac.png
%{_datadir}/help/fr/ukui-power-manager/figures/gpm-prefs-battery.png
%{_datadir}/help/fr/ukui-power-manager/figures/gpm-prefs-general.png
%{_datadir}/help/fr/ukui-power-manager/figures/gpm-stats-graph.png
%{_datadir}/help/fr/ukui-power-manager/figures/gpm-suspend-problem.png
%{_datadir}/help/fr/ukui-power-manager/figures/gpm-unplugged.png
%{_datadir}/help/fr/ukui-power-manager/figures/gs-prefs.png
%{_datadir}/help/fr/ukui-power-manager/index.docbook
%{_datadir}/help/fr/ukui-power-manager/legal.xml
%{_datadir}/help/hu/ukui-power-manager/figures/applet-brightness.png
%{_datadir}/help/hu/ukui-power-manager/figures/applet-inhibit.png
%{_datadir}/help/hu/ukui-power-manager/figures/gpm-cell-capacity.png
%{_datadir}/help/hu/ukui-power-manager/figures/gpm-charged.png
%{_datadir}/help/hu/ukui-power-manager/figures/gpm-critical.png
%{_datadir}/help/hu/ukui-power-manager/figures/gpm-low.png
%{_datadir}/help/hu/ukui-power-manager/figures/gpm-prefs-ac.png
%{_datadir}/help/hu/ukui-power-manager/figures/gpm-prefs-battery.png
%{_datadir}/help/hu/ukui-power-manager/figures/gpm-prefs-general.png
%{_datadir}/help/hu/ukui-power-manager/figures/gpm-stats-graph.png
%{_datadir}/help/hu/ukui-power-manager/figures/gpm-suspend-problem.png
%{_datadir}/help/hu/ukui-power-manager/figures/gpm-unplugged.png
%{_datadir}/help/hu/ukui-power-manager/figures/gs-prefs.png
%{_datadir}/help/hu/ukui-power-manager/index.docbook
%{_datadir}/help/hu/ukui-power-manager/legal.xml
%{_datadir}/help/it/ukui-power-manager/figures/applet-brightness.png
%{_datadir}/help/it/ukui-power-manager/figures/applet-inhibit.png
%{_datadir}/help/it/ukui-power-manager/figures/gpm-cell-capacity.png
%{_datadir}/help/it/ukui-power-manager/figures/gpm-charged.png
%{_datadir}/help/it/ukui-power-manager/figures/gpm-critical.png
%{_datadir}/help/it/ukui-power-manager/figures/gpm-low.png
%{_datadir}/help/it/ukui-power-manager/figures/gpm-prefs-ac.png
%{_datadir}/help/it/ukui-power-manager/figures/gpm-prefs-battery.png
%{_datadir}/help/it/ukui-power-manager/figures/gpm-prefs-general.png
%{_datadir}/help/it/ukui-power-manager/figures/gpm-stats-graph.png
%{_datadir}/help/it/ukui-power-manager/figures/gpm-suspend-problem.png
%{_datadir}/help/it/ukui-power-manager/figures/gpm-unplugged.png
%{_datadir}/help/it/ukui-power-manager/figures/gs-prefs.png
%{_datadir}/help/it/ukui-power-manager/index.docbook
%{_datadir}/help/it/ukui-power-manager/legal.xml
%{_datadir}/help/oc/ukui-power-manager/figures/applet-brightness.png
%{_datadir}/help/oc/ukui-power-manager/figures/applet-inhibit.png
%{_datadir}/help/oc/ukui-power-manager/figures/gpm-cell-capacity.png
%{_datadir}/help/oc/ukui-power-manager/figures/gpm-charged.png
%{_datadir}/help/oc/ukui-power-manager/figures/gpm-critical.png
%{_datadir}/help/oc/ukui-power-manager/figures/gpm-low.png
%{_datadir}/help/oc/ukui-power-manager/figures/gpm-prefs-ac.png
%{_datadir}/help/oc/ukui-power-manager/figures/gpm-prefs-battery.png
%{_datadir}/help/oc/ukui-power-manager/figures/gpm-prefs-general.png
%{_datadir}/help/oc/ukui-power-manager/figures/gpm-stats-graph.png
%{_datadir}/help/oc/ukui-power-manager/figures/gpm-suspend-problem.png
%{_datadir}/help/oc/ukui-power-manager/figures/gpm-unplugged.png
%{_datadir}/help/oc/ukui-power-manager/figures/gs-prefs.png
%{_datadir}/help/oc/ukui-power-manager/index.docbook
%{_datadir}/help/oc/ukui-power-manager/legal.xml
%{_datadir}/help/pa/ukui-power-manager/figures/applet-brightness.png
%{_datadir}/help/pa/ukui-power-manager/figures/applet-inhibit.png
%{_datadir}/help/pa/ukui-power-manager/figures/gpm-cell-capacity.png
%{_datadir}/help/pa/ukui-power-manager/figures/gpm-charged.png
%{_datadir}/help/pa/ukui-power-manager/figures/gpm-critical.png
%{_datadir}/help/pa/ukui-power-manager/figures/gpm-low.png
%{_datadir}/help/pa/ukui-power-manager/figures/gpm-prefs-ac.png
%{_datadir}/help/pa/ukui-power-manager/figures/gpm-prefs-battery.png
%{_datadir}/help/pa/ukui-power-manager/figures/gpm-prefs-general.png
%{_datadir}/help/pa/ukui-power-manager/figures/gpm-stats-graph.png
%{_datadir}/help/pa/ukui-power-manager/figures/gpm-suspend-problem.png
%{_datadir}/help/pa/ukui-power-manager/figures/gpm-unplugged.png
%{_datadir}/help/pa/ukui-power-manager/figures/gs-prefs.png
%{_datadir}/help/pa/ukui-power-manager/index.docbook
%{_datadir}/help/pa/ukui-power-manager/legal.xml
%{_datadir}/help/ru/ukui-power-manager/figures/applet-brightness.png
%{_datadir}/help/ru/ukui-power-manager/figures/applet-inhibit.png
%{_datadir}/help/ru/ukui-power-manager/figures/gpm-cell-capacity.png
%{_datadir}/help/ru/ukui-power-manager/figures/gpm-charged.png
%{_datadir}/help/ru/ukui-power-manager/figures/gpm-critical.png
%{_datadir}/help/ru/ukui-power-manager/figures/gpm-low.png
%{_datadir}/help/ru/ukui-power-manager/figures/gpm-prefs-ac.png
%{_datadir}/help/ru/ukui-power-manager/figures/gpm-prefs-battery.png
%{_datadir}/help/ru/ukui-power-manager/figures/gpm-prefs-general.png
%{_datadir}/help/ru/ukui-power-manager/figures/gpm-stats-graph.png
%{_datadir}/help/ru/ukui-power-manager/figures/gpm-suspend-problem.png
%{_datadir}/help/ru/ukui-power-manager/figures/gpm-unplugged.png
%{_datadir}/help/ru/ukui-power-manager/figures/gs-prefs.png
%{_datadir}/help/ru/ukui-power-manager/index.docbook
%{_datadir}/help/ru/ukui-power-manager/legal.xml
%{_datadir}/help/sv/ukui-power-manager/figures/applet-brightness.png
%{_datadir}/help/sv/ukui-power-manager/figures/applet-inhibit.png
%{_datadir}/help/sv/ukui-power-manager/figures/gpm-cell-capacity.png
%{_datadir}/help/sv/ukui-power-manager/figures/gpm-charged.png
%{_datadir}/help/sv/ukui-power-manager/figures/gpm-critical.png
%{_datadir}/help/sv/ukui-power-manager/figures/gpm-low.png
%{_datadir}/help/sv/ukui-power-manager/figures/gpm-prefs-ac.png
%{_datadir}/help/sv/ukui-power-manager/figures/gpm-prefs-battery.png
%{_datadir}/help/sv/ukui-power-manager/figures/gpm-prefs-general.png
%{_datadir}/help/sv/ukui-power-manager/figures/gpm-stats-graph.png
%{_datadir}/help/sv/ukui-power-manager/figures/gpm-suspend-problem.png
%{_datadir}/help/sv/ukui-power-manager/figures/gpm-unplugged.png
%{_datadir}/help/sv/ukui-power-manager/figures/gs-prefs.png
%{_datadir}/help/sv/ukui-power-manager/index.docbook
%{_datadir}/help/sv/ukui-power-manager/legal.xml
%{_datadir}/help/zh_CN/ukui-power-manager/figures/applet-brightness.png
%{_datadir}/help/zh_CN/ukui-power-manager/figures/applet-inhibit.png
%{_datadir}/help/zh_CN/ukui-power-manager/figures/gpm-cell-capacity.png
%{_datadir}/help/zh_CN/ukui-power-manager/figures/gpm-charged.png
%{_datadir}/help/zh_CN/ukui-power-manager/figures/gpm-critical.png
%{_datadir}/help/zh_CN/ukui-power-manager/figures/gpm-low.png
%{_datadir}/help/zh_CN/ukui-power-manager/figures/gpm-prefs-ac.png
%{_datadir}/help/zh_CN/ukui-power-manager/figures/gpm-prefs-battery.png
%{_datadir}/help/zh_CN/ukui-power-manager/figures/gpm-prefs-general.png
%{_datadir}/help/zh_CN/ukui-power-manager/figures/gpm-stats-graph.png
%{_datadir}/help/zh_CN/ukui-power-manager/figures/gpm-suspend-problem.png
%{_datadir}/help/zh_CN/ukui-power-manager/figures/gpm-unplugged.png
%{_datadir}/help/zh_CN/ukui-power-manager/figures/gs-prefs.png
%{_datadir}/help/zh_CN/ukui-power-manager/index.docbook
%{_datadir}/help/zh_CN/ukui-power-manager/legal.xml