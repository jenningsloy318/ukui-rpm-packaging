# enable download source
%undefine _disable_source_fetch

Name:           ukui-kwin
Version:        master
Release:        1%{?dist}
Summary:        UKUI window manager



License:        GPLv2+
URL:            https://github.com/ukui/ukui-session-manager
Source0:        https://github.com/ukui/ukui-kwin/archive/master.zip#/%{name}-%{version}.zip

BuildArch:      x86_64

# Base

BuildRequires: extra-cmake-modules
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
# Wayland 
BuildRequires: mesa-libEGL-devel
BuildRequires: wayland-devel
BuildRequires: libwayland-client-devel
BuildRequires: libwayland-server-devel
BuildRequires: libwayland-cursor-devel


BuildRequires: kdecoration-devel
BuildRequires: kscreenlocker-devel
BuildRequires: libcap-devel

%description
 This package is a transitional dummy to depend on the renamed ukui-kwin-x11 and
 can be removed.


%package common
Summary: UKUI window manager, common files

Requires: ukui-kwin-data
Requires: kf5-kglobalaccel
Requires: kf5-kirigami2
Requires: kf5-kdeclarative

%description common
  Ukui-kwin  is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paints
 the window decoration, the bar on top of every window with
 (configurable) buttons like close, maximize and minimize.
 It also handles placing of windows and switching between them.
 .
 This package is part of the UKUI project.

%package data
Summary: UKUI window manager data files
Requires:  plasma-framework


%description data
 Ukui-kwin  is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paints
 the window decoration, the bar on top of every window with
 (configurable) buttons like close, maximize and minimize.
 It also handles placing of windows and switching between them.
 .
 This package contains the data files


%package devel
Summary: UKUI window manager - devel files
Requires: ukui-kwin-common 

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
Requires: ukui-kwin-common
Requires: libcap
Requires: xwayland

Provides: ukui-kwin

%description wayland
 Ukui-kwin  is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paintsqt5-qtbase-guiprogress
 project, and is available as a PREVIEW release. Don't expect the same
 stability as with the x11 version.

%package wayland-backend-drm
Summary: UKUI window manager drm plugin
Provides: ukui-kwin-wayland-backend

%description wayland-backend-drm
 Ukui-kwin  is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paints
 the window decoration, the bar on top of every window with
 (configurable) buttons like close, maximize and minimize.
 It also handles placing of windows and switching between them.
 .
 This package is part of the UKUI project


%package wayland-backend-fbdev
Summary: UKUI window manager fbdev plugin
Provides: ukui-kwin-wayland-backend

%description wayland-backend-fbdev
 Ukui-kwin  is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paints
 the window decoration, the bar on top of every window with
 (configurable) buttons like close, maximize and minimize.
 It also handles placing of windows and switching between them.
 .
 This package is part of the UKUI project

%package wayland-backend-virtual
Summary: UKUI window manager virtual plugin
Provides: ukui-kwin-wayland-backend

%description wayland-backend-virtual
 Ukui-kwin  is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paints
 the window decoration, the bar on top of every window with
 (configurable) buttons like close, maximize and minimize.
 It also handles placing of windows and switching between them.
 .
 This backend allows running ukui-kwin-wayland in headless mode,
 useful for testing, or in the Cloud.

%package wayland-backend-wayland

Summary: UKUI window manager drm plugin

Provides: ukui-kwin-wayland-backend
%description wayland-backend-wayland
 Ukui-kwin  is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paints
 the window decoration, the bar on top of every window with
 (configurable) buttons like close, maximize and minimize.
 It also handles placing of windows and switching between them.
 .
 This package is part of the UKUI project

%package wayland-backend-x11
Summary:  UKUI window manager drm plugin
Provides: ukui-kwin-wayland-backend

%description wayland-backend-x11
 Ukui-kwin  is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paints
 the window decoration, the bar on top of every window with
 (configurable) buttons like close, maximize and minimize.
 It also handles placing of windows and switching between them.
 .
 This package is part of the UKUI project


%package x11
Summary: UKUI window manager drm plugin
Provides: ukui-kwin, x-window-manager

%description x11
 Ukui-kwin  is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paints
 the window decoration, the bar on top of every window with
 (configurable) buttons like close, maximize and minimize.
 It also handles placing of windows and switching between them.
 .
 This package is part of the UKUI project.

%package effect-builtins-libs
Summary: UKUI window manager drm plugin
Requires: ukui-kwin-kwineffects-libs
%description effect-builtins-libs
 Ukui-kwin  is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paints
 the window decoration, the bar on top of every window with
 (configurable) buttons like close, maximize and minimize.
 It also handles placing of windows and switching between them.
 .
 This package is part of the UKUI project.


%package effects-libs
Summary:  UKUI window manager effects library
%description effects-libs
 Ukui-kwin is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paints
 the window decoration, the bar on top of every window with
 (configurable) buttons like close, maximize and minimize.
 It also handles placing of windows and switching between them.
 .
 This package is part of the UKUI project.



%package glutils-libs
Summary:  UKUI window manager effects library

%description  glutils-libs
 Ukui-kwin is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paints
 the window decoration, the bar on top of every window with
 (configurable) buttons like close, maximize and minimize.
 It also handles placing of windows and switching between them.
 .
 This package is part of the UKUI project.

%package xrenderutils-libs

Summary: UKUI window manager effects library
%description xrenderutils-libs
 Ukui-kwin is the window manager for the UKUI3.0 Desktop. It
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
%{cmake3} .
%{make_build}
#make 
%install
rm -rf %{buildroot} 
%{make_install}  INSTALL_ROOT=%{buildroot} 
mkdir -p %{buildroot}/usr/share/doc/ukui-kwin/  
cp debian/copyright  %{buildroot}/usr/share/doc/ukui-kwin/copyright
gzip  debian/changelog > %{buildroot}/usr/share/doc/ukui-kwin/changelog.gz

%files
%{_sysconfdir}/xdg/ukui-kwinrc
%{_bindir}
%{_libexecdir}/ukui_kwin_rules_dialog
%{_libdir}/libexec/ukui_kwin_killer_helper

%files common 
%{_datadir}/ukui-kwin
%{_datadir}/qlogging-categories5
%{_datadir}/locale/bo/LC_MESSAGES/kcm-ukui-kwin-scripts.mo
%{_datadir}/locale/bo/LC_MESSAGES/kcm_ukui-kwin_effects.mo
%{_datadir}/locale/bo/LC_MESSAGES/kcm_ukui-kwin_virtualdesktops.mo
%{_datadir}/locale/bo/LC_MESSAGES/kcm_ukuikwindecoration.mo
%{_datadir}/locale/bo/LC_MESSAGES/kcm_ukuikwintabbox.mo
%{_datadir}/locale/bo/LC_MESSAGES/kcmukuikwincommon.mo
%{_datadir}/locale/bo/LC_MESSAGES/kcmukuikwincompositing.mo
%{_datadir}/locale/bo/LC_MESSAGES/kcmukuikwinrules.mo
%{_datadir}/locale/bo/LC_MESSAGES/kcmukuikwinscreenedges.mo
%{_datadir}/locale/bo/LC_MESSAGES/kcmukwm.mo
%{_datadir}/locale/bo/LC_MESSAGES/ukui-kwin.mo
%{_datadir}/locale/bo/LC_MESSAGES/ukui-kwin_clients.mo
%{_datadir}/locale/bo/LC_MESSAGES/ukui-kwin_effects.mo
%{_datadir}/locale/bo/LC_MESSAGES/ukui-kwin_scripting.mo
%{_datadir}/locale/bo/LC_MESSAGES/ukui-kwin_scripts.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/kcm-ukui-kwin-scripts.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/kcm_ukui-kwin_effects.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/kcm_ukui-kwin_virtualdesktops.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/kcm_ukuikwindecoration.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/kcm_ukuikwintabbox.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/kcmukuikwincommon.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/kcmukuikwincompositing.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/kcmukuikwinrules.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/kcmukuikwinscreenedges.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/kcmukwm.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/ukui-kwin.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/ukui-kwin_clients.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/ukui-kwin_effects.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/ukui-kwin_scripting.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/ukui-kwin_scripts.mo
%{_datadir}/kservicetypes5
%{_datadir}/kservices5
%{_datadir}/kpackage
%{_datadir}/knsrcfiles
%{_datadir}/kconf_update
%{_datadir}/icons/hicolor/16x16/apps/ukui-kwin.png
%{_datadir}/icons/hicolor/32x32/apps/ukui-kwin.png
%{_datadir}/icons/hicolor/48x48/apps/ukui-kwin.png
%{_datadir}/doc/ukui-kwin/
%{_datadir}dbus-1/interfaces/org.ukui.KWin.VirtualDesktopManager.xml
%{_datadir}dbus-1/interfaces/org.ukui.KWin.xml
%{_datadir}dbus-1/interfaces/org.ukui.kwin.ColorCorrect.xml
%{_datadir}dbus-1/interfaces/org.ukui.kwin.Compositing.xml
%{_datadir}dbus-1/interfaces/org.ukui.kwin.Effects.xml
%{_datadir}/config.kcfg/ukui-kwin.kcfg
%{_datadir}/config.kcfg/ukui-kwin_colorcorrect.kcfg
%{_datadir}/config.kcfg/ukuikwindecorationsettings.kcfg
%{_datadir}/config.kcfg/ukuivirtualdesktopssettings.kcfg
%{_datadir}/aurorae/themes/Ukui-classic/
%{_datadir}/aurorae/themes/Ukui-classic-dark/
%{_datadir}/applications/ukui-kwin.desktop


%files devel
%{_includedir}/ukui-kwin/