# clipboardRemoveDoubleSlashesFromPath
A simple app that takes whatever is in your clipboard and replaces any double slashes with single forward slashes. So something like: `C:\\Users\\olliv\\.rustup\\toolchains\\stable-x86_64-pc-windows-msvc\\lib\\rustlib\\etc\\libstd.natvis` would become: `C:/Users/olliv/.rustup/toolchains/stable-x86_64-pc-windows-msvc/lib/rustlib/etc/libstd.natvis`

Tested on:
* Win11 Version 10.0.22000.1335
* Python 3.10.2

If you dont have a Python3 interpreter installed ([python.org](https://www.python.org/)), theres a bundled executable for Windows available in [releases](https://github.com/ItsCubeTime/clipboardRemoveDoubleSlashesFromPath/releases).

Usecase & demo:
https://youtu.be/14XHJsrkO2c
