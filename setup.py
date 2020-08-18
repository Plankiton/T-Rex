from setuptools import setup

setup(
    name='T-Rex',
    version='0.0.1',
    description='A Text Analyzer Utilities',
    author='RoboCopGay',
    author_email='vinicios.sousa909@gmail.com',
    url='https://github.com/RoboCopGay/T-Rex',
    packages=['T-Rex'],
    long_description="A module to text management.",
    install_requires=[
        'PyYAML',
    ],
    entry_points={
        'console_scripts': [
            'getter=T-Rex.get:main',
        ]
    }
)
