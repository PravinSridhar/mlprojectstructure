from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements
    """
    requirements = []
    with open(file_path) as f:
        requirements=f.readlines()
        requirements = [req.replace('\n', '') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT) 

    return requirements    



setup(
    name="mlprojectstruct",
    version='0.0.1',
    author="Pravin",
    author_email="pravinsrdhr@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)





