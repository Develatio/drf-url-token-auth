import os
from setuptools import setup

HERE = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(HERE, 'README.rst')).read()

setup(
    name='drf-url-token-auth',
    version='0.1',
    packages=['drf_url_token_auth'],
    description='Authentication scheme for django rest framework that allow to use token in a url',
    long_description=README,
    author='Develatio Technologies S.L.',
    author_email='contacto@develat.io',
    url='https://github.com/develatio/django-tradukoj/',
    license='MIT',
    install_requires=[
        'Django>=2.0',
    ]
)
