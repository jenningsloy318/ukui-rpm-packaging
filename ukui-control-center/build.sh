#!/bin/bash
 
echo "install build dependencies"
dnf install -y $(grep  BuildRequires /root/ukui-control-center.spec |awk '{print $2}')
strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5


echo "build rpm package"
cp /root/ukui-control-center-libdir.patch /root/rpmbuild/SOURCES/ukui-control-center-libdir.patch
rpmbuild -ba /root/ukui-control-center.spec