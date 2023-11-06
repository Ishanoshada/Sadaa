from setuptools import setup, find_packages

setup(
    name='sadaa',
    version='0.3.0',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    author='Ishan Oshada',
    author_email='ic31908@gamil.com',
    description='A package for generating random stories.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ishanoshada/sadaa',
    project_urls={
        'Source': 'https://github.com/ishanoshada/sadaa',
    },
)
