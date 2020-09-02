%global __cmake_in_source_build 1


Name:           ukui-kwin
Version:        master
Release:        1%{?dist}
Summary:        UKUI window manager



License:         GPL-2.0 License
URL:            https://github.com/ukui/ukui-kwin
Source0:        %{name}-%{version}.tar.gz
BuildArch:      x86_64

# Base

BuildRequires: extra-cmake-modules
BuildRequires: kf5-rpm-macros
BuildRequires: glib2-devel

# Qt
BuildRequires: qt5-qtsvg-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qttools-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-qtdeclarative-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qtsensors-devel
BuildRequires: qt5-qttools-static
BuildRequires: gsettings-qt-devel
BuildRequires: poppler-qt5-devel
BuildRequires: qt5-qtbase-static
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qt5-qtvirtualkeyboard-devel
BuildRequires: qt5-qtquickcontrols

# kf5 
BuildRequires: kf5-kconfigwidgets-devel
BuildRequires: kf5-kcrash-devel
BuildRequires: kf5-kglobalaccel-devel
BuildRequires: kf5-ki18n-devel
BuildRequires: kf5-kiconthemes-devel
BuildRequires: kf5-kidletime-devel
BuildRequires: kf5-kinit-devel
BuildRequires: kf5-knotifications-devel
BuildRequires: kf5-kpackage-devel
BuildRequires: kf5-kguiaddons-devel
# on fedora, kf5-plasma-devel is conflicted with qt5-qtquickcontrols, already issue a bug, https://bugzilla.redhat.com/show_bug.cgi?id=1849944
BuildRequires: kf5-plasma-devel 

BuildRequires: kf5-kwayland-devel
BuildRequires: kf5-kwidgetsaddons-devel
BuildRequires: kf5-kcompletion-devel
BuildRequires: kf5-kdeclarative-devel
BuildRequires: kf5-kcmutils-devel
BuildRequires: kf5-kio-devel
BuildRequires: kf5-knewstuff-devel
BuildRequires: kf5-kservice-devel
BuildRequires: kf5-ktextwidgets-devel
BuildRequires: kf5-kxmlgui-devel
BuildRequires: kf5-kactivities-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kirigami2-devel
BuildRequires: kf5-kconfig-devel
BuildRequires: kf5-kcoreaddons-devel
BuildRequires: kf5-kwindowsystem-devel

# X11/OpenGL
BuildRequires: libxcb-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-image-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: xcb-util-renderutil-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libinput-devel
BuildRequires: systemd-devel
BuildRequires: libdrm-devel
BuildRequires: mesa-libgbm-devel
BuildRequires: libepoxy-devel
BuildRequires: libICE-devel
BuildRequires: libSM-devel
BuildRequires: libXi-devel 
# Wayland 
BuildRequires: mesa-libEGL-devel
BuildRequires: wayland-devel
BuildRequires: libwayland-client-devel
BuildRequires: libwayland-server-devel
BuildRequires: libwayland-cursor-devel
BuildRequires: xorg-x11-server-Xwayland


BuildRequires: kdecoration-devel
BuildRequires: kscreenlocker-devel
BuildRequires: libcap-devel
BuildRequires: plasma-breeze-devel

Requires: %{name}-common%{?_isa}  = %{version}-%{release}
Requires: %{name}-libs%{?_isa}  = %{version}-%{release}
Requires: (%{name}-x11%{?_isa} = %{version}-%{release} or %{name}-wayland%{?_isa} = %{version}-%{release})

%description
 This package is a transitional dummy to depend on the renamed ukui-kwin-x11 and
 can be removed.


%package common
Summary: UKUI window manager, common files

Requires: kf5-kglobalaccel
Requires: kf5-kirigami2
Requires: kf5-kdeclarative
Requires: qt5-qtmultimedia
Requires: kf5-plasma
 
Recommends: qt5-qtmultimedia
Recommends: qt5-qtquickcontrols
Recommends: qt5-qtdeclarative
Recommends: qt5-qtvirtualkeyboard
%description common
  Ukui-kwin  is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paints
 the window decoration, the bar on top of every window with
 (configurable) buttons like close, maximize and minimize.
 It also handles placing of windows and switching between them.
 .
 This package is part of the UKUI project.


%package libs
Summary: KWin runtime libraries

Requires: %{name}-common%{?_isa}  = %{version}-%{release}

%description libs
ukui-KWin runtime libraries.


%package devel
Summary: UKUI window manager - devel files
Requires: %{name}-common%{?_isa}  = %{version}-%{release}
Requires: %{name}-libs%{?_isa}  = %{version}-%{release}

%description devel
 Ukui-kwin  is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paints
 the window decoration, the bar on top of every window with
 (configurable) buttons like close, maximize and minimize.
 It also handles placing of windows and switching between them.
 .
 This package is part of the UKUI project.


%package wayland
Summary: UKUI window manager, wayland version
Requires: kwayland-integration
Requires: %{name}-common%{?_isa}  = %{version}-%{release}
Requires: %{name}-libs%{?_isa}  = %{version}-%{release}
Requires: libcap
Requires: xorg-x11-server-Xwayland

Provides: ukui-kwin

%description wayland
 Ukui-kwin  is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paintsqt5-qtbase-guiprogress
 project, and is available as a PREVIEW release. Don't expect the same
 stability as with the x11 version.

%package x11
Summary: UKUI window manager drm plugin
Provides: ukui-kwin, x-window-manager

Requires: %{name}-common%{?_isa}  = %{version}-%{release}
Requires: %{name}-libs%{?_isa}  = %{version}-%{release}
%description x11
 Ukui-kwin  is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paints
 the window decoration, the bar on top of every window with
 (configurable) buttons like close, maximize and minimize.
 It also handles placing of windows and switching between them.
 .
 This package is part of the UKUI project.


%prep
%setup -q

%build
export PATH=%{_qt5_bindir}:$PATH
%{cmake} -DLIBEXEC_INSTALL_DIR:PATH=%{_libexecdir} 
%{make_build}

%install
%{make_install}
%find_lang %name

%files
%doc debian/changelog
%license  debian/copyright 


%files common 

%{_sysconfdir}/xdg/ukui-kwinrc 
%{_libdir}/qt5/plugins/kcm_ukuikwinoptions.so
%{_libdir}/qt5/plugins/kcm_ukuikwinrules.so
%{_libdir}/qt5/plugins/kcm_ukuikwintouchscreen.so
%{_libdir}/qt5/plugins/kcm_ukuikwinscreenedges.so
%{_libdir}/qt5/plugins/kcm_ukuikwin_scripts.so
%{_libdir}/qt5/plugins/kcm_ukuikwintabbox.so
%{_libdir}/qt5/plugins/kcms/kcm_ukuikwin_effects.so
%{_libdir}/qt5/plugins/kcms/kcm_ukuikwindecoration.so
%{_libdir}/qt5/plugins/kf5/org.ukui.kwindowsystem.platforms/KF5WindowSystemKWinPrivatePlugin.so
%{_libdir}/qt5/plugins/kpackage/packagestructure/
%{_libdir}/qt5/plugins/ukuikwincompositing.so
%{_libdir}/qt5/plugins/ukui-kwin/effects/
%{_libdir}/qt5/plugins/org.kde.kdecoration2/ukui_kwin5_aurorae.so
%{_libdir}/qt5/plugins/org.ukui.kglobalaccel5.platforms/KF5GlobalAccelPrivateKWin.so
%{_libdir}/qt5/plugins/org.ukui.kwin.scenes/
%{_libdir}/qt5/qml/org/ukui/kwin/
%{_libdir}/libkdeinit5_ukui_kwin_rules_dialog.so
%{_libdir}/kconf_update_bin/ukui_kwin5_update_default_rules
%{_libexecdir}/ukui_kwin_rules_dialog
%{_libexecdir}/ukui_kwin_killer_helper
%{_datadir}/knsrcfiles/ukui-aurorae.knsrc
%{_datadir}/knsrcfiles/ukui-kwineffect.knsrc
%{_datadir}/knsrcfiles/ukui-kwinscripts.knsrc
%{_datadir}/knsrcfiles/ukui-kwinswitcher.knsrc
%{_datadir}/knsrcfiles/ukui-window-decorations.knsrc
%{_datadir}/qlogging-categories5/org_ukui_kwin.categories
%{_datadir}/applications/ukui-kwin.desktop 
%{_datadir}/aurorae/themes/Ukui-classic/
%{_datadir}/aurorae/themes/Ukui-classic-dark/
%{_datadir}/config.kcfg/*
%{_datadir}/icons/*/*/apps/ukui-kwin.*
%{_datadir}/kconf_update/*
%{_datadir}/knotifications5/ukui-kwin.notifyrc
%{_datadir}/kpackage/kcms/kcm_ukuikwin_effects/
%{_datadir}/kpackage/kcms/kcm_ukuikwin_virtualdesktops/
%{_datadir}/kpackage/kcms/kcm_ukuikwindecoration/
%{_datadir}/kservices5/*
%{_datadir}/kservicetypes5/*
%{_datadir}/ukui-kwin
%{_datadir}/locale/*/LC_MESSAGES/*



%files libs
%{_libdir}/libkcmukuikwincommon.so.1.0.0
%{_libdir}/libkcmukuikwincommon.so.1
%{_libdir}/libukui-kwin.so.1
%{_libdir}/libukui-kwin.so.1.0.0
%{_libdir}/qt5/plugins/kcms/kcm_ukuikwin_virtualdesktops.so
%{_libdir}/qt5/plugins/org.kde.kdecoration2/libkwin-style-ukui.so
%{_libdir}/libukui-kwin4_effect_builtins.so.1
%{_libdir}/libukui-kwin4_effect_builtins.so.1.0.0
%{_libdir}/libukui-kwineffects.so.1.0.0
%{_libdir}/libukui-kwineffects.so.12
%{_libdir}/libukui-kwinglutils.so.1.0.0
%{_libdir}/libukui-kwinglutils.so.12
%{_libdir}/libukui-kwinxrenderutils.so.1.0.0
%{_libdir}/libukui-kwinxrenderutils.so.12



%files devel
%{_includedir}/ukui-kwin/
%{_includedir}/ukui-kwin_export.h
%{_libdir}/cmake/ukui-kwin/KWinDBusInterface/KWinDBusInterfaceConfig.cmake 
%{_datadir}/dbus-1/interfaces/*
%{_libdir}/libukui-kwinglutils.so
%{_libdir}/libukui-kwineffects.so
%{_libdir}/libukui-kwinxrenderutils.so
%{_libdir}/libukui-kwin4_effect_builtins.so

%files wayland
%{_bindir}/ukui-kwin_wayland
%{_libdir}/qt5/plugins/kf5/org.ukui.kidletime.platforms/KF5IdleTimeKWinWaylandPrivatePlugin.so
%{_libdir}/qt5/plugins/platforms/UKUIKWinQpaPlugin.so
%{_libdir}/qt5/plugins/org.ukui.kwin.waylandbackends/KWinWaylandDrmBackend.so
%{_libdir}/qt5/plugins/org.ukui.kwin.waylandbackends/KWinWaylandFbdevBackend.so
%{_libdir}/qt5/plugins/org.ukui.kwin.waylandbackends/KWinWaylandVirtualBackend.so
%{_libdir}/qt5/plugins/org.ukui.kwin.waylandbackends/KWinWaylandWaylandBackend.so
%{_libdir}/qt5/plugins/org.ukui.kwin.waylandbackends/KWinWaylandX11Backend.so

%files x11 
%{_bindir}/ukui-kwin_x11
%{_libdir}/libkdeinit5_ukui-kwin_x11.so
%{_libdir}/qt5/plugins/org.ukui.kwin.platforms/KWinX11Platform.so








%post x11 
#! /bin/sh

update-alternatives --install /usr/bin/x-window-manager x-window-manager /usr/bin/ukui-kwin_x11 50



%post wayland
#!/bin/sh

setcap "CAP_SYS_RESOURCE=+ep"   /usr/bin/ukui-kwin_wayland



%preun x11 
#! /bin/sh
update-alternatives --remove x-window-manager /usr/bin/ukui-kwin_x11

