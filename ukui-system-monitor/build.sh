#!/bin/bash
echo "install build dependencies"
dnf install -y $(grep  BuildRequires /root/ukui-system-monitor.spec |awk '{print $2}')
strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5


echo "build rpm package"
cp /root/ukui-system-monitor-qmake-path.patch /root/rpmbuild/SOURCES
rpmbuild -ba /root/ukui-system-monitor.spec