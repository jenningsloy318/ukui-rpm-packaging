FROM docker.io/library/fedora:32

RUN  sed -i '/metalink/s/$/\&country=cn/g' /etc/yum.repos.d/*.repo && \
      dnf update -y && \
      dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros   qt5-qtbase-devel qt5-qttools-devel glib2-devel qt5-qtbase-devel gsettings-qt-devel kf5-kwindowsystem-devel poppler-qt5-devel qt5-qtx11extras-devel qt5-qtbase-private-devel    && \   
      strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5
