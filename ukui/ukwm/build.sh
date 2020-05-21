#!/bin/bash

echo "install build dependencies"
dnf install -y $(grep  BuildRequires /root/ukwm.spec |awk '{print $2}')


echo "build rpm package"
rpmbuild  -ba /root/ukwm.spec   