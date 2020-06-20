#!/bin/bash
 
echo "update packages"
dnf update -y

echo "build rpm package"
cp /root/ukui-control-center-libdir.patch /root/rpmbuild/SOURCES/ukui-control-center-libdir.patch
rpmbuild -ba /root/ukui-control-center.spec