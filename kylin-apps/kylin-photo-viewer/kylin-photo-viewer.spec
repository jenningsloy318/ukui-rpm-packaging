Name:           kylin-photo-viewer
Version:        1.0.0
Release:        1%{?dist}
Summary:        kylin-photo-viewer



License:        GPL-3.0 License
URL:            https://github.com/ukui/kylin-video
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  qt5-linguist
BuildRequires:  qt5-qtbase-private-devel
BuildRequires:  qt5-qtx11extras-devel
BuildRequires:  qt5-qtsvg-devel

BuildRequires:  opencv-devel
BuildRequires:  kf5-kwindowsystem-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  pkgconf
BuildRequires:  giflib-devel


%description
kylin-photo-viewer


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
