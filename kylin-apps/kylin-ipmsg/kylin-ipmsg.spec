Name:           kylin-ipmsg
Version:        1.1.0
Release:        1%{?dist}
Summary:        Kylin Ipmsg is a LAN chat tool with beautiful Gui


License:         GPL-3.0 License
URL:            https://github.com/ukui/ukui-menu
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  glib2-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  libX11-devel
BuildRequires:  qt5-qtquickcontrols2-devel
Requires:  wmctrl

%description
Kylin Ipmsg is a LAN chat tool with beautiful Gui
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

%files
%doc debian/changelog
%license  debian/copyright
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/kylin-user-guide/data/guide/kylin-ipmsg
