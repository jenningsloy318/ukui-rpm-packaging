Name:           ukui-sidebar
Version:        master
Release:        1%{?dist}
Summary:        parallels toolbox for UKUI


License:         GPL-3.0 License
URL:            https://github.com/ukui/ukui-sidebar
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  glib2-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  dconf-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  kf5-kwindowsystem-devel

%description
The ukui-sidebar is mainly used in the desktop operating system.
The ukui-sidebar is mainly used in the desktop operating system.
It pops up from the right side of the desktop in the form of a tray,
displaying some application notification messages and some cutting
storage information.

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
%doc debian/copyright debian/changelog
%{_sysconfdir}/xdg/autostart/ukui-sidebar.desktop
%{_bindir}/*
%{_libdir}/ukui-sidebar
%{_datadir}/ukui-sidebar-notification
%{_datadir}/applications/*
%{_datadir}/ukui-clock/