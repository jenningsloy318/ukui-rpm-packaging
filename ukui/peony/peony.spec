# enable download source
%undefine _disable_source_fetch

Name:           peony
Version:        2.1.2
Release:        1%{?dist}
Summary:        file Manager for the UKUI desktop

License:        GPLv2+
URL:            https://github.com/ukui/%{name}
Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      x86_64

Requires: libpeony-qt
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




%package -n libpeony2

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

%description -n libpeony2
 Peony is the official file manager for the UKUI desktop. It allows one
 to browse directories, preview files and launch applications associated
 with them. It is also responsible for handling the icons on the UKUI
 desktop. It works on local and remote filesystems.
 .
 This package contains a few runtime libraries needed by Peony's
 extensions.


%package -n libpeony-devel

Summary: libraries for Peony components (development files)


Requires: libpeony2

%description -n libpeony-devel
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
mkdir -p %{buildroot}/usr/share/doc/peony/
cp debian/copyright  %{buildroot}/usr/share/doc/peony/
gzip  debian/changelog > %{buildroot}/usr/share/doc/peony/changelog.gz

%files
%{_bindir}/peony
%{_bindir}/peony-qt-desktop
%{_datadir}/applications/peony.desktop
%{_datadir}/peony-qt/peony-qt_zh_CN.ts
%{_datadir}/peony-qt-desktop/peony-qt-desktop_zh_CN.ts

%files common 
%{_datadir}/doc/peony

%files -n  libpeony2
%{_datadir}/doc
%{_libdir}/libpeony.so
%{_libdir}/libpeony.so.2
%{_libdir}/libpeony.so.2.1
%{_libdir}/libpeony.so.2.1.0
%{_libdir}/pkgconfig/peony.pc
%{_datadir}/libpeony-qt/libpeony-qt_zh_CN.ts


%files -n libpeony-devel
%{_includedir}/peony-qt