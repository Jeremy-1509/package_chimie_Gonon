"""Utilitaires et petites données pour la configuration électronique des atomes.

Ce module fournit des fonctions d'aide pour calculer le remplissage des
orbitales électroniques et définit un petit ensemble d'instances `Atom`
utilisées dans le projet.
"""

# pylint: disable=invalid-name

Sous_couche = [
    (1, 0),  # 1s
    (2, 0),  # 2s
    (2, 1),  # 2p
    (3, 0),  # 3s
    (3, 1),  # 3p
    (4, 0),  # 4s
    (3, 2),  # 3d
    (4, 1),  # 4p
    (5, 0),  # 5s
    (4, 2),  # 4d
    (5, 1),  # 5p
    (6, 0),  # 6s
    (4, 3),  # 4f
    (5, 2),  # 5d
    (6, 1),  # 6p
    (7, 0),  # 7s
    (5, 3),  # 5f
    (6, 2),  # 6d
    (7, 1),  # 7p
]


def num_elec(l):
    """Renvoie le nombre maximal d'électrons pour une sous-couche de nombre quantique l.

    La formule utilisée est (2*l + 1) * 2 car chaque orbitale peut contenir
    deux électrons et il y a (2*l + 1) orbitales pour un l donné.
    """
    return (2 * l + 1) * 2


def get_orbitales(z):
    """Renvoie la liste des orbitales occupées pour un atome à z électrons.

    La liste retournée contient des tuples (n, l, count) décrivant combien
    d'électrons occupent chaque sous-couche selon l'ordre défini dans
    `Sous_couche`.
    """
    atoms = z
    orbitales_atom = []
    i = 0

    while atoms > 0 and i < len(Sous_couche):
        n, l = Sous_couche[i]

        atoms_couche = num_elec(l)

        if atoms >= atoms_couche:
            num_atom = atoms_couche
        else:
            num_atom = atoms

        atoms -= num_atom

        orbitales_atom.append((n, l, num_atom))

        i += 1

    return orbitales_atom


Lettre = {0: "s", 1: "p", 2: "d", 3: "f"}


def elec_config(z):
    """Renvoie une configuration électronique lisible pour z électrons.

    Exemple : elec_config(6) -> ('1s2', '2s2', '2p2')
    """
    orbitales = get_orbitales(z)
    config = []

    for n, l, num_atom in orbitales:
        lettre2 = Lettre[l]
        config.append(f"{n}{lettre2}{num_atom}")

    return tuple(config)


class Atom:
    """Petit objet valeur représentant un atome.

    Attributs
    ---------
    name : str
        Symbole chimique (ex. 'C', 'O').
    num_electron : int
        Nombre d'électrons.
    weight : float
        Masse atomique approchée.
    elec_config : tuple[str, ...]
        Configuration électronique sous forme de tuple de chaînes.
    """

    def __init__(self, name: str, num_electron: int, weight: float):
        self.name = name
        self.num_electron = int(num_electron)
        self.weight = float(weight)
        # configuration électronique sous forme de tuple de str
        self.elec_config = elec_config(self.num_electron)

    def __repr__(self):
        # utilisé dans l’interpréteur / debug
        return self.name

    def __str__(self):
        # pour afficher l'atome de façon lisible
        return f"{self.name} ({self.weight}, {self.num_electron})"

    def __eq__(self, other):
        if not isinstance(other, Atom):
            return NotImplemented
        # égalité raisonnable : mêmes propriétés
        return (
            self.name == other.name
            and self.num_electron == other.num_electron
            and self.weight == other.weight
        )

    def __hash__(self):
        return hash((self.name, self.num_electron, self.weight))


# Atomes courants de la biosphère (poids arrondis)
oxygen = Atom("O", 8, 16)
carbon = Atom("C", 6, 12)
hydrogen = Atom("H", 1, 1)
nitrogen = Atom("N", 7, 14)
calcium = Atom("Ca", 20, 40)
phosphorus = Atom("P", 15, 30)
potassium = Atom("K", 1, 39)
sulfur = Atom("S", 16, 32)
sodium = Atom("Na", 11, 23)
chlorine = Atom("Cl", 17, 35)
iron = Atom("Fe", 26, 56)
iodine = Atom("I", 53, 127)
fluorine = Atom("F", 9, 19)
cobalt = Atom("Co", 27, 58)
molybdenum = Atom("Mo", 42, 96)


# Raccourcis symbole -> instance
O = oxygen
C = carbon
H = hydrogen
N = nitrogen
Ca = calcium
P = phosphorus
K = potassium
S = sulfur
Na = sodium
Cl = chlorine
Fe = iron
I = iodine
F = fluorine
Co = cobalt
Mo = molybdenum


biosphere_elements = [
    oxygen,
    carbon,
    hydrogen,
    nitrogen,
    calcium,
    phosphorus,
    potassium,
    sulfur,
    sodium,
    chlorine,
    iron,
    iodine,
    fluorine,
    cobalt,
    molybdenum,
]
