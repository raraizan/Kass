from setuptools import setup

setup(
    name='kass',
    version='0.1',
    description='Python library to draw on a screen',
    url='https://github.com/raraizan/processing_like',
    author='Ruben Araiza',
    author_email='raraiza@nearsoft.com',
    # license='MIT',
    packages=['kass'],
    install_requires=[
        'pygame',
    ],
    zip_safe=False,
)