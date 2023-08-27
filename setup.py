from setuptools import find_packages, setup

setup(
    name="Pablo's Python Library",
    packages=find_packages(include=["pablospythonlib"]),
    version="0.1.0",
    description="A library where i'll add my functions",
    author="Pablo Cerda V.",
    license="CI",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==4.4.1"],
    test_suite="tests",
)