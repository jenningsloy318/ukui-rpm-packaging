Name:           kylin-screenshot
Version:        1.0.0
Release:        1%{?dist}
Summary:        kylin-screenshot is a powerful yet simple-to-use screenshot software.


License:        GPL-3.0 License
URL:            https://github.com/ukui/kylin-nm
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qttools-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: ffmpeg-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: libXfixes-devel
BuildRequires: libX11-devel
BuildRequires: libXinerama-devel
BuildRequires: qt5-linguist
BuildRequires: alsa-lib-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libX11-devel
BuildRequires: libXext-devel

Requires: qt5-qtsvg

%description
 kylin-screenshot is a powerful yet simple-to-use screenshot software.





%prep

%setup -q

%build
export PATH=%{_qt5_bindir}:$PATH
export CPATH=/usr/include/ffmpeg
mkdir qmake-build
pushd qmake-build
%{qmake_qt5} CONFIG+=packaging ..
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
%{_datadir}/applications/kylinscreenshot.desktop
%{_datadir}/dbus-1/services/org.dharkael.kylinscreenshot.service
%{_datadir}/dbus-1/interfaces/org.dharkael.kylinscreenshot.xml
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_datadir}/icons/hicolor/*/apps/kylin_screenshot.png
%{_datadir}/icons/hicolor/*/apps/kylin_screenshot.svg
%{_datadir}/metainfo/kylinscreenshot.appdata.xml
