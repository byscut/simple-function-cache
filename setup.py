from setuptools import setup, find_packages

# python setup.py sdist upload -r pypi

if __name__ == "__main__":
    with open('README.md', 'rt', encoding="utf-8") as f:
        readme = f.read()

    setup(
        name="simple-function-cache",
        version='0.0.3',
        description="function cache decorator with redis",
        long_description=readme,
        long_description_content_type="text/markdown",
        url="https://github.com/byscut/simple-function-cache.git",
        author="byscut",
        license="MIT",
        test_suite='tests',
        package_dir={'': '.'},
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
        install_requires=[
            "redis",
            "gevent>=21.8.0"
        ],
        python_requires=">=3.7"
    )
