FROM docker.io/library/fedora:32

RUN  sed -i '/metalink/s/$/\&country=cn/g' /etc/yum.repos.d/*.repo && \
      dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  ruby  mysql-devel ruby-devel rubygems && \
      cd /usr/bin/ && ln -s qmake-qt5 qmake &&  \ 
      gem install sass bundler rails compass
