from setuptools import setup

setup(
    name='speciesist-language-check',
    version='0.1.0',
    py_modules=['speciesist_language_check'],
    entry_points={
        'console_scripts': [
            'speciesist-language-check=speciesist_language_check:main',
        ],
    },
    python_requires='>=3.8',
    author='Open Paws',
    author_email='hello@openpaws.ai',
    description='Pre-commit hook for detecting speciesist language',
    license='MIT',
    url='https://github.com/Open-Paws/speciesist-language-pre-commit',
)
