from setuptools import setup


setup(
    name="py_med_box",
    version="0.1.0",
    description="Setting up medbox python package",
    author="Kazakhmedov Kirill",
    author_email="k.kirill777@gmail.com",
    packages=["py_med_box"],
    package_dir={"": "src"},
    install_requires=[""],
    setup_requires=["flake8"],
    scripts=["src/py_med_box.py"],
)
