# Tricc project template

Project template to start a visual authoring project using Tricc


## Content

- Scratchpad: give the drawio shapes supported by Tricc
- L2: folder where the drawio files are stored
- L3: output for Tricc
- .github/workflows: CI that run tricc via github actions

# Getting started online

1. Fork this repository
1. open https://draw.io and use github as storage
1. tweak the github actions to setup the wished output strategy
1. Create content
1. push content on github
1. see the result on the Actions


# Getting started offline

1. Fork this repository
1. open https://draw.io and use github as storage
1. Run `pip install tricc_oo` ideally in a virtual env (`pythom -m venv .venv`)
1. tweak the build.py actions to setup the wished output strategy
1. Create content
1. run build.py
1. see the result on the L3 folder

