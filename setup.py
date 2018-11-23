import io
from os.path import abspath, dirname, join
from shutil import rmtree

try:
    from pip._internal.req import parse_requirements
    from pip._internal.download import PipSession
except ImportError:
    from pip.req import parse_requirements
    from pip.download import PipSession

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

root_dir = abspath(dirname(__file__))

dist_dir = join(root_dir, 'dist')
build_dir = join(root_dir, 'build')

requirements_dir = join(root_dir, 'requirements')
sources_dir = join(root_dir, 'sources')
package_dir = join(sources_dir, 'boltun')


def cleanup():
    rmtree(build_dir, ignore_errors=True)
    rmtree(dist_dir, ignore_errors=True)


def get_about():
    with io.open(join(package_dir, '__about__.py'), encoding='utf-8') as f:
        about = {}
        exec (f.read(), about)
    return about


def get_requirements():
    links = []  # for repo urls (dependency_links)
    requires = []  # for package names

    requirements_file = join(requirements_dir, 'common.txt')
    try:
        requirements = list(parse_requirements(requirements_file))
    except:
        # new versions of pip requires a session
        requirements = list(parse_requirements(
            requirements_file, session=PipSession()))

    for item in requirements:
        if getattr(item, 'url', None):  # older pip has url
            links.append(str(item.url))
        if getattr(item, 'link', None):  # newer pip has link
            links.append(str(item.link))
        if item.req:
            requires.append(str(item.req))  # always the package name

    return requires, links


def setup_package():
    cleanup()

    about = get_about()
    requires, links = get_requirements()

    setup(
        name=about['__title__'],
        description=about['__summary__'],
        author=about['__author__'],
        author_email=about['__email__'],
        url=about['__uri__'],
        license=about['__license__'],

        install_requires=requires,
        dependency_links=links,

        packages=find_packages('sources'),
        package_dir={'': 'sources'},

        scripts=['bin/boltun'],

        use_scm_version={
            'version_scheme': 'guess-next-dev',
            'write_to': 'sources/boltun/__version__.py',
        },

        python_requires='>=3.5.*',

        setup_requires=[
            'pytest-runner', 'setuptools_scm', 'setuptools_scm_git_archive'
        ],

        tests_require=['pytest'],
        test_suite='tests',

        classifiers=[
            'Development Status :: 4 - Beta',
            "License :: OSI Approved :: MIT License",
            'Topic :: Text Processing :: General',
            'Topic :: Text Processing :: Markup',
            'Topic :: Text Processing :: Linguistic',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            "Intended Audience :: Developers",
            "Operating System :: OS Independent",
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Text Processing :: Markup',
        ]
    )


if __name__ == '__main__':
    setup_package()
