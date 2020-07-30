# disable debug package
%define debug_package %{nil}

Name:           kylin-display-switch
Version:        master
Release:        1%{?dist}
Summary:        Gui tool for display switching


License:         GPL-3.0 License
URL:            https://github.com/ukui/kylin-display-switch
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64

BuildRequires: python3
BuildRequires: python3-setuptools
BuildRequires: python3-distutils-extra
BuildRequires: python3-rpm-macros
BuildRequires: python-rpm-macros

Requires:  python3-qt5
Requires:  python3-xlib

%description
 Kylin Display Switch is a Gui tool managing display output.
 Super_L + P/F3/F7 are utilized to activate display switching.
 .
 It also monitors CapsLock and NumLock key, when these
 buttons are clicked, corresponding reminder will popper up.

%prep

%setup -q
 
%build

%{py3_build} 

%install
%{py3_install}


%files
%doc debian/copyright debian/changelog
%{_sysconfdir}/xdg/autostart/kylin-display-switch.desktop
%{_bindir}/kds
%{_datadir}/kylin-display-switch/
%{_datadir}/locale/*/LC_MESSAGES/kylin-display-switch.mo
%{_mandir}/man1/kds.1.gz
%{python3_sitelib}/kylin_display_switch-*.egg-info
