ukui packages:  
- ukui-session-manager 
- ukui-menu 
- ukui-sidebar 
- ukui-control-center 
- ukui-settings-daemon 
- ukui-window-switch 
- ukui-media 
- ukui-power-manager 
- kylin-nm 
- qt5-ukui-platformtheme

## build 
- use [Dockerfile](./Dockerfile) to build image docker.io/jenningsloy318/ukui-builder:f32
- in docker build
  ```
  docker  run  --privileged -v `pwd`:/root docker.io/jenningsloy318/ukui-builder:f32  bash  /root/build.sh 
  ```


## issues
1. biometric-authentication build, already installed   libfprint-devel  and fprintd-devel but still errors

error  happens because on fedora 32 onwards, libfprint default to version 2, but biometric-authentication now is developed to use libfprint version 1
- option 1: rebuild libfprint version 1 on fedora 32, 
- option 2:  wait for biometric-authentication upgrading

 
Tried to grab libfprint v1 from fedora repo and build/install it, then build biometric-autentication, but with following errors 
```
/usr/bin/ld: biometric_config_tool-biometric-config-tool-add-drivero:/root/rpmbuild/BUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-main.h:29: multipledefinition of `bio_config_file'; biometri
c_config_tool-biometric-config-tool-main.o:/root/rpmbuild/BUILDbiometric-authentication-master/src/utils/biometric-config-toolbiometric-config-tool-main.h:29: first defined here
/usr/bin/ld: biometric_config_tool-biometric-config-tool-add-drivero:/root/rpmbuild/BUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-add-driver.h:27:multiple definition of `force_override'; bio
metric_config_tool-biometric-config-tool-main.o:/root/rpmbuildBUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-add-driver.h:27: firstdefined here
/usr/bin/ld: biometric_config_tool-biometric-config-tool-add-drivero:/root/rpmbuild/BUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-add-driver.h:28:multiple definition of `driver_disable'; bio
metric_config_tool-biometric-config-tool-main.o:/root/rpmbuildBUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-add-driver.h:28: firstdefined here
/usr/bin/ld:biometric_config_tool-biometric-config-tool-remove-driver.o:/rootrpmbuild/BUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-main.h:29: multipledefinition of `bio_config_file'; biome
tric_config_tool-biometric-config-tool-main.o:/root/rpmbuild/BUILDbiometric-authentication-master/src/utils/biometric-config-toolbiometric-config-tool-main.h:29: first defined here
/usr/bin/ld:biometric_config_tool-biometric-config-tool-remove-driver.o:/rootrpmbuild/BUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-remove-driver.h:27:multiple definition of `driver_ignore'
; biometric_config_tool-biometric-config-tool-main.o:/root/rpmbuildBUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-remove-driver.h:27:first defined here
/usr/bin/ld:biometric_config_tool-biometric-config-tool-enable-driver.o:/rootrpmbuild/BUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-main.h:29: multipledefinition of `bio_config_file'; biome
tric_config_tool-biometric-config-tool-main.o:/root/rpmbuild/BUILDbiometric-authentication-master/src/utils/biometric-config-toolbiometric-config-tool-main.h:29: first defined here
/usr/bin/ld:biometric_config_tool-biometric-config-tool-enable-driver.o:/rootrpmbuild/BUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-enable-driver.h:27:multiple definition of `driver_ignore'
; biometric_config_tool-biometric-config-tool-main.o:/root/rpmbuildBUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-remove-driver.h:27:first defined here
/usr/bin/ld:biometric_config_tool-biometric-config-tool-disable-driver.o:/rootrpmbuild/BUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-main.h:29: multipledefinition of `bio_config_file'; biom
etric_config_tool-biometric-config-tool-main.o:/root/rpmbuild/BUILDbiometric-authentication-master/src/utils/biometric-config-toolbiometric-config-tool-main.h:29: first defined here
/usr/bin/ld:biometric_config_tool-biometric-config-tool-disable-driver.o:/rootrpmbuild/BUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-disable-driver.h:27:multiple definition of `driver_ignor
e'; biometric_config_tool-biometric-config-tool-main.o:/rootrpmbuild/BUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-remove-driver.h:27:first defined here
/usr/bin/ld: biometric_config_tool-biometric-config-tool-set-key.o:root/rpmbuild/BUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-main.h:29: multipledefinition of `bio_config_file'; biometric_c
onfig_tool-biometric-config-tool-main.o:/root/rpmbuild/BUILDbiometric-authentication-master/src/utils/biometric-config-toolbiometric-config-tool-main.h:29: first defined here
/usr/bin/ld: biometric_config_tool-biometric-config-tool-set-key.o:root/rpmbuild/BUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-set-key.h:29: multipledefinition of `key_is_exist'; biometric_c
onfig_tool-biometric-config-tool-main.o:/root/rpmbuild/BUILDbiometric-authentication-master/src/utils/biometric-config-toolbiometric-config-tool-set-key.h:29: first defined here
/usr/bin/ld: biometric_config_tool-biometric-config-tool-set-key.o:root/rpmbuild/BUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-set-key.h:28: multipledefinition of `ignore_exist'; biometric_c
onfig_tool-biometric-config-tool-main.o:/root/rpmbuild/BUILDbiometric-authentication-master/src/utils/biometric-config-toolbiometric-config-tool-set-key.h:28: first defined here
/usr/bin/ld: biometric_config_tool-biometric-config-tool-set-key.o:root/rpmbuild/BUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-set-key.h:27: multipledefinition of `force_override'; biometric
_config_tool-biometric-config-tool-main.o:/root/rpmbuild/BUILDbiometric-authentication-master/src/utils/biometric-config-toolbiometric-config-tool-add-driver.h:27: first defined here
/usr/bin/ld: biometric_config_tool-biometric-config-tool-remove-keyo:/root/rpmbuild/BUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-main.h:29: multipledefinition of `bio_config_file'; biometri
c_config_tool-biometric-config-tool-main.o:/root/rpmbuild/BUILDbiometric-authentication-master/src/utils/biometric-config-toolbiometric-config-tool-main.h:29: first defined here
/usr/bin/ld: biometric_config_tool-biometric-config-tool-remove-keyo:/root/rpmbuild/BUILD/biometric-authentication-master/src/utilsbiometric-config-tool/biometric-config-tool-remove-key.h:27:multiple definition of `driver_ignore'; biom
etric_config_tool-biometric-config-tool-main.o:/root/rpmbuild/BUILDbiometric-authentication-master/src/utils/biometric-config-toolbiometric-config-tool-remove-driver.h:27: first defined here
collect2: error: ld returned 1 exit status
make[4]: *** [Makefile:481: biometric-config-tool] Error 1
make[4]: Leaving directory '/root/rpmbuild/BUILDbiometric-authentication-master/src/utils/biometric-config-tool'
make[3]: *** [Makefile:407: all-recursive] Error 1
make[2]: *** [Makefile:618: all-recursive] Error 1
make[1]: *** [Makefile:454: all-recursive] Error 1
make: *** [Makefile:386: all] Error 2
error: Bad exit status from /var/tmp/rpm-tmp.I9DH2T (%build)
```