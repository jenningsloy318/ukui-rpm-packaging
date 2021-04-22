Name:           ukui-media
Version:        3.0.1
Release:        1%{?dist}
Summary:        UKUI media utilities


License:        GPL-2.0 License
URL:            https://github.com/ukui/ukui-media
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64

BuildRequires:  intltool
BuildRequires:  qt5-qtbase-devel
BuildRequires:  libcanberra-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  mate-desktop-devel
BuildRequires:  libmatemixer-devel
BuildRequires:  libxml2-devel
BuildRequires:  mate-common
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  bamf-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXtst-devel
BuildRequires:  libX11-devel

Requires:  mate-common
Requires:  %{name}-common%{?_isa} = %{version}-%{release}
Requires:  glib2
Requires:  pulseaudio

Recommends: sound-theme-freedesktop
Recommends: alsa-utils

%description
 This package utilizes the libmatemixer library which provides
 support for ALSA and Pulseaudio as audio backends.

 This package utilizes the libmatemixer library which provides
 support for ALSA and Pulseaudio as audio backends.

%package common
Summary: UKUI media utilities (common files)


%description common
 UKUI media utilities are the audio mixer and the volume
 control applet.
 .
 This package contains the common files.


%prep
%setup -q

%build
export PATH=%{_qt5_bindir}:$PATH
sed -i 's/lrelease/qmake-qt5/g' ukui-volume-control-applet-qt/ukui-volume-control-applet-qt.pro
./autogen.sh
%configure
%{make_build}
mkdir ukui-volume-control-applet-qt/cmake_build
pushd ukui-volume-control-applet-qt/cmake_build
%{qmake_qt5} PREFIX=/usr/share/ukui-media ..
%{make_build}
popd

%install
%{make_install}  INSTALL_ROOT=%{buildroot}
install -d  %{buildroot}/usr/share/man/man1/
gzip -c man/ukui-volume-control-applet-qt.1  > %{buildroot}/usr/share/man/man1/ukui-volume-control-applet-qt.1.gz
gzip -c man/ukui-volume-control-applet.1  > %{buildroot}/usr/share/man/man1/ukui-volume-control-applet.1.gz
gzip -c man/ukui-volume-control.1  > %{buildroot}/usr/share/man/man1/ukui-volume-control.1.gz

pushd ukui-volume-control-applet-qt/cmake_build
%{make_install}  INSTALL_ROOT=%{buildroot}
popd

%find_lang %name

%files
%doc debian/changelog
%license  debian/copyright 
%{_bindir}/*
%{_datadir}/applications/
%{_datadir}/ukui-media/

%files common -f %name.lang
%{_sysconfdir}/xdg/autostart/ukui-volume-control-applet.desktop
%{_datadir}/locale/*/LC_MESSAGES/ukui-media.mo
%{_mandir}/man1/ukui-volume-control-applet-qt.1.gz
%{_mandir}/man1/ukui-volume-control-applet.1.gz
%{_mandir}/man1/ukui-volume-control.1.gz
%{_datadir}/glib-2.0/schemas/org.ukui.media.gschema.xml

%post 
glib-compile-schemas /usr/share/glib-2.0/schemas/  2>/dev/null
