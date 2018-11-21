from os.path import dirname, join

from setuptools import find_packages, setup


def setup_package():
    setup(
        name="boltun",
        packages=find_packages('sources'),
        package_dir={'': 'sources'},

        use_scm_version={
            'version_scheme': 'guess-next-dev',
            'write_to': 'sources/boltun/__version__.py',
        },

        python_requires='>=2.7,!=3.0.*,!=3.1.*,!=3.2.*,!=3.3.*',

        setup_requires=[
            'pytest-runner', 'setuptools_scm', 'setuptools_scm_git_archive'
        ],

        tests_require=['pytest'],
        test_suite='tests',

        version="1.0.0",
        author="meiblorn",
        license="MIT",
        url="https://github.com/meiblorn/boltun",
        description="Massive datasets generator",
        long_description=open(join(dirname(__file__), "readme.md")).read(),
        long_description_content_type="text/markdown",


        scripts=['bin/boltun'],
        classifiers=[
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            "License :: OSI Approved :: MIT License",
            "Intended Audience :: Developers",
            "Operating System :: OS Independent",
        ]
    )


if __name__ == '__main__':
    setup_package()
