from setuptools import setup, find_packages

setup(
    name="ChatbotGPT3",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "aiohttp>=3.7.4",  # Specify the required version of aiohttp here
    ],
    author="Nic",
    description="A package for ai text completion using an AI API",
    long_description="A Python package for generating text completions using an AI text generation API.",
    long_description_content_type="text/markdown",
    url="https://github.com/Nic-223",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
