import tkinter as tk
from tkinter import messagebox

class Morpion:
    def __init__(self, root):
        self.root = root
        self.root.title("Jeu de Morpion")  
        self.current_player = "X"  # joueur actuel (commence par X)
        self.buttons = [[None for _ in range(3)] for _ in range(3)]  
        self.create_buttons()  # crée les boutons sur la fenetre

    def create_buttons(self):# crée les boutons pour chaque cellule de la grille
        for i in range(3):
            for j in range(3):
                
                self.buttons[i][j] = tk.Button(self.root, text=" ", font='normal 20 bold', height=3, width=6,
                                               command=lambda i=i, j=j: self.on_button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)  # place le bouton dans la grille

    def on_button_click(self, i, j):# Fonction appelée lorsque l'utilisateur clique sur un bouton
        if self.buttons[i][j]['text'] == " ":  
            self.buttons[i][j]['text'] = self.current_player  # remplit la case avec le symbole du joueur actuel
            if self.check_winner():  
                messagebox.showinfo("Morpion", f"Le joueur {self.current_player} a gagné !")  # affiche le gagnant
                self.reset_board()  
            elif self.is_board_full():  # Vérifie s'il y a match nul
                messagebox.showinfo("Morpion", "Match nul !")  
                self.reset_board()  
            else:
                self.current_player = "O" if self.current_player == "X" else "X"  # passe au tour du joueur suivant

    def check_winner(self):
        
        for i in range(3):
            if all(self.buttons[i][j]['text'] == self.current_player for j in range(3)):
                return True  # Gagnant sur une ligne
            if all(self.buttons[j][i]['text'] == self.current_player for j in range(3)):
                return True  # Gagnant sur une colonne

        if all(self.buttons[i][i]['text'] == self.current_player for i in range(3)):
            return True  # Gagnant sur la diagonale 
        if all(self.buttons[i][2 - i]['text'] == self.current_player for i in range(3)):
            return True  # Gagnant sur la diagonale 

        return False  

    def is_board_full(self):# Vérifie si la grille est pleine (match nul)
        return all(self.buttons[i][j]['text'] != " " for i in range(3) for j in range(3))

    def reset_board(self):# Réinitialise la grille pour un nouveau jeu
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = " "  # chaque case redeviens vide
        self.current_player = "X"  
if __name__ == "__main__":
    root = tk.Tk()  
    game = Morpion(root)  
    root.mainloop() 