Name:           ukui-system-monitor
Version:        1.0.0
Release:        1%{?dist}
Summary:        simple system monitor written in QT

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
