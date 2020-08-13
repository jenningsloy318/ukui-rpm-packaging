Name:           kylin-video
Version:        2.1.0
Release:        1%{?dist}
Summary:        Front-end for MPlayer and MPV



License:        GPL-3.0 License
URL:            https://github.com/ukui/kylin-video
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64
BuildRequires:  qt5-qtbase-devel
BuildRequires: qt5-qtscript-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-private-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: zlib-devel
BuildRequires: libX11-devel
BuildRequires: libcrystalhd-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: libXext-devel

Requires: (mpv or mplayer)
Requires: mesa-vdpau-drivers
Requires: libcrystalhd
Recommends: crystalhd-firmware


%description
 Qt5 Mplayer and MPV front-end, with basic features like playing
 videos and audios to more advanced features.
 It supports both x86 and ARM platform, and supports most of the
 audio and video formats.



%prep

%setup -q
%build

export PATH=%{_qt5_bindir}:$PATH
mkdir qmake-build
pushd qmake-build
%if 0%{?rhel} == 8
if ! grep -q "qm_files.CONFIG" /usr/lib64/qt5/mkspecs/features/lrelease.prf; then 
sed -i '/qm_files.path/a qm_files.CONFIG = no_check_exist'  /usr/lib64/qt5/mkspecs/features/lrelease.prf
fi
%endif
%{qmake_qt5} ..
%{make_build}
popd 

%install
pushd qmake-build
%{make_install} INSTALL_ROOT=%{buildroot}
popd 
install -d %{buildroot}/usr/share/man/man1/
gzip -c man/kylin-video.1	 > %{buildroot}/usr/share/man/man1/kylin-video.1.gz

%files
%doc debian/changelog
%license  debian/copyright 
%{_bindir}/kylin-video
%{_mandir}/man1/kylin-video.1.gz
%{_datadir}/applications/kylin-video.desktop
%{_datadir}/kylin-video/translations/
%{_datadir}/pixmaps/kylin-video.png
