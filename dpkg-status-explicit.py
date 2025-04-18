#!/usr/bin/env python3

DPKG_STATUS_PATH = "/var/lib/dpkg/status"  # all packages on machine
APT_EXTENDED_STATES_PATH = "/var/lib/apt/extended_states"  # auto installed packages
extended_packages = []

with open(APT_EXTENDED_STATES_PATH) as f:
    extended_package_lines = f.read().strip().split("\n\n")
for p in extended_package_lines:
    if "Auto-Installed: 1" in p:  # make sure package is auto-installed
        # extract the package name from first line
        name = p.splitlines()[0].split(" ")[1]
        extended_packages.append(name)

with open(DPKG_STATUS_PATH) as f:
    package_lines = f.read().strip().split("\n\n")  
for p in package_lines:
    if "install ok installed" in p:
        name = p.splitlines()[0].split(" ")[1]
        if name not in extended_packages:
            # we only want packages that the user installed explicitly
            print(name)
