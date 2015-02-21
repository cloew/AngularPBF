from distutils.core import setup

setup(name='pbf_ng',
      version='0.1.0',
      description="Programmer's Best Friend Utility Extension for AngularJS",
      author='Chris Loew',
      author_email='cloew123@gmail.com',
      packages=['pbf_ng', 'pbf_ng.Commands', 'pbf_ng.templates'],
      package_data = {'pbf_ng.templates':['module.js']},
     )