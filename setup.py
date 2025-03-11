from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="initkit",
    version="0.1.0",
    packages=find_packages(include=["initkit", "initkit.*"]),
    install_requires=[
        "Flask>=2.0.0",
        "click>=8.0.0",
        "python-dotenv>=0.19.0",
    ],
    entry_points={
        "console_scripts": [
            "flask-template=initkit.cli:cli",
        ],
    },
    include_package_data=True,
    package_data={
        "initkit": ["templates/*"],
    },
    author="lyznne",
    author_email="emuthiani26@gmail.com",
    description="A Flask CLI tool for generating starter templates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lyznne/flask-blog-starter.git",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    keywords=["flask", "cli", "template", "starter", "boilerplate"],
    project_urls={
        "Bug Reports": "https://github.com/lyznne/flask-blog-starter/issues",
        "Source": "https://github.com/lyznne/flask-blog-starter",
    },
)
