import tkinter as tk
from globales import SIZE
import random

class Echec(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.title("SAÉ 2.02")
        self.geometry(f"{SIZE*100}x{SIZE*100}")
        self.cavalier = "♞"
        self.canvas = tk.Canvas(self, width=SIZE*100, height=SIZE*100)
        self.canvas.pack()
        self.ancienne_position = None # Variable pour stocker l'ancienne position du cavalier
        self.dessineEchec()
    
    def dessineEchec(self):
        colors = ["white", "gray"]
        for i in range(SIZE):
            for j in range(SIZE):
                color = colors[(i + j) % 2]
                x1, y1 = j * 100, i * 100
                x2, y2 = x1 + 100, y1 + 100
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)
        
    def placerCavalier(self, coord):
        x, y = coord
        self.canvas.create_text(x * 100 + 50, y * 100 + 50, text=self.cavalier, font=("Arial", 64), tag="cavalier")
        if not self.ancienne_position:
            x_center = x * 100 + 50
            y_center = y * 100 + 50
            self.canvas.create_oval(x_center - 25, y_center - 25, x_center + 25, y_center +25, fill="red", outline="red", width=2)
        self.ancienne_position = coord
        
    def deplacerCavalier(self, coord):
        x, y = coord
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        if self.ancienne_position:
            x1, y1 = self.ancienne_position
            self.canvas.create_line(x1 * 100 + 50, y1 * 100 + 50, x * 100 + 50, y * 100 + 50, fill='#{0:02x}{1:02x}{2:02x}'.format(r, g, b), width=5)
            
        self.canvas.delete("cavalier")  # Supprime l'ancien cavalier
        self.placerCavalier((x, y))  # Place le cavalier à la nouvelle position
        self.ancienne_position = coord
        
    def afficher(self):
        self.mainloop()


if __name__ == "__main__":

    echec = Echec()

    echec.afficher()

