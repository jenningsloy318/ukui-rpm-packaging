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
2. ukui-panel (latest code)
      ```
      /root/rpmbuild/BUILD/ukui-panel-master/plugin-tray/ukuitray.cpp: In member function 'virtual bool UKUIStorageFrame::eventFilter(QObject*, QEvent*)':
      /root/rpmbuild/BUILD/ukui-panel-master/plugin-tray/ukuitray.cpp:1473:42: error: invalid 'static_cast' from type 'QEvent*' to type 'QMouseEvent*'
      1473 |                QMouseEvent *mouseEvent = static_cast<QMouseEvent *>(event);
            |                                          ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      In file included from /usr/include/qt5/QtWidgets/qframe.h:44,
                  from /usr/include/qt5/QtWidgets/QFrame:1,
                  from /root/rpmbuild/BUILD/ukui-panel-master/plugin-tray/trayicon.h:32,
                  from /root/rpmbuild/BUILD/ukui-panel-master/plugin-tray/ukuitray.cpp:42:
      /usr/include/qt5/QtWidgets/qwidget.h:72:7: note: class type 'QMouseEvent' is incomplete
      72 | class QMouseEvent;
            |       ^~~~~~~~~~~
      /root/rpmbuild/BUILD/ukui-panel-master/plugin-tray/ukuitray.cpp:1474:30: error: invalid use of incomplete type 'class QMouseEvent'
      1474 |                if (mouseEvent->button() == Qt::LeftButton)
            |                              ^~
      In file included from /usr/include/qt5/QtWidgets/qframe.h:44,
                  from /usr/include/qt5/QtWidgets/QFrame:1,
                  from /root/rpmbuild/BUILD/ukui-panel-master/plugin-tray/trayicon.h:32,
                  from /root/rpmbuild/BUILD/ukui-panel-master/plugin-tray/ukuitray.cpp:42:
      /usr/include/qt5/QtWidgets/qwidget.h:72:7: note: forward declaration of 'class QMouseEvent'
      72 | class QMouseEvent;
            |       ^~~~~~~~~~~
      /root/rpmbuild/BUILD/ukui-panel-master/plugin-tray/ukuitray.cpp:1480:34: error: invalid use of incomplete type 'class QMouseEvent'
      1480 |                else if(mouseEvent->button() == Qt::RightButton)
            |                                  ^~
      In file included from /usr/include/qt5/QtWidgets/qframe.h:44,
                  from /usr/include/qt5/QtWidgets/QFrame:1,
                  from /root/rpmbuild/BUILD/ukui-panel-master/plugin-tray/trayicon.h:32,
                  from /root/rpmbuild/BUILD/ukui-panel-master/plugin-tray/ukuitray.cpp:42:
      /usr/include/qt5/QtWidgets/qwidget.h:72:7: note: forward declaration of 'class QMouseEvent'
      72 | class QMouseEvent;
            |       ^~~~~~~~~~~
      make[2]: *** [plugin-tray/CMakeFiles/tray.dir/build.make:116: plugin-tray/CMakeFiles/tray.dir/ukuitray.cpp.o] Error 1
      ```
3. kwin (latest code)
      ```
      /root/rpmbuild/BUILD/ukui-kwin-master/effects/blur/blur.cpp: In member function 'QStringList KWin::BlurEffect::readFile(QString)':
      /root/rpmbuild/BUILD/ukui-kwin-master/effects/blur/blur.cpp:252:5: error: 'QFile' was not declared in this scope
      252 |     QFile file(strFilePath);
            |     ^~~~~
      /root/rpmbuild/BUILD/ukui-kwin-master/effects/blur/blur.cpp:254:17: error: 'file' was not declared in this scope; did you mean 'fileno'?
      254 |     if(false == file.exists()) {
            |                 ^~~~
            |                 fileno
      /root/rpmbuild/BUILD/ukui-kwin-master/effects/blur/blur.cpp:258:9: error: 'file' was not declared in this scope; did you mean 'fileno'?
      258 |     if(!file.open(QIODevice::ReadOnly | QIODevice::Text)) {
            |         ^~~~
            |         fileno
      /root/rpmbuild/BUILD/ukui-kwin-master/effects/blur/blur.cpp:261:29: error: 'file' was not declared in this scope; did you mean 'fileno'?
      261 |     QTextStream textStream(&file);
            |                             ^~~~
            |                             fileno
      /root/rpmbuild/BUILD/ukui-kwin-master/effects/blur/blur.cpp:249:42: warning: unused parameter 'strFilePath' [-Wunused-parameter]
      249 | QStringList BlurEffect::readFile(QString strFilePath)
            |                                  ~~~~~~~~^~~~~~~~~~~
      make[2]: *** [effects/CMakeFiles/kwin4_effect_builtins.dir/build.make:354: effects/CMakeFiles/kwin4_effect_builtins.dir/blur/blur.cpp.o] Error 1

```