from typing import Sequence
from setuptools import find_packages, setup
from glob import glob 
import os

package_name = 'transbot_description'

data_files : list[tuple[str, Sequence[str]]] = [
    ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    ]
# Recursively include all files in urdf/ and meshes/ preserving subfolders
for folder in ('launch', 'rviz', 'urdf', 'meshes'):
    for root, dirs, files in os.walk(folder):
        if files:
            # Destination path mirrors the source structure under share/package_name/
            dest = os.path.join('share', package_name, root)
            files_full = [os.path.join(root, f) for f in files]
            data_files.append((dest, files_full))


setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=data_files,
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='transbot',
    maintainer_email='you@example.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
