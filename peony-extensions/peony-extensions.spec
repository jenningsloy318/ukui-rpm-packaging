Name:           peony-extensions
Version:        master
Release:        1%{?dist}
Summary:        Peony qt extensions (common files)



License:        LGPL-3.0 License
URL:            https://github.com/ukui/peony-extensions
# %%Source0:        https://github.com/ukui/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source0:        https://github.com/ukui/%{name}/archive/%{version}.zip#/%{name}-%{version}.zip

Patch0:        peony-extensions-libdir-and-qmake.patch

BuildArch:      x86_64

BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtx11extras-devel

BuildRequires:  glib2-devel
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qttools-devel
BuildRequires:  poppler-qt5-devel
BuildRequires:  peony-devel
BuildRequires:  gsettings-qt-devel

Requires:  peony-share 
Requires:  peony-parchives
Requires:  peony-open-terminal
Requires:  peony-set-wallpaper
Requires:  peony-computer-view

%description
 Peony is the official file manager for the UKUI desktop. This
 package adds extended functionality to the Peony file manager.


%package -n peony-share
Summary: Allows one to quickly share a folder from the Peony file manager

Requires:  peony-libs
Requires:  samba
Requires:  samba-common
Requires:  samba-common-tools
%description -n peony-share
 Peony is the official file manager for the UKUI desktop. This
 package adds extended functionality to the Peony file manager.
 .
 The Peony share extension allows you to quickly share a folder from the
 Peony file manager without requiring root access. It uses Samba, so your
 folders can be accessed by any operating system.


%package -n peony-parchives
Summary: Peony qt plugin for file compress and uncompress
Requires:  peony-libs
Requires:  engrampa

%description -n peony-parchives
 Parchives is an archive manager for the UKUI environment. You can use
 this plugin to compress or uncompress file or folder.
 .
 This package adds extended functionality to the Peony file manager.

%package -n peony-open-terminal
Summary: Peony plugin for opening terminals in arbitrary local paths
Requires:  peony-libs
Requires:  mate-terminal

%description -n peony-open-terminal
 Peony is the official file manager for the UKUI desktop. This
 package adds extended functionality to the Peony file manager.
 .
 peony-open-terminal is a proof-of-concept Peony extension
 which allows you to open a terminal in arbitrary local folders.

%package -n peony-set-wallpaper
Summary: Peony plugin for right click a picture to set as wallpaper.
Requires:  peony-libs

%description -n peony-set-wallpaper
Description: Peony plugin for right click a picture to set as wallpaper.
 Peony is the official file manager for the UKUI desktop. This
 package adds extended functionality to the Peony file manager.
 .
 In addition to set wallpaper in ukui-control-center, you can select a 
 picture and right click to quickly set as wallpaper.


%package -n peony-computer-view
Summary: Peony plugin for displaying computer:/// with more information.
Requires:  peony-libs

%description -n peony-computer-view

 Peony is the official file manager for the UKUI desktop. This
 package adds extended functionality to the Peony file manager.
 .
 peony-extionsion-computer-view is a proof-of-concept Peony extension
 which allows user browsering computer:/// with more information, which
 not provided in icon view and list view.


%prep
%setup -q
%patch0 -p0

%build
mkdir cmake-build
pushd cmake-build
%cmake3 ..
make
popd
%install
mkdir -p  %{buildroot}/usr/lib64/peony-qt-extensions 
cp testdir/{libpeony-qt-computer-view-plugin.so,libpeony-qt-engrampa-menu-plugin.so,libpeony-qt-menu-plugin-mate-terminal.so,libpeony-qt-set-wallpaper.so} %{buildroot}/usr/lib64/peony-qt-extensions
cp peony-extensions-cmake/peony-qt-share/libpeony-qt-share.so  %{buildroot}/usr/lib64/peony-qt-extensions


%files
%doc debian/copyright  debian/changelog

%files  -n peony-share
%{_libdir}/peony-qt-extensions/libpeony-qt-share.so

%files  -n peony-parchives
%{_libdir}/peony-qt-extensions/libpeony-qt-engrampa-menu-plugin.so


%files -n peony-open-terminal
%{_libdir}/peony-qt-extensions/libpeony-qt-menu-plugin-mate-terminal.so


%files -n peony-set-wallpaper
%{_libdir}/peony-qt-extensions/libpeony-qt-set-wallpaper.so

%files -n peony-computer-view
%{_libdir}/peony-qt-extensions/libpeony-qt-computer-view-plugin.so

%post -n peony-share

[ -d /var/lib/samba/usershares  ] || mkdir /var/lib/samba/usershares 
sed -i '/^\[global/a \\tusershare allow guests = yes\n\tusershare path = /var/lib/samba/usershares\n\tusershare max shares = 100\n\tusershare owner only = yes' /etc/samba/smb.conf
systemctl restart smb
systemctl restart nmb
systemctl enable smb
systemctl enable nmb

%preun -n peony-share
sed -i '/usershare/d' /etc/samba/smb.conf
systemctl restart smb
systemctl restart nmb
