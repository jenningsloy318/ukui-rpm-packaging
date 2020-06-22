#!/bin/bash

echo "update packages"
dnf update -y 
echo "build rpm package"
mkdir -p /root/rpmbuild/SOURCES
cp /root/fix-qfile-class.patch /root/rpmbuild/SOURCES
rpmbuild -ba /root/ukui-kwin.spec