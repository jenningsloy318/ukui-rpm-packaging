FROM docker.io/library/fedora:32

RUN  sed -i '/metalink/s/$/\&country=cn/g' /etc/yum.repos.d/*.repo && \
      dnf update -y && \
      dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  gtk3-devel libwnck3-devel qt5-qtbase-devel intltool libcanberra-devel libcanberra-gtk3 glib2-devel dbus-glib-devel libnotify-devel libtool libgcrypt-devel upower-devel libX11-devel libXext-devel libXrandr-devel perl-XML-Parser qt5-qtx11extras-devel gsettings-qt-devel mate-common mate-desktop-devel qt5-qtcharts-devel xmlto yelp-tools libgnome-keyring-devel && \
      strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5
