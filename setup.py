from setuptools import find_packages, setup

setup(
    name="goldenverba",
    version="0.3.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "verba=goldenverba.server.cli:cli",
        ],
    },
    author="Weaviate",
    author_email="edward@weaviate.io",
    description="Welcome to Verba: The Golden RAGtriever, an open-source initiative designed to offer a streamlined, user-friendly interface for Retrieval-Augmented Generation (RAG) applications. In just a few easy steps, dive into your data and make meaningful interactions!",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/weaviate/Verba",
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    include_package_data=True,
    install_requires=[
        "weaviate-client==3.23.1",
        "python-dotenv==1.0.0",
        "openai==0.27.9",
        "wasabi==1.1.2",
        "spacy",
        "fastapi==0.102.0",
        "uvicorn[standard]",
        "click== 8.1.7",
        "asyncio",
        "tiktoken",
        "cohere==4.33",
        "requests",
        "pypdf2",
        "accelerate",
        "transformers"
    ],
    extras_require={
        "dev": [
            "pytest",
            "wheel",
            "twine",
            "black>=23.7.0",
            "setuptools",
            "pre-commit",
        ],
        "huggingface": [
            "sentence-transformers",
            "transformers",
            "torch",
            "huggingface_hub",
            "accelerate",
        ],
    },
)
