# enable download source
%undefine _disable_source_fetch
%define debug_package %{nil}

Name:           ukui-desktop-environment
Version:        2.0.2
Release:        1%{?dist}
Summary:        UKUI Desktop Environment 




License:        GPLv2+
URL:            https://github.com/ukui/ukui-desktop-environment/
Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

Recommends: atril
Recommends: desktop-base
Recommends: engrampa
Recommends: eom
Recommends: ffmpegthumbnailer
Recommends: mate-calc
Recommends: ukui-media
Recommends: mate-notification-daemon
Recommends: ukui-power-manager
Recommends: ukui-screensaver
Recommends: gnome-screenshot
Recommends: pluma
Recommends: qt5-ukui-platformtheme

Requires: ukui-desktop-environment-core

Provides: ukui


%description
UKUI Desktop Environment (metapackage)
The UKUI Desktop Environment is the continuation of MATE. It provides an
intuitive and attractive desktop environment using traditional metaphors for
Linux and other Unix-like operating systems.

UKUI is under active development to add support for new technologies while
preserving a traditional desktop experience.
This package depends on a very basic set of programs that are necessary to
start a UKUI desktop environment session. The set of programs includes the
UKUI file manager (Peony), the UKUI control center and a limited set of
other obligatory UKUI desktop components.



%package core
Summary:  UKUI Desktop Environment (essential components, metapackage)

Requires:  peony
Requires:  ukui-menu
Requires:  ukui-sidebar
Requires:  ukui-control-center
Requires:  ukui-session-manager
Requires:  gvfs-smb
Requires:  gvfs-afc
Requires:  gvfs-afp
Requires:  gvfs-goa

Requires:  gvfs-mtp
Requires:  gvfs-nfs
Requires:  gvfs-fuse
Requires:  gvfs-gphoto2
Requires:  gvfs-archive
Requires:  gvfs
Requires:  ukwm
Requires:  ukui-panel
Requires:  mate-desktop
Requires:  mate-notification-daemon
Requires:  mate-polkit
Requires:  ukui-settings-daemon
Requires:  mate-terminal
Requires:  ukui-themes

%description core
UKUI Desktop Environment (essential components, metapackage)

 The UKUI Desktop Environment is the continuation of MATE. It provides an
 intuitive and attractive desktop environment using traditional metaphors for
 Linux and other Unix-like operating systems.
 .
 UKUI is under active development to add support for new technologies while
 preserving a traditional desktop experience.
 .
 This package depends on a very basic set of programs that are necessary to
 start a UKUI desktop environment session. The set of programs includes the
 UKUI file manager (Peony), the UKUI control center and a limited set of
 other obligatory UKUI desktop components.


%package extras
Summary: UKUI Desktop Environment (extra components, metapackage)

Recommends: blueman
Recommends: dconf-editor
Recommends: gnome-keyring
Recommends: yelp

Requires: ukui-desktop-environment 

Provides: ukui-extras

%description extras
UKUI Desktop Environment (extra components, metapackage)
 The UKUI Desktop Environment is the continuation of MATE. It provides an
 intuitive and attractive desktop environment using traditional metaphors for
 Linux and other Unix-like operating systems.
 .
 UKUI is under active development to add support for new technologies while
 preserving a traditional desktop experience.
 .
 This package installs an extra set of UKUI components that are
 also part of the official UKUI release.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/share/doc/ukui-desktop-environment/ %{buildroot}/usr/share/glib-2.0/schemas/
cp debian/copyright  %{buildroot}/usr/share/doc/ukui-desktop-environment/
gzip  debian/changelog > %{buildroot}/usr/share/doc/ukui-desktop-environment/changelog.gz
cp debian/ukui-ubuntu.gschema.override %{buildroot}/usr/share/glib-2.0/schemas/ukui.gschema.override

%files 
%{_datadir}/doc/ukui-desktop-environment/changelog.gz
%{_datadir}/doc/ukui-desktop-environment/copyright

%files core
%{_datadir}/glib-2.0/schemas/ukui.gschema.override

%files extras
