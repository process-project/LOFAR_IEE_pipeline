from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(name='LOFAR_IEE_pipeline',
      version='0.1',
      description='',
      long_description=readme(),
      packages=['LOFAR_IEE_pipeline'],
      include_package_data=True,
      zip_safe=True)
