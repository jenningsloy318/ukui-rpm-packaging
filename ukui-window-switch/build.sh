#!/bin/bash
echo "update packages"
dnf update -y 


echo "build rpm package"
mkdir -p /root/rpmbuild/SOURCES 
rpmbuild -ba /root/ukui-window-switch.spec