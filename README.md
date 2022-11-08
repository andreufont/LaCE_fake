# LaCE_fake

This is a fork from Chris-Pedersen/LaCE_manager, that was used to manage the hydrodynamic simulations of the LaCE emulator (Pedersen et al. 2021, 2022).

LaCE is the Lyman-alpha Cosmology Emulator. This code is a Gaussian process emulator for the 1D flux power spectrum of the Lyman-alpha forest. The emulator itself is accessible via: https://github.com/igmhub/LaCE

This fork focuses on the post-processing of the hydrodynamic simulations using fake_spectra, from https://github.com/sbird/fake_spectra


# Instructions below need to be updated #




## Installation

1. Make sure you have LaCE properly installed, and that the variable `export LACE_REPO=/path/to/repo/LaCE` is set.
2. Set a similar environment variables for this repo: `export LACE_FAKE_REPO=/path/to/repo/LaCE_fake`. Best to set this in a `.bashrc` or similar.
3. Ensure the python dependencies below are installed
4. Run `python setup.py install`


#### Dependencies:

The following modules are required:

`numpy`

`scipy`

`matplotlib`

`configobj`

`CAMB` version 1.1.3 or later https://github.com/cmbant/CAMB (only works with Python 3.6 or later as of 14/01/2021)

`cProfile`

To setup/run/postprocess simulations:

`configargparse`

`fake_spectra` branch at https://github.com/Chris-Pedersen/fake_spectra which includes temperature rescalings in postprocessing

`validate`

`classylss`

`asciitable`
