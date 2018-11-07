from setuptools import setup

setup(name='packpack',
      version='0.1',
      description='python package template',
      url='https://github.com/omrishuva/packpack',
      author='Omri Shuva',
      author_email='omrishuva1@gmail.com',
      license='MIT',
      packages=['packpack'],
      install_requires=[
          'jinja2',
      ],
      zip_safe=False)
