from setuptools import find_packages, setup
from typing import List

# Read and print project description from readme.md
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


# Set variables
__version__ = "0.0.0"

REPO_NAME = "Chicken_Disease_Classification_Project" #folder name from github
AUTHOR_USER_NAME = "aprilhong"
SRC_REPO = "ClassifierProj"
AUTHOR_EMAIL = "aprilhong62@gmail.com"


setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=find_packages(where="src")
)



Hypen_e_dot='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will remove the '-e .' from requirements.txt and 
    return the list of requirements to install
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if Hypen_e_dot in requirements:
            requirements.remove(Hypen_e_dot)
    
    return requirements