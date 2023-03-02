from setuptools import setup
from setuptools import find_packages
setup(

    name='engineer_app',
    version='1.0.0',
    description="Package containing mohr's circle as well as unit converter.",
    author='Chase Eckhart',
    packages=find_packages(),
     install_requires=["numpy", "matplotlib", "tkinter"]

)
