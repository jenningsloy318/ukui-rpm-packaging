FROM docker.io/library/fedora:32

RUN  sed -i '/metalink/s/$/\&country=cn/g' /etc/yum.repos.d/*.repo && \
      dnf -y install gcc gcc-c++ make cmake cmake-rpm-macros autoconf  rpm-build qt5-rpm-macros 
