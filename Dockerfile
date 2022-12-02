FROM rockylinux:8
RUN dnf install -y which python3 epel-release
RUN dnf config-manager --set-enabled powertools
RUN dnf install -y python3-openimageio python3-numpy
RUN pip3 install -U pip
RUN pip3 install opencv-python