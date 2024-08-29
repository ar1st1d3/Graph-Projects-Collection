# Générateur de Labyrinthes

Bienvenue dans le projet de générateur de labyrinthes ! Ce projet utilise des graphes non orientés pour générer des labyrinthes de manière procédurale. Chaque nœud représente une cellule du labyrinthe, et chaque arête représente un chemin entre deux cellules.

## Table des Matières

- [Description](#description)
- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Visualisation](#visualisation)
- [Contribution](#contribution)
- [Licence](#licence)

## Description

Ce projet génère des labyrinthes de manière procédurale en utilisant des algorithmes comme l'algorithme de Prim ou de Kruskal. Le labyrinthe est représenté comme un graphe non orienté, où chaque nœud représente une cellule et chaque arête représente un chemin entre deux cellules.

## Fonctionnalités

- **Génération Procédurale** : Génère des labyrinthes différents à chaque exécution.
- **Visualisation** : Utilise NetworkX et Matplotlib pour visualiser le labyrinthe.
- **Calcul du Plus Court Chemin** : Implémente l'algorithme de Dijkstra pour trouver le plus court chemin dans le labyrinthe.

## Installation

Pour installer les dépendances nécessaires, utilisez les commandes suivantes :

```bash
pip install networkx matplotlib
