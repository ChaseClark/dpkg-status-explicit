# DPKG-STATUS-EXPLICIT

## Not meant for actual use

A simple program that mimics "apt-mark showmanual" or Gentoo's selected set.

Tested on Ubuntu 24.04 and Debian 12

## How to Install

```sh
git clone https://github.com/ChaseClark/dpkg-status-explicit.git
cd dpkg-status-explicit
sudo dpkg -i dpkg-status-explicit.deb
```

## How to Run

in a terminal:

```sh
dpkg-status-explicit
```

Compare results with "apt-mark showmanual":

```sh
./test.sh
```

There should be no output.
