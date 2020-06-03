# enable download source
%undefine _disable_source_fetch

Name:           ukui-biometric-manager
Version:        1.0.0
Release:        1%{?dist}
Summary:        kylin-fingerprint, kylin-fprint-login


License:        GPLv2+
URL:            https://github.com/ukui/ukui-biometric-manager
Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      x86_64
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel

Requires: pam-biometric

%description
 This package is a tool to manage the drivers of biometric devices and
 users' features and manage whether biometric authentication is enabled.
 The service is provided by biometric-authentication.service in
 biometric-auth package.


%prep

%setup -q
 
%build
  %{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  biometric-manager.pro	
  %{make_build}

%install
rm -rf %{buildroot}
%{make_install}  INSTALL_ROOT=%{buildroot} 
mkdir -p %{buildroot}/usr/share/doc/ukui-biometric-manager/ %{buildroot}/usr/share/man/man1/
gzip -c man/biometric-manager.1		 > %{buildroot}/usr/share/man/man1/biometric-manager.1.gz

%files
%{_mandir}/man1/biometric-manager.1.gz
%{_bindir}/biometric-manager
%{_datadir}/applications/biometric-manager.desktop
%{_datadir}/pixmaps/biometric-manager.png