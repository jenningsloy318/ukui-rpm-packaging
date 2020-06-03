# enable download source
%undefine _disable_source_fetch

Name:           ukui-greeter
Version:        1.2.5
Release:        1%{?dist}
Summary:        Lightdm greeter for UKUI


License:        GPLv2+
URL:            https://github.com/ukui/ukui-greeter
Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      x86_64


BuildRequires: qt5-qtbase-devel
BuildRequires: qt5-qtx11extras-devel
BuildRequires: qt5-qtsvg-devel
BuildRequires: lightdm-qt5-devel
BuildRequires: libX11-devel
BuildRequires: libXtst-devel
BuildRequires: libXrandr-devel
BuildRequires: qt5-qttools-devel
BuildRequires: imlib2-devel

Requires: lightdm

Provides: lightdm-greeter

%description
 A greeter for UKUI desktop environment written by Qt5.
 The greeter supports biometric authentication which is
 provided by biometric-authentication service.



%prep

%setup -q
 
%build
  %{qmake_qt5} %{_qt5_qmake_flags} CONFIG+=enable-by-default  ukui-greeter.pro	
make
%install
rm -rf %{buildroot}
%{make_install}  INSTALL_ROOT=%{buildroot} 
mkdir -p %{buildroot}/usr/share/doc/ukui-greeter/   %{buildroot}/usr/share/man/man8/
cp debian/copyright  %{buildroot}/usr/share/doc/ukui-greeter/
gzip -c  debian/changelog > %{buildroot}/usr/share/doc/ukui-greeter/changelog.gz
gzip -c ukui-greeter/man/ukui-greeter.8 > %{buildroot}/usr/share/man/man8/ukui-greeter.8.gz

%files
%{_sysconfdir}/lightdm/ukui-greeter.conf
%{_datadir}/doc/ukui-greeter/
%{_datadir}/man/man8/ukui-greeter.8.gz
%{_sbindir}/ukui-greeter
%{_datadir}/lightdm/lightdm.conf.d/95-ukui-greeter.conf
%{_datadir}/ukui-greeter/images/arrow_left.png
%{_datadir}/ukui-greeter/images/arrow_left_active.png
%{_datadir}/ukui-greeter/images/arrow_left_prelight.png
%{_datadir}/ukui-greeter/images/arrow_right.png
%{_datadir}/ukui-greeter/images/background-ubuntu.png
%{_datadir}/ukui-greeter/images/badges/budgie_badge.png
%{_datadir}/ukui-greeter/images/badges/gnome_badge.png
%{_datadir}/ukui-greeter/images/badges/kde_badge.png
%{_datadir}/ukui-greeter/images/badges/lubuntu_badge.png
%{_datadir}/ukui-greeter/images/badges/mate_badge.png
%{_datadir}/ukui-greeter/images/badges/pantheon_badge.png
%{_datadir}/ukui-greeter/images/badges/plasma_badge.png
%{_datadir}/ukui-greeter/images/badges/ubuntu_badge.png
%{_datadir}/ukui-greeter/images/badges/ukui_badge.png
%{_datadir}/ukui-greeter/images/badges/unknown_badge.png
%{_datadir}/ukui-greeter/images/badges/xfce_badge.png
%{_datadir}/ukui-greeter/images/badges/xubuntu_badge.png
%{_datadir}/ukui-greeter/images/capslock.png
%{_datadir}/ukui-greeter/images/cof.png
%{_datadir}/ukui-greeter/images/combobox_down.png
%{_datadir}/ukui-greeter/images/default_face.png
%{_datadir}/ukui-greeter/images/dialog_close.png
%{_datadir}/ukui-greeter/images/dialog_close_highlight.png
%{_datadir}/ukui-greeter/images/dialog_close_press.png
%{_datadir}/ukui-greeter/images/hibernate.png
%{_datadir}/ukui-greeter/images/hibernate_highlight.png
%{_datadir}/ukui-greeter/images/hide-password.png
%{_datadir}/ukui-greeter/images/is_logined.png
%{_datadir}/ukui-greeter/images/keyboard.png
%{_datadir}/ukui-greeter/images/login-button.png
%{_datadir}/ukui-greeter/images/next.png
%{_datadir}/ukui-greeter/images/power.png
%{_datadir}/ukui-greeter/images/prev.png
%{_datadir}/ukui-greeter/images/restart.png
%{_datadir}/ukui-greeter/images/restart_highlight.png
%{_datadir}/ukui-greeter/images/scrollbar_down.png
%{_datadir}/ukui-greeter/images/scrollbar_down_clicked.png
%{_datadir}/ukui-greeter/images/scrollbar_down_hover.png
%{_datadir}/ukui-greeter/images/scrollbar_up.png
%{_datadir}/ukui-greeter/images/scrollbar_up_clicked.png
%{_datadir}/ukui-greeter/images/scrollbar_up_hover.png
%{_datadir}/ukui-greeter/images/show-password.png
%{_datadir}/ukui-greeter/images/shutdown.png
%{_datadir}/ukui-greeter/images/shutdown_highlight.png
%{_datadir}/ukui-greeter/images/suspend.png
%{_datadir}/ukui-greeter/images/suspend_highlight.png
%{_datadir}/ukui-greeter/images/waiting.png
%{_datadir}/xgreeters/ukui-greeter.desktop