Boltun (aka rus. [Болтун](https://en.wiktionary.org/wiki/%D0%B1%D0%BE%D0%BB%D1%82%D1%83%D0%BD))
===

Generates massive datasets from just a single template.

```text
Command:
> python -m boltun "{{ Hi || Hello }}, [[ 'welcome' | upper? ]][[? ' back' ]] to Boltun [% repeat('!', [1, 3]) %]"

Hi, WELCOME back to Boltun !
Hello, WELCOME back to Boltun !
Hi, welcome back to Boltun !
Hello, welcome back to Boltun !
Hi, WELCOME to Boltun !
Hello, WELCOME to Boltun !
Hi, welcome to Boltun !
Hello, welcome to Boltun !
Hi, WELCOME back to Boltun !!!
Hello, WELCOME back to Boltun !!!
Hi, welcome back to Boltun !!!
Hello, welcome back to Boltun !!!
Hi, WELCOME to Boltun !!!
Hello, WELCOME to Boltun !!!
Hi, welcome to Boltun !!!
Hello, welcome to Boltun !!!
```

Branch   | CI status
---------|-------------------
master   | [![Build Status](https://travis-ci.org/meiblorn/boltun.svg?branch=master)](https://travis-ci.org/meiblorn/boltun)[![codecov](https://codecov.io/gh/meiblorn/boltun/branch/master/graph/badge.svg)](https://codecov.io/gh/meiblorn/boltun)
develop  | [![Build Status](https://travis-ci.org/meiblorn/boltun.svg?branch=develop)](https://travis-ci.org/meiblorn/boltun)[![codecov](https://codecov.io/gh/meiblorn/boltun/branch/develop/graph/badge.svg)](https://codecov.io/gh/meiblorn/boltun)

## About

[![boltun_simpsons_bart](https://raw.githubusercontent.com/meiblorn/boltun/master/static/simpsons_bart.png)](https://github.com/meiblorn/boltun)

**Boltun** is designed to be best alternative for the natural language machine-learning developers and enthusiasts.

It was developed as an alternative for such projects as 
[Chatito](https://github.com/rodrigopivi/Chatito) and [Tracery](http://tracery.io/). 
Yes, they are almost perfect, especially Tracery, but both of them are written for NodeJS platform. 
NodeJS is a single threaded language, so that tools are perfect only for small amounts of data. 
Boltun breaks that bounds of data generation limits.

## Getting Started

### Installing

Using pip ([PyPI repository](https://pypi.org/project/boltun/)):

```bash
pip install boltun
```

Boltun is also available on 
[Docker Hub](https://hub.docker.com/r/meiblorn/boltun):

```bash
docker pull meiblorn/boltun
```

For macOS users, Boltun is available via 
[Homebrew](https://brew.sh)

```bash
brew install boltun
```

### Usage

```bash
pip -m boltun "<your template>"
```


## Contributing

You are welcome to contribute ! Just submit your PR and become a part of Boltun community!

Please read [contributing.md](contributing.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org) for versioning. For the versions available, see the [tags on this repository](https://github.com/meiblorn/boltun/tags). 

## Authors

* **Vadim Fedorenko** - [Meiblorn](https://github.com/meiblorn) -*Initial work*

See also the list of [authors](authors.md) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Your questions will appear here. Feel free to ask me.