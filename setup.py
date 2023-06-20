from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

## edit below variables as per your requirements -
REPO_NAME = "Book Recommendation System"
AUTHOR_USER_NAME = "Musa Khalid"
SRC_REPO = "books_recommender"
LIST_OF_REQUIREMENTS = []


setup(
    name=SRC_REPO,
    version="0.0.1",
    author="Musa Khalid",
    description="A small local packages for ML based books recommendations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mkothm/book-recommendation-system",
    author_email="mkalbani96@gmail.com",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
