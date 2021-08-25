v_inicial = 'Arad'
v_final = 'Bucharest'

V = {'Arad', 'Sibiu', 'Timisoara', 'Zerind', 'Fagaras', 'Oradea', 'Rimnicu', 'Bucharest', 'Craiova', 'Pitesti', 'Lugoj'}
H = {'Arad': 366, 'Sibiu': 253, 'Timisoara': 329, 'Zerind': 374, 'Fagaras': 176, 'Oradea': 380, 'Rimnicu': 193, 'Bucharest': 0, 'Craiova': 160, 'Pitesti': 100, 'Lugoj': 244}

A = {'Arad': ['Sibiu', 'Timisoara', 'Zerind'],
     'Sibiu': ['Arad','Fagaras', 'Oradea', 'Rimnicu'],
     'Timisoara': ['Arad', 'Lugoj'],
     'Zerind': ['Arad', 'Oradea'],
     'Fagaras': ['Bucharest', 'Sibiu'],
     'Oradea': ['Zerind', 'Sibiu'],
     'Rimnicu': ['Sibiu', 'Pitesti'],
     'Bucharest': ['Craiova', 'Fagaras'],
     'Craiova': ['Rimnicu', 'Pitesti'],
     'Pitesti': ['Rimnicu', 'Bucharest', 'Craiova'],
     'Lugoj': ['Timisoara']}

C = {('Arad', 'Timisoara'): 118, ('Arad', 'Sibiu'): 140, ('Arad', 'Zerind'): 75,
     ('Sibiu', 'Arad'): 140, ('Sibiu', 'Fagaras'): 99, ('Sibiu', 'Rimnicu'): 80, ('Sibiu', 'Oradea'): 151,
     ('Timisoara', 'Lugoj'): 111, ('Timisoara', 'Arad'): 118,
     ('Zerind', 'Oradea'): 71, ('Zerind', 'Arad'): 75,
     ('Fagaras', 'Sibiu'): 99, ('Fagaras', 'Bucharest'): 211,
     ('Oradea', 'Zerind'): 71, ('Oradea', 'Sibiu'): 151,
     ('Rimnicu', 'Sibiu'): 80, ('Rimnicu', 'Pitesti'): 97, ('Rimnicu', 'Craiova'): 146,
     ('Bucharest', 'Pitesti'): 101, ('Bucharest', 'Fagaras'): 211,
     ('Craiova', 'Pitesti'): 138 ,
     ('Pitesti', 'Craiova'): 138, ('Pitesti', 'Rimnicu'): 97, ('Pitesti', 'Bucharest'): 101,
     ('Lugoj', 'Timisoara'): 111
     }


def reconstruir_caminho(P, v_atual, v_inicial):
    caminho = [v_atual]
    while v_atual != v_inicial:
        v_atual = P[v_atual]
        caminho.append(v_atual)
    print(caminho[::-1])


def a_star(v_inicial, v_final, V, H, A, C):
    Q = []
    Q.append(v_inicial)
    O = []
    v_atual = 'inf'

    G = dict()
    F = dict()
    P = dict()
    for v_i in V:
        G.update([(v_i, float('inf'))])
        F.update([(v_i, float('inf'))])
        P.update([(v_i, None)])

    G[v_inicial] = 0
    F[v_inicial] = G[v_inicial] + H[v_inicial]

    while len(Q) > 0:
        minimo = float('inf')
        for i in range(len(Q)):
            if F[Q[i]] < minimo:
                minimo = F[Q[i]]
                v_atual = Q[i]

        Q.remove(v_atual)
        O.append(v_atual)

        if v_atual == v_final:
            return reconstruir_caminho(P, v_atual, v_inicial)

        for a_i in A[v_atual]:
            if a_i not in O:
                g = G[v_atual] + C[(v_atual, a_i)]
                f = g + H[a_i]
                if a_i not in Q or G[a_i] > g:
                    F[a_i] = f
                    G[a_i] = g
                    P[a_i] = v_atual
                    Q.append(a_i)


a_star(v_inicial, v_final, V, H, A, C)
