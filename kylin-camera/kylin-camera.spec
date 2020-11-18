Name:           kylin-camera
Version:        1.0.2
Release:        1%{?dist}
Summary:        kylin-camera


License:        GPL-3.0 License
URL:            https://github.com/UbuntuKylin/kylin-camera
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64

BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qttools-devel
BuildRequires: qt5-qtmultimedia-devel
BuildRequires: qt5-qtscript-devel


%description
kylin-camera




%prep

%setup -q
 
%build
export PATH=%{_qt5_bindir}:$PATH

%{qmake_qt5} 
%{make_build}

%install
%{make_install} INSTALL_ROOT=%{buildroot}

%files
%doc debian/changelog
%license  debian/copyright 
%{_bindir}/*
%{_datadir}/applications/kylin-camera.desktop
