
pipeline {
  agent {
        label 'fedora'
    }
  environment {
        TOP = "${HOME}/rpmbuild"
    }

  stages {
    
    stage ('prepare environment') { 
        steps {
        	sh  '''
            mkdir -p ${TOP}/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
            dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  ruby  mysql-devel ruby-devel rubygems  meson ninja-build qt5-qtbase
            strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5
            gem install sass bundler rails compass
          '''

        }
    }
    stage ('build and install peony ') { 

             steps { 
              sh '''
                  cp peony/peony-libdir.patch ${TOP}/SOURCES
                  cp peony/peony.spec ${TOP}/SPECS
                  dnf install -y $(grep  BuildRequires ${TOP}/SPECS/peony.spec | awk '{print $2}')
                  rpmbuild --define "_topdir ${TOP}" -bb ${TOP}/SPECS/peony.spec
              '''
         
              sh '''
                dnf -y install ${TOP}/RPMS/x86_64/{peony-2.2.0-1.fc32.x86_64.rpm,peony-common-2.2.0-1.fc32.x86_64.rpm,peony-devel-2.2.0-1.fc32.x86_64.rpm,peony-libs-2.2.0-1.fc32.x86_64.rpm}
              '''
             }
    }
    stage ('build  peony-extensions ') { 

             steps { 
              sh '''
                  cp peony-extensions/peony-extensions-libdir-and-qmake.patch ${TOP}/SOURCES
                  cp peony-extensions/peony-extensions.spec ${TOP}/SPECS
                  dnf install -y $(grep  BuildRequires ${TOP}/SPECS/peony-extensions.spec | awk '{print $2}')
                  rpmbuild --define "_topdir ${TOP}" -bb ${TOP}/SPECS/peony-extensions.spec
              '''
             }
    }
    stage ('build  qt5-ukui-platformtheme ') { 

             steps { 
              sh '''
                  cp qt5-ukui-platformtheme/qt5-ukui-platformtheme.spec ${TOP}/SPECS
                  dnf install -y $(grep  BuildRequires ${TOP}/SPECS/qt5-ukui-platformtheme.spec | awk '{print $2}')
                  rpmbuild --define "_topdir ${TOP}" -bb ${TOP}/SPECS/qt5-ukui-platformtheme.spec
              '''
             }
    }
    stage ('build  ukui-biometric-auth ') { 

             steps { 
              sh '''
                  cp ukui-biometric-auth/ukui-biometric-auth-libdir.patch ${TOP}/SOURCES
                  cp ukui-biometric-auth/ukui-biometric-auth.spec ${TOP}/SPECS
                  dnf install -y $(grep  BuildRequires ${TOP}/SPECS/ukui-biometric-auth.spec | awk '{print $2}')
                  rpmbuild --define "_topdir ${TOP}" -bb ${TOP}/SPECS/ukui-biometric-auth.spec
              '''
              sh '''
                dnf -y install ${TOP}/RPMS/x86_64/{pam-biometric-1.2.0-1.fc32.x86_64.rpm,ukui-biometric-auth-1.2.0-1.fc32.x86_64.rpm,ukui-polkit-1.2.0-1.fc32.x86_64.rpm}
                '''
             }
    }

    stage ('build  ukui-biometric-manager ') { 

             steps { 
              sh '''
                  cp ukui-biometric-manager/ukui-biometric-manager.spec ${TOP}/SPECS
                  dnf install -y $(grep  BuildRequires ${TOP}/SPECS/ukui-biometric-manager.spec | awk '{print $2}')
                  rpmbuild --define "_topdir ${TOP}" -bb ${TOP}/SPECS/ukui-biometric-manager.spec
              '''
             }
    }

    stage ('build  ukui-control-center ') { 

             steps { 
              sh '''
                  cp ukui-control-center/ukui-control-center-libdir.patch ${TOP}/SOURCES
                  cp ukui-control-center/ukui-control-center.spec ${TOP}/SPECS
                  dnf install -y $(grep  BuildRequires ${TOP}/SPECS/ukui-control-center.spec | awk '{print $2}')
                  rpmbuild --define "_topdir ${TOP}" -bb ${TOP}/SPECS/ukui-control-center.spec
              '''
             }
    }  
    
    stage ('build  ukui-desktop-environment ') { 

             steps { 
              sh '''
                  cp ukui-desktop-environment/ukui-desktop-environment.spec ${TOP}/SPECS
                  rpmbuild --define "_topdir ${TOP}" -bb ${TOP}/SPECS/ukui-desktop-environment.spec
              '''
             }
    }
    stage ('build  ukui-greeter ') { 

             steps { 
              sh '''
                  cp ukui-greeter/ukui-greeter.spec ${TOP}/SPECS
                  dnf install -y $(grep  BuildRequires ${TOP}/SPECS/ukui-greeter.spec | awk '{print $2}')
                  rpmbuild --define "_topdir ${TOP}" -bb ${TOP}/SPECS/ukui-greeter.spec
              '''
             }
    } 
    stage ('build  ukui-kwin ') { 

             steps { 
              sh '''
                  cp ukui-kwin/ukui-kwin.spec ${TOP}/SPECS
                  dnf install -y $(grep  BuildRequires ${TOP}/SPECS/ukui-kwin.spec | awk '{print $2}')
                  rpmbuild --define "_topdir ${TOP}" -bb ${TOP}/SPECS/ukui-kwin.spec
              '''
             }
    }
  }
}