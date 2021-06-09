Name:           kylin-recorder
Version:        1.2.0
Release:        1%{?dist}
Summary:        kylin-recorder



License:        GPL-3.0 License
URL:            https://github.com/UbuntuKylin/kylin-recorder
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtscript-devel
BuildRequires: qt5-qttools-devel
BuildRequires: qt5-linguist
BuildRequires: qt5-qtbase-private-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: zlib-devel
BuildRequires: libX11-devel
BuildRequires: libcrystalhd-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: libXext-devel
BuildRequires: lame-devel
BuildRequires: gsettings-qt-devel
BuildRequires: qt5-qtmultimedia-devel

%description
kylin-recording

%prep

%setup -q
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
%{_bindir}/kylin-recorder
%{_datadir}/applications/kylin-recorder.desktop
%{_datadir}/pixmaps/recording_128.svg 
%{_datadir}/glib-2.0/schemas/*
%{_datadir}/kylin-recorder/translations/*
