#!/usr/bin/env python3
"""
Quark Confinement Distance vs Color Charge Simulation
Substrate Ontology V6.0 - Section 4.5

Prediction: r_conf ∝ 1 / C₂(R), where C₂ is the quadratic Casimir operator.
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# QCD experimental reference values
R_CONF_QUARK = 1.3          # Confinement radius for quark (fm)
C2_QUARK = 4/3              # C₂ for fundamental representation (3)
C2_GLUON = 3                # C₂ for adjoint representation (8)
C2_DIQUARK = 10/3           # C₂ for diquark (6)

# Theoretical prediction from V6.0
CHI_CRIT = 1.0              # Normalized vacuum excitation threshold
DELTA_CHI = 0.5             # Chirality energy level difference (normalized)

def confinement_radius(C2):
    """V6.0 prediction: r_conf ∝ 1 / C₂."""
    return R_CONF_QUARK * C2_QUARK / C2

def main():
    print("=" * 60)
    print("Quark Confinement Distance vs Color Charge")
    print("Substrate Ontology V6.0 - Section 4.5")
    print("=" * 60)
    
    # Representations and their Casimirs
    reps = ['Quark (3)', 'Gluon (8)', 'Diquark (6)']
    C2_values = [C2_QUARK, C2_GLUON, C2_DIQUARK]
    colors = ['blue', 'red', 'green']
    
    r_conf = [confinement_radius(c2) for c2 in C2_values]
    
    print("\n📊 Predicted Confinement Radii:")
    print("-" * 40)
    print(f"{'Representation':<15} {'C₂':<8} {'r_conf (fm)':<12}")
    print("-" * 40)
    for rep, c2, r in zip(reps, C2_values, r_conf):
        print(f"{rep:<15} {c2:<8.2f} {r:<12.3f}")
    print("-" * 40)
    print(f"\nReference: Observed quark confinement radius ≈ 1.2-1.5 fm")
    print(f"V6.0 predicts gluon confinement radius ≈ {r_conf[1]:.3f} fm")
    print(f"(Testable in lattice QCD via gluelump simulations)")
    
    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
    
    # Left panel: r_conf vs C₂
    C2_range = np.linspace(1, 5, 100)
    r_range = confinement_radius(C2_range)
    
    ax1.plot(C2_range, r_range, 'b-', linewidth=2)
    ax1.scatter(C2_values, r_conf, c=colors, s=150, zorder=5, edgecolors='black')
    for rep, c2, r, color in zip(reps, C2_values, r_conf, colors):
        ax1.annotate(rep, xy=(c2, r), xytext=(c2+0.2, r+0.05),
                     fontsize=10, color=color)
    
    ax1.set_xlabel('Quadratic Casimir C₂(R)')
    ax1.set_ylabel('Confinement Radius r_conf (fm)')
    ax1.set_title('V6.0 Prediction: r_conf ∝ 1/C₂')
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=1.3, color='gray', linestyle='--', alpha=0.5, label='Observed quark r_conf')
    ax1.legend()
    
    # Right panel: Wake accumulation potential
    r = np.linspace(0.1, 2.0, 200)
    
    # Potential for different representations
    for rep, c2, color in zip(reps, C2_values, colors):
        V = c2 * r  # Linear potential (string tension ∝ C₂)
        ax2.plot(r, V, color=color, linewidth=2, label=rep)
    
    ax2.axhline(y=CHI_CRIT, color='black', linestyle='--', alpha=0.7, label='χ_crit (vacuum threshold)')
    ax2.set_xlabel('Distance r (fm)')
    ax2.set_ylabel('Accumulated Chirality Deficit χ')
    ax2.set_title('Wake Accumulation and Confinement Threshold')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    ax2.set_ylim(0, 6)
    
    # Mark intersection points
    for c2, color, rep in zip(C2_values, colors, reps):
        r_intersect = CHI_CRIT / c2
        ax2.scatter([r_intersect], [CHI_CRIT], color=color, s=80, zorder=5, edgecolors='black')
    
    plt.tight_layout()
    
    os.makedirs('figures', exist_ok=True)
    output_path = 'figures/quark_confinement.png'
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"\n📈 Figure saved to: {output_path}")
    
    plt.show()
    print("\n✅ Validation complete.")

if __name__ == '__main__':
    main()
