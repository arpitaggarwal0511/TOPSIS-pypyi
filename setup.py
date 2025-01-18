from setuptools import setup, find_packages

setup(
    name="topsis_102203872",
    version="0.1.0",
    packages=["topsis_102203872"],
    install_requires=[
        'numpy',
        'pandas',
        'openpyxl',  # Added for handling Excel files
    ],
    entry_points={
        'console_scripts': [
            'topsis-cli = topsis_102203872.topsis_102203872:main',  # Ensure this matches the function path
        ],
    },
    author="Arpit Aggarwal",
    author_email="your_email@example.com",
    description="TOPSIS Algorithm Implementation with CLI",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/arpitaggarwal/topsis_package",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    include_package_data=True,  # Optional: Include additional files
)
