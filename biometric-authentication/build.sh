#!/bin/bash

echo "update packages"
dnf update -y

echo "build biometric-authentication package"

rpmbuild  -ba /root/biometric-authentication.spec
