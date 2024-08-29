# Graph Projects Collection

Bienvenue dans la collection de projets sur les graphes ! Ce dépôt contient une variété de projets qui utilisent des graphes non orientés pour résoudre différents types de problèmes. Chaque projet est conçu pour vous aider à mieux comprendre les concepts des graphes et à appliquer ces concepts à des applications pratiques.

<img src="/images/cover.jpg">

## Table des Matières

- [Projets](#projets)
  - [Générateur de Labyrinthes](#générateur-de-labyrinthes)
  - [Simulateur de Réseau Social](#simulateur-de-réseau-social)
  - [Planificateur de Trajets](#planificateur-de-trajets)
  - [Simulateur de Réseau Électrique](#simulateur-de-réseau-électrique)
  - [Simulateur de Réseau de Transport](#simulateur-de-réseau-de-transport)
- [Installation](#installation)

## Projets

### Générateur de Labyrinthes

**Description** : Ce projet génère des labyrinthes de manière procédurale en utilisant des algorithmes comme l'algorithme de Prim ou de Kruskal. Le labyrinthe est représenté comme un graphe non orienté, où chaque nœud représente une cellule et chaque arête représente un chemin entre deux cellules.

**Fonctionnalités** :
- Génération procédurale de labyrinthes.
- Visualisation du labyrinthe.
- Calcul du plus court chemin dans le labyrinthe.

**Dossier** : [Labyrinthe](./labyrinthe)

### Simulateur de Réseau Social

**Description** : Ce projet simule un réseau social où les utilisateurs peuvent se connecter en tant qu'amis. Le réseau social est représenté comme un graphe non orienté, où chaque nœud représente un utilisateur et chaque arête représente une connexion d'amitié entre deux utilisateurs.

**Fonctionnalités** :
- Création d'utilisateurs.
- Ajout d'amis.
- Visualisation du réseau social.
- Analyse du réseau pour détecter des communautés ou des influenceurs.

**Dossier** : [Réseau Social](./reseau_social)

### Planificateur de Trajets

**Description** : Ce projet aide les utilisateurs à trouver le meilleur itinéraire entre deux points en fonction de divers critères (temps, distance, coût, etc.). Le réseau de transport est représenté comme un graphe non orienté, où chaque nœud représente une intersection et chaque arête représente une route entre deux intersections.

**Fonctionnalités** :
- Calcul d'itinéraire.
- Sélection de critères pour l'itinéraire.
- Navigation détaillée.
- Visualisation de l'itinéraire.

**Dossier** : [Planificateur de Trajets](./planificateur_trajets)

### Simulateur de Réseau Électrique

**Description** : Ce projet simule un réseau électrique où les centrales électriques, les sous-stations et les consommateurs sont connectés par des lignes électriques. Le réseau électrique est représenté comme un graphe non orienté, où chaque nœud représente une centrale électrique, une sous-station ou un consommateur, et chaque arête représente une ligne électrique entre deux nœuds.

**Fonctionnalités** :
- Création de nœuds (centrales électriques, sous-stations, consommateurs).
- Ajout de lignes électriques.
- Visualisation du réseau électrique.
- Calcul du flux d'énergie.
- Analyse du réseau pour détecter des points de défaillance.

**Dossier** : [Réseau Électrique](./reseau_electrique)

### Simulateur de Réseau de Transport

**Description** : Ce projet simule un réseau de transport où les villes sont connectées par des routes. Le réseau de transport est représenté comme un graphe non orienté, où chaque nœud représente une ville et chaque arête représente une route entre deux villes.

**Fonctionnalités** :
- Création de villes.
- Ajout de routes.
- Visualisation du réseau de transport.
- Calcul du plus court chemin entre deux villes.
- Analyse du réseau pour détecter des points de congestion.

**Dossier** : [Réseau de Transport](./reseau_transport)

## Installation

Pour installer les dépendances nécessaires, utilisez les commandes suivantes :

```bash
pip install networkx matplotlib
