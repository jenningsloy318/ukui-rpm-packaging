# enable download source
%undefine _disable_source_fetch

Name:           ukui-biometric-auth
Version:        1.2.0
Release:        1%{?dist}
Summary:        ukui-biometric-auth

License:        GPLv2+
URL:            https://github.com/ukui/%{name}
Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:       lib-path.patch

BuildArch:      x86_64
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  pam-devel
BuildRequires:  polkit-qt5-1-devel

Requires: pam-biometric
Requires: ukui-polkit

%description
ukui-biometric-auth



%package -n pam-biometric
Summary: Insertable authentication module for PAM




%description -n pam-biometric
 The indispensable part for biometric authentication in
 ukui desktop environment.
 This package contains a modules for PAM.




%package -n ukui-polkit

Summary: UKUI authentication agent for PolicyKit-1


%description -n ukui-polkit
 The ukui-polkit package supports general authentication and
 biometric authentication that the service is provided by the
 biometric-auth package.


%prep

%setup -q
  cp %{SOURCE1} .
  patch -p0 < lib-path.patch


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
mkdir  -p %{buildroot}/usr/share/doc/ukui-biometric-auth %{buildroot}/usr/share/man/man1/
cp debian/copyright  %{buildroot}/usr/share/doc/ukui-biometric-auth/
gzip  debian/changelog > %{buildroot}/usr/share/doc/ukui-biometric-auth/changelog.gz
gzip man/bioctl.1 > %{buildroot}/usr/share/man/man1/bioctl.1.gz
gzip man/bioauth.1 > %{buildroot}/usr/share/man/man1/bioauth.1.gz
gzip man/biodrvctl.1 > %{buildroot}/usr/share/man/man1/biodrvctl.1.gz

%files
%{_datadir}/doc/ukui-biometric-auth
%{_datadir}/ukui-biometric/images
%{_datadir}/ukui-biometric/i18n_qm/es.qm
%{_datadir}/ukui-biometric/i18n_qm/fr.qm
%{_datadir}/ukui-biometric/i18n_qm/pt.qm
%{_datadir}/ukui-biometric/i18n_qm/ru.qm
%{_datadir}/ukui-biometric/i18n_qm/zh_CN.qm

%files -n pam-biometric
%{_bindir}/bioauth
%{_bindir}/bioctl
%{_bindir}/biodrvctl
%{_sysconfdir}/biometric-auth/ukui-biometric.conf
%{_libdir}/security/pam_biometric.so
%{_datadir}/pam-configs/pam-biometric
%{_datadir}/polkit-1/actions/org.freedesktop.plicykit.pkexec.bioctl.policy
%{_datadir}/polkit-1/actions/org.freedesktop.plicykit.pkexec.biodrvctl.policy
%{_datadir}/ukui-biometric/i18n_qm/bioauth-bin
%{_mandir}/man1/bioctl.1.gz
%{_mandir}/man1/bioauth.1.gz
%{_mandir}/man1/biodrvctl.1.gz


%files -n  ukui-polkit
%{_sysconfdir}/xdg/autostart/polkit-ukui-authentication-agent-1.desktop
%{_libdir}/ukui-polkit/polkit-ukui-authentication-agent-1
%{_datadir}/ukui-biometric/i18n_qm/polkit/es.qm
%{_datadir}/ukui-biometric/i18n_qm/polkit/fr.qm
%{_datadir}/ukui-biometric/i18n_qm/polkit/pt.qm
%{_datadir}/ukui-biometric/i18n_qm/polkit/ru.qm
%{_datadir}/ukui-biometric/i18n_qm/polkit/zh_CN.qm
        