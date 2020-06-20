FROM docker.io/library/fedora:32

RUN  sed -i '/metalink/s/$/\&country=cn/g' /etc/yum.repos.d/*.repo && \
      dnf update -y && \
      dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  SAASound-devel dbusmenu-qt5-devel glib2-devel libicu-devel kf5-solid-devel kf5-kwindowsystem-devel pulseaudio-libs-devel pulseaudio-qt-devel qt5-qtsvg-devel qt5-qtx11extras-devel lm_sensors-devel libstatgrab-devel libX11-devel libxcb-devel xcb-util-devel xcb-util-keysyms-devel xcb-util-image-devel libXcomposite-devel libXdamage-devel libxkbcommon-devel libxkbcommon-x11-devel libXrandr-devel qt5-qtwebkit-devel libqtxdg-devel qt5-qttools-devel gsettings-qt-devel dconf-devel qt5-qtbase-devel qt5-qtbase-private-devel     && \
      strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5
