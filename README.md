# Initial Validation Suite for Substrate Ontology V6.0

This repository provides independent numerical validation of key predictions from Substrate Ontology V6.0 theory.

## Core Validation Modules

### 1. CMB Low-Frequency Cutoff (`cmb_spectrum_corrected.py`)
- **Prediction**: 38 dB attenuation at 1 MHz due to geometric dilution
- **Calibration**: ALPHA = 0.876 calibrated to exact 38 dB deviation
- **Validation Path**: FARSIDE 2029 lunar mission
- **Falsification Criterion**: < 36 dB at 1 MHz

### 2. Quark Confinement Scaling (`quark_confinement_calibrated.py`)
- **Prediction**: r_conf ∝ 1/C₂ with σ = 0.577 fm⁻¹
- **Calibration**: Anchored to experimental quark r_conf = 1.3 fm
- **Validation Path**: Lattice QCD gluelump simulations
- **Falsification Criterion**: Gluon r_conf outside [0.45, 0.75] fm

### 3. Olbers' Paradox Resolution (`olbers_cmb_unified.py`)
- **Prediction**: Unified explanation for dark visible sky and bright microwave sky
- **Mechanism**: Geometric dilution preserves CMB while diluting starlight
- **Validation Path**: Multi-wavelength sky brightness measurements

## Quick Start

```bash
git clone https://github.com/myheast333/Initial-validation-suite-for-Substrate-Ontology-V6.0.git
cd Initial-validation-suite-for-Substrate-Ontology-V6.0
pip install -r requirements.txt

# Run individual validations
python simulations/cmb_spectrum_corrected.py
python simulations/quark_confinement_calibrated.py
python simulations/olbers_cmb_unified.py
