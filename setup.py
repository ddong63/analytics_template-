from setuptools import setup, find_packages

setup(
    name='data_science_template',
    version='0.1',
    description='A package for data science templates and common functions',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'jinja2',
        # Add other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'generate_analysis = examples.generate_analysis:main',
            'conduct_analysis = examples.conduct_analysis:main',
        ],
    },
)
