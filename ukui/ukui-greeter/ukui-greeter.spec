Name:           ukui-greeter
Version:        3.0.0
Release:        1%{?dist}
Summary:        Lightdm greeter for UKUI


License:        GPL-2.0 License
URL:            https://github.com/ukui/ukui-greeter
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64


BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: lightdm-qt5-devel
BuildRequires: libX11-devel
BuildRequires: libXtst-devel
BuildRequires: libXrandr-devel
BuildRequires: qt5-qttools-devel
BuildRequires: imlib2-devel

Requires: lightdm

Provides: lightdm-greeter

%description
 A greeter for UKUI desktop environment written by Qt5.
 The greeter supports biometric authentication which is
 provided by biometric-authentication service.



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
install -d %{buildroot}/usr/share/man/man8/
gzip -c ukui-greeter/man/ukui-greeter.8 > %{buildroot}/usr/share/man/man8/ukui-greeter.8.gz

%files
%doc debian/changelog
%license  debian/copyright 
%{_sysconfdir}/lightdm/ukui-greeter.conf
%{_datadir}/man/man8/ukui-greeter.8.gz
%{_sbindir}/ukui-greeter
%{_datadir}/lightdm/lightdm.conf.d/95-ukui-greeter.conf
%{_datadir}/ukui-greeter/
%{_datadir}/xgreeters/ukui-greeter.desktop