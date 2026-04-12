from setuptools import setup

REPO_URL = "https://github.com/Open-Paws/no-animal-violence-pre-commit"

setup(
    name='no-animal-violence-check',
    version='0.2.0',
    py_modules=['no_animal_violence_check'],
    entry_points={
        'console_scripts': [
            'no-animal-violence-check=no_animal_violence_check:main',
        ],
    },
    python_requires='>=3.8',
    author='Open Paws',
    author_email='hello@openpaws.ai',
    description='Pre-commit hook for detecting language that normalizes violence toward animals',
    license='MIT',
    url=REPO_URL,
)
