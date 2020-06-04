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


Requires: ukui-kwin-x11

%description
 This package is a transitional dummy to depend on the renamed ukui-kwin-x11 and
 can be removed.


%package common
Summary: UKUI window manager, common files

Requires: ukui-kwin-data
Requires: kf5-kglobalaccel
Requires: kf5-kirigami2
Requires: kf5-kdeclarative
Requires: qt5-qtmultimedia

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
Requires: qt5-qtmultimedia

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
Requires: ukui-kwin-wayland-backend-drm,ukui-kwin-wayland-backend-fbdev,ukui-kwin-wayland-backend-x11,ukui-kwin-wayland-backend-virtual,ukui-kwin-wayland-backend-wayland

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

Requires: ukui-kwin-common
Requires: ukui-kwin-kwinglutils
Requires: ukui-kwin-kwinxrenderutils
%description x11
 Ukui-kwin  is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paints
 the window decoration, the bar on top of every window with
 (configurable) buttons like close, maximize and minimize.
 It also handles placing of windows and switching between them.
 .
 This package is part of the UKUI project.

%package kwin4-effect-builtins
Summary: UKUI window manager drm plugin
Requires: ukui-kwin-kwineffects

%description kwin4-effect-builtins
 Ukui-kwin  is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paints
 the window decoration, the bar on top of every window with
 (configurable) buttons like close, maximize and minimize.
 It also handles placing of windows and switching between them.
 .
 This package is part of the UKUI project.


%package kwineffects
Summary:  UKUI window manager effects library
%description kwineffects
 Ukui-kwin is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paints
 the window decoration, the bar on top of every window with
 (configurable) buttons like close, maximize and minimize.
 It also handles placing of windows and switching between them.
 .
 This package is part of the UKUI project.



%package kwinglutils
Summary:  UKUI window manager effects library

%description  kwinglutils
 Ukui-kwin is the window manager for the UKUI3.0 Desktop. It
 gives you complete control over your windows, making sure
 they're not in the way but aid you in your task. It paints
 the window decoration, the bar on top of every window with
 (configurable) buttons like close, maximize and minimize.
 It also handles placing of windows and switching between them.
 .
 This package is part of the UKUI project.

%package kwinxrenderutils

Summary: UKUI window manager effects library
%description kwinxrenderutils
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
mkdir cmake-build
pushd cmake-build
%cmake3 ..
%{make_build}
popd

%install
pushd cmake-build
%{make_install}  INSTALL_ROOT=%{buildroot} 
mkdir -p %{buildroot}/usr/share/doc/ukui-kwin/  
popd
cp debian/copyright  %{buildroot}/usr/share/doc/ukui-kwin/copyright
gzip -c  debian/changelog > %{buildroot}/usr/share/doc/ukui-kwin/changelog.gz

%files
%{_datadir}/doc/ukui-kwin/


%files common 

%{_libdir}/qt5/plugins/kcm_ukuikwinoptions.so
%{_libdir}/qt5/plugins/kcm_ukuikwinrules.so
%{_libdir}/qt5/plugins/kcm_ukuikwintouchscreen.so
%{_libdir}/qt5/plugins/kcm_ukuikwinscreenedges.so
%{_libdir}/qt5/plugins/kcm_ukuikwin_scripts.so
%{_libdir}/qt5/plugins/kcm_ukuikwintabbox.so
%{_libdir}/qt5/plugins/kcms/kcm_ukuikwin_effects.so
%{_libdir}/qt5/plugins/kcms/kcm_ukuikwin_virtualdesktops.so
%{_libdir}/qt5/plugins/kcms/kcm_ukuikwindecoration.so
%{_libdir}/qt5/plugins/kf5/org.ukui.kwindowsystem.platforms/KF5WindowSystemKWinPrivatePlugin.so
%{_libdir}/qt5/plugins/kpackage/packagestructure/
%{_libdir}/qt5/plugins/ukuikwincompositing.so
%{_libdir}/qt5/plugins/ukui-kwin/effects/
%{_libdir}/qt5/plugins/org.kde.kdecoration2/ukui_kwin5_aurorae.so
%{_libdir}/qt5/plugins/org.kde.kdecoration2/libkwin-style-ukui.so
%{_libdir}/qt5/plugins/org.ukui.kglobalaccel5.platforms/KF5GlobalAccelPrivateKWin.so
%{_libdir}/qt5/plugins/org.ukui.kwin.scenes/
%{_libdir}/qt5/qml/org/ukui/kwin/
%{_libdir}/libukui-kwin.so.1
%{_libdir}/libukui-kwin.so.1.0.0
%{_libdir}/libkdeinit5_ukui_kwin_rules_dialog.so
%{_libdir}/libkcmukuikwincommon.so.1.0.0
%{_libdir}/libkcmukuikwincommon.so.1
%{_libdir}/libexec/ukui_kwin_rules_dialog
%{_libdir}/libexec/ukui_kwin_killer_helper
%{_libdir}/kconf_update_bin/ukui_kwin5_update_default_rules
%{_datadir}/doc/ukui-kwin/
%{_datadir}/knsrcfiles/ukui-aurorae.knsrc
%{_datadir}/knsrcfiles/ukui-kwineffect.knsrc
%{_datadir}/knsrcfiles/ukui-kwinscripts.knsrc
%{_datadir}/knsrcfiles/ukui-kwinswitcher.knsrc
%{_datadir}/knsrcfiles/ukui-window-decorations.knsrc
%{_datadir}/qlogging-categories5/org_ukui_kwin.categories

%files data 
%{_sysconfdir}/xdg/ukui-kwinrc 
%{_datadir}/applications/ukui-kwin.desktop 
%{_datadir}/aurorae/themes/Ukui-classic/
%{_datadir}/aurorae/themes/Ukui-classic-dark/
%{_datadir}/config.kcfg/ukui-kwin.kcfg
%{_datadir}/config.kcfg/ukui-kwin_colorcorrect.kcfg
%{_datadir}/config.kcfg/ukuikwindecorationsettings.kcfg
%{_datadir}/config.kcfg/ukuivirtualdesktopssettings.kcfg
%{_datadir}/icons/*/*/apps/ukui-kwin.*
%{_datadir}/kconf_update/ukui-kwin-5.16-auto-bordersize.sh
%{_datadir}/kconf_update/ukui-kwin-5.18-move-animspeed.py
%{_datadir}/kconf_update/ukui-kwin.upd
%{_datadir}/knotifications5/ukui-kwin.notifyrc
%{_datadir}/kpackage/kcms/kcm_ukuikwin_effects/
%{_datadir}/kpackage/kcms/kcm_ukuikwin_virtualdesktops/
%{_datadir}/kpackage/kcms/kcm_ukuikwindecoration/
%{_datadir}/kservices5/ukui-kwin/
%{_datadir}/kservices5/kcm_ukuikwin_effects.desktop
%{_datadir}/kservices5/kcm_ukuikwin_virtualdesktops.desktop
%{_datadir}/kservices5/ukuikwinactions.desktop
%{_datadir}/kservices5/ukuikwinadvanced.desktop
%{_datadir}/kservices5/ukuikwincompositing.desktop
%{_datadir}/kservices5/ukuikwindecoration.desktop
%{_datadir}/kservices5/ukuikwinfocus.desktop
%{_datadir}/kservices5/ukuikwinmoving.desktop
%{_datadir}/kservices5/ukuikwinoptions.desktop
%{_datadir}/kservices5/ukuikwinrules.desktop
%{_datadir}/kservices5/ukuikwinscreenedges.desktop
%{_datadir}/kservices5/ukuikwinscripts.desktop
%{_datadir}/kservices5/ukuikwintabbox.desktop
%{_datadir}/kservices5/ukuikwintouchscreen.desktop
%{_datadir}/kservicetypes5/ukui-kwin/
%{_datadir}/kservicetypes5/ukuikwindecoration.desktop
%{_datadir}/ukui-kwin
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

%files devel
%{_includedir}/ukui-kwin/
%{_includedir}/ukui-kwin_export.h
%{_libdir}/cmake/ukui-kwin/KWinDBusInterface/KWinDBusInterfaceConfig.cmake 
%{_datadir}/dbus-1/interfaces/org.ukui.KWin.VirtualDesktopManager.xml
%{_datadir}/dbus-1/interfaces/org.ukui.KWin.xml
%{_datadir}/dbus-1/interfaces/org.ukui.kwin.ColorCorrect.xml
%{_datadir}/dbus-1/interfaces/org.ukui.kwin.Compositing.xml
%{_datadir}/dbus-1/interfaces/org.ukui.kwin.Effects.xml

%files wayland
%{_bindir}/ukui-kwin_wayland
%{_libdir}/qt5/plugins/kf5/org.ukui.kidletime.platforms/KF5IdleTimeKWinWaylandPrivatePlugin.so
%{_libdir}/qt5/plugins/platforms/UKUIKWinQpaPlugin.so

%files wayland-backend-drm
%{_libdir}/qt5/plugins/org.ukui.kwin.waylandbackends/KWinWaylandDrmBackend.so

%files wayland-backend-fbdev
%{_libdir}/qt5/plugins/org.ukui.kwin.waylandbackends/KWinWaylandFbdevBackend.so

%files wayland-backend-virtual
%{_libdir}/qt5/plugins/org.ukui.kwin.waylandbackends/KWinWaylandVirtualBackend.so

%files wayland-backend-wayland
%{_libdir}/qt5/plugins/org.ukui.kwin.waylandbackends/KWinWaylandWaylandBackend.so

%files wayland-backend-x11
%{_libdir}/qt5/plugins/org.ukui.kwin.waylandbackends/KWinWaylandX11Backend.so

%files x11 
%{_bindir}/ukui-kwin_x11
%{_libdir}/libkdeinit5_ukui-kwin_x11.so
%{_libdir}/qt5/plugins/org.ukui.kwin.platforms/KWinX11Platform.so


%files kwin4-effect-builtins
%{_libdir}/libukui-kwin4_effect_builtins.so
%{_libdir}/libukui-kwin4_effect_builtins.so.1
%{_libdir}/libukui-kwin4_effect_builtins.so.1.0.0

%files kwineffects
%{_libdir}/libukui-kwineffects.so
%{_libdir}/libukui-kwineffects.so.1.0.0
%{_libdir}/libukui-kwineffects.so.12



%files kwinglutils
%{_libdir}/libukui-kwinglutils.so
%{_libdir}/libukui-kwinglutils.so.1.0.0
%{_libdir}/libukui-kwinglutils.so.12


%files kwinxrenderutils
%{_libdir}/libukui-kwinxrenderutils.so
%{_libdir}/libukui-kwinxrenderutils.so.1.0.0
%{_libdir}/libukui-kwinxrenderutils.so.12

%post x11 
#! /bin/sh
# postinst script for kwin
#
# see: dh_installdeb(1)

set -e

# summary of how this script can be called:
#        * <postinst> `configure' <most-recently-configured-version>
#        * <old-postinst> `abort-upgrade' <new version>
#        * <conflictor's-postinst> `abort-remove' `in-favour' <package>
#          <new-version>
#        * <deconfigured's-postinst> `abort-deconfigure' `in-favour'
#          <failed-install-package> <version> `removing'
#          <conflicting-package> <version>
# for details, see http://www.debian.org/doc/debian-policy/ or
# the debian-policy package
#

case "$1" in
    configure)
        update-alternatives --remove x-window-manager /usr/bin/ukui-kwin
	update-alternatives --install /usr/bin/x-window-manager x-window-manager /usr/bin/ukui-kwin_x11 50
    ;;

    abort-upgrade|abort-remove|abort-deconfigure)

    ;;

    *)
        echo "postinst called with unknown argument \`$1'" >&2
        exit 1
    ;;
esac

# dh_installdeb will replace this with shell code automatically
# generated by other debhelper scripts.

#DEBHELPER#

exit 0


%post wayland
#!/bin/sh

set -e

if [ "$1" = configure ]; then
    # Set the capabilities
    if command -v setcap > /dev/null && \
       setcap "CAP_SYS_RESOURCE=+ep" \
            /usr/bin/kwin_wayland; then
        echo "Sucessfully set capabilities for ukui-kwin_wayland"
    else
        echo "Failed to set capabilities for ukui-kwin_wayland" >&2
    fi
fi

#DEBHELPER#

exit 0


%preun x11 
#! /bin/sh
# prerm script for kwin
#
# see: dh_installdeb(1)

set -e

# summary of how this script can be called:
#        * <prerm> `remove'
#        * <old-prerm> `upgrade' <new-version>
#        * <new-prerm> `failed-upgrade' <old-version>
#        * <conflictor's-prerm> `remove' `in-favour' <package> <new-version>
#        * <deconfigured's-prerm> `deconfigure' `in-favour'
#          <package-being-installed> <version> `removing'
#          <conflicting-package> <version>
# for details, see http://www.debian.org/doc/debian-policy/ or
# the debian-policy package


case "$1" in
    remove)
        update-alternatives --remove x-window-manager /usr/bin/ukui-kwin_x11
    ;;

    upgrade|deconfigure)
    ;;

    failed-upgrade)
    ;;

    *)
        echo "prerm called with unknown argument \`$1'" >&2
        exit 1
    ;;
esac

# dh_installdeb will replace this with shell code automatically
# generated by other debhelper scripts.

#DEBHELPER#

exit 0
