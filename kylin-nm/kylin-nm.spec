# enable download source
%undefine _disable_source_fetch

Name:           kylin-nm
Version:        1.2.4
Release:        1%{?dist}
Summary:        Gui Applet tool for display and edit network simply


License:        GPLv2+
URL:            https://github.com/ukui/kylin-nm
Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      x86_64
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qtchooser
BuildRequires: qt5-qtscript-devel
BuildRequires:  qt5-qttools-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires:  gsettings-qt-devel
BuildRequires: kf5-kwindowsystem-devel

Requires: NetworkManager

%description
 Kylin NM is a Applet tool for managing network settings simply.
 It has beautiful UI and very comfortable to use.
 It's better work together with UKUI.


%prep

%setup -q
 
%build
  %{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  kylin-nm.pro	
  %{make_build}

%install
rm -rf %{buildroot}
%{make_install}  INSTALL_ROOT=%{buildroot} 
mkdir -p %{buildroot}/usr/share/doc/kylin-nm/ %{buildroot}/usr/share/man/man1/
cp debian/copyright  %{buildroot}/usr/share/doc/kylin-nm/
gzip -c  debian/changelog > %{buildroot}/usr/share/doc/kylin-nm/changelog.gz
gzip -c man/kylin-nm.1	 > %{buildroot}/usr/share/man/man1/kylin-nm.1.gz

%files
%{_sysconfdir}/xdg/autostart/kylin-nm.desktop
%{_bindir}/kylin-nm
%{_datadir}/doc/kylin-nm/changelog.gz
%{_datadir}/doc/kylin-nm/copyright
%{_mandir}/man1/kylin-nm.1.gz
