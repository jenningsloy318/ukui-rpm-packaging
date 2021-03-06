Name:           ukui-system-monitor
Version:        1.0.1
Release:        1%{?dist}
Summary:        Monitor for UKUI desktop environment

License:         GPL-3.0 License
URL:            https://github.com/ukui/ukui-system-monitor
Source0:        %{name}-%{version}.tar.gz
BuildArch:      x86_64



BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  glib2-devel
BuildRequires:  libgtop2-devel
BuildRequires:  systemd-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  libpcap-devel
BuildRequires:  kf5-kwindowsystem-devel

Requires: libcap
Requires: libgtop2


%description
 Monitor for UKUI desktop environment
 UKUI system monitor allows you to graphically view and manipulate the
 running processes, It also provides an overview of the resources (such
 as CPU and memory) and File Systems on your system.

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
%{_bindir}/ukui-system-monitor
%{_datadir}/applications/ukui-system-monitor.desktop
%{_datadir}/icons/hicolor/ukui-system-monitor.png
%{_datadir}/glib-2.0/schemas/org.ukui.system-monitor.menu.gschema.xml
