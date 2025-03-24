from setuptools import setup


setup(
    name='Unixtime Converter',
    version='1.0.0',
    author='Franz Wiesinger',
    author_email='py@roadrunnerserver.com',
    description='application for converting local time or UTC into Unixtime \
        and viceversa',
    url='https://www.roadrunnerserver.com',
    license='MIT license',
    packages=[
        'res',
        'tests'
    ],
    install_requires=[
        'datetime', 'tkinter', 'pytz', 'zoneinfo', 'tkhtmlview'
    ],
    python_requires='> 3.7',
    entry_points={
        'console_scripts': [
            'unixtime = unixtime.__main__:unixtime'
        ]
    }
)
