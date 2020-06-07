import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fort-img-utk11",
    version="0.0.1",
    author="Utkarsh Pamdey",
    author_email="utkarshpandey647@gmail.com",
    description="Spam detection through Image footprinting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/utkarsh261/fort/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)