### Hexlet tests and linter status:
[![Actions Status](https://github.com/Savin20153/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Savin20153/python-project-50/actions)

[![Python CI](https://github.com/Savin20153/python-project-50/actions/workflows/main.yml/badge.svg)](https://github.com/Savin20153/python-project-50/actions/workflows/main.yml)

# gendiff

gendiff - is a program that looks for the differences between the two.json or yaml formats and displays the result on the screen

## Installation

- Сloning the github repository
```
$ git clone git@github.com:ivanvasutinskiy/python-project-49.git
```
- Install make on Ubuntu
```
$ sudo apt install make
```
- UV Installation
```
$ curl -LsSf https://astral.sh/uv/install.sh | sh
```

- Launching the program
```
$ make install
$ make build 
$ make package-install
```
Output formats:
- stylish - shows clearly the differences in the two files;
- plain - shows the changes flatly.
- json - shows changes in the json format

## Example of work

[![asciicast](https://asciinema.org/a/4UaUMmKJi6eCkopVmq2BE1BDc.svg)](https://asciinema.org/a/4UaUMmKJi6eCkopVmq2BE1BDc)
