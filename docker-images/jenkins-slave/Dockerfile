FROM ubuntu:16.04

RUN apt update && \
    apt -y install vim python openssh-server git

# Setup jenkins user
ENV JENKINS_HOME /home/jenkins
RUN useradd jenkins && \
    usermod -aG sudo jenkins && \
    mkdir -p $JENKINS_HOME/.ssh

COPY config/authorized_keys $JENKINS_HOME/.ssh/authorized_keys
RUN chown jenkins:jenkins $JENKINS_HOME -R

RUN mkdir -p /root/.ssh
COPY config/authorized_keys /root/.ssh/authorized_keys


# Setup ssh server
RUN mkdir /var/run/sshd
EXPOSE 22
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

CMD ["/usr/sbin/sshd", "-D"]
