from setuptools import setup, find_packages

setup(
    name="soundcloud_downloader",
    version="0.1.2",
    author="Your Name",
    description="A library for downloading music from SoundCloud using scdl",
    packages=find_packages(),
    install_requires=["scdl>=2.12.3"],  # Dependency on scdl
    python_requires=">=3.6",  # Compatible with 3.6+, tested up to 3.12
)