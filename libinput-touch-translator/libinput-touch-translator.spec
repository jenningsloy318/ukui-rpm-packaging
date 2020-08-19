Name:           libinput-touch-translator
Version:        0.1
Release:        1%{?dist}
Summary:        Map actions in touch screen and touchpad to keyboard shortcuts or other input devices.


License:         GPL-3.0 License
URL:            https://github.com/UbuntuKylin/indicator-china-weather
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64

BuildRequires: libinput-devel
BuildRequires: libgudev-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: kf5-kxmlgui-devel

Requires: libinput
Requires: libgudev
Requires: qt5-qtbase
Requires: qt5-qtbase-gui
Requires: kf5-kxmlgui

%description
 Map actions in touch screen and touchpad to keyboard shortcuts or other input devices

%prep

%setup -q
sed -i 's|/lib/systemd/system|/usr/lib/systemd/system/|g' src/src.pro 
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
%{_unitdir}/libinput-touch-translator.service
%{_libexecdir}/libinput-touch-translator
