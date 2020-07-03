
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
            dnf -y install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros python3-rpm-macros rubygem-sass meson ninja-build 
            strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5
          '''

        }
    }
   
    stage ('build all ') { 

             steps { 
              sh '''
                make clean
                make build
              '''
             }
    }
  }
}