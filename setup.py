from setuptools import find_packages ,setup 



def get_requirements()->list[str]:

    reuirements_list = list[str] =[]

    return reuirements_list






setup (
name = 'sensor',
version="0.0.1",
author="prince",
author_email="princekatiyar986@gmail.com",
packages = find_packages(),
install_requires = get_requirements() , #["pymongo"]

)

