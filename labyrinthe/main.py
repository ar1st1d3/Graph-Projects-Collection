from random import randint
import networkx as nx
import matplotlib.pyplot as plt

# Là où le hasard danse et l'algorithme veille,
# Nous créons un graphe, tel un rêve qui s'éveille.
def creation_graphe_pondéré(n):
    # Un vaste tableau, une matrice sans fin,
    # Où naîtront les liens, fils d'un destin incertain.
    matrice = [[0 for _ in range(n)] for _ in range(n)]

    # Pour chaque paire de sommets, le destin est jeté,
    # L'arête naîtra, ou bien elle sera rejetée.
    for i in range(n):
        for j in range(i + 1, n):
            if randint(0, 1) == 1:
                m = randint(1, 9)
                matrice[i][j] = m
                matrice[j][i] = m

    # Et voilà, le graphe pondéré est né,
    # Prêt à révéler ce que le hasard a semé.
    return matrice

# Dans le royaume des nombres, les liens s'affichent,
# Chaque ligne, chaque colonne, par un souffle d'or s'enrichent.
def afficher_graphe_matrice(matrice):
    for ligne in matrice:
        print(" ".join(map(str, ligne)))

# Sur un canevas numérique, le graphe prend forme,
# Les arêtes s'élancent, les sommets se conform.
def afficher_graphe_graphique(matrice):
    G = nx.Graph()

    # Les nœuds, tels des étoiles, s'allument un à un,
    # Dans ce firmament mathématique où tout est commun.
    for i in range(len(matrice)):
        G.add_node(i)

    # Les liens s'étirent, invisibles mais réels,
    # Unissant les points, tissant des arcs de ciel.
    for i in range(len(matrice)):
        for j in range(i + 1, len(matrice[i])):
            if matrice[i][j] > 0:
                G.add_edge(i, j, weight=matrice[i][j])

    # La gravité numérique dessine les chemins,
    # Où chaque nœud trouve place, là où il s'éteint ou s'épanouit enfin.
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, font_size=12, font_weight='bold', edge_color='gray')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

# Sur l'arbre de Prim, la forêt d'arêtes pousse,
# Cherchant le chemin minimal, là où l'ombre est douce.
def algo_prim(matrice):
    n = len(matrice)
    matrice_prim = [[0 for _ in range(n)] for _ in range(n)]
    mini = float('inf')
    arrete = ()
    sommets = [0]
    edges = []

    # D'un sommet à l'autre, le fil d'or s'étend,
    # Reliant l'inconnu, d'une lumière vacillante.
    while len(sommets) < n:
        for i in sommets:
            for j in range(n):
                if j not in sommets and 0 < matrice[i][j] < mini:
                    mini = matrice[i][j]
                    arrete = (i, j)

        if mini == float('inf'):
            # Quand le lien se rompt, et que tout semble perdu,
            # On cherche un nouvel écho, un cri encore entendu.
            for i in range(n):
                if i not in sommets:
                    for j in range(n):
                        if matrice[i][j] > 0 and (i, j) not in edges and (j, i) not in edges:
                            arrete = (i, j)
                            mini = matrice[i][j]
                            break
                    if mini != float('inf'):
                        break

        # Le sommet est choisi, et le chemin est tracé,
        # Dans la matrice de Prim, les arêtes sont posées.
        sommets.append(arrete[1])
        matrice_prim[arrete[0]][arrete[1]] = mini
        matrice_prim[arrete[1]][arrete[0]] = mini
        edges.append(arrete)
        mini = float('inf')

    # Ainsi s'élève la structure, solide et légère,
    # Un graphe minimal, où chaque arête éclaire.
    return matrice_prim


# La matrice prend vie, sous l'ombre des chiffres,
# Et le labyrinthe se trace, à travers les lignes et les chiffres.
matrice =  creation_graphe_pondéré(6)
matrice_prim = algo_prim(matrice)

# L'affichage se fait, tel un tableau suspendu,
# Où le graphe et le labyrinthe, sont enfin étendus.
afficher_graphe_graphique(matrice_prim)
