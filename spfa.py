def spfa(v_inicial, v_final, V, C, A):
    Q = [v_inicial]
    D = dict()
    P = dict()
    for v_i in V:
        D.update([(v_i, float('inf'))])
        P.update([(v_i, None)])

    D[v_inicial] = 0
    while len(Q) > 0:
        v_atual = Q.pop(0)

        for a_i in A[v_atual]:
            C_total = D[v_atual] + C[(v_atual, a_i)]
            if C_total < D[a_i]:
                D[a_i] = C_total
                P[a_i] = v_atual
                if a_i not in Q:
                    Q.append(a_i)
    return reconstruir_caminho(P, v_final, v_inicial)
