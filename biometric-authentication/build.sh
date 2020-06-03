#!/bin/bash

echo "install build dependencies"
dnf install -y $(grep  BuildRequires /root/biometric-authentication.spec |awk '{print $2}')


echo "build rpm package"
cp /root/libfprint-pkgconfig.patch /root/rpmbuild/SOURCES/libfprint-pkgconfig.patch
rpmbuild  -ba /root/biometric-authentication.spec