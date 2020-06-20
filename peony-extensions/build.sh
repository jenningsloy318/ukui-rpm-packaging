#!/bin/bash

echo "install build dependencies"
dnf install /root/peony-libs-master-1.fc32.x86_64.rpm  /root/peony-devel-master-1.fc32.x86_64.rpm  -y
dnf update -y


echo "build rpm package"
cp /root/peony-extensions-libdir-and-qmake.patch /root/rpmbuild/SOURCES/peony-extensions-libdir-and-qmake.patch 
rpmbuild -ba /root/peony-extensions.spec