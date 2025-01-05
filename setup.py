from setuptools import setup

package_name = 'internet_speed_display'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    py_modules=[
        'internet_speed_display.node'
    ],
    install_requires=['setuptools', 'speedtest-cli'],
    zip_safe=True,
    maintainer='Teruma Yamamoto',
    maintainer_email='TRyamamototeruma@gmail.com',
    description='A ROS 2 package to display internet speed.',
    license='BSD-3-Clause',
    entry_points={
        'console_scripts': [
            'internet_speed_node = internet_speed_display.node:main'
        ],
    },
)

