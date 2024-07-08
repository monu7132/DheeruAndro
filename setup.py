from setuptools import setup, find_packages

setup(
    name='DheeruAndro',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'tabulate',
    ],
    entry_points={
        'console_scripts': [
            'dheeruandro = DheeruAndro:main',
        ],
    },
)
