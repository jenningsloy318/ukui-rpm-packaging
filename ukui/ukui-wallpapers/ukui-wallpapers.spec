# enable download source
%undefine _disable_source_fetch
%define debug_package %{nil}

Name:           ukui-wallpapers
Version:        20.04.2
Release:        1%{?dist}
Summary:        Wallpapers for UKUI desktop environment


License:        GPLv2+
URL:            https://github.com/ukui/ukui-wallpapers
Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      x86_64
BuildRequires:  ninja-build
BuildRequires:  meson
%description
 The default UKUI wallpaper. Outstanding wallpapers selected
 from Ubuntu Kylin 20.04 Wallpaper Contest. These wallpapers
 are expected to show wonderful Chinese style.



%prep

%setup -q
 
%build
meson build --buildtype debugoptimized --prefix=/usr
ninja -C build

%install
rm -rf %{buildroot}

DESTDIR=%{buildroot}  ninja -C build install  
mkdir -p %{buildroot}/usr/share/doc/ukui-wallpapers/
cp debian/copyright  %{buildroot}/usr/share/doc/ukui-wallpapers/
gzip  debian/changelog > %{buildroot}/usr/share/doc/ukui-wallpapers/changelog.gz


%files

%{_datadir}/backgrounds/calla.png
%{_datadir}/backgrounds/city.png
%{_datadir}/backgrounds/default.jpg
%{_datadir}/backgrounds/desert.png
%{_datadir}/backgrounds/firstgeneration.jpg
%{_datadir}/backgrounds/fluent-color.png
%{_datadir}/backgrounds/focal-ubuntukylin.png
%{_datadir}/backgrounds/goldfish.png
%{_datadir}/backgrounds/rhythm.jpg
%{_datadir}/backgrounds/rollpaper.png
%{_datadir}/backgrounds/string.jpg
%{_datadir}/backgrounds/the-mouse.jpg
%{_datadir}/doc/ukui-wallpapers/changelog.gz
%{_datadir}/doc/ukui-wallpapers/copyright
%{_datadir}/locale/bo/LC_MESSAGES/ukui-wallpapers.mo
%{_datadir}/locale/tr/LC_MESSAGES/ukui-wallpapers.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/ukui-wallpapers.mo
%{_datadir}/locale/zh_TW/LC_MESSAGES/ukui-wallpapers.mo
%{_datadir}/ukui-background-properties/