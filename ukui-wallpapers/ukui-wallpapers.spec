# disable debug package
%define debug_package %{nil}

Name:           ukui-wallpapers
Version:        20.04.2
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
%find_lang %name

%files -f %name.lang
%doc debian/changelog
%license  debian/copyright
%{_datadir}/backgrounds/*
%{_datadir}/ukui-background-properties/
