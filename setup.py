from setuptools import setup, find_packages

setup(
    name="initkit",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["Flask", "click"],
    entry_points={
        "console_scripts": [
            "flask-template=flask_template_cli.cli:cli",
        ],
    },
    author="lyznne",
    author_email="emuthiani26@gmail.com",
    description="A Flask CLI tool for generating starter templates",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/lyznne/flask-blog-starter.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
