import tkinter as tk
from globales import SIZE
import random

class Echec(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.taille_des_cases = (min(self.winfo_screenwidth(), self.winfo_screenheight()) - 200) / SIZE
        self.title("SAE 2.02")
        self.geometry(f"{int(SIZE*self.taille_des_cases)}x{int(SIZE*self.taille_des_cases + 41)}") # 41px est la hauteur du texte qui indique le temps d'execution
        self.cavalier = "♞"
        self.canvas = tk.Canvas(self, width=SIZE*self.taille_des_cases, height=SIZE*self.taille_des_cases)
        self.ancienne_position = None # Variable pour stocker l'ancienne position du cavalier
        self.dessineEchec()
    
    def dessineEchec(self):
        colors = ["white", "gray"]
        for i in range(SIZE):
            for j in range(SIZE):
                color = colors[(i + j) % 2]
                x1, y1 = j * self.taille_des_cases, i * self.taille_des_cases
                x2, y2 = x1 + self.taille_des_cases, y1 + self.taille_des_cases
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        
    def placerCavalier(self, coord):
        x, y = coord
        self.canvas.create_text(x * self.taille_des_cases + (self.taille_des_cases / 2), y * self.taille_des_cases + (self.taille_des_cases / 2), text=self.cavalier, font=("Arial", int(self.taille_des_cases * 0.9)), tag="cavalier")
        if not self.ancienne_position:
            x_center = x * self.taille_des_cases + (self.taille_des_cases / 2)
            y_center = y * self.taille_des_cases + (self.taille_des_cases / 2)
            self.canvas.create_oval(x_center - self.taille_des_cases / 4, y_center - self.taille_des_cases / 4, x_center + self.taille_des_cases / 4, y_center +self.taille_des_cases / 4, fill="red", outline="red", width=2)
        self.ancienne_position = coord
        
    def deplacerCavalier(self, coord):
        x, y = coord
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        if self.ancienne_position:
            x1, y1 = self.ancienne_position
            self.canvas.create_line(x1 * self.taille_des_cases + (self.taille_des_cases / 2), y1 * self.taille_des_cases + (self.taille_des_cases / 2), x * self.taille_des_cases + (self.taille_des_cases / 2), y * self.taille_des_cases + (self.taille_des_cases / 2), fill='#{0:02x}{1:02x}{2:02x}'.format(r, g, b), width=max(1, min(5, int(self.taille_des_cases * 0.1))))
            
        self.canvas.delete("cavalier")  # Supprime l'ancien cavalier
        self.placerCavalier((x, y))  # Place le cavalier à la nouvelle position
        self.ancienne_position = coord
        
    def afficher(self, temps):
        self.text = tk.Label(text="Temps d'exécution : %.3f secondes" % temps, font=("sans-serif", 20))
        self.text.pack()
        self.canvas.pack()
        self.mainloop()


if __name__ == "__main__":

    echec = Echec()

    echec.afficher(0)

