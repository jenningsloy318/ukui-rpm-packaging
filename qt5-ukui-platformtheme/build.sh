#!/bin/bash
echo "update packages"
dnf update -y 

echo "build rpm package"
mkdir -p /root/rpmbuild/SOURCES 
rpmbuild -ba /root/qt5-ukui-platformtheme.spec