Name:           ukui-system-monitor
Version:        master
Release:        1%{?dist}
Summary:        simple system monitor written in QT

License:        GPLv2+
URL:            https://github.com/ukui/ukui-system-monitor
# %%Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0:        https://github.com/ukui/%{name}/archive/%{version}.zip#/%{name}-%{version}.zip
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

Requires: inotify-tools
Requires: hdparm
Requires: lm_sensors
Requires: ethtool 
Requires: lshw
Requires: dmidecode
Requires: CPUFreqUtility
Requires: pciutils
%description
 simple system monitor written in QT

%prep
%setup -q


%build
mkdir qmake-build
pushd qmake-build
%{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  ..	
%{make_build}
popd

%install
pushd qmake-build
%{make_install}  INSTALL_ROOT=%{buildroot} 
popd

%files
%doc debian/copyright debian/changelog
%{_bindir}/ukui-system-monitor
%{_datadir}/applications/ukui-system-monitor.desktop
