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
1.  ukui-panel with errors 
      ```
      (0x7ffc66705c50) Warning: "Icon Theme not set. Fallbacking to Oxygen, if installed"
      (0x7ffc66705c50) Warning: "Fallback Icon Theme (Oxygen) not found"
      (0x7ffc66705c50) Warning: QCoreApplication::postEvent: Unexpected null receiver
      ```
