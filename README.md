# LaCE_fake

This is a fork from Chris-Pedersen/LaCE_manager, that was used to manage the hydrodynamic simulations of the LaCE emulator (Pedersen et al. 2021, 2022).

LaCE is the Lyman-alpha Cosmology Emulator. This code is a Gaussian process emulator for the 1D flux power spectrum of the Lyman-alpha forest. The emulator itself is accessible via: https://github.com/igmhub/LaCE

This fork focuses on the post-processing of the hydrodynamic simulations using fake_spectra, from https://github.com/sbird/fake_spectra


## Installation

1. Make sure you have LaCE properly installed, and that the variable `export LACE_REPO=/path/to/repo/LaCE` is set.
2. Ensure the python dependencies below are installed
3. Run `python setup.py install`


### Dependencies:

The following modules are required:

- inherited from LaCE

 `numpy`

 `scipy`

 `matplotlib`

 `configobj`

 `camb` 

- to extract / read skewers using fake_spectra
  
 `fake_spectra` 

 `bigfile` 

 `hdf5`

 - extra book-keeping

`configargparse`

`validate`
