from globales import SIZE

echiquier = [[False for _ in range(SIZE)] for _ in range(SIZE)]

def backtracking(echiquier : list, numero_case: int = 0) -> bool:
    resultat = False
    ligne, colonne = int
    if(numero_case == SIZE*SIZE):
        resultat = True
    else:
        ligne = numero_case // SIZE
        colonne = numero_case % SIZE
        if not echiquier[ligne][colonne]:
            resultat = backtracking(echiquier, numero_case + 1)
        else:
            for i in range(1, SIZE):
                pass



















"""
bool backtracking(t_grille_backtracking grille, int numeroCase)
{
        else
        {
            for (int valeur = 1; valeur <= TAILLE_GRILLE; valeur++)
            {
                if (possible(grille, ligne, colonne, valeur))
                {
                    // Si la valeur est autorisee on l'inscrit
                    //dans la case...
                    grille[ligne][colonne].valeur = valeur;
                    // ... et on passe a la suivante : appel recursif
                    // pour voir si ce choix est bon par la suite
                    if (backtracking(grille, numeroCase + 1))
                    {
                        result = true;
                    }
                    else
                    {
                        grille[ligne][colonne].valeur = 0;
                    }
                }
            }
        }
    }

    return result;
}
"""