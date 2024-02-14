# setup.py

from setuptools import setup, find_packages

# setuptools is a Python library used to facilitate packaging and distribution of Python packages.
# It provides necessary functions to specify what files and dependencies are needed.

setup(
    name="tic_tac_toe",  # This is the name of your package
    version="0.1",  # The initial release version
    packages=find_packages(where='src'),  # This function automatically finds all packages in the 'src' directory.
    package_dir={'': 'src'},  # This specifies that the packages are located under the 'src' directory.

    # Here we specify dependencies. These are external packages that your project depends on.
    # These packages will be installed automatically when installing your package.
    install_requires=[
        # For this project, there are no dependencies, but typically it would look like this:
        # 'numpy', 'pandas', etc.
    ],

    # Metadata for your project
    author="Your Name",
    author_email="your-email@example.com",
    description="A refactored version of a Tic Tac Toe game",
    license="MIT",
    keywords="tic-tac-toe refactoring",
    url="http://github.com/your_username/tic-tac-toe",  # project home page
)

# With this setup.py in place, you can install your project in another environment with pip:
# pip install .
# The '.' means that setup.py is in the current directory

