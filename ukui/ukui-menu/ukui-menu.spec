# enable download source
%undefine _disable_source_fetch

Name:           ukui-menu
Version:        2.0.6
Release:        1%{?dist}
Summary:        Advanced ukui menu


License:        GPLv2+
URL:            https://github.com/ukui/ukui-session-manager
Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      x86_64

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  glib2-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  bamf-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXtst-devel
BuildRequires:  libX11-devel

Requires:  gsettings-qt
Requires:  qt5-qtx11extras
Requires:  bamf-daemon
Requires:  libXrandr
Requires:  libXtst
Requires:  libX11

%description
 UKUI menu provides start menu development library and advanced
 graphical user interface.
 .
 The package contains executable file.

%prep
%setup -q
%build
  %{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  ukui-menu.pro	
  %{make_build}

%install
rm -rf $RPM_BUILD_ROOT
%{make_install}  INSTALL_ROOT=%{buildroot} 
mkdir -p %{buildroot}/usr/share/doc/ukui-menu/ %{buildroot}/usr/share/man/man1/
cp debian/copyright  %{buildroot}/usr/share/doc/ukui-menu/
gzip  debian/changelog > %{buildroot}/usr/share/doc/ukui-menu/changelog.gz
gzip man/ukui-menu.1  > %{buildroot}/usr/share/man/man1/ukui-menu.1.gz
%files
%{_sysconfdir}/xdg/autostart/ukui-menu.desktop
%{_bindir}/ukui-menu
%{_datadir}/doc/ukui-menu/changelog.gz
%{_datadir}/doc/ukui-menu/copyright
%{_datadir}/man/man1/ukui-menu.1.gz
