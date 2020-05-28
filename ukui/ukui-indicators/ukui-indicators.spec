# enable download source
%undefine _disable_source_fetch

Name:           ukui-indicators
Version:        1.1.8
Release:        1%{?dist}
Summary:        notification area use to show time, network, etc.


License:        GPLv2+
URL:            https://github.com/ukui/%{name}
Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      x86_64
BuildRequires:  webkit2gtk3-devel
BuildRequires:  libX11-devel
BuildRequires:  python3
BuildRequires:  libwnck3-devel
BuildRequires:  gobject-introspection-devel 

Requires: python3
Requires: gobject-introspection
Provides: ukui-indicators
Suggests: ukui-window-switch

%description
 A small applet to display information from various applications
 consistently in the panel.
 .
 The indicator applet exposes Ayatana Indicators in the UKUI Panel.
 Ayatana Indicators are an initiative by Canonical to provide crisp and
 clean system and application status indication. They take the form of an
 icon and associated menu, displayed (usually) in the desktop panel.
 Existing indicators include the Message Menu, Battery Menu and Sound
 menu.


%prep
%setup -q
./autogen.sh --prefix=/usr --sysconfdir=/etc --libdir=/usr/lib64 -enable-introspection --enable-compile-warnings=yes  --enable-egl-device     --enable-wayland        --enable-native-backend
%build
%{cmake3} .

make

%install
rm -rf $RPM_BUILD_ROOT
cd build 
%{make_install}  INSTALL_ROOT=%{buildroot} 
cd ..
mkdir -p %{buildroot}/usr/share/doc/ukui-indicators/ %{buildroot}/usr/share/man/man1/
cp debian/copyright  %{buildroot}/usr/share/doc/ukui-indicators/
gzip  debian/changelog > %{buildroot}/usr/share/doc/ukui-indicators/changelog.gz

%files
%{_bindir}
%{_sysconfdir}/xdg/autostart/
%{_mandir}/man1/diskstatusicon.1.gz
