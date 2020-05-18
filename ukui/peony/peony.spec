# enable download source
%undefine _disable_source_fetch

Name:           peony
Version:        2.1.2
Release:        1%{?dist}
Summary:        file Manager for the UKUI desktop

License:        GPLv2+
URL:            https://github.com/ukui/ukui-session-manager
Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      x86_64

Requires: peony-libpeony-qt
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




%package libpeony-qt

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

%description libpeony-qt
 Peony is the official file manager for the UKUI desktop. It allows one
 to browse directories, preview files and launch applications associated
 with them. It is also responsible for handling the icons on the UKUI
 desktop. It works on local and remote filesystems.
 .
 This package contains a few runtime libraries needed by Peony's
 extensions.


%package libpeony-qt-devel

Summary: libraries for Peony components (development files)


Requires: libpeony-qt

%description libpeony-qt-devel
 Peony is the official file manager for the UKUI desktop. It allows one
 to browse directories, preview files and launch applications associated
 with them. It is also responsible for handling the icons on the UKUI
 desktop. It works on local and remote filesystems.
 .
 This package contains the development files for the libraries needed
 by Peony's extensions.


%prep

%setup -q
 
%build
  %{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  peony-qt.pro
  %{make_build}

%install
rm -rf %{buildroot}
%{make_install}  INSTALL_ROOT=%{buildroot} 
mkdir -p %{buildroot}/usr/share/doc/ukui-desktop-environment/
cp debian/copyright  %{buildroot}/usr/share/doc/ukui-desktop-environment/
gzip  debian/changelog > %{buildroot}/usr/share/doc/ukui-desktop-environment/changelog.gz

%files
%{_bindir}/peony
%{_bindir}/peony-qt-desktop
%{_datadir}/doc/ukui-desktop-environment/changelog.gz
%{_datadir}/doc/ukui-desktop-environment/copyright
%{_datadir}/applications/peony.desktop
%{_datadir}/peony-qt/peony-qt_zh_CN.ts
%{_datadir}/peony-qt-desktop/peony-qt-desktop_zh_CN.ts

%files common 
%{_datadir}/doc

%files libpeony-qt
%{_datadir}/doc
%{_libdir}/libpeony.so
%{_libdir}/libpeony.so.2
%{_libdir}/libpeony.so.2.1
%{_libdir}/libpeony.so.2.1.0
%{_libdir}/pkgconfig/peony.pc
%{_datadir}/doc/ukui-desktop-environment/changelog.gz
%{_datadir}/doc/ukui-desktop-environment/copyright
%{_datadir}/libpeony-qt/libpeony-qt_zh_CN.ts


%files libpeony-qt-devel
%{_datadir}/doc/ukui-desktop-environment/changelog.gz
%{_datadir}/doc/ukui-desktop-environment/copyright
%{_includedir}/peony-qt