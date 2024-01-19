from setuptools import setup
from setuptools import find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(filepath:str)->List[str]:
    requirements = []
    with open(filepath) as file_obj:
        requirements = file_obj.readlines()
        requirements = [i.replace("\n","") for i in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

setup(
    version="0.0.1",
    description="Income Prediction using Machine Learning",
    author="Samagra Shrivastava",
    author_email="samagra@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt") 
)