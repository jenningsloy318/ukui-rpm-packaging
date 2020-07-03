FROM docker.io/library/fedora:32

RUN  sed -i '/metalink/s/$/\&country=cn/g' /etc/yum.repos.d/*.repo && \
      dnf update -y && \
      dnf -y  intltool qt5-qtbase-devel libcanberra-devel gsettings-qt-devel glib2-devel gtk3-devel mate-desktop-devel libmatemixer-devel libxml2-devel mate-common qt5-qtsvg-devel qt5-qtmultimedia-devel qt5-qtx11extras-devel bamf-devel libXrandr-devel libXtst-devel libX11-devel && \
      strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5
