Name:           kylin-scanner
Version:        1.0.0
Release:        1%{?dist}
Summary:        Kylin Scanner is an interface-friendly scanning software developed with Qt5


License:        GPL-3.0 License
URL:            https://github.com/ukui/kylin-nm
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64

BuildRequires: glib2-devel
BuildRequires: leptonica-devel
BuildRequires: opencv-devel
BuildRequires: libinsane
BuildRequires: libksane-devel
BuildRequires: sane-backends-devel
BuildRequires: tesseract-devel
BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qttools-devel
BuildRequires: tesseract-tools
BuildRequires: tesseract


Requires: tesseract
Requires: sane-backends
Requires: opencv-core

%description
Kylin Scanner is an interface-friendly scanning software developed with Qt5. The software can scan according to the resolution, size and color mode of the scanning device itself. At the same time, It Increases post-processing of scanned pictures, including one-click beautification, intelligent correction and text recognition. Other image processing tips can also be reflected in this software, such as clipping, rotation, etc.




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
%{_datadir}/applications/kylin-scanner.desktop
%{_datadir}/kylin-scanner/translations/kylin-scanner.zh_CN.qm
%{_datadir}/pixmaps/scanner.png
