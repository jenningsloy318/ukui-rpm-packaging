FROM docker.io/library/fedora:32

RUN  sed -i '/metalink/s/$/\&country=cn/g' /etc/yum.repos.d/*.repo && \
      dnf update -y && \
      dnf -y install qt5-qtbase-devel qt5-qtscript-devel qt5-qttools-devel qt5-qtbase-private-devel qt5-qtx11extras-devel zlib-devel libX11-devel libcrystalhd-devel qt5-linguist && \
      strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5
