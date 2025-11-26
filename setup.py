from setuptools import find_packages, setup

def get_requirements(file_path: str) -> list[str]:
    ''''This function will return the list of requirements'''
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip()]
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name="mlproject",
    version="0.1.0",
    author="Balaji",
    author_email="poralabalaji@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)