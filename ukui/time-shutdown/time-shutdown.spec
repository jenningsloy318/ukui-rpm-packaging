Name:           time-shutdown 
Version:        1.1.0
Release:        1%{?dist}
Summary:        The time-shutdown is mainly used in the desktop operating system


License:         GPL-3.0 License
URL:            https://github.com/ukui/ukui-menu
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  glib2-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  libX11-devel
Requires:  gsettings-qt
Requires:  libX11
Requires:  ukui-notification-daemon

%description
 The time-shutdown is mainly used in the desktop operating system.
 Timed shutdown program The shutdown frequency can be selected. 
 When the time is set, the shutdown interface will be triggered 
 and a notification popup will be sent. You can select, postpone and set.

%prep
%setup -q
sed -i 's|/lib/ukui-notification-daemon|/lib64/ukui-notification-daemon|g' time-shutdown.pro
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
%{_bindir}/*
%{_datadir}/glib-2.0/schemas/org.ukui.time.shutdown.settings.gschema.xml
%{_datadir}/ukui-time-shutdown/time-shutdown_zh_CN.qm
