from setuptools import setup, find_packages


setup(
    name='twitchat',
    version='1.0.0',
    install_requires=[
        'irc',
        'requests'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'twitchat = twitchat.bin:run'
        ]
    }
)
