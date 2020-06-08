# enable download source
%undefine _disable_source_fetch

Name:           ukui-sidebar
Version:        master
Release:        1%{?dist}
Summary:        parallels toolbox for UKUI


License:        GPLv2+
URL:            https://github.com/ukui/ukui-session-manager
#Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0:        https://github.com/ukui/ukui-sidebar/archive/master.zip#/%{name}-%{version}.zip
Source1:        ukui-sidebar-plugin-libdir.patch

BuildArch:      x86_64
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  glib2-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  dconf-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  qt5-qtmultimedia-devel

%description
The ukui-sidebar is mainly used in the desktop operating system.
The ukui-sidebar is mainly used in the desktop operating system.
It pops up from the right side of the desktop in the form of a tray,
displaying some application notification messages and some cutting
storage information.

%prep

%setup -q
cp %{SOURCE1} .
patch -p0 < ukui-sidebar-plugin-libdir.patch
 
%build
  %{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  ukui-sidebar.pro
  make

%install
rm -rf %{buildroot}
%{make_install}  INSTALL_ROOT=%{buildroot} 
mkdir -p %{buildroot}/usr/share/doc/ukui-sidebar/
cp debian/copyright  %{buildroot}/usr/share/doc/ukui-sidebar/
gzip -c  debian/changelog > %{buildroot}/usr/share/doc/ukui-sidebar/changelog.gz

%files
%{_sysconfdir}/xdg/autostart/ukui-sidebar.desktop
%{_bindir}/*
%{_libdir}/ukui-sidebar
%{_datadir}/ukui-sidebar-notification
%{_datadir}/doc/ukui-sidebar/
%{_datadir}/applications/*