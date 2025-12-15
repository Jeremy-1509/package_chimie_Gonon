# package_chimie_Gonon

Package Python permettant de modéliser des **atomes**, des **molécules** et des **réactions chimiques simples** à l’aide de la programmation orientée objet.  
Ce projet s’inscrit dans le cadre du **Projet Python ISUP – Parcours ISDS**.

## Objectif du projet
L’objectif de ce projet est de mettre en pratique les concepts de **programmation orientée objet**, de **structuration d’un package Python** et de **qualité de code**.  
Le package propose une modélisation simple de concepts chimiques sans nécessiter de connaissances approfondies en chimie.

## Fonctionnalités
- Représentation d’**atomes** via une classe `Atom` (symbole, nombre d’électrons, masse, configuration électronique)
- Représentation de **molécules** via une classe `Molecule` à partir d’une formule brute
- Calcul automatique de la **masse molaire** d’une molécule
- Vérification de la **validité d’une réaction chimique** (conservation des atomes)
- Modélisation simple de la **cinétique de décomposition** d’une molécule

## Structure du projet

```
package_chimie_Gonon/
├── chempkg/
│ ├── atom.py
│ ├── mol.py
│ ├── reaction_utils.py
│ └── init.py
└── tests
    ├── test_atom.py
    ├── test_molecule.py
    └── test_reactions_utils.py
└── README.md
```

## 📥 Installation
Cloner le dépôt puis installer le package en mode développement :
```bash
git clone https://github.com/Jeremy-1509/package_chimie_Gonon
cd package_chimie_Gonon
pip install -e .
