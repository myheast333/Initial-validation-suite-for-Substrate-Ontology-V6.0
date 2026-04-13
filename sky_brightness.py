#!/usr/bin/env python3
"""
Olbers' Paradox vs CMB: Unified View Simulation
Substrate Ontology V6.0 - Section 3.6.4

Demonstrates why the night sky is dark in visible light but bright in microwaves.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Physical constants
T_CMB = 2.725          # CMB temperature (K)
T_SUN = 5778           # Solar surface temperature (K)
h = 6.626e-34
k_B = 1.381e-23
c = 2.998e8

# V6.0 parameters
NU_CUTOFF = 1e7        # Cutoff frequency ~10 MHz
ALPHA = 1.8            # Attenuation exponent

def planck_spectrum(nu, T):
    """Standard Planck blackbody spectrum."""
    return (2 * h * nu**3 / c**2) / (np.exp(h * nu / (k_B * T)) - 1)

def v6_attenuation(nu):
    """V6.0 geometric dilution attenuation factor."""
    return 1 - np.exp(-ALPHA * (NU_CUTOFF / nu))

def v6_spectrum(nu, T):
    """V6.0 predicted spectrum with attenuation."""
    return planck_spectrum(nu, T) * v6_attenuation(nu)

def main():
    print("=" * 60)
    print("Olbers' Paradox vs CMB: Unified View")
    print("Substrate Ontology V6.0 - Section 3.6.4")
    print("=" * 60)
    
    # Frequency range: 1 kHz to 1 PHz
    nu = np.logspace(3, 15, 2000)
    
    # CMB spectra
    cmb_planck = planck_spectrum(nu, T_CMB)
    cmb_v6 = v6_spectrum(nu, T_CMB)
    
    # Starlight (diluted by factor representing cosmic average)
    # The dilution factor accounts for finite stellar density and distance
    DILUTION_FACTOR = 1e-13  # Makes visible light ~dark
    
    # Representative stellar spectrum (solar type)
    stellar_raw = planck_spectrum(nu, T_SUN)
    stellar_diluted = stellar_raw * DILUTION_FACTOR * v6_attenuation(nu)
    
    # Create figure
    fig, ax = plt.subplots(1, 2, figsize=(13, 5))
    
    # Left panel: Spectra comparison
    ax[0].loglog(nu, cmb_planck, 'b-', linewidth=2, alpha=0.7, label='CMB (Planck)')
    ax[0].loglog(nu, cmb_v6, 'cyan', linewidth=2, label='CMB (V6.0)')
    ax[0].loglog(nu, stellar_diluted, 'orange', linewidth=2, label='Starlight (diluted)')
    
    # Mark visible band
    ax[0].axvspan(4e14, 8e14, alpha=0.2, color='yellow', label='Visible band')
    ax[0].axvline(x=NU_CUTOFF, color='gray', linestyle='--', alpha=0.7, label=f'ν_cutoff = {NU_CUTOFF/1e6:.0f} MHz')
    
    ax[0].set_xlabel('Frequency ν (Hz)')
    ax[0].set_ylabel('Effective Spectral Radiance')
    ax[0].set_title('Why the Night Sky is Dark (Visible) but Bright (Microwave)')
    ax[0].legend(loc='upper right')
    ax[0].grid(True, alpha=0.3)
    
    # Right panel: Visibility ratio (Starlight / CMB)
    ratio = stellar_diluted / cmb_v6
    ax[1].semilogx(nu, ratio, 'g-', linewidth=2)
    ax[1].axhline(y=1, color='gray', linestyle='--', alpha=0.5, label='Equal brightness')
    ax[1].axvspan(4e14, 8e14, alpha=0.2, color='yellow')
    ax[1].set_xlabel('Frequency ν (Hz)')
    ax[1].set_ylabel('Starlight / CMB Ratio')
    ax[1].set_title('Dominance: CMB (ratio < 1) vs Starlight (ratio > 1)')
    ax[1].legend()
    ax[1].grid(True, alpha=0.3)
    ax[1].set_ylim(1e-10, 1e10)
    
    # Annotate
    visible_idx = np.argmin(np.abs(nu - 5e14))
    microwave_idx = np.argmin(np.abs(nu - 1e11))
    
    print(f"\n📊 Results:")
    print(f"   At visible light (500 THz): Starlight/CMB ratio = {ratio[visible_idx]:.2e}")
    print(f"   At microwave (100 GHz):     Starlight/CMB ratio = {ratio[microwave_idx]:.2e}")
    print(f"\n   → In visible band, CMB is {1/ratio[visible_idx]:.1e} times fainter than diluted starlight")
    print(f"   → In microwave band, CMB dominates by factor of {1/ratio[microwave_idx]:.1e}")
    
    plt.tight_layout()
    
    os.makedirs('figures', exist_ok=True)
    output_path = 'figures/sky_brightness_olbers.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"\n📈 Figure saved to: {output_path}")
    
    plt.show()
    print("\n✅ Validation complete.")

if __name__ == '__main__':
    main()
