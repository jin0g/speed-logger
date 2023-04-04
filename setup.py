from setuptools import setup, find_packages


setup(
    name="speedlogger",
    version="1.0.0",
    author="jin0g",
    author_email="your.email@example.com",
    description="A Python tool to monitor and log internet speeds using WandB.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jin0g/speedlogger",
    py_modules=["speedlogger"],
    python_requires=">=3.6",
    install_requires=[
        "speedtest-cli",
        "wandb"
    ],
    entry_points={
        "console_scripts": [
            "speedlogger=speedlogger:main",
        ],
    },
)