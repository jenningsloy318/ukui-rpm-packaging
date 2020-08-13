Name:           indicator-china-weather
Version:        3.1.0
Release:        1%{?dist}
Summary:        Indicator that displays China weather information



License:         GPL-3.0 License
URL:            https://github.com/UbuntuKylin/indicator-china-weather
Source0:        %{name}-%{version}.tar.gz

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
%{qmake_qt5} ..
%{make_build}
popd 

%install
pushd qmake-build
%{make_install} INSTALL_ROOT=%{buildroot}
popd 
install -d %{buildroot}/usr/share/man/man1/
gzip -c man/indicator-china-weather.1	 > %{buildroot}/usr/share/man/man1/indicator-china-weather.1.gz


%files
%doc debian/changelog
%license  debian/copyright 
%{_mandir}/man1/indicator-china-weather.1.gz
%{_sysconfdir}/xdg/autostart/indicator-china-weather.desktop
%{_bindir}/indicator-china-weather
%{_datadir}/applications/indicator-china-weather.desktop
%{_datadir}/indicator-china-weather/
