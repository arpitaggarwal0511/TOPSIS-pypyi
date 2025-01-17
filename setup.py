from setuptools import setup, find_packages

setup(
    name="topsis_102203872",  # Update the package name if you want it to match
    version="0.1.0",
    packages=["topsis_102203872"],  # Updated package name
    install_requires=[
        'numpy',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'topsis-cli = topsis_102203872.topsis_102203872:main',  # Update this if necessary
        ],
    },
    author="Your Name",
    author_email="your_email@example.com",
    description="TOPSIS Algorithm Implementation with CLI",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/topsis_package",  # Update GitHub URL if needed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
