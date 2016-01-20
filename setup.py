from setuptools import setup
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