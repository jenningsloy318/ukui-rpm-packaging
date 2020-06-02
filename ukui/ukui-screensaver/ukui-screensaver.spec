# enable download source
%undefine _disable_source_fetch

Name:           ukui-screensaver
Version:        2.1.1
Release:        1%{?dist}
Summary:         Screensaver for UKUI desktop environment




License:        GPLv2+
URL:            https://github.com/ukui/ukui-screensaver
Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      x86_64


BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: gdm-pam-extensions-devel
BuildRequires: pam-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  glib2-devel
BuildRequires:  libX11-devel
BuildRequires: libXtst-devel
BuildRequires: gsettings-qt-devel


Requires: ukui-session-manager
Requires: mate-common

%description
A simple and lightweight screensaver written by Qt5.
 The screensaver supports biometric auhentication which is
 provided by biometric-auth service.

%prep

%setup -q
 
%build
mkdir cmake-build
pushd cmake-build
%cmake3 ..
%{make_build}
popd

%install
pushd cmake-build
%{make_install}  INSTALL_ROOT=%{buildroot} 
popd
mkdir -p %{buildroot}/usr/share/doc/ukui-screensaver/ %{buildroot}/usr/share/man/man1
cp debian/copyright  %{buildroot}/usr/share/doc/ukui-screensaver/
gzip  debian/changelog > %{buildroot}/usr/share/doc/ukui-screensaver/changelog.gz
gzip man/ukui-screensaver-backend.1 >  %{buildroot}/usr/share/man/man1/ukui-screensaver-backend.1.gz
gzip man/ukui-screensaver-dialog.1 >  %{buildroot}/usr/share/man/man1/ukui-screensaver-dialog.1.gz
gzip man/ukui-screensaver-command.1 >  %{buildroot}/usr/share/man/man1/ukui-screensaver-command.1.gz

%files
%{_sysconfdir}/pam.d/ukui-screensaver-qt
%{_sysconfdir}/xdg/autostart/ukui-screensaver.desktop
%{_sysconfdir}/xdg/menus/ukui-screensavers.menu
%{_bindir}/ukui-screensaver-backend
%{_bindir}/ukui-screensaver-command
%{_bindir}/ukui-screensaver-dialog
%{_datadir}/desktop-directories/ukui-screensaver.directory
%{_datadir}/glib-2.0/schemas/org.ukui.screensaver.gschema.xml 
%{_datadir}/ukui-screensaver/
%{_datadir}/doc/ukui-screensaver
%{_mandir}/man1/ukui-screensaver-backend.1.gz
%{_mandir}/man1/ukui-screensaver-dialog.1.gz
%{_mandir}/man1/ukui-screensaver-command.1.gz
