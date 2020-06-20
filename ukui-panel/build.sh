#!/bin/bash

echo "update packages"
dnf install /root/peony-libs-master-1.fc32.x86_64.rpm  /root/peony-devel-master-1.fc32.x86_64.rpm  -y
dnf update -y

echo "build rpm package"
rpmbuild -ba /root/ukui-panel.spec