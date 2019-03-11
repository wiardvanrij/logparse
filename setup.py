from setuptools import setup

setup(name='logparse',
      version='0.1',
      description='Parsing log files',
      author='Wiard van Rij',
      author_email='wiard@outlook.com',
      license='MIT',
      packages=['logparse'],
      install_requires=[
          'apache_log_parser',
          'ConfigParser'
      ],
      entry_points={
          'console_scripts': ['logparse=logparse.command_line:main'],
      },
      zip_safe=False)