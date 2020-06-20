#!/bin/bash

echo "update packages"
dnf update -y 

echo "build rpm package"
mkdir -p /root/rpmbuild/SOURCES/
cp /root/peony-libdir.patch /root/rpmbuild/SOURCES/peony-libdir.patch
rpmbuild  -ba /root/peony.spec   