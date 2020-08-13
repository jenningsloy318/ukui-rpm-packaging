%global __cmake_in_source_build 1


Name:           ukui-screensaver
Version:        3.0.0
Release:        1%{?dist}
Summary:         Screensaver for UKUI desktop environment


License:        GPLv2+
URL:            https://github.com/ukui/ukui-screensaver
Source0:        %{name}-%{version}.tar.gz
BuildArch:      x86_64


BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtx11extras-devel
#BuildRequires: gdm-pam-extensions-devel
BuildRequires: pam-devel
BuildRequires: qt5-qttools-devel
BuildRequires: glib2-devel
BuildRequires: libX11-devel
BuildRequires: libXtst-devel
BuildRequires: gsettings-qt-devel
BuildRequires: extra-cmake-modules

Requires: ukui-session-manager
Requires: mate-common

%description
A simple and lightweight screensaver written by Qt5.
 The screensaver supports biometric auhentication which is
 provided by biometric-auth service.

%prep

%setup -q
sed -i 's|lib/ukui-screensaver|lib64/ukui-screensaver|g' screensaver/CMakeLists.txt

%build
export PATH=%{_qt5_bindir}:$PATH
%{cmake} 

%install
%{make_install} INSTALL_ROOT=%{buildroot}
install -d %{buildroot}/usr/share/man/man1
gzip -c man/ukui-screensaver-backend.1 >  %{buildroot}/usr/share/man/man1/ukui-screensaver-backend.1.gz
gzip -c man/ukui-screensaver-dialog.1 >  %{buildroot}/usr/share/man/man1/ukui-screensaver-dialog.1.gz
gzip -c man/ukui-screensaver-command.1 >  %{buildroot}/usr/share/man/man1/ukui-screensaver-command.1.gz

%files
%doc debian/changelog
%license  debian/copyright
%{_sysconfdir}/pam.d/ukui-screensaver-qt
%{_sysconfdir}/xdg/autostart/ukui-screensaver.desktop
%{_sysconfdir}/xdg/menus/ukui-screensavers.menu
%{_bindir}/ukui-screensaver-backend
%{_bindir}/ukui-screensaver-command
%{_bindir}/ukui-screensaver-dialog
%{_libdir}/ukui-screensaver
%{_datadir}/desktop-directories/ukui-screensaver.directory
%{_datadir}/glib-2.0/schemas/org.ukui.screensaver.gschema.xml 
%{_datadir}/ukui-screensaver/
%{_mandir}/man1/ukui-screensaver-backend.1.gz
%{_mandir}/man1/ukui-screensaver-dialog.1.gz
%{_mandir}/man1/ukui-screensaver-command.1.gz

