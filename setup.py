from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """Returns a list of project dependencies."""
    requirement_list = []
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()
                if requirement and requirement != '-e .':
                    requirement_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. Please ensure it exists in the project directory.")

    return requirement_list
print (get_requirements())

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Anjana Bharamnaikar',
    author_email='anjanabbharamnaikar@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements()
)
