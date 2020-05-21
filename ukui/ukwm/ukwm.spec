# enable download source
%undefine _disable_source_fetch

Name:           ukwm
Version:        1.2.0
Release:        1%{?dist}
Summary:        file Manager for the UKUI desktop

License:        GPLv2+
URL:            https://github.com/ukui/ukui-session-manager
Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

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
./autogen.sh	
%build
  %{make_build}

%install
rm -rf %{buildroot}
%{make_install}  INSTALL_ROOT=%{buildroot} 
mkdir -p %{buildroot}/usr/share/doc/ukwm/
cp debian/copyright  %{buildroot}/usr/share/doc/ukwm/
gzip  debian/changelog > %{buildroot}/usr/share/doc/ukwm/changelog.gz

%files
%{_bindir}/

%files libs 
%{_libdir}/

%files common
%{_datadir}/doc


%files devel
%{_includedir}/ukwm

%files gobject
