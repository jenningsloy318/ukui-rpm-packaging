#!/bin/bash

echo "install build dependencies"
dnf install -y $(grep  BuildRequires /root/peony.spec |awk '{print $2}')
strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5


echo "build rpm package"
cp /root/peony-libdir.patch /root/rpmbuild/SOURCES
rpmbuild  -ba /root/peony.spec   