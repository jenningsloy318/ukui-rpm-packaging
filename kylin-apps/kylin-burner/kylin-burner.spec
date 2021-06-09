Name:           kylin-burner
Version:        3.1.0
Release:        1%{?dist}
Summary:        a easy useful burn software.




License:        GPL-3.0 License
URL:            https://github.com/UbuntuKylin/%{name}
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtbase-gui
BuildRequires: qt5-qtwebkit-devel
BuildRequires: gsettings-qt-devel
BuildRequires: libsamplerate-devel
BuildRequires: kf5-libkcddb-devel
BuildRequires: libdvdread-devel
BuildRequires: taglib-devel,taglib-extras-devel
BuildRequires: libmusicbrainz5-devel
BuildRequires: ffmpeg-devel
BuildRequires: flac-devel
BuildRequires: libmad-devel
BuildRequires: libmpcdec-devel
BuildRequires: libsndfile-devel
BuildRequires: lame-devel
BuildRequires: libvorbis-devel
BuildRequires: libogg-devel
BuildRequires: kf5-knotifyconfig-devel
BuildRequires: kf5-karchive-devel
BuildRequires: kf5-kfilemetadata-devel

Requires: ffmpeg-libs
Requires: flac-libs
Requires: libmad
Requires: libmpcdec
Requires: libsndfile
Requires: lame-libs
Requires: libvorbis
Requires: libogg
Requires: libdvdread
Requires: qt5-qtbase
Requires: qt5-qtbase-gui
Requires: qt5-qtwebkit
Requires: kf5-knotifyconfig
Requires: kf5-karchive
Requires: kf5-kfilemetadata
Requires: kf5-libkcddb
Requires: gsettings-qt
Requires: libmusicbrainz5
Requires: libsamplerate

%description
Kylin Burner forked from k3b.

a easy useful burn software.



%prep

%setup -q
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

%find_lang k3b
%find_lang kio_videodvd
%find_lang libk3b
%find_lang libk3bdevice

%files -f k3b.lang -f kio_videodvd.lang -f libk3b.lang -f libk3bdevice.lang
%doc debian/changelog
%license  debian/copyright
%{_bindir}/burner
%{_includedir}/k3b*.h
%{_datadir}/k3b
%{_libdir}/libexec/k3bhelper
%{_libdir}/libk3b*
%{_qt5_plugindir}/k3b*
%{_qt5_plugindir}/kcm_k3b*
%{_qt5_plugindir}/kf5/kio/videodvd.so
%{_datadir}/applications/org.kde.kylin-burner.desktop
%{_datadir}/dbus-1/system-services/org.kde.k3b.service
%{_datadir}/dbus-1/system.d/org.kde.k3b.conf
%{_datadir}/kservices5/ServiceMenus/k3b*
%{_datadir}/kservices5/k3b*
%{_datadir}/kservices5/kcm_k3b*
%{_datadir}/kservices5/videodvd.protocol
%{_datadir}/kservicetypes5/k3bplugin.desktop
%{_datadir}/kxmlgui5/k3b/
%{_datadir}/doc/HTML/*/k3b/
%{_datadir}/icons/hicolor/*/apps/k3b.*
%{_datadir}/icons/hicolor/*/mimetypes/application-x-k3b.*
%{_datadir}/knotifications5/k3b.notifyrc
%{_datadir}/knsrcfiles/k3btheme.knsrc
%{_datadir}/konqsidebartng/virtual_folders/services/videodvd.desktop
%{_datadir}/metainfo/org.kde.k3b.appdata.xml
%{_datadir}/mime/packages/x-k3b.xml
%{_datadir}/polkit-1/actions/*k3b*
%{_datadir}/solid/actions/k3b*
