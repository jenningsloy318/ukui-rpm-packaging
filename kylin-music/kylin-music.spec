Name:           kylin-music
Version:        1.0.0
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



%description
kylin-music


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

%files
%doc debian/changelog
%license  debian/copyright 
%{_bindir}/kylin-music
%{_datadir}/applications/kylin-music.desktop
%{_datadir}/pixmaps/kylin-music.png
