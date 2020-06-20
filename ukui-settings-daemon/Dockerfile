FROM docker.io/library/fedora:32

RUN  sed -i '/metalink/s/$/\&country=cn/g' /etc/yum.repos.d/*.repo && \
      dnf update -y && \
      dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  libcanberra-devel dbus-glib-devel dconf-devel fontconfig-devel glib2-devel gtk3-devel mate-desktop-devel libmatekbd-devel libmatemixer-devel libnotify-devel polkit-devel nss-devel pulseaudio-libs-devel pulseaudio-qt-devel startup-notification-devel libX11-devel libXext-devel libXi-devel libxklavier-devel libXrandr-devel libXt-devel xorg-x11-proto-devel mate-desktop-devel mate-utils-devel mate-common && \
      strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5
