from setuptools import find_packages, setup

package_name = 'steron_control'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Serhat',
    maintainer_email='varliserhatt@gmail.com',
    description='ROS 2 control nodes for the Steron autonomous mobile robot platform.',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'odometry_monitor = steron_control.odometry_monitor:main',
            'closed_loop_controller = steron_control.closed_loop_controller:main',
        ],
    },
)
