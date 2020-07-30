Name:           ukui-session-manager
Version:        master
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

Requires: peony
Requires: (ukui-kwin or ukwm)
Requires: ukui-panel
Requires: ukui-polkit
Requires: ukui-screensaver
Requires: ukui-settings-daemon

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
mkdir cmake-build
pushd cmake-build
%if 0%{?rhel} == 8
if ! grep -q "qm_files.CONFIG" /usr/lib64/qt5/mkspecs/features/lrelease.prf; then 
sed -i '/qm_files.path/a qm_files.CONFIG = no_check_exist'  /usr/lib64/qt5/mkspecs/features/lrelease.prf
fi
%endif
%{cmake_kf5} ..
%{cmake_build}
popd

%install
pushd cmake-build
%{cmake_install}
popd
install -d %{buildroot}/etc/X11/Xsession.d/    %{buildroot}/usr/share/man/man1/
install -m644  debian/99ukui-environment %{buildroot}/etc/X11/Xsession.d/99ukui-environment
gzip -c man/ukui-session.1 >  %{buildroot}/usr/share/man/man1/ukui-session.1.gz 
gzip -c man/ukui-session-tools.1 > %{buildroot}/usr/share/man/man1/ukui-session-tools.1.gz


%files
%doc debian/changelog debian/copyright
%{_datadir}/ukui/translations/ukui-session-manager/
%{_datadir}/xsessions/ukui.desktop
%{_datadir}/glib-2.0/schemas/org.ukui.session.gschema.xml
%{_bindir}/ukui-session
%{_bindir}/ukui-session-tools
%{_sysconfdir}/X11/Xsession.d/99ukui-environment
%{_datadir}/man/man1/ukui-session.1.gz 
%{_datadir}/man/man1/ukui-session-tools.1.gz