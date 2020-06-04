#!/bin/bash
echo "install build dependencies"
dnf install -y $(grep  BuildRequires /root/kylin-display-switch.spec |awk '{print $2}')


echo "build rpm package"
rpmbuild -ba /root/kylin-display-switch.spec