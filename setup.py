from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    #This function will return list of requirements
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
    pass

setup(
    name="mlproject",
    version="0.0.1",
    author="Arpit Shourya",
    author_email="arpitshourya2233@gmail.com",
    packages=find_packages(),
    py_modules=get_requirements("requirements.txt")

)