from setuptools import setup, find_packages
import some_build_toolkit

def get_version():
    version = some_build_toolkit.compute_version()
    return version

setup(
    name='lime_stratified',
    version=get_version(),
    description='Using Stratified Sampling to Improve LIME Image Explanations',
    url='https://github.com/rashidrao-pk/lime_stratified',
    author='Muhammad Rashid',
    author_email='rashidunito@gmail.com',
    license='MIT',
    packages=find_packages(exclude=['js', 'node_modules']),
    python_requires='>=3.5',
    install_requires=[
        'matplotlib>=3.0,<4.0',
        'numpy>=1.16,<2.0',
        'scipy>=1.2,<2.0',
        'tqdm>=4.29.1,<5.0',
        'scikit-learn>=0.18,<1.0',
        'scikit-image>=0.12,<1.0',
        'pyDOE2==1.3.0'
    ],
    extras_require={
        'dev': ['pytest', 'flake8', 'black', 'mypy'],
    },
    include_package_data=True,
    zip_safe=False
)
