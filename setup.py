from setuptools import setup

setup(
    name='TextAnalizer',
    version='0.0.1',
    description='A Text Analizer Utilities',
    author='RoboCopGay',
    author_email='vinicios.sousa909@gmail.com',
    url='https://github.com/RoboCopGay/TextAnalizer',
    packages=['textanalizer'],
    long_description="A module to text management.",
    install_requires=[
        'PyYAML',
    ],
    entry_points={
        'console_scripts': [
            'getter=textanalizer.getter:main',
            'translater=textanalizer.translater:main'
        ]
    }
)
