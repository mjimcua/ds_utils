import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ds_utils-mjimcua", 
    version="0.0.1",
    author="Miguel Ángel Jiménez Cuadrillero",
    author_email="miguelangeljimenezcuadrillero@gmail.com",
    description="Data Sciente Utils is a module with some useful functions for beginers data scientist",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mjimcua/ds_utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)