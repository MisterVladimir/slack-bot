from setuptools import find_packages, setup

requirements = [
    "slackclient",
    "requests",
]
requirments_dev = [
    "Sphinx",
    "pytest",
    "pytest-runner",
    "black",
    "pytest-black",
    "pytest-cov",
    "pylint",
    "pylint-mccabe",
    "twine",
]


if __name__ == "__main__":

    setup(
        name="slack_bot",
        packages=find_packages(),
        install_requires=requirements,
        extras_require={
            "dev": requirments_dev,
        },
        version="0.1.0",
        description="A project which no description will do justice.",
        author="Anonymous",
        license="MIT",
    )
