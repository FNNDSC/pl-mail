import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='pl-mail',
    version='0.0.2',
    author='FNNDSC',
    author_email='dev@babyMRI.org',
    description='A ChRIS plugin for email',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='',
    py_modules=['mail'],
    license='MIT',
    entry_points={
        'console_scripts': [
            'mail = mail:main',
        ]
    },
    install_requires=[
        'chris_plugin',
        'pflog',
    ],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Medical Science Apps.'
   ],
)
