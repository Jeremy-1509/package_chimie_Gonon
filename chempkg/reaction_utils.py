"""Fonctions utilitaires pour réactions chimiques.

Ce module contient de petits helpers pour vérifier si une réaction
chimique est équilibrée (comptes d'atomes identiques des deux côtés) et
un modèle cinétique très simple pour une décomposition d'ordre 1 avec
option de sauvegarde du graphe.
"""

import numpy as np
import matplotlib.pyplot as plt
from chempkg.mol import Molecule


def valid_reaction(
    reactives: list[tuple[Molecule, int]],
    products: list[tuple[Molecule, int]],
) -> bool:

    """
    Vérifie si une réaction chimique est valide.

    Une réaction est valide si le nombre total d'atomes de chaque type
    est identique du côté des réactifs et des produits.

    Args:
        reactives (list[tuple[Molecule, int]]): Réactifs avec coefficients.
        products (list[tuple[Molecule, int]]): Produits avec coefficients.

    Returns:
        bool: True si la réaction est valide, False sinon.
    """
    reactives_count = {}
    for molecule, coeff in reactives:
        for atom, number in molecule.atoms.items():
            reactives_count[atom] = (
                reactives_count.get(atom, 0) + number * coeff
            )

    products_count = {}
    for molecule, coeff in products:
        for atom, number in molecule.atoms.items():
            products_count[atom] = (
                products_count.get(atom, 0) + number * coeff
            )

    return reactives_count == products_count



def kinetic_decomp(a0, k, t, steps=10, figure_path=None):
    """Calcule la décomposition d'ordre 1 A -> produits.

    Renvoie le tableau des concentrations A(t) échantillonné en ``steps``
    points entre 0 et ``t``. Si ``figure_path`` est donné, un tracé est
    sauvegardé à ce chemin.
    """

    times = np.linspace(0, t, steps)
    a_t = a0 * np.exp(-k * times)

    # tracer la courbe si demandé
    if figure_path is not None:
        plt.plot(times, a_t)
        plt.xlabel("Temps")
        plt.ylabel("[A](t)")
        plt.title("Cinétique de décomposition")
        plt.savefig(figure_path)
        plt.close()

    return a_t
