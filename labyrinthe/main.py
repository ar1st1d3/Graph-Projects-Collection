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

# Dans les méandres d'un donjon, se dessine un plan,
# Un labyrinthe de cases, une aventure sans fin.
def creer_donjon(matrice, n):
    n *= 4
    donjon = [["." for _ in range(n)] for _ in range(n)]

    # Une liste d'adjacence, pour guider le destin,
    # De chaque salle, chaque couloir, chaque chemin.
    liste_d_adjacence = {}
    for i in range(len(matrice)):
        liste_d_adjacence[i] = []
        for j in range(len(matrice)):
            if matrice[i][j] > 0:
                liste_d_adjacence[i].append(j)

    # Le centre est choisi, le cœur du labyrinthe,
    # Là où commence l'errance, où s'étire la plainte.
    x = n // 2
    y = n // 2
    l = []
    ajout_case(liste_d_adjacence, 0, n, l, x, y, donjon)

    # Le donjon est tracé, tel un rêve incarné,
    # Chaque salle, chaque couloir, dans la matrice est gravé.
    return donjon

# Une pièce est ajoutée, où s'étend le carré,
# Chaque coin est marqué, chaque passage refermé.
def ajout_case(liste_d_adjacence, key, n, l, x, y, donjon):
    if key in l:
        return

    # Un carré est formé, en neuf petits points,
    # Tel un pavé de lumière, où l'ombre n'a point de loin.
    carré = [[x-1, y-1],[x, y-1],[x+1, y-1],[x-1, y+1],[x, y+1],[x+1, y+1],[x-1, y],[x, y],[x+1, y]]
    for [dx, dy] in carré:
        if [dx, dy] == [x, y]:
            donjon[dx][dy] = key
        elif 0 <= dx < n and 0 <= dy < n and donjon[dx][dy] == ".":
            donjon[dx][dy] = "#"

    # Le chemin se prolonge, les portes se dessinent,
    # Pour qu'un nouvel horizon se dessine dans la brume fine.
    l.append(key)

    for i in liste_d_adjacence[key]:
        if i not in l:
            k = randint(1, 4)
            if k == 1 and x + 4 < n:
                donjon[x+2][y] = "|"
                ajout_case(liste_d_adjacence, i, n, l, x+4, y, donjon)
            elif k == 2 and x - 4 >= 0:
                donjon[x-2][y] = "|"
                ajout_case(liste_d_adjacence, i, n, l, x-4, y, donjon)
            elif k == 3 and y + 4 < n:
                donjon[x][y+2] = "-"
                ajout_case(liste_d_adjacence, i, n, l, x, y+4, donjon)
            elif k == 4 and y - 4 >= 0:
                donjon[x][y-2] = "-"
                ajout_case(liste_d_adjacence, i, n, l, x, y-4, donjon)

# Enfin, le donjon s'éveille, dans une mosaïque de pierres,
# Où chaque ligne raconte, une histoire de mystères.
def affichage_donjon(donjon): 
    for ligne in donjon:
        print(" ".join(map(str, ligne)))

# La matrice prend vie, sous l'ombre des chiffres,
# Et le donjon se trace, à travers les lignes et les chiffres.
matrice =  creation_graphe_pondéré(6)
matrice_prim = algo_prim(matrice)
donjon = creer_donjon(matrice_prim, 6)

# L'affichage se fait, tel un tableau suspendu,
# Où le graphe et le donjon, sont enfin étendus.
affichage_donjon(donjon)
afficher_graphe_graphique(matrice_prim)
