#!/bin/bash

echo "build rpm package"
mkdir -p /root/rpmbuild/SOURCES 
rpmbuild -ba /root/ukui-themes.spec