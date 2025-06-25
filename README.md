

A Jupyter notebook-based Finite-Difference Time-Domain (FDTD) simulation of a gold (Au)  and silicon (Si) nanocube using [MEEP](https://meep.readthedocs.io/) and [tidy3D](https://tidy3d.simulation.cloud/learning-center). This project sets up a 3D simulation domain, defines a Gaussian electromagnetic source, places a cubic Au object at the center, applies perfectly-matched-layer (PML) boundaries, and records flux data to analyze scattering, absorption, and transmission spectra.

---

## 🚀 Features

- # 3D FDTD Simulation 
  Leverages MEEP to model a metallic cube (Au) and a dielectric silicon (Si) cube  in a uniform background.

- # Custom Material Properties 
  Uses the built-in `Au` material model from `meep.materials`.

-  # Source & Monitors
  Adds a pulsed Gaussian source and flux monitors to capture spectral response.
  The pulse acts as a broadband source. The scattered flux with the wavelength frequency window of 0.65 um t0 0.75um is studied.

- # Data Export & Analysis  
  – Save “empty domain” flux baseline  
  – Compute incident intensity  
  – Run with/without the Au cube and compare spectra  
  – Fourier transform time-domain fields to obtain frequency-domain results  



# 📦 Prerequisites

- Python 3.8+  
- [MEEP](https://meep.readthedocs.io/) (with Python bindings)  
- `numpy`  
- `matplotlib`
- Optional 
- A small `plot` helper module located in `plot/plot_style.py`  

You can install most dependencies via `conda` or `pip`:

```bash
# with conda (recommended for MEEP)
conda install -c conda-forge meep numpy matplotlib
conda activate  pmp

# or with pip
pip install numpy matplotlib
# (follow MEEP install instructions separately)
