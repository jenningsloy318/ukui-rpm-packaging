%global __cmake_in_source_build 1


Name:           ukui-panel
Version:        3.0.1
Release:        1%{?dist}
Summary:        ukui desktop panel


License:         LGPL-2.1 License
URL:            https://github.com/ukui/ukui-panel
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64
BuildRequires:  kf5-rpm-macros
BuildRequires:  peony-devel
BuildRequires:  dbusmenu-qt5-devel
BuildRequires:  glib2-devel
BuildRequires:  libicu-devel
BuildRequires:  kf5-solid-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  pulseaudio-qt-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  libstatgrab-devel
BuildRequires:  libX11-devel
BuildRequires:  libxcb-devel
BuildRequires:  xcb-util-devel
BuildRequires:  xcb-util-keysyms-devel
BuildRequires:  xcb-util-image-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  libXdamage-devel
BuildRequires:  libxkbcommon-devel
BuildRequires:  libxkbcommon-x11-devel
BuildRequires:  libXrandr-devel
BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  libqtxdg-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  dconf-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  dbusmenu-qt5-devel

Provides: ukui-indicators
Suggests: ukui-window-switch

%description
 The ukui desktop panel is used on ukui desktop and has some plugins like
 starmenu, quicklaunch and other useful tools.
 .
 This package contains the ukui panel.


%prep
%setup -q
sed -i  '/UKUiPreventInSourceBuilds.cmake/d'  panel/common/CMakeLists.txt panel/xdg/CMakeLists.txt CMakeLists.txt
%build
export PATH=%{_qt5_bindir}:$PATH
mkdir cmake-build
pushd cmake-build
%{cmake} ..
%{make_build} 
popd

%install
pushd cmake-build
%{make_install} INSTALL_ROOT=%{buildroot}
popd
install -d   %{buildroot}/usr/share/man/man1/
gzip -c man/ukui-panel.1  > %{buildroot}/usr/share/man/man1/ukui-panel.1.gz
gzip -c man/ukui-flash-disk.1 > %{buildroot}/usr/share/man/man1/ukui-flash-disk.1.gz

%files
%doc debian/changelog
%license  debian/copyright
%{_bindir}/ukui-panel
%{_bindir}/ukui-flash-disk
%{_sysconfdir}/xdg/autostart/ukui-flash-disk.desktop
%{_sysconfdir}/xdg/autostart/ukui-panel.desktop
%{_includedir}/ukui/
%{_libdir}/pkgconfig/ukui.pc
%{_libdir}/ukui-panel/
%{_datadir}/man/man1/ukui-panel.1.gz
%{_datadir}/man/man1/ukui-flash-disk.1.gz
%{_datadir}/cmake/ukui/ukui-config-version.cmake
%{_datadir}/cmake/ukui/ukui-config.cmake
%{_datadir}/glib-2.0/schemas/org.ukui.panel.settings.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.panel.tray.gschema.xml
%{_datadir}/ukui-panel/
%{_datadir}/ukui/
