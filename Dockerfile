FROM  jenkins/jenkins:lts-centos7
MAINTAINER longyu<273397699@qq.com>
USER root
RUN yum -y install wget && yum -y install vim  && yum -y install python3
ADD apache-maven-3.6.3-bin.tar.gz  /usr/local
ENV MYPATH  /usr/local/
WORKDIR $MYPATH
ENV MAVEN_HOME=/usr/local/apache-maven-3.6.3
ENV PATH $PATH:$MAVEN_HOME/bin
USER jenkins


#RUN yum -y install wget && yum -y install vim  && yum -y install gcc && yum install libffi-devel -y \
#&& yum -y install zlib* && wget https://www.python.org/ftp/python/3.7.9/Python-3.7.9.tar.xz && cp Python-3.7.9.tar.xz /usr/local\
#&& tar -xvf /usr/local/Python-3.7.9.tar.x && cd /usr/local/Python-3.7.9 && ./configure --prefix=/usr/local/Python-3.7.9/ && make && make install \
#&& ln -s /usr/local/Python-3.7.9/bin/python3 /usr/bin/python3 && ln -s /usr/local/Python-3.7.9/bin/pip3 /usr/bin/pip3\
#&& usermod -aG 999 jenkins
