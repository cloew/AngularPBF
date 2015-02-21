from distutils.core import setup

setup(name='pbf_ng',
      version='.1',
      description="Programmer's Best Friend Utility Extension for pbf_ng",
      author='', # Add your name here
      author_email='', # Add your e-mail here
      packages=['pbf_ng', 'pbf_ng.Commands', 'pbf_ng.templates'],
      #package_data = {'pbf_ng.templates':[]}, # Add template files
     )