FROM docker.io/library/fedora:32

RUN  sed -i '/metalink/s/$/\&country=cn/g' /etc/yum.repos.d/*.repo && \
      dnf update -y && \
      dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build      qt5-qtsvg-devel qt5-qtx11extras-devel glib2-devel qt5-qtbase-devel qt5-qttools-devel poppler-qt5-devel gsettings-qt-devel && \
      strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5
