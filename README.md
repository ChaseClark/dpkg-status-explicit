TODO

- write instructions and description in readme
- push to github
- respond to email and send them a link to github repo

# DPKG-STATUS-EXPLICIT

A simple program that mimics "apt-mark showmanual" or Gentoo's selected set.

## How to Install

```sh
git clone ''
cd dpkg-status-explicit
sudo dpkg -i dpkg-status-explicit
```

## How to Run

in a terminal:

```sh
dpkg-status-explicit
```

Compare results with "apt-mark showmanual":

```sh
chmod +x test.sh
./test.sh
```

There should be no output.
