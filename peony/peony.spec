# enable download source
%undefine _disable_source_fetch

Name:           peony
Version:        2.2.0
Release:        1%{?dist}
Summary:        file Manager for the UKUI desktop

License:        GPLv2+
URL:            https://github.com/ukui/%{name}
Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
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
  %{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  peony-qt.pro
  %{make_build}

%install
rm -rf %{buildroot}
%{make_install}  INSTALL_ROOT=%{buildroot} 
mkdir  -p %{buildroot}/usr/share/man/man1/ %{buildroot}/usr/share/dbus-1/interfaces/ %{buildroot}/usr/share/dbus-1/services/  %{buildroot}/usr/share/doc/peony
cp peony-qt-desktop/freedesktop-dbus-interfaces.xml %{buildroot}/usr/share/dbus-1/interfaces/freedesktop-dbus-interfaces.xml
cp peony-qt-desktop/org.ukui.freedesktop.FileManager1.service %{buildroot}/usr/share/dbus-1/services/org.ukui.freedesktop.FileManager1.service
gzip -c src/man/peony.1 > %{buildroot}/usr/share/man/man1/peony.1.gz
gzip -c peony-qt-desktop/man/peony-qt-desktop.1 >  %{buildroot}/usr/share/man/man1/peony-qt-desktop.1.gz
cp data/*.desktop %{buildroot}/usr/share/applications/
cp debian/copyright  %{buildroot}/usr/share/doc/peony/
gzip -c debian/changelog > %{buildroot}/usr/share/doc/peony/changelog.gz


%files
%{_bindir}/peony
%{_bindir}/peony-qt-desktop
%{_datadir}/applications/peony.desktop 
%{_datadir}/applications/peony-computer.desktop 
%{_datadir}/applications/peony-home.desktop 
%{_datadir}/applications/peony-trash.desktop 
%{_datadir}/applications/peony-desktop.desktop
%{_datadir}/peony-qt-desktop/peony-qt-desktop_tr.ts
%files common 
%{_mandir}/man1/peony-qt-desktop.1.gz
%{_mandir}/man1/peony.1.gz
%{_datadir}/peony-qt/peony-qt_zh_CN.ts
%{_datadir}/peony-qt-desktop/peony-qt-desktop_zh_CN.ts
%{_datadir}/dbus-1/interfaces/freedesktop-dbus-interfaces.xml
%{_datadir}/dbus-1/services/org.ukui.freedesktop.FileManager1.service
%{_datadir}/doc/peony/

%files libs
%{_libdir}/libpeony.so
%{_libdir}/libpeony.so.2
%{_libdir}/libpeony.so.2.1
%{_libdir}/libpeony.so.2.1.0
%{_datadir}/libpeony-qt/libpeony-qt_zh_CN.ts


%files devel
%{_includedir}/peony-qt
%{_libdir}/pkgconfig/peony.pc
