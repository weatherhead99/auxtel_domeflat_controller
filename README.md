# Auxtel Domeflat Control manual script

This is a simple controller for the auxtel dome flat that can be used from
`jupyter` notebooks, `python` scripts, or with a very simple command line
utility.

## Installation

The package is pyproject.toml compliant, a recent python stack should be able
to use any one of `pip`, `pipx`, `poetry` etc to install it. As usual, I
recommend installing in a virtualenv. But, assuming you have the environment
set up as you want it, installation should be as simple as:

```
git clone https://github.com/weatherhead99/auxtel_domeflat_controller
cd auxtel_domeflat_controller
pip install .
```

(replace the last line with `pip install --user .` if for some reason you
don't have virtualenv properly set up and want this in your local python
environment

## Usage

There is an example notebook in this repository at
[/Example_notebook.ipynb](/Example_notebook.ipynb). It should be near self
explanatory.

Once installed, you should also have access to a command line script which can
be run from the terminal, called `domeflat_control`. It can be used to read
back the current value of the flat field with `domeflat_control --read`, or it
can be used to set the dome flat on (with `domeflat_control 1`) or off (with
`domeflat_control 0`).

Happy dome flatting!
