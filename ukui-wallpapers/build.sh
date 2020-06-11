#!/bin/bash
echo "install build dependencies"
dnf install -y $(grep  BuildRequires /root/ukui-wallpapers.spec |awk '{print $2}')

echo "build rpm package"
mkdir -p /root/rpmbuild/SOURCES 
rpmbuild -ba /root/ukui-wallpapers.spec