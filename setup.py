import os
from glob import glob
from setuptools import setup

package_name = 'moveit2_tutorials'

setup(
    name=package_name,
    version='0.0.0',
    packages=['ompl_constrained_planning'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # # Include all other files
        # (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        # (os.path.join('share', package_name, 'urdf'), glob('urdf/*')),
        # (os.path.join('share', package_name, 'meshes'), glob('meshes/*')),
        # (os.path.join('share', package_name, 'rviz'), glob('rviz/*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Joshua Liu',
    maintainer_email='liushuya7@gmail.com',
    description='snake tool ROS2 description',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'ompl_constrained_planning_tutorial = ompl_constrained_planning.ompl_constrained_planning_tutorial:main'
        ],
    },
)
