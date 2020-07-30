# disable debug package
%define debug_package %{nil}

Name:           ukui-wallpapers
Version:        master
Release:        1%{?dist}
Summary:        Wallpapers for UKUI desktop environment


License:        Creative Commons Attribution-ShareAlike 3.0 Unported License
URL:            https://github.com/ukui/ukui-wallpapers
Source0:        %{name}-%{version}.tar.gz

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

%{meson} 
%{meson_build}


%install
%{meson_install}


%files
%doc debian/copyright debian/changelog
%{_datadir}/backgrounds/*
%{_datadir}/locale/bo/LC_MESSAGES/ukui-wallpapers.mo
%{_datadir}/locale/tr/LC_MESSAGES/ukui-wallpapers.mo
%{_datadir}/locale/zh_CN/LC_MESSAGES/ukui-wallpapers.mo
%{_datadir}/locale/zh_TW/LC_MESSAGES/ukui-wallpapers.mo
%{_datadir}/ukui-background-properties/