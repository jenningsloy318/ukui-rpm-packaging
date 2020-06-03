
pipeline {
  agent {
        label 'fedora'
    }
  environment {
        TOP = "/root/rpmbuild"
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
        stages {

          stage ('build peony') {
             steps { 
              sh '''
                  cp peony/peony-libdir.patch ${TOP}/SOURCES
                  cp peony/peony.spec ${TOP}/SPECS
                  dnf install -y $(grep  BuildRequires ${TOP}/SPECS/peony.spec | awk '{print $2}')
                  rpmbuild --define "_topdir ${TOP}" -bb ${TOP}/SPECS/peony.spec
              '''
              }
            }

          stage ('install peony')  {
             steps { 
              sh '''
                dnf -y install ${TOP}/RPMS/x86_64/{peony-2.2.0-1.fc32.x86_64.rpm,peony-common-2.2.0-1.fc32.x86_64.rpm,peony-devel-2.2.0-1.fc32.x86_64.rpm,peony-libs-2.2.0-1.fc32.x86_64.rpm}
              '''
              }
            }

          } 

        }
  }
}