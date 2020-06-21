FROM docker.io/library/fedora:32

RUN  sed -i '/metalink/s/$/\&country=cn/g' /etc/yum.repos.d/*.repo && \
      dnf update -y && \
      dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros   automake python3-devel glib2-devel gtk3-devel libusb-devel sqlite-devel  polkit-devel libtool libuuid-devel  git gtk-doc meson glib2-devel libusb-devel nss-devel pixman-devel && \
      rpm -ivh https://download-ib01.fedoraproject.org/pub/fedora/linux/releases/31/Everything/source/tree/Packages/l/libfprint-1.0-1.fc31.src.rpm  && \
      rpmbuild  -ba /root/rpmbuild/SPECS/libfprint.spec && \ 
      dnf install -y  /root/rpmbuild/RPMS/x86_64/libfprint-1.0-1.fc32.x86_64.rpm /root/rpmbuild/RPMS/x86_64/libfprint-devel-1.0-1.fc32.x86_64.rpm
