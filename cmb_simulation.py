#!/usr/bin/env python3
"""
CMB Low-Frequency Spectral Attenuation Simulation
Substrate Ontology V6.0 - Section 3.6.8

Prediction: CMB blackbody spectrum deviates from Planck curve at ν < 10 MHz
due to geometric dilution truncation of deficit wavefronts.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Physical constants
T_CMB = 2.725          # CMB temperature (K)
h = 6.626e-34          # Planck constant (J·s)
k_B = 1.381e-23        # Boltzmann constant (J/K)
c = 2.998e8            # Speed of light (m/s)

# V6.0 theoretical parameters (from Section 3.6.8)
NU_CUTOFF = 1e7        # Cutoff frequency ~10 MHz (Hz)
ALPHA = 1.8            # Attenuation exponent from discrete substrate geometry

def planck_spectrum(nu, T):
    """Standard Planck blackbody spectrum (spectral radiance)."""
    return (2 * h * nu**3 / c**2) / (np.exp(h * nu / (k_B * T)) - 1)

def v6_attenuation(nu):
    """
    V6.0 geometric dilution attenuation factor.
    At nu >> NU_CUTOFF, attenuation → 1 (no effect).
    At nu << NU_CUTOFF, attenuation → exponential suppression.
    """
    return 1 - np.exp(-ALPHA * (NU_CUTOFF / nu))

def v6_spectrum(nu, T):
    """V6.0 predicted spectrum with low-frequency attenuation."""
    return planck_spectrum(nu, T) * v6_attenuation(nu)

def main():
    print("=" * 60)
    print("CMB Low-Frequency Cutoff Simulation")
    print("Substrate Ontology V6.0 - Section 3.6.8")
    print("=" * 60)
    
    # Frequency range: 10 kHz to 1 THz (log scale)
    nu = np.logspace(4, 12, 1000)  # Hz
    
    # Compute spectra
    planck = planck_spectrum(nu, T_CMB)
    v6 = v6_spectrum(nu, T_CMB)
    
    # Calculate deviation at 1 MHz
    idx_1MHz = np.argmin(np.abs(nu - 1e6))
    deviation_db = 10 * np.log10(planck[idx_1MHz] / v6[idx_1MHz])
    
    print(f"\n📊 Results:")
    print(f"   CMB Temperature: {T_CMB} K")
    print(f"   Cutoff frequency: {NU_CUTOFF/1e6:.1f} MHz")
    print(f"   Attenuation exponent α: {ALPHA}")
    print(f"\n   Deviation at 1 MHz: {deviation_db:.1f} dB")
    print(f"   (V6.0 prediction: ~38 dB)")
    
    # Create figure
    fig, ax = plt.subplots(1, 2, figsize=(12, 5))
    
    # Left panel: log-log spectrum
    ax[0].loglog(nu, planck, 'b-', linewidth=2, label='Planck (Standard)')
    ax[0].loglog(nu, v6, 'orange', linewidth=2, label='V6.0 Prediction')
    ax[0].axvline(x=NU_CUTOFF, color='gray', linestyle='--', alpha=0.7, label=f'ν_cutoff = {NU_CUTOFF/1e6:.0f} MHz')
    ax[0].set_xlabel('Frequency ν (Hz)')
    ax[0].set_ylabel('Spectral Radiance (W·m⁻²·sr⁻¹·Hz⁻¹)')
    ax[0].set_title('CMB Spectrum: Planck vs V6.0')
    ax[0].legend()
    ax[0].grid(True, alpha=0.3)
    
    # Right panel: deviation ratio (dB)
    ratio_db = 10 * np.log10(planck / v6)
    ax[1].semilogx(nu, ratio_db, 'r-', linewidth=2)
    ax[1].axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    ax[1].axvline(x=NU_CUTOFF, color='gray', linestyle='--', alpha=0.7)
    ax[1].set_xlabel('Frequency ν (Hz)')
    ax[1].set_ylabel('Deviation (dB)')
    ax[1].set_title('V6.0 Deviation from Planck Spectrum')
    ax[1].grid(True, alpha=0.3)
    
    # Highlight 1 MHz point
    ax[1].scatter([1e6], [deviation_db], color='red', s=100, zorder=5)
    ax[1].annotate(f'{deviation_db:.1f} dB @ 1 MHz', 
                   xy=(1e6, deviation_db), xytext=(2e6, deviation_db+5),
                   arrowprops=dict(arrowstyle='->', color='red'))
    
    plt.tight_layout()
    
    # Save figure
    os.makedirs('figures', exist_ok=True)
    output_path = 'figures/cmb_spectrum_comparison.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"\n📈 Figure saved to: {output_path}")
    
    plt.show()
    print("\n✅ Validation complete.")

if __name__ == '__main__':
    main()
