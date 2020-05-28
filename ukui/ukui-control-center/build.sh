#!/bin/bash
 
echo "install build dependencies"
dnf install -y $(grep  BuildRequires /root/ukui-control-center.spec |awk '{print $2}')
strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5


echo "build rpm package"
cp /root/lib-path.patch /root/rpmbuild/SOURCES/lib-path.patch 
rpmbuild -ba /root/ukui-control-center.spec