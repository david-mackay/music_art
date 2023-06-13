from setuptools import setup, find_packages

setup(
    name='gpt_code_review',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gpt_review = gpt_code_review.entry_points.code_review:main'
        ]
    }
)