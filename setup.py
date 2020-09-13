from setuptools import setup, find_packages
from os import path

# Path of the extension
here = path.abspath(path.dirname(__file__))


# Get description from Readme.md
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='dipline',  # Required
    version='1.0',
    description='Data pipeline package for ETL/NLP/ML process',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='git@github.com:gtkChop/EMPortal.git',
    author='Swaroop',
    author_email='swaroopbhak@gmail.com',
    classifiers=[  # Optional
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'Topic : 'Data pipeline package for ETL/NLP/ML process',
        'License : Open License',
        'Programming Language :: Python :: 3.6'
    ],
    keywords='Datapipeline ETL ML-pipeline NLP-pipeline',
    packages=find_packages(
        exclude=['contrib', 'docs', 'tests'],
    ),
    python_requires='>=3.6',

    # All install packages should go on requirements.txt file
    install_requires=[
    ],
    extras_require={
    },
    package_data={
    },
    data_files=[
    ],

    message_extractors={
    },

    # Entry Points
    entry_points={
    }
)
