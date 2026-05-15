# TRANSBOT - ROS2 WORKSPACE

Workspace de ROS2 conteniendo los archivos del Transbot  
**Nota:** Es recomendable usar la imagen del Docker *roslac* para que funcione este repositorio [^docker_roslac] 

## Estructura de archivos base:

+ [`src`](./src):  archivos fuente del repositorio, contiene los paquetes de ROS2. 
+ [`ws_build.sh`](ws_build.sh): script atajo para compilar todos los paquetes del repositorio.
+ `build`: (ignorado por git) archivos de compilación 
+ `install`: (ignorado por git) archivos ejecutables, lanzadores y extras que ROS2 puede correr/utilizar. Son los paquetes *finales* utilizables
+ `log`: (ignorado por git) registros de compilación

## Comandos útiles

### Visualizar modelos en Rviz
```bash
ros2 launch transbot_description display.launch.py
```
Ver argumentos:  
```bash
ros2 launch transbot_description display.launch.py --show-arguments
```
#### Cambiar el modelo del robot para visualizar

Los siguientes argumentos permiten modificar el robot que se va a visualizar:

+ `robot_model`: se puede seleccionar un modelo según el contenido del paquete [transbot_description/urdf](src/transbot_description/urdf). El nombre del directorio es el nombre del modelo. Para más información, ver el paquete.
+ `robot_pkg`: indica el paquete de donde se debe cargar el modelo del robot.
+ `robot_name`: asigna al robot un nombre en ROS. Por defecto: `transbot`.

### Lanzar Gazebo 

```bash
ros2 launch transbot_gazebo gazebo.launch.py
```
Ver argumentos:  
```bash
ros2 launch transbot_gazebo gazebo.launch.py --show-arguments
```
#### Cambiar el modelo del robot para simular

Los siguientes argumentos permiten modificar el robot que se va a simular:

+ `robot_model`: se puede seleccionar un modelo según el contenido del paquete [transbot_gazebo/urdf](src/transbot_gazebo/urdf). El nombre del directorio es el nombre del modelo. Para más información, ver el paquete.
+ `robot_pkg`: indica el paquete de donde se debe cargar el modelo del robot.
+ `robot_name`: asigna al robot un nombre en ROS. Por defecto: `transbot`.

#### Cambiar el mundo de Gazebo

Los siguientes argumentos permiten modificar el mundo de Gazebo a simular

+ `world`: archivo `sdf` del mundo de Gazebo


[^docker_roslac]: No es estrictamente requerido usar la imagen base del docker pero se recomienda usarla para gestionar bien las dependencias.