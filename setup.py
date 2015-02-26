import setuptools

setup(
    name='tescolabsapi',
    description='An unofficial Python client for querying products with '
                'Tesco Labs API',
    version='0.1',
    license='Apache License',
    author='Alex Willmer',
    author_email='alex@moreati.org.uk',
    url='https://github.com/moreati/tescolabsapi',
    py_modules=['tescolabsapi'],
    install_requires=[
        'requests',
        ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2',
        'Topic :: Software Development :: Libraries',
        ],
    )
