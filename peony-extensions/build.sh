#!/bin/bash

echo "install build dependencies"
dnf install /root/peony-devel-2.1.2-1.fc32.x86_64.rpm /root/peony-libs-2.1.2-1.fc32.x86_64.rpm -y
dnf install -y $(grep  BuildRequires /root/peony-extensions.spec |awk '{print $2}')
strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5


echo "build rpm package"
cp /root/lib-path.patch /root/rpmbuild/SOURCES/lib-path.patch 
rpmbuild -ba /root/peony-extensions.spec