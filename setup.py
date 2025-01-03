from setuptools import setup

package_name = 'internet_speed_display'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    py_modules=[
        'internet_speed_display.internet_speed_publisher'  # ファイル名を指定
    ],
    install_requires=['setuptools', 'speedtest-cli'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your_email@example.com',
    description='A ROS 2 package to publish internet speed.',
    license='BSD 3-Clause',
    entry_points={
        'console_scripts': [
            'internet_speed_publisher = internet_speed_display.internet_speed_publisher:main'
        ],
    },
)

