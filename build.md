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
  ```
  ../../../../src/drivers/community-multidevice/community_ops.h:50:54: error: 'FP_ENROLL_COMPLETE' undeclared here (not in a function)
    50 |  COMMUNITY_ENROLL_COMPLETE = COMMUNITY_ENROLL_BASE + FP_ENROLL_COMPLETE,
        |                                                      ^~~~~~~~~~~~~~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.h:57:50: error: 'FP_ENROLL_FAIL' undeclared here (not in a function); did you mean 'OPS_ENROLL_FAIL'?
    57 |  COMMUNITY_ENROLL_FAIL = COMMUNITY_ENROLL_BASE + FP_ENROLL_FAIL,
        |                                                  ^~~~~~~~~~~~~~
        |                                                  OPS_ENROLL_FAIL
  ../../../../src/drivers/community-multidevice/community_ops.h:63:50: error: 'FP_ENROLL_PASS' undeclared here (not in a function)
    63 |  COMMUNITY_ENROLL_PASS = COMMUNITY_ENROLL_BASE + FP_ENROLL_PASS,
        |                                                  ^~~~~~~~~~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.h:70:51: error: 'FP_ENROLL_RETRY' undeclared here (not in a function)
    70 |  COMMUNITY_COMMON_RETRY = COMMUNITY_ENROLL_BASE + FP_ENROLL_RETRY,
        |                                                   ^~~~~~~~~~~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.h:76:61: error: 'FP_ENROLL_RETRY_TOO_SHORT' undeclared here (not in a function); did you mean 'FP_DEVICE_RETRY_TOO_SHORT'?
    76 |  COMMUNITY_COMMON_RETRY_TOO_SHORT = COMMUNITY_ENROLL_BASE + FP_ENROLL_RETRY_TOO_SHORT,
        |                                                             ^~~~~~~~~~~~~~~~~~~~~~~~~
        |                                                             FP_DEVICE_RETRY_TOO_SHORT
  ../../../../src/drivers/community-multidevice/community_ops.h:82:65: error: 'FP_ENROLL_RETRY_CENTER_FINGER' undeclared here (not in a function); did you mean 'FP_DEVICE_RETRY_CENTER_FINGER'?
    82 |  COMMUNITY_COMMON_RETRY_CENTER_FINGER = COMMUNITY_ENROLL_BASE + FP_ENROLL_RETRY_CENTER_FINGER,
        |                                                                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        |                                                                 FP_DEVICE_RETRY_CENTER_FINGER
  ../../../../src/drivers/community-multidevice/community_ops.h:89:65: error: 'FP_ENROLL_RETRY_REMOVE_FINGER' undeclared here (not in a function); did you mean 'FP_DEVICE_RETRY_REMOVE_FINGER'?
    89 |  COMMUNITY_COMMON_RETRY_REMOVE_FINGER = COMMUNITY_ENROLL_BASE + FP_ENROLL_RETRY_REMOVE_FINGER,
        |                                                                 ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        |                                                                 FP_DEVICE_RETRY_REMOVE_FINGER
  ../../../../src/drivers/community-multidevice/community_ops.c:89:22: warning: 'struct fp_img' declared inside parameter list will not be visible outside of this definition or declaration
    89 |               struct fp_img *img,
        |                      ^~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.c:101:21: warning: 'struct fp_img' declared inside parameter list will not be visible outside of this definition or declaration
    101 |              struct fp_img *img,
        |                     ^~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.c: In function 'community_ops_enroll':
  ../../../../src/drivers/community-multidevice/community_ops.c:343:9: warning: implicit declaration of function 'fp_print_data_get_data'; did you mean 'fp_print_to_data'? [-Wimplicit-function-declaration]
    343 |   len = fp_print_data_get_data(cfpdev->enrolled_print, &plaintext);
        |         ^~~~~~~~~~~~~~~~~~~~~~
        |         fp_print_to_data
  ../../../../src/drivers/community-multidevice/community_ops.c:344:3: warning: implicit declaration of function 'fp_print_data_free'; did you mean 'fp_print_get_type'? [-Wimplicit-function-declaration]
    344 |   fp_print_data_free(cfpdev->enrolled_print);
        |   ^~~~~~~~~~~~~~~~~~
        |   fp_print_get_type
  ../../../../src/drivers/community-multidevice/community_ops.c: In function 'community_internal_device_init':
  ../../../../src/drivers/community-multidevice/community_ops.c:878:2: warning: implicit declaration of function 'fp_init' [-Wimplicit-function-declaration]
    878 |  fp_init();
        |  ^~~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.c:880:20: warning: implicit declaration of function 'fp_discover_devs' [-Wimplicit-function-declaration]
    880 |  discovered_devs = fp_discover_devs();
        |                    ^~~~~~~~~~~~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.c:880:18: warning: assignment to 'struct fp_dscv_dev **' from 'int' makes pointer from integer without a cast [-Wint-conversion]
    880 |  discovered_devs = fp_discover_devs();
        |                  ^
  ../../../../src/drivers/community-multidevice/community_ops.c:887:9: warning: implicit declaration of function 'fp_dscv_dev_get_driver'; did you mean 'fp_device_get_driver'? [-Wimplicit-function-declaration]
    887 |   drv = fp_dscv_dev_get_driver(ddev);
        |         ^~~~~~~~~~~~~~~~~~~~~~
        |         fp_device_get_driver
  ../../../../src/drivers/community-multidevice/community_ops.c:887:7: warning: assignment to 'struct fp_driver *' from 'int' makes pointer from integer without a cast [-Wint-conversion]
    887 |   drv = fp_dscv_dev_get_driver(ddev);
        |       ^
  ../../../../src/drivers/community-multidevice/community_ops.c:888:12: warning: implicit declaration of function 'fp_driver_get_driver_id'; did you mean 'fp_device_get_driver'? [-Wimplicit-function-declaration]
    888 |   drv_id = fp_driver_get_driver_id(drv);
        |            ^~~~~~~~~~~~~~~~~~~~~~~
        |            fp_device_get_driver
  ../../../../src/drivers/community-multidevice/community_ops.c:892:20: warning: implicit declaration of function 'fp_dev_open'; did you mean 'fp_device_open'? [-Wimplicit-function-declaration]
    892 |    community_dev = fp_dev_open(ddev);
        |                    ^~~~~~~~~~~
        |                    fp_device_open
  ../../../../src/drivers/community-multidevice/community_ops.c:892:18: warning: assignment to 'struct fp_dev *' from 'int' makes pointer from integer without a cast [-Wint-conversion]
    892 |    community_dev = fp_dev_open(ddev);
        |                  ^
  ../../../../src/drivers/community-multidevice/community_ops.c:896:11: warning: implicit declaration of function 'fp_driver_get_full_name'; did you mean 'fp_print_get_username'? [-Wimplicit-function-declaration]
    896 |           fp_driver_get_full_name(drv));
        |           ^~~~~~~~~~~~~~~~~~~~~~~
        |           fp_print_get_username
  ../../../../src/drivers/community-multidevice/community_ops.c:903:2: warning: implicit declaration of function 'fp_dscv_devs_free' [-Wimplicit-function-declaration]
    903 |  fp_dscv_devs_free(discovered_devs);
        |  ^~~~~~~~~~~~~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.c:917:26: warning: implicit declaration of function 'fp_dev_get_nr_enroll_stages'; did you mean 'fp_device_get_nr_enroll_stages'? [-Wimplicit-function-declaration]
    917 |   cfpdev->enroll_times = fp_dev_get_nr_enroll_stages(community_dev);
        |                          ^~~~~~~~~~~~~~~~~~~~~~~~~~~
        |                          fp_device_get_nr_enroll_stages
  ../../../../src/drivers/community-multidevice/community_ops.c: In function 'community_internal_device_free':
  ../../../../src/drivers/community-multidevice/community_ops.c:929:2: warning: implicit declaration of function 'fp_dev_close'; did you mean 'fp_device_close'? [-Wimplicit-function-declaration]
    929 |  fp_dev_close(community_dev);
        |  ^~~~~~~~~~~~
        |  fp_device_close
  ../../../../src/drivers/community-multidevice/community_ops.c:940:2: warning: implicit declaration of function 'fp_exit'; did you mean '_exit'? [-Wimplicit-function-declaration]
    940 |  fp_exit();
        |  ^~~~~~~
        |  _exit
  ../../../../src/drivers/community-multidevice/community_ops.c: In function 'community_internal_create_fp_data':
  ../../../../src/drivers/community-multidevice/community_ops.c:998:22: warning: implicit declaration of function 'fp_print_data_from_data'; did you mean 'fp_print_new_from_data'? [-Wimplicit-function-declaration]
    998 |    fp_data_list[i] = fp_print_data_from_data(plaintext, len);
        |                      ^~~~~~~~~~~~~~~~~~~~~~~
        |                      fp_print_new_from_data
  ../../../../src/drivers/community-multidevice/community_ops.c:998:20: warning: assignment to 'struct fp_print_data *' from 'int' makes pointer from integer without a cast [-Wint-conversion]
    998 |    fp_data_list[i] = fp_print_data_from_data(plaintext, len);
        |                    ^
  ../../../../src/drivers/community-multidevice/community_ops.c: In function 'community_internal_enroll':
  ../../../../src/drivers/community-multidevice/community_ops.c:1060:6: warning: implicit declaration of function 'fp_async_enroll_start' [-Wimplicit-function-declaration]
  1060 |  r = fp_async_enroll_start(community_dev,
        |      ^~~~~~~~~~~~~~~~~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.c: At top level:
  ../../../../src/drivers/community-multidevice/community_ops.c:1081:22: warning: 'struct fp_img' declared inside parameter list will not be visible outside of this definition or declaration
  1081 |               struct fp_img *img,
        |                      ^~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.c:1078:13: error: conflicting types for 'community_internal_enroll_stage_cb'
  1078 | static void community_internal_enroll_stage_cb(struct fp_dev *fpdev,
        |             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.c:86:13: note: previous declaration of 'community_internal_enroll_stage_cb' was here
    86 | static void community_internal_enroll_stage_cb(struct fp_dev *fpdev,
        |             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.c: In function 'community_internal_enroll_stop':
  ../../../../src/drivers/community-multidevice/community_ops.c:1174:2: warning: implicit declaration of function 'fp_async_enroll_stop' [-Wimplicit-function-declaration]
  1174 |  fp_async_enroll_stop(community_dev,
        |  ^~~~~~~~~~~~~~~~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.c: In function 'community_internal_identify':
  ../../../../src/drivers/community-multidevice/community_ops.c:1225:6: warning: implicit declaration of function 'fp_async_identify_start' [-Wimplicit-function-declaration]
  1225 |  r = fp_async_identify_start(community_dev, print_gallery,
        |      ^~~~~~~~~~~~~~~~~~~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.c:1241:7: warning: implicit declaration of function 'fp_handle_events_timeout'; did you mean 'libusb_handle_events_timeout'? [-Wimplicit-function-declaration]
  1241 |   r = fp_handle_events_timeout(&(cfpdev->ops_detection_interval_tv));
        |       ^~~~~~~~~~~~~~~~~~~~~~~~
        |       libusb_handle_events_timeout
  ../../../../src/drivers/community-multidevice/community_ops.c: At top level:
  ../../../../src/drivers/community-multidevice/community_ops.c:1269:21: warning: 'struct fp_img' declared inside parameter list will not be visible outside of this definition or declaration
  1269 |              struct fp_img *img,
        |                     ^~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.c:1266:6: error: conflicting types for 'community_internal_identify_cb'
  1266 | void community_internal_identify_cb(struct fp_dev *fpdev,
        |      ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.c:98:13: note: previous declaration of 'community_internal_identify_cb' was here
    98 | static void community_internal_identify_cb(struct fp_dev *fpdev,
        |             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.c: In function 'community_internal_identify_cb':
  ../../../../src/drivers/community-multidevice/community_ops.c:1280:12: error: 'FP_VERIFY_NO_MATCH' undeclared (first use in this function); did you mean 'OPS_VERIFY_NO_MATCH'?
  1280 |   result = FP_VERIFY_NO_MATCH;
        |            ^~~~~~~~~~~~~~~~~~
        |            OPS_VERIFY_NO_MATCH
  ../../../../src/drivers/community-multidevice/community_ops.c:1280:12: note: each undeclared identifier is reported only once for each function it appears in
  ../../../../src/drivers/community-multidevice/community_ops.c:1289:8: error: 'FP_VERIFY_MATCH' undeclared (first use in this function); did you mean 'OPS_VERIFY_MATCH'?
  1289 |   case FP_VERIFY_MATCH:
        |        ^~~~~~~~~~~~~~~
        |        OPS_VERIFY_MATCH
  ../../../../src/drivers/community-multidevice/community_ops.c:1293:8: error: 'FP_VERIFY_RETRY' undeclared (first use in this function); did you mean 'FP_DEVICE_RETRY'?
  1293 |   case FP_VERIFY_RETRY:
        |        ^~~~~~~~~~~~~~~
        |        FP_DEVICE_RETRY
  ../../../../src/drivers/community-multidevice/community_ops.c:1297:8: error: 'FP_VERIFY_RETRY_TOO_SHORT' undeclared (first use in this function); did you mean 'FP_DEVICE_RETRY_TOO_SHORT'?
  1297 |   case FP_VERIFY_RETRY_TOO_SHORT:
        |        ^~~~~~~~~~~~~~~~~~~~~~~~~
        |        FP_DEVICE_RETRY_TOO_SHORT
  ../../../../src/drivers/community-multidevice/community_ops.c:1301:8: error: 'FP_VERIFY_RETRY_CENTER_FINGER' undeclared (first use in this function); did you mean 'FP_DEVICE_RETRY_CENTER_FINGER'?
  1301 |   case FP_VERIFY_RETRY_CENTER_FINGER:
        |        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        |        FP_DEVICE_RETRY_CENTER_FINGER
  ../../../../src/drivers/community-multidevice/community_ops.c:1305:8: error: 'FP_VERIFY_RETRY_REMOVE_FINGER' undeclared (first use in this function); did you mean 'FP_DEVICE_RETRY_REMOVE_FINGER'?
  1305 |   case FP_VERIFY_RETRY_REMOVE_FINGER:
        |        ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        |        FP_DEVICE_RETRY_REMOVE_FINGER
  ../../../../src/drivers/community-multidevice/community_ops.c: In function 'community_internal_identify_stop':
  ../../../../src/drivers/community-multidevice/community_ops.c:1329:2: warning: implicit declaration of function 'fp_async_identify_stop' [-Wimplicit-function-declaration]
  1329 |  fp_async_identify_stop(community_dev,
        |  ^~~~~~~~~~~~~~~~~~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.c: At top level:
  ../../../../src/drivers/community-multidevice/community_ops.c:86:13: warning: 'community_internal_enroll_stage_cb' used but never defined
    86 | static void community_internal_enroll_stage_cb(struct fp_dev *fpdev,
        |             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.c:98:13: warning: 'community_internal_identify_cb' used but never defined
    98 | static void community_internal_identify_cb(struct fp_dev *fpdev,
        |             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ../../../../src/drivers/community-multidevice/community_ops.c:1078:13: warning: 'community_internal_enroll_stage_cb' defined but not used [-Wunused-function]
  1078 | static void community_internal_enroll_stage_cb(struct fp_dev *fpdev,
        |             ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  make[5]: *** [Makefile:1365: ../../../../src/drivers/community-multidevice/upekts_la-community_ops.lo] Error 1
  make[5]: Leaving directory '/root/rpmbuild/BUILD/biometric-authentication-0.9.62/src/drivers/community-multidevice/drivers'
  make[4]: *** [Makefile:406: all-recursive] Error 1
  make[4]: Leaving directory '/root/rpmbuild/BUILD/biometric-authentication-0.9.62/src/drivers/community-multidevice'
  make[3]: *** [Makefile:407: all-recursive] Error 1
  make[3]: Leaving directory '/root/rpmbuild/BUILD/biometric-authentication-0.9.62/src/drivers'
  make[2]: *** [Makefile:618: all-recursive] Error 1
  make[2]: Leaving directory '/root/rpmbuild/BUILD/biometric-authentication-0.9.62/src'
  make[1]: *** [Makefile:454: all-recursive] Error 1
  make[1]: Leaving directory '/root/rpmbuild/BUILD/biometric-authentication-0.9.62'
  make: *** [Makefile:386: all] Error 2
  error: Bad exit status from /var/tmp/rpm-tmp.9sYjKJ (%build)」
  ```