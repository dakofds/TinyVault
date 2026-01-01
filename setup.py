from setuptools import setup, find_packages

setup(
    name="tvault",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "bitcoinlib>=0.6.6"
    ],
    entry_points={
        "console_scripts": [
            "tvault = tvault.cli:main",
        ],
    },
    author="dakofds"
    description="CLI wallet Bitcoin",
)
