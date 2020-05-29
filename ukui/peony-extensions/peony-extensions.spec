# enable download source
%undefine _disable_source_fetch

Name:           peony-extensions
Version:        2.0.2
Release:        1%{?dist}
Summary:        Peony qt extensions (common files)



License:        GPLv2+
URL:            https://github.com/ukui/ukui-session-manager
Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:       lib-path.patch

BuildArch:      x86_64

BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtx11extras-devel

BuildRequires:  glib2-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  poppler-qt5-devel
BuildRequires:  peony-devel

Requires:  peony-extensions-parchives
Requires:  peony-extensions-share 
Requires:  peony-extensions-open-terminal


%description
 Peony is the official file manager for the UKUI desktop. This
 package adds extended functionality to the Peony file manager.


%package share
Summary: Allows one to quickly share a folder from the Peony file manager

Requires:  peony-libs
Requires:  samba
Requires:  samba-common
Requires:  samba-common-tools
%description share
 Peony is the official file manager for the UKUI desktop. This
 package adds extended functionality to the Peony file manager.
 .
 The Peony share extension allows you to quickly share a folder from the
 Peony file manager without requiring root access. It uses Samba, so your
 folders can be accessed by any operating system.


%package parchives
Summary: Peony qt plugin for file compress and uncompress
Requires:  peony-libs
Requires:  engrampa

%description parchives
 Parchives is an archive manager for the UKUI environment. You can use
 this plugin to compress or uncompress file or folder.
 .
 This package adds extended functionality to the Peony file manager.

%package open-terminal
Summary: Peony plugin for opening terminals in arbitrary local paths
Requires:  peony-libs
Requires:  mate-terminal

%description open-terminal
 Peony is the official file manager for the UKUI desktop. This
 package adds extended functionality to the Peony file manager.
 .
 peony-open-terminal is a proof-of-concept Peony extension
 which allows you to open a terminal in arbitrary local folders.



%prep
%setup -q
cp %{SOURCE1} .
patch -p0 < lib-path.patch

%build
%{cmake3} .
%{make_build}
# CMakeLists.txt DON'T contain install clause
%install
rm -rf $RPM_BUILD_ROOT

mkdir -p %{buildroot}/usr/share/doc/peony-extensions/  %{buildroot}/usr/lib64/peony-qt-extensions 
cp testdir/libpeony-qt-engrampa-menu-plugin.so  testdir/libpeony-qt-menu-plugin-mate-terminal.so  peony-extensions-cmake/peony-qt-share/libpeony-qt-share.so %{buildroot}/usr/lib64/peony-qt-extensions
cp debian/copyright  %{buildroot}/usr/share/doc/peony-extensions/copyright
gzip  debian/changelog > %{buildroot}/usr/share/doc/peony-extensions/changelog.gz

%files
%{_datadir}/doc/peony-extensions/

%files  share
%{_libdir}/peony-qt-extensions/libpeony-qt-share.so

%files  parchives
%{_libdir}/peony-qt-extensions/libpeony-qt-engrampa-menu-plugin.so


%files open-terminal
%{_libdir}/peony-qt-extensions/libpeony-qt-menu-plugin-mate-terminal.so

%post share

[ -d /var/lib/samba/usershares  ] || mkdir /var/lib/samba/usershares 
sed -i '/^\[global/a \\tusershare allow guests = yes\n\tusershare path = /var/lib/samba/usershares\n\tusershare max shares = 100\n\tusershare owner only = yes' /etc/samba/smb.conf
systemctl restart smb
systemctl restart nmb
systemctl enable smb
systemctl enable nmb

%preun share
sed -i '/usershare/d' /etc/samba/smb.conf
systemctl restart smb
systemctl restart nmb