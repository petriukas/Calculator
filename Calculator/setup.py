from setuptools import setup, find_packages

setup(
    name='Calculator',
    version='1.0',
    description='Console application that calculates',
    author='Aistis Jampolskis',
    long_description = 'file: README.md',
    long_description_content_type = 'text/markdown',
    author_email='aistis.jampolskis@gmail.com',
    url='https://github.com/petriukas/Calculator.git',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
        # ...
    ]
)

