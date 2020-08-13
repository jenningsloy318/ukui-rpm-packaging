Name:           ukui-menu
Version:        2.0.7
Release:        1%{?dist}
Summary:        Advanced ukui menu


License:         GPL-3.0 License
URL:            https://github.com/ukui/ukui-menu
Source0:        %{name}-%{version}.tar.gz

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
BuildRequires:  qt5-linguist
BuildRequires:  kf5-kwindowsystem-devel
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
export PATH=%{_qt5_bindir}:$PATH
mkdir qmake-build
pushd qmake-build
%if 0%{?rhel} == 8
if ! grep -q "qm_files.CONFIG" /usr/lib64/qt5/mkspecs/features/lrelease.prf; then 
sed -i '/qm_files.path/a qm_files.CONFIG = no_check_exist'  /usr/lib64/qt5/mkspecs/features/lrelease.prf
fi
%endif
%{qmake_qt5} ..
%{make_build}
popd

%install
pushd qmake-build
%{make_install} INSTALL_ROOT=%{buildroot}
popd 
install -d %{buildroot}/usr/share/man/man1/
gzip -c man/ukui-menu.1  > %{buildroot}/usr/share/man/man1/ukui-menu.1.gz

%files
%doc debian/changelog
%license  debian/copyright
%{_sysconfdir}/xdg/autostart/ukui-menu.desktop
%{_bindir}/ukui-menu
%{_datadir}/man/man1/ukui-menu.1.gz
%{_datadir}/ukui-menu/
