# enable download source
%undefine _disable_source_fetch

Name:           peony
Version:        master
Release:        1%{?dist}
Summary:        file Manager for the UKUI desktop

License:         GPL-2.0 License
URL:            https://github.com/ukui/peony
Source0:        https://github.com/ukui/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         peony-libdir.patch

BuildArch:      x86_64

Requires: peony-libs
Requires: peony-common
Requires: kf5-kwindowsystem


Recommends: gvfs-backends
Recommends: peony-open-terminal
Recommends: peony-admin
Recommends: peony-share
Recommends: parchives

%description
 Peony is the official file manager for the UKUI desktop. It allows one
 to browse directories, preview files and launch applications associated
 with them. It is also responsible for handling the icons on the UKUI
 desktop. It works on local and remote filesystems.




%package common
Summary: file manager for the UKUI desktop (common files)




%description common
 Peony is the official file manager for the UKUI desktop. It allows one
 to browse directories, preview files and launch applications associated
 with them. It is also responsible for handling the icons on the UKUI
 desktop. It works on local and remote filesystems.
 .
 This package contains the architecture independent files.




%package libs

Summary: libraries for Peony components

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  glib2-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  poppler-qt5-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtbase-private-devel

%description libs
 Peony is the official file manager for the UKUI desktop. It allows one
 to browse directories, preview files and launch applications associated
 with them. It is also responsible for handling the icons on the UKUI
 desktop. It works on local and remote filesystems.
 .
 This package contains a few runtime libraries needed by Peony's
 extensions.


%package devel

Summary: libraries for Peony components (development files)


Requires: peony-libs

%description devel
 Peony is the official file manager for the UKUI desktop. It allows one
 to browse directories, preview files and launch applications associated
 with them. It is also responsible for handling the icons on the UKUI
 desktop. It works on local and remote filesystems.
 .
 This package contains the development files for the libraries needed
 by Peony's extensions.


%prep

%setup -q
%patch0 -p0

%build
export PATH=%{_qt5_bindir}:$PATH
mkdir qmake-build
pushd qmake-build
%{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  ..
%{make_build}
popd

%install
pushd qmake-build
%{make_install}  INSTALL_ROOT=%{buildroot} 
popd
mkdir  -p %{buildroot}/usr/share/man/man1/ %{buildroot}/usr/share/dbus-1/interfaces/ %{buildroot}/usr/share/dbus-1/services/
install -m644  peony-qt-desktop/freedesktop-dbus-interfaces.xml %{buildroot}/usr/share/dbus-1/interfaces/freedesktop-dbus-interfaces.xml
install -m644  peony-qt-desktop/org.ukui.freedesktop.FileManager1.service %{buildroot}/usr/share/dbus-1/services/org.ukui.freedesktop.FileManager1.service
gzip -c src/man/peony.1 > %{buildroot}/usr/share/man/man1/peony.1.gz
gzip -c peony-qt-desktop/man/peony-qt-desktop.1 >  %{buildroot}/usr/share/man/man1/peony-qt-desktop.1.gz
install -m644  data/peony.desktop %{buildroot}/usr/share/applications/peony.desktop
install -m644  data/peony-computer.desktop %{buildroot}/usr/share/applications/peony-computer.desktop
install -m644  data/peony-home.desktop %{buildroot}/usr/share/applications/peony-home.desktop
install -m644  data/peony-trash.desktop %{buildroot}/usr/share/applications/peony-trash.desktop
install -m644  data/peony-desktop.desktop %{buildroot}/usr/share/applications/peony-desktop.desktop


%files
%{_bindir}/peony
%{_bindir}/peony-qt-desktop
%{_datadir}/applications/peony.desktop 
%{_datadir}/applications/peony-computer.desktop 
%{_datadir}/applications/peony-home.desktop 
%{_datadir}/applications/peony-trash.desktop 
%{_datadir}/applications/peony-desktop.desktop

%files common 
%doc debian/copyright debian/changelog
%{_mandir}/man1/peony-qt-desktop.1.gz
%{_mandir}/man1/peony.1.gz
%{_datadir}/dbus-1/interfaces/freedesktop-dbus-interfaces.xml
%{_datadir}/dbus-1/services/org.ukui.freedesktop.FileManager1.service
%{_datadir}/libpeony-qt/
%{_datadir}/peony-qt-desktop/
%{_datadir}/peony-qt/

%files libs
%{_libdir}/libpeony.so
%{_libdir}/libpeony.so.2
%{_libdir}/libpeony.so.2.1
%{_libdir}/libpeony.so.2.1.0

%files devel
%{_includedir}/peony-qt
%{_libdir}/pkgconfig/peony.pc
