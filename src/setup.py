from setuptools import setup, find_packages

setup(
    name="nutrient-analysis",
    version="0.0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "beautifulsoup4",
        "psycopg2-binary",
        "scikit-learn",
        "matplotlib",
        "pandas"
    ],
    extras_require={
        'interactive': ["matplotlib", "jupyter"],
    },
    entry_points={
        "console_scripts": [
            "nutrient-main=nutrient-analysis.main:cli"
        ]
    },
    setup_requires=['flake8']
)