 echo "install build tools"
 rm -rf /root/rpmbuild
 sed -i '/metalink/s/$/\&country=cn/g' /etc/yum.repos.d/*.repo
 dnf -y install rpm-build 

 echo "build rpm package"
 
rpmbuild -ba /root/ukui-desktop-environment.spec