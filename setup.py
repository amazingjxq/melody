from setuptools import setup

setup(
    name='melody',
    version='0.1',
    description='A realtime markdown render',
    url='http://github.com/storborg/funniest',
    author='Xuqing Jia',
    author_email='amazingjxq@gmail.com',
    license='MIT',
    packages=['melody'],
    zip_safe=False,
    entry_points = {
        'console_scripts': ['melody=melody.cli:main'],
    },
    install_requires=[
        'markdown',
        'jinja2',
        'pygments',
    ],
)
