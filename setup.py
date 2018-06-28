from setuptools import setup

setup(name='hds_821pr',
      version='0.0.1',
      description='Library to interface with HDS-821PR HDMI 2x1 Multi-Viewer Switch Seamless Switcher w/ PIP Function',
      url='https://github.com/ragingcomputer/hds_821pr',
      download_url='https://github.com/ragingcomputer/hds_821pr/archive/0.0.1.tar.gz',
      author='Raging Computer',
      license='MIT',
      packages=['hds_821pr'],
      install_requires=['pyserial==3.4'],
      zip_safe=True)
