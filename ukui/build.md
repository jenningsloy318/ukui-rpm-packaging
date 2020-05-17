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
1.  ukui-session-manager

  ```
  dnf install -y qt5-qtdeclarative-devel qt5-qtbase-devel qt5-qtmultimedia-devel qt5-qtx11extras-devel kf5-kidletime-devel qt5-linguist gsettings-qt-devel libXtst-devel systemd-devel
  git clone https://github.com/ukui/ukui-session-manager.git
  cd ukui-session-manager
  mkdir build
  cd build
  cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_SYSCONFDIR=/etc  -DCMAKE_INSTALL_LIBDIR=/usr/lib64 ..  
  make
  make install
  ```
2. ukui-menu
   ```
  dnf install -y bamf-devel  libXrandr-devel
  git clone https://github.com/ukui/ukui-menu.git
  cd ukui-menu
  qmake-qt5  && make 
  ```

  errors:
  ```
  g++ -c -pipe -g -O2 -pthread -pthread -Wall -W -D_REENTRANT -fPIC -DQT_NO_DEBUG -DQT_NO_KEYWORDS -DQT_SVG_LIB -DQT_WIDGETS_LIB -DQT_X11EXTRAS_LIB -DQT_GUI_LIB -DQT_DBUS_LIB -DQT_NETWORK_LIB -DQT_CORE_LIB -I. -Isrc/QtSingleApplication -isystem /usr/include/glib-2.0 -I/usr/lib64/glib-2.0/include -isystem /usr/include/gio-unix-2.0 -isystem /usr/include/libmount -isystem /usr/include/blkid -isystem /usr/include/qt5/QGSettings -isystem /usr/include/libbamf3 -I/usr/lib64/libbamf3/include -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtSvg -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtX11Extras -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtDBus -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/qt5/QtCore -I. -I. -I/usr/lib64/qt5/mkspecs/linux-g++ -o xeventmonitor.o src/XEventMonitor/xeventmonitor.cpp
  In file included from src/XEventMonitor/xeventmonitor.h:27,
                  from src/XEventMonitor/xeventmonitor.cpp:22:
  /usr/include/c++/10/bits/istream.tcc: In member function ‘std::streamsize std::basic_istream<_CharT, _Traits>::readsome(std::basic_istream<_CharT, _Traits>::char_type*, std::streamsize)’:
  /usr/include/c++/10/bits/istream.tcc:699:46: error: expected unqualified-id before ‘(’ token
    699 |   _M_gcount = this->rdbuf()->sgetn(__s, std::min(__num, __n));
        |                                              ^~~
  make: *** [Makefile:1382: xeventmonitor.o] Error 1
  ```


3. ukui-sidebar
   ```
  dnf install -y  glib2-devel qt5-qtbase-devel qt5-qtsvg-devel qt5-qttools-devel qt5-qttools dconf-devel gsettings-qt-devel qt5-qtmultimedia-devel
  git clone https://github.com/ukui/ukui-sidebar.git
  cd ukui-sidebar && mkdir build && cd build
  qmake-qt5 .. && make
  ```
4. ukui-control-center
    ```
    git clone https://github.com/ukui/ukui-control-center.git
    qmake-qt5  && make 
    ```
5. ukui-settings-daemon
    ```
    dnf install mate-common autogen dbus-glib-devel gtk3-devel mate-desktop-devel libmatekbd-devel libxklavier-devel -y

    git clone https://github.com/ukui/ukui-settings-daemon.git
    ./autogen.sh --prefix=/usr --sysconfdir=/etc --libdir=/usr/lib64 
    make
    ```

6. ukui-window-switch 
  ```
  git clone git clone https://github.com/ukui/ukui-window-switch.git









10. qt5-ukui-platformtheme
    ```
    git clone https://github.com/ukui/qt5-ukui-platformtheme.git
    qmake-qt5 && make 
    make install
    ```