Name:           ukui-notification-daemon
Version:        1.0.0
Release:        1%{?dist}
Summary:        daemon to display passive popup notifications


License:         GPL-3.0 License
URL:            https://github.com/ukui/ukui-menu
Source0:        %{name}-%{version}.tar.gz

BuildArch:      x86_64

BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  dconf-devel
BuildRequires:  glib2-devel
BuildRequires:  gsettings-qt-devel
BuildRequires:  libX11-devel
Requires:  gsettings-qt
Requires:  libX11
Requires:  dconf
%description
daemon to display passive popup notifications
ukui-notification-daemon displays passive popup notifications, as per
the Desktop Notifications Specification.

The Desktop Notifications Specification provides a standard way of
doing passive popup notifications on the Linux desktop. These are
designed to notify the user of something without interrupting their
work with a dialog box that they must close.  Passive popups can
automatically disappear after a short period of time, as per the
Desktop Notifications spec.

%prep
%setup -q
sed -i 's|/lib/ukui-notification-daemon|/lib64/ukui-notification-daemon|g' ukui-notification-daemon.pro
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
%{_libdir}/ukui-notification-daemon/ukui-notifications
%{_datadir}/dbus-1/services/org.ukui.freedesktop.Notification.service
%{_datadir}/glib-2.0/schemas/org.ukui.notification.gschema.xml