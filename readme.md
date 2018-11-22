Boltun (aka rus. [Болтун](https://en.wiktionary.org/wiki/%D0%B1%D0%BE%D0%BB%D1%82%D1%83%D0%BD))
===

Generates massive datasets from just a single template.

```text
Command:
> python -m boltun "{{ Hi || Hello }}, [[ 'welcome' | upper? ]][[? ' back' ]] to Boltun! What[% any('\'s', ' is') %] your name [% any('?', '??') %]"

Hello, welcome to Boltun! What's your name ?
Hi, WELCOME back to Boltun! What is your name ?
Hello, WELCOME back to Boltun! What is your name ?
Hi, welcome back to Boltun! What is your name ?
Hello, welcome back to Boltun! What is your name ?
Hi, WELCOME to Boltun! What is your name ?
Hello, WELCOME to Boltun! What is your name ?
Hi, welcome to Boltun! What is your name ?
Hello, welcome to Boltun! What is your name ?
Hi, WELCOME back to Boltun! What's your name ??
Hello, WELCOME back to Boltun! What's your name ??
Hi, welcome back to Boltun! What's your name ??
Hello, welcome back to Boltun! What's your name ??
Hi, WELCOME to Boltun! What's your name ??
Hello, WELCOME to Boltun! What's your name ??
Hi, welcome to Boltun! What's your name ??
Hello, welcome to Boltun! What's your name ??
Hi, WELCOME back to Boltun! What is your name ??
Hello, WELCOME back to Boltun! What is your name ??
Hi, welcome back to Boltun! What is your name ??
Hello, welcome back to Boltun! What is your name ??
Hi, WELCOME to Boltun! What is your name ??
Hello, WELCOME to Boltun! What is your name ??
Hi, welcome to Boltun! What is your name ??
Hello, welcome to Boltun! What is your name ??
```

Branch   | CI status
---------|-------------------
master   | [![Build Status](https://travis-ci.org/meiblorn/boltun.svg?branch=master)](https://travis-ci.org/meiblorn/boltun)[![codecov](https://codecov.io/gh/meiblorn/boltun/branch/master/graph/badge.svg)](https://codecov.io/gh/meiblorn/boltun)
develop  | [![Build Status](https://travis-ci.org/meiblorn/boltun.svg?branch=develop)](https://travis-ci.org/meiblorn/boltun)[![codecov](https://codecov.io/gh/meiblorn/boltun/branch/develop/graph/badge.svg)](https://codecov.io/gh/meiblorn/boltun)

## About

[![boltun_simpsons_bart](https://raw.githubusercontent.com/meiblorn/boltun/master/static/simpsons_bart.png)](https://github.com/meiblorn/boltun)

Designed was designed to be best alternative for the NLP machine learning developers.
It was developed as an alternative for such projects as 
[Chatito](https://github.com/rodrigopivi/Chatito) and [Tracery](http://tracery.io/). 
Yes, they almost good, especially Tracery, but both of them are written for Node.JS platform.
And, as you know, Node.js is a single threaded language — 
so, as result, that tools are perfect only for small amounts of data. 
Boltun breaks that bounds of data generation limits.

## Getting Started

### Installing

`pip install boltun`

### Usage

`pip -m boltun "<your template>"`

## Contributing

You are welcome to contribute ! Just submit your PR and become a part of Boltun community!

Please read [contributing.md](contributing.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/meiblorn/boltun/tags). 

## Authors

* **Vadim Fedorenko** - [Meiblorn](https://github.com/meiblorn) -*Initial work*

See also the list of [authors](authors.md) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Your questions will appear here. Feel free to ask me.