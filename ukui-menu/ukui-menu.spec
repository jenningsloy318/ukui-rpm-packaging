Name:           ukui-menu
Version:        master
Release:        1%{?dist}
Summary:        Advanced ukui menu


License:         GPL-3.0 License
URL:            https://github.com/ukui/ukui-menu
# %%Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0:        https://github.com/ukui/%{name}/archive/%{version}.zip#/%{name}-%{version}.zip

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
%{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  ..
%{make_build}
popd

%install
pushd qmake-build
%{make_install}  INSTALL_ROOT=%{buildroot} 
popd 
mkdir -p  %{buildroot}/usr/share/man/man1/
gzip -c man/ukui-menu.1  > %{buildroot}/usr/share/man/man1/ukui-menu.1.gz

%files
%doc debian/changelog debian/copyright
%{_sysconfdir}/xdg/autostart/ukui-menu.desktop
%{_bindir}/ukui-menu
%{_datadir}/man/man1/ukui-menu.1.gz
%{_datadir}/ukui-menu/