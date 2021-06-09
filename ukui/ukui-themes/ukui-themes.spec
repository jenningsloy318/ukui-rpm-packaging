# disable debug package
%define debug_package %{nil}

Name:           ukui-themes
Version:        1.4.1
Release:        1%{?dist}
Summary:        Official themes for the UKUI desktop


License:        GPL-3.0 License
URL:            https://github.com/ukui/ukui-themes
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      x86_64

BuildRequires: meson


%description
 This package contains the official desktop themes of the UKUI desktop
 environment.


%prep

%setup -q



%build

%{meson}
%{meson_build}

%install
%{meson_install}

%files
%doc debian/changelog
%license  debian/copyright
%{_datadir}/mime/packages/ukui-custom.xml
%{_datadir}/glib-2.0/schemas/25_ukui-themes.gschema.override
%{_datadir}/icons/*
%exclude %{_datadir}/themes/meson.build
%{_datadir}/themes/ukui
%{_datadir}/themes/ukui-black
%{_datadir}/themes/ukui-white
%{_datadir}/themes/ukui-light
%{_datadir}/themes/ukui-dark

%post
gsettings set org.ukui.style icon-theme-name ukui