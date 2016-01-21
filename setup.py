try:
    from setuptools import setup
except ImportError:
    from distutils.core import setuptools   # use distutils if we don't have setuptools

setup(
    name = "jtest",
    version = "0.1.0",
    packages = ['maths'],
    entry_points={
        'console_scripts': [
            'maths = maths.__main__:main'
        ]
    },
    test_suite="tests",

    # metadata for upload to PyPI
    author = "Jon Tutcher",
)