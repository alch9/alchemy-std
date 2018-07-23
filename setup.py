from setuptools import setup

setup(
    name='alchemy-std',
    version='0.2.1',
    author='Sudeep Jathar',
    author_email='sudeep.jathar@gmail.com',
    url='https://github.com/sudeep9/alchemy-std',
    description='Standard library for Alchemy automation framework',
    license='MIT',
    classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 2.7',
          'Operating System :: POSIX :: Linux'
    ],

    packages=['alchemy_std'],
    install_requires=['alchemy', 'paramiko'],
    package_data = {
        'alchemy_std': ["*.yml"]
    }
)
