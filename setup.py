from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="text_extractor",
    version="0.1",
    author="Sandra Costa",
    author_email="sandralin.9@gmail.com",
    description="Um pacote para extrair textos de imagens usando pytesseract",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sannlin9/text_extractor_package",  # Atualize com seu repositório
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
