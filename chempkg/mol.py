"""Utilitaires d'analyse des molécules.

Ce module expose une classe Molecule simple capable d'analyser des
formules chimiques comme C2H5OH et de calculer les comptes d'atomes ainsi
qu'une masse approchée.
"""

from .atom import biosphere_elements


# dictionnaire qui associe le nom de l'atome et son symbol
SYMBOL_TO_ATOM = {atom.name: atom for atom in biosphere_elements}


class Molecule:
    """Représentation d'une molécule.

    Le parseur gère des formules simples (symboles d'éléments suivis
    d'un entier optionnel). Pas de parenthèses ni de multiplications.
    """

    def __init__(self, formula: str):
        self.formula = formula
        self.atoms = self._parse_formula(formula)
        # poids approximé en sommant les masses atomiques
        self.weight = float(
            sum(atom.weight * count for atom, count in self.atoms.items())
        )

    def __repr__(self) -> str:  # pragma: no cover - trivial
        return f"Molecule({self.formula})"

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.formula

    def __eq__(self, other) -> bool:
        if not isinstance(other, Molecule):
            return NotImplemented
        return self.atoms == other.atoms

    def _parse_formula(self, formula: str) -> dict:
        """Parse une formule chimique simple et retourne {Atom: count}.

        Le parseur accepte des symboles d'éléments (majuscule puis
        éventuellement une minuscule) suivis d'un entier optionnel.
        """
        atoms_dict: dict = {}
        i = 0
        n = len(formula)

        while i < n:
            ch = formula[i]
            if not ch.isupper():
                raise ValueError(f"Symbole invalide dans la formule: '{ch}'")

            symbol = ch
            i += 1
            if i < n and formula[i].islower():
                symbol += formula[i]
                i += 1

            atom = SYMBOL_TO_ATOM.get(symbol)
            if atom is None:
                raise ValueError(f"Atome inconnu : {symbol}")

            # lire un entier éventuel
            num_str = ""
            while i < n and formula[i].isdigit():
                num_str += formula[i]
                i += 1

            count = int(num_str) if num_str else 1
            atoms_dict[atom] = atoms_dict.get(atom, 0) + count

        return atoms_dict
