# disable debug package
%define debug_package %{nil}

Name:           ukui-themes
Version:        1.4.0
Release:        1%{?dist}
Summary:        Official themes for the UKUI desktop


License:        GPL-3.0 License
URL:            https://github.com/ukui/ukui-themes
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildArch:      x86_64

BuildRequires: sassc


%description
 This package contains the official desktop themes of the UKUI desktop
 environment.


%prep

%setup -q
 
%build
%{make_build} SASS=sassc

%install
%{make_install} INSTALL_ROOT=%{buildroot}
install -d %{buildroot}/usr/share/mime/packages/ %{buildroot}/usr/share/glib-2.0/schemas/  %{buildroot}/usr/share/icons/
install -m 644 ukui-custom.xml	%{buildroot}/usr/share/mime/packages/ukui-custom.xml
install -m 644 debian/25_ukui-themes.gschema.override %{buildroot}/usr/share/glib-2.0/schemas/25_ukui-themes.gschema.override
cp -r  ukui-icon-theme-basic %{buildroot}/usr/share/icons/
cp -r  ukui-icon-theme-classical %{buildroot}/usr/share/icons/
cp -r  ukui-icon-theme-default %{buildroot}/usr/share/icons/

%files
%doc debian/changelog
%license  debian/copyright
%exclude %{_datadir}/icons/ukui-icon-theme-basic/16x16/devices/media-optical-audio.svg
%exclude %{_datadir}/icons/ukui-icon-theme-basic/16x16/devices/media-cdrom-audio.svg
%exclude %{_datadir}/icons/ukui-icon-theme-basic/16x16/devices/gnome-dev-disc-audio.svg
%exclude %{_datadir}/icons/ukui-icon-theme-basic/16x16/devices/gnome-dev-cdrom-audio.svg
%{_datadir}/mime/packages/ukui-custom.xml
%{_datadir}/glib-2.0/schemas/25_ukui-themes.gschema.override
%{_datadir}/icons/ukui-icon-theme-basic
%{_datadir}/icons/ukui-icon-theme-classical
%{_datadir}/icons/ukui-icon-theme-default
%{_datadir}/themes/ukui-black
%{_datadir}/themes/ukui-white


%post 
gsettings set org.ukui.style icon-theme-name  ukui-icon-theme-default
