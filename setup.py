from setuptools import setup, find_packages

setup(name='lime_stratified',
      version='0.1',
      description='Using Stratified Sampling to Improve LIME Image Explanations',
      url='https://github.com/rashidrao-pk/lime_stratified',
      author='Muhammad Rashid',
      author_email='rashidunito@gmail.com',
      license='MIT',
      packages=find_packages(exclude=['js', 'node_modules', 'tests']),
      python_requires='>=3.5',
      install_requires=[
          'matplotlib',
          'numpy',
          'scipy',
          'tqdm >= 4.29.1',
          'scikit-learn>=0.18',
          'scikit-image>=0.12',
          'pyDOE2==1.3.0'
      ],
      extras_require={
          'dev': ['pytest', 'flake8'],
      },
      include_package_data=True,
      zip_safe=False)
