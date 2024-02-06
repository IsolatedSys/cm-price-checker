from setuptools import setup, find_packages

setup(
    name='cm-price-checker',
    version='1.0.0',
    description='Price checker for cm products',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/cm-price-checker',
    author='Your Name',
    author_email='your@email.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='price checker cm',
    packages=find_packages(),
    install_requires=[
        're',
        'cfscrape',
        'beautifulsoup4',
        'fake_useragent',
        'pandas',
    ],
)