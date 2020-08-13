Name:           ukui-biometric-manager
Version:        1.0.0
Release:        1%{?dist}
Summary:        kylin-fingerprint, kylin-fprint-login


License:         GPL-3.0 License
URL:            https://github.com/ukui/ukui-biometric-manager
Source0:        %{name}-%{version}.tar.gz

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
export PATH=%{_qt5_bindir}:$PATH
mkdir qmake-build
pushd qmake-build
%{qmake_qt5} ..
%{make_build}
popd

%install
pushd qmake-build
%{make_install} INSTALL_ROOT=%{buildroot}
popd
install -d %{buildroot}/usr/share/man/man1/
gzip -c man/biometric-manager.1		 > %{buildroot}/usr/share/man/man1/biometric-manager.1.gz

%files
%doc debian/changelog
%license  debian/copyright 
%{_mandir}/man1/biometric-manager.1.gz
%{_bindir}/biometric-manager
%{_datadir}/applications/biometric-manager.desktop
%{_datadir}/pixmaps/biometric-manager.png
%{_datadir}/biometric-manager/
