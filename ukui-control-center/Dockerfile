FROM docker.io/library/fedora:32

RUN  sed -i '/metalink/s/$/\&country=cn/g' /etc/yum.repos.d/*.repo && \
      dnf update -y && \
      dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros qt5-qtbase-devel qt5-qtsvg-devel gsettings-qt-devel glib2-devel qt5-qtx11extras-devel libmatekbd-devel libxklavier-devel kf5-kconfigwidgets-devel kf5-kconfig-devel qt5-qtdeclarative-devel dconf-devel redshift edid-decode libmatemixer-devel libqtxdg-devel qt5-qtmultimedia-devel libxml2-devel libkscreen-qt5-devel kf5-ki18n-devel && \
      strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5
