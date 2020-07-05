Name:           kylin-nm
Version:        master
Release:        1%{?dist}
Summary:        Gui Applet tool for display and edit network simply


License:        GPL-3.0 License
URL:            https://github.com/ukui/kylin-nm
# %%Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0:        https://github.com/ukui/%{name}/archive/%{version}.zip#/%{name}-%{version}.zip

BuildArch:      x86_64
BuildRequires:  qt5-qtbase-devel

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
mkdir qmake-build
pushd qmake-build
%{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  ..
%{make_build}
popd 

%install
pushd qmake-build
%{make_install}  INSTALL_ROOT=%{buildroot} 
popd 
mkdir -p %{buildroot}/usr/share/man/man1/
gzip -c man/kylin-nm.1	 > %{buildroot}/usr/share/man/man1/kylin-nm.1.gz

%files
%doc debian/changelog  debian/copyright
%{_sysconfdir}/xdg/autostart/kylin-nm.desktop
%{_bindir}/kylin-nm
%{_mandir}/man1/kylin-nm.1.gz
