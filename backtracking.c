#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define SIZE 8
#define X 0
#define Y 0
#define and &&
#define or ||


int deplacements_x[] = {2, 1, -1, -2, -2, -1, 1, 2};
int deplacements_y[] = {1, 2, 2, 1, -1, -2, -2, -1};

typedef struct {
    int echiquier[SIZE][SIZE];
} echiquier_t;


bool estValide(int x, int y, echiquier_t echiquier);
void trouverCheminHamiltonien(echiquier_t *echiquier);
bool trouverCheminUtil(int x, int y, int etape, echiquier_t *echiquier, int dx[], int dy[]);


int main()
{
    echiquier_t echiquier;
    trouverCheminHamiltonien(&echiquier);
    for (int i = 0; i < SIZE; i++)
    {
        for (int j = 0; j < SIZE; j++)
        {
            printf("%d ", echiquier.echiquier[i][j]);
        }
        printf("\n");
    }
    return 0;
}


bool estValide(int x, int y, echiquier_t echiquier)
{
    return x >= 0 and y >= 0 and x < SIZE and y < SIZE and echiquier.echiquier[x][y] == -1;
}


void trouverCheminHamiltonien(echiquier_t *echiquier)
{
    for (int i = 0; i < SIZE; i++)
    {
        for (int j = 0; j < SIZE; j++)
        {
            echiquier->echiquier[i][j] = -1;
        }
    }
    echiquier->echiquier[X][Y] = 0;

    if (!trouverCheminUtil(X, Y, 1, echiquier, deplacements_x, deplacements_y))
    {
        printf("Pas de solution");
        exit(1);
    }
}


bool trouverCheminUtil(int x, int y, int etape, echiquier_t *echiquier, int dx[], int dy[])
{
    if (etape == SIZE * SIZE)
    {
        return true;
    }

    for (int i = 0; i < SIZE; i++)
    {
        int prochain_x = x + dx[i];
        int prochain_y = y + dy[i];
        if (estValide(prochain_x, prochain_y, *echiquier))
        {
            echiquier->echiquier[prochain_x][prochain_y] = etape;
            if (trouverCheminUtil(prochain_x, prochain_y, etape + 1, echiquier, dx, dy))
            {
                return true;
            }
            echiquier->echiquier[prochain_x][prochain_y] = -1;
        }
    }

    return false;
}
