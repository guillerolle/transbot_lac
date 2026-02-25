ARG ROSDISTRO=jazzy
ARG GZ_VERSION=harmonic

# Use the official ROS 2 desktop-full image (includes RViz, demos, etc.)
FROM osrf/ros:$ROSDISTRO-desktop-full

ARG USERNAME=roslac
# ARG UID DEBE SER EL MISMO UID DEL USUARIO EN EL HOST PARA EVITAR PROBLEMAS DE PERMISOS CON LOS VOLUMENES MONTADOS
# DEBE HABER OTRA MANERA DE SOLUCIONAR ESTO, PERO ESTA POR AHORA FUNCIONA BIEN
ARG UID
ARG GID=$UID

# If a user with the target UID already exists (e.g., 'ubuntu' in some base images), remove it.
RUN if id -u $UID ; then userdel `id -un $UID` ; fi

# Create our user with the specified UID/GID
RUN groupadd --gid $GID $USERNAME \
    && useradd --uid $UID --gid $GID -m $USERNAME \
    #
    # [Optional] Add sudo support. Omit if you don't need to install software after connecting.
    && apt-get update \
    && apt-get install -y sudo apt-utils \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME

# Install common development tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip \
    python3-venv \
    python3-colcon-common-extensions \
    git \
    nano \
    vim \
    wget \
    gnupg \
    lsb-release \
    htop \
    && rm -rf /var/lib/apt/lists/*

ENV SHELL=/bin/bash

# ********************************************************
# * Anything else you want to do like clean up goes here *
# ********************************************************

# --- Add Gazebo Harmonic repository and install ---
ARG GZ_VERSION
RUN curl https://packages.osrfoundation.org/gazebo.gpg --output /usr/share/keyrings/pkgs-osrf-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/pkgs-osrf-archive-keyring.gpg] https://packages.osrfoundation.org/gazebo/ubuntu-stable $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/gazebo-stable.list > /dev/null \
    && apt-get update && apt-get install -y --no-install-recommends \
    gz-$GZ_VERSION \
    && rm -rf /var/lib/apt/lists/*

# Setup ROS
ARG ROSDISTRO
RUN apt-get update \
&& apt-get install -y --no-install-recommends --no-install-suggests \
        ros-$ROSDISTRO-ros-gz \
        ros-$ROSDISTRO-controller-manager \
        ros-$ROSDISTRO-position-controllers \
        ros-$ROSDISTRO-pid-controller \
        ros-$ROSDISTRO-joint-state-publisher-gui \
        ros-$ROSDISTRO-slider-publisher \
        ros-$ROSDISTRO-ros2-control \
        ros-$ROSDISTRO-gz-ros2-control \
        ros-$ROSDISTRO-gz-ros2-control-demos \
        ros-$ROSDISTRO-rqt* \
        python-pygraphviz-doc \
        ros-$ROSDISTRO-navigation2 \
        ros-$ROSDISTRO-nav2-bringup \
        ros-$ROSDISTRO-turtlebot3 \
    && rm -rf /var/lib/apt/lists/*


RUN echo "source /opt/ros/$ROSDISTRO/setup.bash" >> /home/$USERNAME/.bashrc

# AUTOMATICALLY SOURCE PROJECT .bashrc ON STARTUP 
RUN echo 'if [ -n "$WORKSPACEDIR" ] && [ -f ~/"$WORKSPACEDIR"/.bashrc ]; then\n\
    source ~/"$WORKSPACEDIR"/.bashrc\n\
    echo "Sourced project .bashrc from ~/$WORKSPACEDIR/.bashrc"\n\
elif [ -f ~/ws/.bashrc ]; then\n\
    source ~/ws/.bashrc\n\
    echo "Sourced project .bashrc from ~/ws/.bashrc (default)"\n\
else\n\
    echo "No project .bashrc found. Set WORKSPACEDIR env var or place one in ~/ws/.bashrc"\n\
fi' >> /home/$USERNAME/.bashrc

USER $USERNAME
CMD ["/bin/bash"]
WORKDIR /home/$USERNAME

# RUN export PYTHONWARNINGS="ignore:::setuptools.command.install,ignore:::setuptools.command.easy_install,ignore:::pkg_resources"
