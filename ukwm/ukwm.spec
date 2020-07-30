# enable download source
%undefine _disable_source_fetch

Name:           ukwm
Version:        master
Release:        1%{?dist}
Summary:        file Manager for the UKUI desktop

License:        GPLv2+
URL:            https://github.com/ukui/ukwm
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64



Provides: x-window-manager



BuildRequires: gtk3-devel
BuildRequires: glib2-devel
BuildRequires: libcanberra-gtk3
BuildRequires: libcanberra-devel
BuildRequires: gobject-introspection-devel
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: json-glib-devel
BuildRequires: mesa-libgbm-devel
BuildRequires: pango-devel
BuildRequires: cairo-devel 
BuildRequires: mesa-libGL-devel
BuildRequires: libdrm-devel 
BuildRequires: mesa-libEGL-devel
BuildRequires: gnome-desktop3-devel
BuildRequires: libgudev-devel
BuildRequires: libinput-devel
BuildRequires: startup-notification-devel
BuildRequires: systemd-devel
BuildRequires: upower-devel
BuildRequires: libwacom-devel
BuildRequires: libxcb-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXi-devel
BuildRequires: libxkbfile-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: libxkbcommon-devel
BuildRequires: libX11-xcb
BuildRequires: libXfixes-devel
BuildRequires: libXdamage-devel
BuildRequires: libXcursor-devel
BuildRequires: libXt-devel
BuildRequires: libX11-devel
BuildRequires: libXinerama-devel
BuildRequires: libXext-devel
BuildRequires: libXrandr-devel
BuildRequires: libSM-devel
BuildRequires: libICE-devel
BuildRequires: pam-devel
BuildRequires: wayland-devel
BuildRequires: wayland-protocols-devel
BuildRequires: libglvnd-devel
BuildRequires: libglvnd-core-devel

Recommends: ukui-window-switch
Suggests: ukui-control-center
Suggests: xdg-user-dirs

Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Requires: ukui-settings-daemon
Requires: gsettings-desktop-schemas
Requires: zenity

%description 
 Ukwm is a small window manager, using GTK+ and Clutter to do
 everything.
 .
 Ukwm is the clutter-based evolution of Metacity, which, as the
 author says, is a "Boring window manager for the adult in you. Many
 window managers are like Marshmallow Froot Loops; Metacity is like
 Cheerios."
 .
 This package contains the core binaries.



%package libs
Summary: window manager library from the Ukwm window manager
Requires: gsettings-desktop-schemas
Requires: %{name}-common%{?_isa} = %{version}-%{release}

%description libs
 Ukwm is a small window manager, using GTK+ and Clutter to do
 everything.
 .
 Ukwm is the clutter-based evolution of Metacity, which, as the
 author says, is a "Boring window manager for the adult in you. Many
 window managers are like Marshmallow Froot Loops; Metacity is like
 Cheerios."
 .
 This package contains the window manager shared library, used by ukwm
 itself, and gnome-shell.



%package common

Summary: shared files for the Ukwm window manager

%description common
 Ukwm is a small window manager, using GTK+ and Clutter to do
 everything.
 .
 Ukwm is the clutter-based evolution of Metacity, which, as the
 author says, is a "Boring window manager for the adult in you. Many
 window managers are like Marshmallow Froot Loops; Metacity is like
 Cheerios."
 .
 This package contains the shared files.


%package devel


Summary: Development files for the Ukwm window manager

Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-libs%{?_isa} = %{version}-%{release}
Requires: %{name}-common%{?_isa} = %{version}-%{release}
Requires: gtk3-devel
Requires: cairo-devel 
Requires: glib2-devel
Requires: atk-devel
Requires: pango-devel
Requires: json-glib-devel
Requires: mesa-libEGL-devel
Requires: wayland-devel
Requires: libdrm-devel 
Requires: mesa-libgbm-devel
Requires: libinput-devel
Requires: libgudev-devel
Requires: libXext-devel
Requires: libXdamage-devel
Requires: libXcomposite-devel
Requires: libXi-devel
Requires: gdk-pixbuf2-devel
Requires: libXfixes-devel
Requires: libXrandr-devel

%description devel
 Ukwm is a small window manager, using GTK+ and Clutter to do
 everything.
 .
 Ukwm is the clutter-based evolution of Metacity, which, as the
 author says, is a "Boring window manager for the adult in you. Many
 window managers are like Marshmallow Froot Loops; Metacity is like
 Cheerios."
 .
 This package contains the development files.

%package gobject

Summary: GObject introspection data for Ukwm

%description gobject

 Ukwm is a small window manager, using GTK+ and Clutter to do
 everything.
 .
 Ukwm is the clutter-based evolution of Metacity, which, as the
 author says, is a "Boring window manager for the adult in you. Many
 window managers are like Marshmallow Froot Loops; Metacity is like
 Cheerios."
 .
 This package contains the GObject introspection data which may be
 used to generate dynamic bindings.



%prep

%setup -q
./autogen.sh --prefix=/usr --sysconfdir=/etc --libdir=/usr/lib64 -enable-introspection --enable-compile-warnings=yes 	--enable-egl-device 	--enable-wayland 	--enable-native-backend

%define gettext_version %(dnf info gettext |grep Version |awk '{print $3}'| awk -F "." 'BEGIN {OFS = FS} {print $1,$2}')
sed -i "/GETTEXT_MACRO_VERSION/s/0.19/%{gettext_version}/g" po/Makefile.in.in


%build
%{make_build}

%install
%{make_install}

%files
%{_bindir}/ukwm
%{_datadir}/applications/ukwm.desktop
%{_libexecdir}/ukwm-restart-helper
%{_libdir}/ukwm/plugins/default.so
%{_datadir}/ukui/plugin/org.ukui.ukwm.UkwmPlugin.xml

%files libs 
%{_libdir}/libukwm-1.la
%{_libdir}/libukwm-1.so
%{_libdir}/libukwm-1.so.0
%{_libdir}/libukwm-1.so.0.0.0
%{_libdir}/ukwm/libukwm-clutter-1.la
%{_libdir}/ukwm/libukwm-clutter-1.so
%{_libdir}/ukwm/libukwm-cogl-1.la
%{_libdir}/ukwm/libukwm-cogl-1.so
%{_libdir}/ukwm/libukwm-cogl-pango-1.la
%{_libdir}/ukwm/libukwm-cogl-pango-1.so
%{_libdir}/ukwm/libukwm-cogl-path-1.la
%{_libdir}/ukwm/libukwm-cogl-path-1.so


%files common
%doc debian/copyright debian/changelog
%{_datadir}/locale/*/LC_MESSAGES/ukwm.mo
%{_datadir}/man/man1/ukwm.1.gz
%{_datadir}/gnome-control-center/keybindings/50-ukwm-navigation.xml
%{_datadir}/gnome-control-center/keybindings/50-ukwm-system.xml
%{_datadir}/gnome-control-center/keybindings/50-ukwm-windows.xml
%{_datadir}/GConf/gsettings/ukwm-schemas.convert
%{_datadir}/glib-2.0/schemas/org.ukui.ukwm.gschema.xml
%{_datadir}/glib-2.0/schemas/org.ukui.ukwm.wayland.gschema.xml

%files devel
%{_includedir}/ukwm
%{_libdir}/pkgconfig/libukwm-1.pc
%{_libdir}/pkgconfig/ukwm-clutter-1.pc
%{_libdir}/pkgconfig/ukwm-clutter-x11-1.pc
%{_libdir}/pkgconfig/ukwm-cogl-1.pc
%{_libdir}/pkgconfig/ukwm-cogl-pango-1.pc
%{_libdir}/pkgconfig/ukwm-cogl-path-1.pc
%{_libdir}/ukwm/Meta-1.gir
%{_libdir}/ukwm/Cogl-1.gir
%{_libdir}/ukwm/Cally-1.gir
%{_libdir}/ukwm/Clutter-1.gir

%files gobject
%{_libdir}/ukwm/Cally-1.typelib
%{_libdir}/ukwm/Clutter-1.typelib
%{_libdir}/ukwm/ClutterX11-1.gir
%{_libdir}/ukwm/ClutterX11-1.typelib
%{_libdir}/ukwm/Cogl-1.typelib
%{_libdir}/ukwm/CoglPango-1.gir
%{_libdir}/ukwm/CoglPango-1.typelib
%{_libdir}/ukwm/Meta-1.typelib


%post 
set -e
action="$1"

if [ "$action" = configure ]; then
    # register the alternatives of x-window-manager manually
    # because dh_installwm doesn't register manpage as slave yet.
    update-alternatives --install /usr/bin/x-window-manager \
        x-window-manager /usr/bin/ukwm 60 \
        --slave /usr/share/man/man1/x-window-manager.1.gz \
        x-window-manager.1.gz /usr/share/man/man1/ukwm.1.gz
fi

%preun
set -e

action="$1"

if [ "$action" = remove ]; then
    update-alternatives --remove x-window-manager \
        /usr/bin/ukwm
fi

