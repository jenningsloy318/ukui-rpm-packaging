#!/bin/bash

echo "update packages"
dnf update -y

echo "build rpm package"
mkdir -p /root/rpmbuild/SOURCES
cp /root/ukui-biometric-auth-libdir.patch /root/rpmbuild/SOURCES
rpmbuild  -ba /root/ukui-biometric-auth.spec