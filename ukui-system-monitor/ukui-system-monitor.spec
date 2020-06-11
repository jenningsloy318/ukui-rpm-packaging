# enable download source
%undefine _disable_source_fetch

Name:           ukui-system-monitor
Version:        master
Release:        1%{?dist}
Summary:         simple system monitor written in QT




License:        GPLv2+
URL:            https://github.com/ukui/ukui-system-monitor
#Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0:        https://github.com/ukui/%{name}/archive/master.zip#/%{name}-%{version}.zip
Patch0:        ukui-system-monitor-qmake-path.patch
BuildArch:      x86_64



BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  glib2-devel
BuildRequires:  libgtop2-devel
BuildRequires:  systemd-devel

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
%patch0 -p0

%build
  %{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  ukui-system-monitor.pro		
  %{make_build}
%install
rm -rf %{buildroot}
%{make_install}  INSTALL_ROOT=%{buildroot} 
mkdir -p %{buildroot}/usr/share/doc/ukui-system-monitor/
cp debian/copyright  %{buildroot}/usr/share/doc/ukui-system-monitor/
gzip -c  debian/changelog > %{buildroot}/usr/share/doc/ukui-system-monitor/changelog.gz

%files
%{_bindir}/ukui-system-monitor
%{_datadir}/applications/ukui-system-monitor.desktop
%{_datadir}/doc/ukui-system-monitor