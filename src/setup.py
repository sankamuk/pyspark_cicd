import setuptools

with open("../README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyspark_cicd", 
    version="1.1.0-SNAPSHOT",
    author="Sankar Mukherjee",
    author_email="sanmuk21@gmail.com",
    description="PySpark CICD Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sankamuk/pyspark_cicd",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
