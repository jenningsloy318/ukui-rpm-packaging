#!/bin/bash

echo "install build dependencies"
dnf install -y $(grep  BuildRequires /root/ukui-biometric-auth.spec |awk '{print $2}')
strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5


echo "build rpm package"
cp /root/lib-path.patch /root/rpmbuild/SOURCES
rpmbuild  -ba /root/ukui-biometric-auth.spec