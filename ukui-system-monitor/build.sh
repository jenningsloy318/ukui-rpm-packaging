#!/bin/bash
echo "update packages"
dnf update -y 

echo "build rpm package"
cp /root/ukui-system-monitor-qmake-path.patch /root/rpmbuild/SOURCES/ukui-system-monitor-qmake-path.patch
rpmbuild -ba /root/ukui-system-monitor.spec