from setuptools import setup, find_packages

"""
Uma biblioteca para leitura de arquivos CNAB 240.
"""

setup(
    name='sbcnab240',
    version='0.1.0',
    url='https://github.com/Superbuy-Team/sbcnab240/',
    license='MIT',
    author='SuperBuy Team',
    author_email='ti@superbuy.com.br',
    description='Uma biblioteca para leitura de arquivos CNAB 240',
    long_description=__doc__,
    keywords='cnab cnab240 boleto',
    #packages=['sbcnab240'],
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    package_data={
        'bancos': ['sbcnab240/bancos/santander.json'],
    },
    include_package_data=True,
    zip_safe=False,
    python_requires='~=2.6',
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Natural Language :: Portuguese (Brazilian)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
