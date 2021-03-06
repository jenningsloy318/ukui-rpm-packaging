%global __cmake_in_source_build 1

Name:           ukui-session-manager
Version:        3.0.1
Release:        1%{?dist}
Summary:        Session manager of the UKUI desktop environment


License:        LGPL-2.1 License
URL:            https://github.com/ukui/ukui-session-manager
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64
BuildRequires:  qt5-qtdeclarative-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  kf5-kidletime-devel
BuildRequires:  qt5-qttools-devel 
BuildRequires:  qt5-qttools
BuildRequires:  qt5-linguist
BuildRequires:  gsettings-qt-devel
BuildRequires:  libXtst-devel
BuildRequires:  libqtxdg-devel
BuildRequires:  systemd-devel
BuildRequires:  kf5-rpm-macros
BuildRequires:  libX11-devel
BuildRequires: xdg-user-dirs

Requires: peony
Requires: (ukui-kwin or ukwm)
Requires: ukui-panel
Requires: ukui-polkit
Requires: ukui-screensaver
Requires: ukui-settings-daemon
Requires: qt5-qtmultimedia


Provides: x-session-manager


%description
 This package contains a session that can be started from a display
 manager such as lightdm. It will load all necessary applications for
 a full-featured user session.
 This package contain the session manager component.

%prep
%setup -q

%build
export PATH=%{_qt5_bindir}:$PATH
%{cmake} 
%{make_build} 

%install
%{make_install} INSTALL_ROOT=%{buildroot}
install -d   %{buildroot}/usr/share/man/man1/
install -D -m644 data/com.ubuntu.enable-hibernate.pkla -t %{buildroot}/etc/polkit-1/localauthority/50-local.d/
gzip -c man/ukui-session.1 >  %{buildroot}/usr/share/man/man1/ukui-session.1.gz 
gzip -c man/ukui-session-tools.1 > %{buildroot}/usr/share/man/man1/ukui-session-tools.1.gz


%files
%doc debian/changelog
%license  debian/copyright 
%{_sysconfdir}/polkit-1/localauthority/50-local.d/com.ubuntu.enable-hibernate.pkla
%{_datadir}/ukui/translations/ukui-session-manager/
%{_datadir}/xsessions/ukui.desktop
%{_datadir}/glib-2.0/schemas/org.ukui.session.gschema.xml
%{_bindir}/ukui-session
%{_bindir}/ukui-session-tools
%{_datadir}/man/man1/ukui-session.1.gz 
%{_datadir}/man/man1/ukui-session-tools.1.gz

%post 
glib-compile-schemas /usr/share/glib-2.0/schemas/ 2>/dev/null
