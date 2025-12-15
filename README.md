# package_chimie_Gonon

# chempkg

Package Python (Projet Python ISUP/ISDS – Partie 2) pour manipuler des **atomes**, des **molécules** et des **réactions chimiques simples** en programmation orientée objet. :contentReference[oaicite:1]{index=1}

## Fonctionnalités
- `Atom` : symbole, nombre d’électrons, masse, configuration électronique (règle de Klechkowski), + `__str__`, `__repr__`, `__eq__`
- `Molecule` : parsing d’une formule brute (ex: `"C2OH6"`), dictionnaire `{Atom: quantité}`, masse molaire totale
- `reaction_utils` :
  - vérification de validité d’une réaction (conservation des atomes)
  - cinétique de décomposition (loi exponentielle) + sauvegarde optionnelle d’une figure

## Structure
- `atom.py` : classe `Atom`
- `mol.py` : classe `Molecule`
- `reaction_utils.py` : fonctions liées aux réactions
- `__init__.py` : point d’entrée du package :contentReference[oaicite:2]{index=2}

## Installation (local)
Dans le dossier du projet :
```bash
pip install -e .
