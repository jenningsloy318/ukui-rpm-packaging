#!/bin/bash
echo "install build dependencies"
dnf install -y $(grep  BuildRequires /root/ukui-sidebar.spec |awk '{print $2}')
strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5


echo "build rpm package"
mkdir -p /root/rpmbuild/SOURCES 
cp /root/plugin-path.patch /root/rpmbuild/SOURCES 
rpmbuild -ba /root/ukui-sidebar.spec