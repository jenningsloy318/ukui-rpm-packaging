#!/bin/bash
echo "update packages"
dnf update -y 

echo "build rpm package"
cp /root/ukui-screensaver-libexec-path.patch /root/rpmbuild/SOURCES/ukui-screensaver-libexec-path.patch
rpmbuild -ba /root/ukui-screensaver.spec