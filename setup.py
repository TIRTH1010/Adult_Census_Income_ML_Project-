from setuptools import find_packages,setup
from typing import List

Hyphen='-e .'

def get_requirments(file_path:str)->List[str]:
    requirments=[]
    with open(file_path) as f_obj:
        requirments=f_obj.readlines()
        requirments = [i.replace("\n", "") for i in requirments]

        if Hyphen in requirments:
            requirments.remove(Hyphen)





setup(
    name='Adult_Census_Income_ML_Project',
    version='0.0.2',
    description='Machine Learning pipeline project',
    author='Tirth Bhatt',
    author_email='tirthc58@gmail.com',
    install_requires=get_requirments('requirements.txt'),
    packages=find_packages()

)

