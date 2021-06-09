Name:           kylin-music
Version:        1.0.4
Release:        1%{?dist}
Summary:        kylin-music



License:        GPL-3.0 License
URL:            https://github.com/UbuntuKylin/kylin-music
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  zlib-devel
BuildRequires:  libX11-devel
BuildRequires:  libcrystalhd-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  libXext-devel
BuildRequires:  taglib-devel
BuildRequires:  qt5-qtmultimedia-devel


%description
kylin-music


%prep

%setup -q
%build

export PATH=%{_qt5_bindir}:$PATH
sed -i 's|/usr/lib/libtag.so|/usr/lib64/libtag.so|g' kylin-music.pro
sed -i 's|/usr/lib/libtag_c.so|/usr/lib64/libtag_c.so|g' kylin-music.pro

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
%{_bindir}/kylin-music
%{_datadir}/applications/kylin-music.desktop
%{_datadir}/glib-2.0/schemas/org.kylin-music-data.gschema.xml
%{_datadir}/pixmaps/kylin-music.png
