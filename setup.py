from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        
        if '-e .' in requirements:
            requirements.remove('-e .')
setup(
    name="mlproject",
    version="0.0.1 ",
    author="yaswanth",
    author_email="kondalayaswanth026@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)