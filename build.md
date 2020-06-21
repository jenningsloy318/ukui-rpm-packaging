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
   option 1: rebuild libfprint version 1 on fedora 32, 
   option 2:  wait for biometric-authentication upgrading

  ```

  2. ukui-panel master 
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
3. kwin 
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