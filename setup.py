from setuptools import setup

setup(name='logparse',
      version='0.1',
      description='Parsing log files',
      author='Wiard van Rij',
      author_email='wiard@outlook.com',
      license='MIT',
      packages=['logparse'],
      install_requires=[
          'markdown',
      ],
      zip_safe=False)