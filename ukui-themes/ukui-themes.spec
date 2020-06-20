# enable download source
%undefine _disable_source_fetch
%define debug_package %{nil}

Name:           ukui-themes
Version:        master
Release:        1%{?dist}
Summary:        Official themes for the UKUI desktop


License:        GPLv2+
URL:            https://github.com/ukui/ukui-themes
#Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0:        https://github.com/ukui/%{name}/archive/%{version}.zip#/%{name}-%{version}.zip

BuildArch:      x86_64
BuildRequires: rubygem-sass

%description
 This package contains the official desktop themes of the UKUI desktop
 environment.


%prep

%setup -q
 
%build
%{make_build}

%install
%{make_install}  INSTALL_ROOT=%{buildroot} 
mkdir -p  %{buildroot}/usr/share/mime/packages/ %{buildroot}/usr/share/glib-2.0/schemas/  %{buildroot}/usr/share/icons/
install -m 644 ukui-custom.xml	%{buildroot}/usr/share/mime/packages/ukui-custom.xml
install -m 644 debian/25_ukui-themes.gschema.override %{buildroot}/usr/share/glib-2.0/schemas/25_ukui-themes.gschema.override
cp -r  ukui-icon-theme-basic %{buildroot}/usr/share/icons/
cp -r  ukui-icon-theme-classical %{buildroot}/usr/share/icons/
cp -r  ukui-icon-theme-default %{buildroot}/usr/share/icons/

%files
%doc debian/changelog  debian/copyright
%{_datadir}/mime/packages/ukui-custom.xml
%{_datadir}/glib-2.0/schemas/25_ukui-themes.gschema.override
%{_datadir}/icons/ukui-icon-theme-basic
%{_datadir}/icons/ukui-icon-theme-classical
%{_datadir}/icons/ukui-icon-theme-default
%{_datadir}/themes/ukui-black
%{_datadir}/themes/ukui-white


%post 
gsettings set org.ukui.style icon-theme-name  ukui-icon-theme-default