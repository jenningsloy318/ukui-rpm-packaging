
pipeline {
  agent {
        label 'fedora'
    }
  environment {
        TOP = /root/rpmbuild
    }

  stages {
    
    stage ('prepare environment') { 
        steps {
        	sh "mkdir ${TOP}/{BUILD,RPMS,SOURCES,SPECS,SRPMS}"
          sh "install which gcc gcc-c++ make cmake cmake-rpm-macros autoconf automake intltool rpm-build qt5-rpm-macros  ruby  mysql-devel ruby-devel rubygems  meson ninja-build qt5-qtbase"
          sh "strip --remove-section=.note.ABI-tag /usr/lib64/libQt5Core.so.5"
          sh "gem install sass bundler rails compass"

        }
    }
    stage ('build peony') { 
        steps {
        	sh "cp peony/lib-path.patch ${TOP}/SOURCES"
          sh "cp peony/peony.spec ${TOP}/SPECS"
          sh "dnf install -y $(grep  BuildRequires ${TOP}/SOURCES/peony.spec |awk '{print $2}')"
          sh "rpmbuild --define "_topdir ${TOP}" -bb ${TOP}/SPECS/peony.spec"
        }
    }

    stage ('install peony') { 
      steps {
        sh "dnf -y install ${TOP}/RPMS/x86_64/{peony-2.2.0-1.fc32.x86_64.rpm,peony-common-2.2.0-1.fc32.x86_64.rpm,peony-devel-2.2.0-1.fc32.x86_64.rpm,peony-libs-2.2.0-1.fc32.x86_64.rpm}"
        }
    }
  }
}