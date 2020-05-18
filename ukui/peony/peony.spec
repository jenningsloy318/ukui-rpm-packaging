# enable download source
%undefine _disable_source_fetch

Name:           peony
Version:        2.1.2
Release:        1%{?dist}
Summary:        file Manager for the UKUI desktop

License:        GPLv2+
URL:            https://github.com/ukui/ukui-session-manager
Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        plugin-path.patch

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


%description libs
 Peony is the official file manager for the UKUI desktop. It allows one
 to browse directories, preview files and launch applications associated
 with them. It is also responsible for handling the icons on the UKUI
 desktop. It works on local and remote filesystems.
 .
 This package contains a few runtime libraries needed by Peony's
 extensions.


%package libs-devel

Summary: libraries for Peony components (development files)


Requires: peony-libs

%description libs-devel
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
  %{qmake_qt5} %_qt5_qmake_flags CONFIG+=enable-by-default  peony-qt.pro
  %make_build

%install
rm -rf %{buildroot}
%make_install  INSTALL_ROOT=%{buildroot} 
mkdir -p %{buildroot}/usr/share/doc/ukui-desktop-environment/
cp debian/copyright  %{buildroot}/usr/share/doc/ukui-desktop-environment/
gzip  debian/changelog > %{buildroot}/usr/share/doc/ukui-desktop-environment/changelog.gz

%files
%{_bindir}/
%{_libdir}/
%{_datadir}/doc


%files common 
%{_datadir}/doc

%file libs
%{_datadir}/doc

%files libs-devel
%{_datadir}/doc