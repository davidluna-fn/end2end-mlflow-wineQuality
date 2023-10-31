import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

__version__ = '0.0.1'

REPONAME = 'end2end-mlflow-wineQuality'
AUTHOR = 'davidluna-fn'
SRC_REPO = 'wineQuality'
AUTHOR_EMAIL = 'davidluna.fn@gmail.com'

setuptools.setup(
    name=REPONAME,
    version=__version__,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description="A small example package for ML projects with MLFlow",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR}/{SRC_REPO}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR}/{SRC_REPO}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)