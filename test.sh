#!/usr/bin/env bash

# compare our output with apt-mark showmanual
# if working, there should be nothing in the diff
apt-mark showmanual | sort > manual.txt
dpkg-status-explicit | sort > ours.txt
diff manual.txt ours.txt
