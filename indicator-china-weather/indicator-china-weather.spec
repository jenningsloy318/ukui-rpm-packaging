Name:           indicator-china-weather
Version:        master
Release:        1%{?dist}
Summary:        Indicator that displays China weather information



License:         GPL-3.0 License
URL:            https://github.com/ukui/kylin-display-switch
# %%Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0:        https://github.com/UbuntuKylin/%{name}/archive/%{version}.zip#/%{name}-%{version}.zip

BuildArch:      x86_64

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qttools-devel
BuildRequires: GeoIP-devel


%description
  Kylin Weather displays detail weather information for one place,
 including weather forecast and observe weather, and you can
 change it.


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
mkdir -p %{buildroot}/usr/share/man/man1/
gzip -c man/indicator-china-weather.1	 > %{buildroot}/usr/share/man/man1/indicator-china-weather.1.gz


%files
%doc debian/copyright debian/changelog
%{_mandir}/man1/indicator-china-weather.1.gz
%{_sysconfdir}/xdg/autostart/indicator-china-weather.desktop
%{_bindir}/indicator-china-weather
%{_datadir}/applications/indicator-china-weather.desktop
%{_datadir}/indicator-china-weather/