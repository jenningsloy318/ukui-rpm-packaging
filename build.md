ukui packages:  
- kylin-display-switch 
- kylin-nm
- kylin-video
- indicator-china-weather 
- qt5-ukui-platformtheme
- peony 
- peony-extensions 
- ukui-biometric-auth 
- ukui-biometric-manager 
- ukui-control-center
- ukui-greeter
- ukui-kwin or ukwm
- ukui-menu 
- ukui-panel 
- ukui-power-manager
- ukui-screensaver
- ukui-session-manager
- ukui-settings-daemon
- ukui-sidebar
- ukui-system-monitor
- ukui-window-switch
- ukui-wallpapers
- ukui-themes
- ukui-media

## build 
- in docker build
  ```
  make docker-build
  ```


## issues
1. biometric-authentication build, already installed   libfprint-devel  and fprintd-devel but still errors

error  happens because on fedora 32 onwards, libfprint default to version 2, but biometric-authentication now is developed to use libfprint version 1
- option 1: rebuild libfprint version 1 on fedora 32, 
- option 2:  wait for biometric-authentication upgrading


2. ukui runs with  many errors on both fedora 32/33 and centos 8 , desktop will auto logout several minutes later

    symtoms:
    1. desktop session will terminated after some minutes, and return to login window 
    2. even desktop session exists, the keyboard input will get no response, nothing will display or input as typing, but mouse can move or drag, but sometimes still can't operate correctly
    
    ```
    Jul 01 01:27:28 centos8-builder.lmy.com systemd[1]: session-c1.scope: Killing process 1228 (ukui-greeter) with signal SIGTERM.
    Jul 01 01:27:28 centos8-builder.lmy.com dbus-daemon[1285]: [session uid=0 pid=1285] Activating via systemd: service name='org.a11y.Bus' unit='at-spi-dbus-bus.service' requested by ':1.8' (uid=0 pid=1325 comm="/usr/libexec/ukui-settings-daemon " label="unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023")
    Jul 01 01:27:28 centos8-builder.lmy.com at-spi-bus-launcher[1334]: dbus-daemon[1339]: Activating service name='org.a11y.atspi.Registry' requested by ':1.0' (uid=0 pid=1325 comm="/usr/libexec/ukui-settings-daemon " label="unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023")
    Jul 01 01:27:28 centos8-builder.lmy.com ukui-settings-daemon[1325]: use default theme name=Breeze_Snow=
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: ------usd_keybindings_manager_start-------
    Jul 01 01:27:29 centos8-builder.lmy.com dbus-daemon[1285]: [session uid=0 pid=1285] Activating service name='org.kde.kglobalaccel' requested by ':1.13' (uid=0 pid=1326 comm="/usr/bin/ukui-kwin_x11 " label="unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023")
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Script" listed in "/usr/share/ukui-kwin/scripts/videowall/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Script" listed in "/usr/share/ukui-kwin/scripts/synchronizeskipswitcher/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Script" listed in "/usr/share/ukui-kwin/scripts/minimizeall/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Script" listed in "/usr/share/ukui-kwin/scripts/desktopchangeosd/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com dbus-daemon[1285]: [session uid=0 pid=1285] Activating service name='ca.desrt.dconf' requested by ':1.7' (uid=0 pid=1324 comm="/usr/bin/ukui-panel " label="unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023")
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_fade/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_fadedesktop/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_dialogparent/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_fadingpopups/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_windowaperture/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_eyeonscreen/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_translucency/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_frozenapp/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_login/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_logout/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_morphingpopups/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_maximize/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_scale/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_squash/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_dimscreen/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_sessionquit/metadata.desktop"
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 657, resource id: 10485769, major code: 3 (GetWindowAttributes), minor code: 0
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: qt.qpa.xcb: QXcbConnection: XCB error: 9 (BadDrawable), sequence: 658, resource id: 10485769, major code: 14 (GetGeometry), minor code: 0
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 827, resource id: 8388612, major code: 18 (ChangeProperty), minor code: 0
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 828, resource id: 8388612, major code: 12 (ConfigureWindow), minor code: 0
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 832, resource id: 8388620, major code: 18 (ChangeProperty), minor code: 0
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 833, resource id: 8388620, major code: 12 (ConfigureWindow), minor code: 0
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 837, resource id: 8388624, major code: 18 (ChangeProperty), minor code: 0
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-kwin_x11[1326]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 838, resource id: 8388624, major code: 12 (ConfigureWindow), minor code: 0
    Jul 01 01:27:29 centos8-builder.lmy.com dbus-daemon[1285]: [session uid=0 pid=1285] Activating via systemd: service name='org.gtk.vfs.UDisks2VolumeMonitor' unit='gvfs-udisks2-volume-monitor.service' requested by ':1.6' (uid=0 pid=1325 comm="/usr/libexec/ukui-settings-daemon " label="unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023")
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui_kylin_nm[1397]: Kylin Network Manager Is Already Launched
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui_kylin_nm[1397]: Using the icon theme named 'ukui-icon-theme-default'
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-flash-disk[1399]: QMetaObject::connectSlotsByName: No matching signal for on_Maininterface_hide()
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:29 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com dbus-daemon[1285]: [session uid=0 pid=1285] Activating via systemd: service name='org.ayatana.bamf' unit='bamfdaemon.service' requested by ':1.22' (uid=0 pid=1400 comm="/usr/bin/ukui-menu " label="unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023")
    Jul 01 01:27:30 centos8-builder.lmy.com dbus-daemon[829]: [system] Activating via systemd: service name='org.freedesktop.UPower' unit='upower.service' requested by ':1.58' (uid=0 pid=1402 comm="/usr/bin/ukui-power-manager " label="unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023")
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-sidebar[1404]: ---------------------------主界面加载完毕---------------------------
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui_kylin_nm[1397]: state of network: '0' is connected, '1' is disconnected, '2' is net device switch off
    Jul 01 01:27:30 centos8-builder.lmy.com ukui_kylin_nm[1397]: current network state:  wired state =0,  wifi state =2
    Jul 01 01:27:30 centos8-builder.lmy.com ukui_kylin_nm[1397]: Launch kylin-nm, Lan already connected
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-kwin_x11[1326]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 1297, resource id: 20971524, major code: 12 (ConfigureWindow), minor code: 0
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-menu[1400]: qt.qpa.xcb: QXcbConnection: XCB error: 8 (BadMatch), sequence: 421, resource id: 25165831, major code: 42 (SetInputFocus), minor code: 0
    Jul 01 01:27:30 centos8-builder.lmy.com ukui_kylin_nm[1397]: already insert an active lannet in the top of lan list
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:30 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:31 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:31 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:31 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:32 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:32 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:32 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:32 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:32 centos8-builder.lmy.com ukui-kwin_x11[1326]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 2139, resource id: 46137350, major code: 18 (ChangeProperty), minor code: 0
    Jul 01 01:27:32 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:32 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:32 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:32 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:32 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:32 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:32 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:32 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:32 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-control-center[1545]: Create youker Interface Failed When Get Computer info:  QDBusError("org.freedesktop.DBus.Error.ServiceUnknown", "The name com.kylin.assistant.systemdaemon was not provided by any .service files")
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-control-center[1545]: "/root/.pam_environment"  not found
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-control-center[1545]: QLayout: Attempting to add QLayout "" to QFrame "", which already has a layout
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-control-center[1545]: QLayout: Attempting to add QLayout "" to UkmediaMainWidget "Audio", which already has a layout
    Jul 01 01:27:36 centos8-builder.lmy.com dbus-daemon[829]: [system] Activating via systemd: service name='org.freedesktop.timedate1' unit='dbus-org.freedesktop.timedate1.service' requested by ':1.71' (uid=0 pid=1545 comm="ukui-control-center " label="unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023")
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-control-center[1545]: QWidget::setMinimumSize: (listWidget/QListWidget) Negative sizes (0,-58) are not possible
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-control-center[1545]: QWidget::setMaximumSize: (listWidget/QListWidget) Negative sizes (16777215,-58) are not possible
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-control-center[1545]: QPixmap::scaled: Pixmap is a null pixmap
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:36 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com dbus-daemon[1285]: [session uid=0 pid=1285] Activating service name='org.kde.KScreen' requested by ':1.41' (uid=0 pid=1545 comm="ukui-control-center " label="unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023")
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:37 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:40 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:40 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:40 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:41 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:41 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:41 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:41 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:41 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:44 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:44 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:44 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:44 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:44 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:44 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:44 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:44 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:44 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:44 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:45 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:46 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:46 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:46 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:46 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:46 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:46 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:46 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:46 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:46 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:46 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:46 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:46 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:46 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:46 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:46 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:50 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:50 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:50 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:50 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:50 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:50 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:50 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:50 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:50 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:50 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:50 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:50 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:50 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:50 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:50 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:50 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:50 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:50 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:52 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:52 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:52 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:57 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:57 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:57 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:57 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:57 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:57 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:57 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:57 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:57 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:58 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:58 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:58 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:58 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:58 centos8-builder.lmy.com ukui-kwin_x11[1326]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 7882, resource id: 54525958, major code: 18 (ChangeProperty), minor code: 0
    Jul 01 01:27:58 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:58 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:58 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:58 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:58 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:58 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:58 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:58 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:27:58 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:28:07 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:28:07 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:28:07 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:28:07 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:28:07 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:28:07 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:28:07 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:28:07 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:28:07 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:28:15 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:28:15 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:29:41 centos8-builder.lmy.com ukui-control-center[1545]: QImage::scaled: Image is a null image
    Jul 01 01:29:41 centos8-builder.lmy.com ukui-control-center[1545]: QImage::scaled: Image is a null image
    Jul 01 01:29:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:29:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:29:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:29:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:29:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:29:47 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:34:48 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:34:48 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:34:48 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:34:48 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:34:48 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:34:48 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:34:48 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:34:48 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:34:48 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:34:48 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:34:48 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:34:48 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:34:48 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 01:42:21 centos8-builder.lmy.com ukui_kylin_nm[1397]: kylin-nm receive a signal 'Device.Wired PropertiesChanged' about interface.
    Jul 01 01:44:46 centos8-builder.lmy.com ukui_kylin_nm[1397]: kylin-nm receive a signal 'Device.Wired PropertiesChanged' about interface.
    Jul 01 01:44:46 centos8-builder.lmy.com ukui_kylin_nm[1397]: wired physical cable is already plug out
    Jul 01 01:44:51 centos8-builder.lmy.com ukui_kylin_nm[1397]: kylin-nm receive a signal 'Device.Wired PropertiesChanged' about interface.
    Jul 01 01:44:51 centos8-builder.lmy.com ukui_kylin_nm[1397]: wired physical cable is already plug in
    Jul 01 01:44:53 centos8-builder.lmy.com ukui_kylin_nm[1397]: already insert an active lannet in the top of lan list
    Jul 01 01:59:51 centos8-builder.lmy.com ukui_kylin_nm[1397]: kylin-nm receive a signal 'Device.Wired PropertiesChanged' about interface.
    Jul 01 02:14:51 centos8-builder.lmy.com ukui_kylin_nm[1397]: kylin-nm receive a signal 'Device.Wired PropertiesChanged' about interface.
    Jul 01 02:21:18 centos8-builder.lmy.com kernel: MonitorThread[1450]: segfault at 2b1140 ip 00000000002b1140 sp 00007fcee607f7f8 error 14 in ukui-sidebar[55b1717e9000+2a000]
    Jul 01 02:21:18 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 02:21:18 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 02:21:18 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 02:21:18 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 02:21:18 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 02:21:18 centos8-builder.lmy.com kernel: ukui-session[1271]: segfault at 84b06 ip 0000000000084b06 sp 00007ffe0388c918 error 14 in ukui-session[55907b975000+ce000]
    Jul 01 02:21:18 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 02:21:18 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 02:21:18 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 02:21:18 centos8-builder.lmy.com kernel: ukui-window-swi[1407]: segfault at 2b1140 ip 00000000002b1140 sp 00007fff9f4cf998 error 14 in ukui-window-switch[55f52bca7000+40000]
    Jul 01 02:21:18 centos8-builder.lmy.com systemd-coredump[1860]: Process 1404 (ukui-sidebar) of user 0 dumped core.
    Jul 01 02:21:18 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 02:21:18 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 02:21:18 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 02:21:18 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 02:21:18 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 02:21:18 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 02:21:19 centos8-builder.lmy.com systemd-coredump[1847]: Process 1545 (ukui-control-ce) of user 0 dumped core.
                                                                    #16 0x000055a5fcc1ab41 main (ukui-control-center)
                                                                    #18 0x000055a5fcc1aeee _start (ukui-control-center)
    Jul 01 02:21:19 centos8-builder.lmy.com ukui-settings-daemon[1325]: keybindings_filter
    Jul 01 02:21:19 centos8-builder.lmy.com kernel: QDBusConnection[1408]: segfault at 2b1140 ip 00000000002b1140 sp 00007f4d5f0437f8 error 14 in ukui-screensaver-backend[5588e3f03000+d000]
    Jul 01 02:21:19 centos8-builder.lmy.com kernel: QXcbEventQueue[1420]: segfault at 84fa6 ip 0000000000084fa6 sp 00007fb5fc7f3a28 error 14 in ukui-menu[5567c6d5d000+a6000]
    Jul 01 02:21:19 centos8-builder.lmy.com kernel: QXcbEventQueue[1409]: segfault at 84fa6 ip 0000000000084fa6 sp 00007f64561b8a28 error 14 in ukui-flash-disk[559cffa1e000+2c000]
    Jul 01 02:21:19 centos8-builder.lmy.com systemd-coredump[1914]: Process 1271 (ukui-session) of user 0 dumped core.
    Jul 01 02:21:20 centos8-builder.lmy.com systemd-coredump[1917]: Process 1407 (ukui-window-swi) of user 0 dumped core.
    Jul 01 02:21:22 centos8-builder.lmy.com systemd-coredump[1952]: Process 1403 (ukui-screensave) of user 0 dumped core.
    Jul 01 02:21:24 centos8-builder.lmy.com systemd-coredump[1963]: Process 1400 (ukui-menu) of user 0 dumped core.
    Jul 01 02:21:24 centos8-builder.lmy.com systemd-coredump[1962]: Process 1399 (ukui-flash-disk) of user 0 dumped core.
    Jul 01 02:21:53 centos8-builder.lmy.com systemd-coredump[1915]: Process 1326 (ukui-kwin_x11) of user 0 dumped core.
    Jul 01 02:22:11 centos8-builder.lmy.com systemd-coredump[1849]: Process 1324 (ukui-panel) of user 0 dumped core.
    Jul 01 02:46:48 centos8-builder.lmy.com systemd[1]: session-c2.scope: Killing process 2007 (ukui-greeter) with signal SIGTERM.
    Jul 01 02:46:48 centos8-builder.lmy.com at-spi-bus-launcher[1334]: dbus-daemon[1339]: Activating service name='org.a11y.atspi.Registry' requested by ':1.18' (uid=0 pid=3755 comm="/usr/libexec/ukui-settings-daemon " label="unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023")
    Jul 01 02:46:48 centos8-builder.lmy.com ukui-settings-daemon[3755]: use default theme name=Breeze_Snow=
    Jul 01 02:46:48 centos8-builder.lmy.com ukui-settings-daemon[3755]: ------usd_keybindings_manager_start-------
    Jul 01 02:46:48 centos8-builder.lmy.com dbus-daemon[1285]: [session uid=0 pid=1285] Activating service name='org.kde.kglobalaccel' requested by ':1.57' (uid=0 pid=3756 comm="/usr/bin/ukui-kwin_x11 " label="unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023")
    Jul 01 02:46:48 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:48 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Script" listed in "/usr/share/ukui-kwin/scripts/videowall/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Script" listed in "/usr/share/ukui-kwin/scripts/synchronizeskipswitcher/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Script" listed in "/usr/share/ukui-kwin/scripts/minimizeall/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Script" listed in "/usr/share/ukui-kwin/scripts/desktopchangeosd/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_fade/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_fadedesktop/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_dialogparent/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_fadingpopups/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_windowaperture/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_eyeonscreen/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_translucency/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_frozenapp/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_login/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_logout/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_morphingpopups/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_maximize/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_scale/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_squash/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_dimscreen/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_sessionquit/metadata.desktop"
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 848, resource id: 6291460, major code: 18 (ChangeProperty), minor code: 0
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 849, resource id: 6291460, major code: 12 (ConfigureWindow), minor code: 0
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 853, resource id: 6291468, major code: 18 (ChangeProperty), minor code: 0
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 854, resource id: 6291468, major code: 12 (ConfigureWindow), minor code: 0
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 858, resource id: 6291472, major code: 18 (ChangeProperty), minor code: 0
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 859, resource id: 6291472, major code: 12 (ConfigureWindow), minor code: 0
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 865, resource id: 10485778, major code: 3 (GetWindowAttributes), minor code: 0
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: qt.qpa.xcb: QXcbConnection: XCB error: 9 (BadDrawable), sequence: 866, resource id: 10485778, major code: 14 (GetGeometry), minor code: 0
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui_kylin_nm[3811]: Kylin Network Manager Is Already Launched
    Jul 01 02:46:49 centos8-builder.lmy.com ukui_kylin_nm[3811]: Using the icon theme named 'ukui-icon-theme-default'
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-flash-disk[3813]: QMetaObject::connectSlotsByName: No matching signal for on_Maininterface_hide()
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com dbus-daemon[1285]: [session uid=0 pid=1285] Activating via systemd: service name='org.ayatana.bamf' unit='bamfdaemon.service' requested by ':1.68' (uid=0 pid=3814 comm="/usr/bin/ukui-menu " label="unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023")
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-sidebar[3818]: ---------------------------主界面加载完毕---------------------------
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-kwin_x11[3756]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 1015, resource id: 18874372, major code: 12 (ConfigureWindow), minor code: 0
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:49 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui_kylin_nm[3811]: state of network: '0' is connected, '1' is disconnected, '2' is net device switch off
    Jul 01 02:46:50 centos8-builder.lmy.com ukui_kylin_nm[3811]: current network state:  wired state =0,  wifi state =2
    Jul 01 02:46:50 centos8-builder.lmy.com ukui_kylin_nm[3811]: Launch kylin-nm, Lan already connected
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui_kylin_nm[3811]: already insert an active lannet in the top of lan list
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-menu[3814]: qt.qpa.xcb: QXcbConnection: XCB error: 8 (BadMatch), sequence: 424, resource id: 25165831, major code: 42 (SetInputFocus), minor code: 0
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:50 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:51 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:51 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:46:51 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:53:27 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:53:27 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:53:27 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:53:27 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:53:27 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:53:27 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:53:28 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:53:28 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:53:28 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:53:28 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:53:28 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:53:28 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:53:28 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 02:59:51 centos8-builder.lmy.com ukui_kylin_nm[3811]: kylin-nm receive a signal 'Device.Wired PropertiesChanged' about interface.
    Jul 01 03:12:10 centos8-builder.lmy.com kernel: ukui-panel[3754]: segfault at 2b1140 ip 00000000002b1140 sp 00007ffe43216a28 error 14 in ukui-panel[55daae6ef000+144000]
    Jul 01 03:12:10 centos8-builder.lmy.com kernel: MonitorThread[3874]: segfault at 2b1140 ip 00000000002b1140 sp 00007fe13ab677f8 error 14 in ukui-sidebar[55edf826f000+2a000]
    Jul 01 03:12:11 centos8-builder.lmy.com kernel: ukui-session[3711]: segfault at 84b06 ip 0000000000084b06 sp 00007fff79545bd8 error 14 in ukui-session[55eda6431000+ce000]
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com systemd-coredump[4284]: Process 3818 (ukui-sidebar) of user 0 dumped core.
    Jul 01 03:12:11 centos8-builder.lmy.com systemd-coredump[4282]: Process 3754 (ukui-panel) of user 0 dumped core.
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com kernel: QDBusConnection[3821]: segfault at 2b1140 ip 00000000002b1140 sp 00007f697eb117f8 error 14 in ukui-screensaver-backend[5627a728c000+d000]
    Jul 01 03:12:11 centos8-builder.lmy.com ukui-settings-daemon[3755]: keybindings_filter
    Jul 01 03:12:11 centos8-builder.lmy.com kernel: ukui-window-swi[3820]: segfault at 2b1140 ip 00000000002b1140 sp 00007fff8ad27f68 error 14 in ukui-window-switch[55601335b000+40000]
    Jul 01 03:12:11 centos8-builder.lmy.com systemd-coredump[4294]: Process 3711 (ukui-session) of user 0 dumped core.
    Jul 01 03:12:11 centos8-builder.lmy.com systemd-coredump[4311]: Process 3817 (ukui-screensave) of user 0 dumped core.
    Jul 01 03:12:12 centos8-builder.lmy.com systemd-coredump[4324]: Process 3820 (ukui-window-swi) of user 0 dumped core.
    Jul 01 03:12:12 centos8-builder.lmy.com systemd-coredump[4322]: Process 3814 (ukui-menu) of user 0 dumped core.
                                                                    #7  0x0000558303adee4a _ZN20XEventMonitorPrivate3runEv (ukui-menu)
                                                                    #6  0x0000558303a958fc main (ukui-menu)
                                                                    #8  0x0000558303a95c6e _start (ukui-menu)
    Jul 01 03:12:12 centos8-builder.lmy.com systemd-coredump[4323]: Process 3813 (ukui-flash-disk) of user 0 dumped core.
                                                                    #6  0x0000556307064156 main (ukui-flash-disk)
                                                                    #8  0x000055630706433e _start (ukui-flash-disk)
    Jul 01 03:12:26 centos8-builder.lmy.com systemd-coredump[4293]: Process 3756 (ukui-kwin_x11) of user 0 dumped core.
    Jul 01 03:12:42 centos8-builder.lmy.com kernel: ukui-greeter[4458]: segfault at 2b1140 ip 00000000002b1140 sp 00007ffd918c9408 error 14 in ukui-greeter[565535a8f000+c6000]
    Jul 01 03:12:42 centos8-builder.lmy.com systemd-coredump[4882]: Process 4458 (ukui-greeter) of user 993 dumped core.
    Jul 01 03:18:05 centos8-builder.lmy.com kernel: MonitorWatcher[4934]: segfault at 84c36 ip 0000000000084c36 sp 00007fb7708e5968 error 14 in ukui-greeter[560ffbb3b000+c6000]
    Jul 01 03:18:06 centos8-builder.lmy.com systemd-coredump[7115]: Process 4925 (ukui-greeter) of user 993 dumped core.
    Jul 01 03:27:04 centos8-builder.lmy.com kernel: ukui-greeter[7162]: segfault at 2b1140 ip 00000000002b1140 sp 00007ffd678c76b8 error 14 in ukui-greeter[55a104b3d000+c6000]
    Jul 01 03:27:06 centos8-builder.lmy.com systemd-coredump[8917]: Process 7162 (ukui-greeter) of user 993 dumped core.
    Jul 01 03:31:12 centos8-builder.lmy.com kernel: ukui-greeter[9004]: segfault at 2b1140 ip 00000000002b1140 sp 00007ffd1fac6d78 error 14 in ukui-greeter[5609acad4000+c6000]
    Jul 01 03:31:12 centos8-builder.lmy.com systemd-coredump[10580]: Process 9004 (ukui-greeter) of user 993 dumped core.
    Jul 01 03:31:22 centos8-builder.lmy.com kernel: ukui-greeter[10702]: segfault at 2b1140 ip 00000000002b1140 sp 00007ffe47f6d888 error 14 in ukui-greeter[55e7d9a9b000+c6000]
    Jul 01 03:31:22 centos8-builder.lmy.com systemd-coredump[10742]: Process 10702 (ukui-greeter) of user 993 dumped core.
    Jul 01 03:32:14 centos8-builder.lmy.com systemd[1]: session-c8.scope: Killing process 10871 (ukui-greeter) with signal SIGTERM.
    Jul 01 03:32:16 centos8-builder.lmy.com at-spi-bus-launcher[1334]: dbus-daemon[1339]: Activating service name='org.a11y.atspi.Registry' requested by ':1.22' (uid=0 pid=11233 comm="/usr/libexec/ukui-settings-daemon " label="unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023")
    Jul 01 03:32:16 centos8-builder.lmy.com ukui-settings-daemon[11233]: use default theme name=Breeze_Snow=
    Jul 01 03:32:17 centos8-builder.lmy.com ukui-settings-daemon[11233]: ------usd_keybindings_manager_start-------
    Jul 01 03:32:17 centos8-builder.lmy.com dbus-daemon[1285]: [session uid=0 pid=1285] Activating service name='org.kde.kglobalaccel' requested by ':1.87' (uid=0 pid=11234 comm="/usr/bin/ukui-kwin_x11 " label="unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023")
    Jul 01 03:32:17 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui_kylin_nm[11287]: Kylin Network Manager Is Already Launched
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-flash-disk[11288]: QMetaObject::connectSlotsByName: No matching signal for on_Maininterface_hide()
    Jul 01 03:32:18 centos8-builder.lmy.com ukui_kylin_nm[11287]: Using the icon theme named 'ukui-icon-theme-default'
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com dbus-daemon[1285]: [session uid=0 pid=1285] Activating via systemd: service name='org.ayatana.bamf' unit='bamfdaemon.service' requested by ':1.99' (uid=0 pid=11289 comm="/usr/bin/ukui-menu " label="unconfined_u:unconfined_r:unconfined_t:s0-s0:c0.c1023")
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-sidebar[11294]: ---------------------------主界面加载完毕---------------------------
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:18 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-kwin_x11[11234]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 643, resource id: 6291460, major code: 12 (ConfigureWindow), minor code: 0
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-kwin_x11[11234]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 644, resource id: 6291468, major code: 12 (ConfigureWindow), minor code: 0
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-kwin_x11[11234]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 645, resource id: 6291472, major code: 12 (ConfigureWindow), minor code: 0
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-kwin_x11[11234]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 784, resource id: 23068676, major code: 12 (ConfigureWindow), minor code: 0
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Script" listed in "/usr/share/ukui-kwin/scripts/videowall/metadata.desktop"
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Script" listed in "/usr/share/ukui-kwin/scripts/synchronizeskipswitcher/metadata.desktop"
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Script" listed in "/usr/share/ukui-kwin/scripts/minimizeall/metadata.desktop"
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Script" listed in "/usr/share/ukui-kwin/scripts/desktopchangeosd/metadata.desktop"
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:19 centos8-builder.lmy.com ukui-menu[11289]: qt.qpa.xcb: QXcbConnection: XCB error: 8 (BadMatch), sequence: 448, resource id: 29360135, major code: 42 (SetInputFocus), minor code: 0
    Jul 01 03:32:19 centos8-builder.lmy.com ukui_kylin_nm[11287]: state of network: '0' is connected, '1' is disconnected, '2' is net device switch off
    Jul 01 03:32:19 centos8-builder.lmy.com ukui_kylin_nm[11287]: current network state:  wired state =0,  wifi state =2
    Jul 01 03:32:19 centos8-builder.lmy.com ukui_kylin_nm[11287]: Launch kylin-nm, Lan already connected
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_fade/metadata.desktop"
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_fadedesktop/metadata.desktop"
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_dialogparent/metadata.desktop"
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_fadingpopups/metadata.desktop"
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_windowaperture/metadata.desktop"
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_eyeonscreen/metadata.desktop"
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_translucency/metadata.desktop"
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_frozenapp/metadata.desktop"
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_login/metadata.desktop"
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_logout/metadata.desktop"
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_morphingpopups/metadata.desktop"
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_maximize/metadata.desktop"
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_scale/metadata.desktop"
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_squash/metadata.desktop"
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_dimscreen/metadata.desktop"
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-kwin_x11[11234]: kf5.kcoreaddons.desktopparser: Unable to find service type for service "UKUIKWin/Effect" listed in "/usr/share/ukui-kwin/effects/kwin4_effect_sessionquit/metadata.desktop"
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-kwin_x11[11234]: qt.qpa.xcb: QXcbConnection: XCB error: 3 (BadWindow), sequence: 1188, resource id: 10485786, major code: 3 (GetWindowAttributes), minor code: 0
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-kwin_x11[11234]: qt.qpa.xcb: QXcbConnection: XCB error: 9 (BadDrawable), sequence: 1189, resource id: 10485786, major code: 14 (GetGeometry), minor code: 0
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:20 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:21 centos8-builder.lmy.com ukui_kylin_nm[11287]: already insert an active lannet in the top of lan list
    Jul 01 03:32:21 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:21 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:21 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:21 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:21 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:21 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:21 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:21 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:21 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:21 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:21 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:21 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:21 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:22 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:22 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:22 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:23 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:24 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:24 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:24 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:24 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:24 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:24 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:24 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:24 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:24 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:24 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:25 centos8-builder.lmy.com ukui-kwin_x11[11234]: Module 'org.ukui.kwin.decoration' does not contain a module identifier directive - it cannot be protected from external registrations.
    Jul 01 03:32:25 centos8-builder.lmy.com ukui-kwin_x11[11234]: Icon theme "gnome" not found.
    Jul 01 03:32:25 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:25 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:25 centos8-builder.lmy.com ukui-kwin_x11[11234]: QPainter::begin: Paint device returned engine == 0, type: 3
    Jul 01 03:32:25 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:25 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:25 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:25 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:25 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:25 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:25 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:25 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:25 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:25 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:25 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:25 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:25 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:26 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:26 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:26 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:26 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:26 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:26 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:26 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:26 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:26 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:26 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:26 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:26 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:26 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:30 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:30 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:30 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:30 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:30 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:30 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:30 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:32:30 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:40:34 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:40:34 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:40:34 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:40:34 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:40:34 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:40:34 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:40:34 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:40:34 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:40:34 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:40:34 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:40:34 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:40:34 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:40:34 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:44:51 centos8-builder.lmy.com ukui_kylin_nm[11287]: kylin-nm receive a signal 'Device.Wired PropertiesChanged' about interface.
    Jul 01 03:52:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:52:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:52:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:52:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:52:47 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:52:47 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:57:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:57:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:57:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:57:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:57:47 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:57:47 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 03:59:51 centos8-builder.lmy.com ukui_kylin_nm[11287]: kylin-nm receive a signal 'Device.Wired PropertiesChanged' about interface.
    Jul 01 04:02:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:02:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:02:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:02:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:02:47 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:02:47 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:07:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:07:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:07:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:07:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:07:47 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:07:47 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:12:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:12:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:12:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:12:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:12:47 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:12:47 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:14:51 centos8-builder.lmy.com ukui_kylin_nm[11287]: kylin-nm receive a signal 'Device.Wired PropertiesChanged' about interface.
    Jul 01 04:17:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:17:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:17:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:17:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:17:47 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:17:47 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:22:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:22:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:22:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:22:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:22:47 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:22:47 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:27:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:27:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:27:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:27:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:27:47 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:27:47 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:29:51 centos8-builder.lmy.com ukui_kylin_nm[11287]: kylin-nm receive a signal 'Device.Wired PropertiesChanged' about interface.
    Jul 01 04:32:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:32:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:32:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:32:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:32:47 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:32:47 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:37:45 centos8-builder.lmy.com kernel: MonitorThread[11376]: segfault at 2b1140 ip 00000000002b1140 sp 00007ffa5987e7f8 error 14 in ukui-sidebar[562a06d1d000+2a000]
    Jul 01 04:37:46 centos8-builder.lmy.com kernel: ukui-panel[11232]: segfault at 2b1140 ip 00000000002b1140 sp 00007ffd92af2338 error 14 in ukui-panel[55d2401af000+144000]
    Jul 01 04:37:46 centos8-builder.lmy.com kernel: ukui-session[11181]: segfault at 84b06 ip 0000000000084b06 sp 00007ffd1d97c918 error 14 in ukui-session[55c440f20000+ce000]
    Jul 01 04:37:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:37:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:37:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:37:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:37:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:37:46 centos8-builder.lmy.com systemd-coredump[36846]: Process 11294 (ukui-sidebar) of user 0 dumped core.
    Jul 01 04:37:46 centos8-builder.lmy.com kernel: QDBusConnection[11297]: segfault at 2b1140 ip 00000000002b1140 sp 00007f5c865f17f8 error 14 in ukui-screensaver-backend[55b4f16c6000+d000]
    Jul 01 04:37:46 centos8-builder.lmy.com ukui-settings-daemon[11233]: keybindings_filter
    Jul 01 04:37:46 centos8-builder.lmy.com kernel: ukui-window-swi[11296]: segfault at 2b1140 ip 00000000002b1140 sp 00007fff4b583a88 error 14 in ukui-window-switch[562faa071000+40000]
    Jul 01 04:37:46 centos8-builder.lmy.com kernel: QXcbEventQueue[11316]: segfault at 84fa6 ip 0000000000084fa6 sp 00007f2b5a66aa28 error 14 in ukui-menu[55e031d9f000+a6000]
    Jul 01 04:37:46 centos8-builder.lmy.com kernel: QXcbEventQueue[11305]: segfault at 84fa6 ip 0000000000084fa6 sp 00007f55c313ea28 error 14 in ukui-flash-disk[555e50aaf000+2c000]
    Jul 01 04:37:46 centos8-builder.lmy.com systemd-coredump[36852]: Process 11181 (ukui-session) of user 0 dumped core.
    Jul 01 04:37:46 centos8-builder.lmy.com systemd-coredump[36848]: Process 11232 (ukui-panel) of user 0 dumped core.
    Jul 01 04:37:47 centos8-builder.lmy.com systemd-coredump[36873]: Process 11289 (ukui-menu) of user 0 dumped core.
    Jul 01 04:37:47 centos8-builder.lmy.com systemd-coredump[36860]: Process 11293 (ukui-screensave) of user 0 dumped core.
    Jul 01 04:37:47 centos8-builder.lmy.com systemd-coredump[36871]: Process 11296 (ukui-window-swi) of user 0 dumped core.
    Jul 01 04:37:47 centos8-builder.lmy.com systemd-coredump[36874]: Process 11288 (ukui-flash-disk) of user 0 dumped core.
    Jul 01 04:37:58 centos8-builder.lmy.com systemd-coredump[36851]: Process 11234 (ukui-kwin_x11) of user 0 dumped core.
    Jul 01 04:38:17 centos8-builder.lmy.com kernel: ukui-greeter[37021]: segfault at 2b1140 ip 00000000002b1140 sp 00007fffb1c117f8 error 14 in ukui-greeter[55c6dcb5c000+c6000]
    Jul 01 04:38:18 centos8-builder.lmy.com systemd-coredump[37449]: Process 37021 (ukui-greeter) of user 993 dumped core.
    ```   


  3. ukui-kwin build failed on fedora 33 as kscreenlocker-devel don't have function such as setWaylandDisplay,greeterClientConnectionChanged,greeterClientConnection
    ```
    make[3]: Entering directory '/root/rpmbuild/BUILD/ukui-kwin-master/cmake-build'
    [ 64%] Building CXX object CMakeFiles/ukui-kwin.dir/wayland_server.cpp.o
    /usr/bin/g++ -DKCOREADDONS_LIB -DQT_CONCURRENT_LIB -DQT_CORE_LIB -DQT_DBUS_LIB -DQT_DISABLE_DEPRECATED_BEFORE=0 -DQT_GUI_LIB -DQT_NETWORK_LIB -DQT_NO_DEBUG -DQT_NO_URL_CAST_FROM_STRING -DQT_QMLMODELS_LIB -DQT_QML_LIB -DQT_QUICK_LIB -DQT_SCRIPT_LIB -DQT_SENSORS_LIB -DQT_USE_QSTRINGBUILDER -DQT_WIDGETS_LIB -DQT_X11EXTRAS_LIB -DQT_XML_LIB -D_GNU_SOURCE -D_LARGEFILE64_SOURCE -Dukui_kwin_EXPORTS -I/root/rpmbuild/BUILD/ukui-kwin-master/cmake-build -I/root/rpmbuild/BUILD/ukui-kwin-master -I/root/rpmbuild/BUILD/ukui-kwin-master/cmake-build/ukui-kwin_autogen/include -I/root/rpmbuild/BUILD/ukui-kwin-master/platformsupport -I/root/rpmbuild/BUILD/ukui-kwin-master/tabbox -I/root/rpmbuild/BUILD/ukui-kwin-master/effects -I/root/rpmbuild/BUILD/ukui-kwin-master/libkwineffects -I/root/rpmbuild/BUILD/ukui-kwin-master/cmake-build/libkwineffects -I/root/rpmbuild/BUILD/ukui-kwin-master/cmake-build/effects -I/usr/include/qt5/QGSettings -I/usr/include/qt5/QtGui/5.14.2 -I/usr/include/qt5/QtGui/5.14.2/QtGui -I/usr/include/qt5/QtCore/5.14.2 -I/usr/include/qt5/QtCore/5.14.2/QtCore -isystem /usr/include/qt5 -isystem /usr/include/qt5/QtDBus -isystem /usr/include/qt5/QtCore -isystem /usr/lib64/qt5/mkspecs/linux-g++ -isystem /usr/include/qt5/QtWidgets -isystem /usr/include/qt5/QtGui -isystem /usr/include/qt5/QtQuick -isystem /usr/include/qt5/QtQmlModels -isystem /usr/include/qt5/QtQml -isystem /usr/include/qt5/QtNetwork -isystem /usr/include/KF5/KConfigCore -isystem /usr/include/KF5 -isystem /usr/include/KF5/KCoreAddons -isystem /usr/include/KF5/KWindowSystem -isystem /usr/include/KF5/KDeclarative -isystem /usr/include/KF5/KPackage -isystem /usr/include/qt5/QtConcurrent -isystem /usr/include/qt5/QtScript -isystem /usr/include/qt5/QtSensors -isystem /usr/include/KF5/KConfigWidgets -isystem /usr/include/KF5/KCodecs -isystem /usr/include/KF5/KWidgetsAddons -isystem /usr/include/KF5/KConfigGui -isystem /usr/include/qt5/QtXml -isystem /usr/include/KF5/KAuth -isystem /usr/include/KF5/KGlobalAccel -isystem /usr/include/qt5/QtX11Extras -isystem /usr/include/KF5/KI18n -isystem /usr/include/KF5/KNotifications -isystem /usr/include/KF5/Plasma -isystem /usr/include/KF5/KService -isystem /usr/include/KDecoration2 -isystem /usr/include/KScreenLocker -isystem /usr/include/KF5/KActivities -isystem /usr/include/KF5/KWayland/Client -isystem /usr/include/KF5/KWayland/Server -O2 -fexceptions -g -grecord-gcc-switches -pipe -Wall -Werror=format-security -Wp,-D_FORTIFY_SOURCE=2 -Wp,-D_GLIBCXX_ASSERTIONS -specs=/usr/lib/rpm/redhat/redhat-hardened-cc1 -fstack-protector-strong -specs=/usr/lib/rpm/redhat/redhat-annobin-cc1  -m64 -mtune=generic -fasynchronous-unwind-tables -fstack-clash-protection -fcf-protection -fno-operator-names -fno-exceptions -Wall -Wextra -Wcast-align -Wchar-subscripts -Wformat-security -Wno-long-long -Wpointer-arith -Wundef -Wnon-virtual-dtor -Woverloaded-virtual -Werror=return-type -Wvla -Wdate-time -Wsuggest-override -Wlogical-op -fPIC -fvisibility=hidden -fvisibility-inlines-hidden -fPIC -std=gnu++14 -o CMakeFiles/ukui-kwin.dir/wayland_server.cpp.o -c /root/rpmbuild/BUILD/ukui-kwin-master/wayland_server.cpp
    /root/rpmbuild/BUILD/ukui-kwin-master/wayland_server.cpp: In member function 'void KWin::WaylandServer::initScreenLocker()':
    /root/rpmbuild/BUILD/ukui-kwin-master/wayland_server.cpp:518:36: error: 'class ScreenLocker::KSldApp' has no member named 'setWaylandDisplay'
      518 |     ScreenLocker::KSldApp::self()->setWaylandDisplay(m_display);
          |                                    ^~~~~~~~~~~~~~~~~
    /root/rpmbuild/BUILD/ukui-kwin-master/wayland_server.cpp:522:68: error: 'greeterClientConnectionChanged' is not a member of 'ScreenLocker::KSldApp'
      522 |     connect(ScreenLocker::KSldApp::self(), &ScreenLocker::KSldApp::greeterClientConnectionChanged, this,
          |                                                                    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    /root/rpmbuild/BUILD/ukui-kwin-master/wayland_server.cpp: In lambda function:
    /root/rpmbuild/BUILD/ukui-kwin-master/wayland_server.cpp:524:77: error: 'class ScreenLocker::KSldApp' has no member named 'greeterClientConnection'
      524 |             m_screenLockerClientConnection = ScreenLocker::KSldApp::self()->greeterClientConnection();
          |                                                                             ^~~~~~~~~~~~~~~~~~~~~~~
    /root/rpmbuild/BUILD/ukui-kwin-master/wayland_server.cpp: In member function 'quint16 KWin::WaylandServer::createClientId(KWayland::Server::ClientConnection*)':
    /root/rpmbuild/BUILD/ukui-kwin-master/wayland_server.cpp:740:43: warning: 'QSet<T> QList<T>::toSet() const [with T = short unsigned int]' is deprecated: Use QSet<T>(list.begin(), list.end()) instead. [-Wdeprecated-declarations]
      740 |     auto ids = m_clientIds.values().toSet();
    ```

  4. peony-extensions don't have install target in CMake config, thus need to copy it manually
  5. many repos don't support set the libdir correctly
  6. ukui-system-monitor missing target to create qm files
  7. ukui-biometric-auth, ukui-polkit file /etc/xdg/autostart/polkit-ukui-authentication-agent-1.desktop has wrong polkit-ukui-authentication-agent-1 path, it should be /usr/lib64/ukui-polkit/polkit-ukui-authentication-agent-1 instead of /usr/lib//ukui-polkit/polkit-ukui-authentication-agent-1
  8. monitor resolution can't be restore after logout or reboot, but I can see there is a file ~/.config/monitors.xml which has stored last settings.