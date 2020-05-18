 echo "install build tools"
 #rm -rf /root/rpmbuild
 sed -i '/metalink/s/$/\&country=cn/g' /etc/yum.repos.d/*.repo
 dnf -y install gcc gcc-c++ make cmake cmake-rpm-macros autoconf  rpm-build qt5-rpm-macros 
 
 echo "install build dependencies"
 dnf install -y $(grep  BuildRequires /root/peony.spec |awk '{print $2}')
 strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5


 echo "build rpm package"
rpmbuild  -ba /root/peony.spec   