import psutil
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *


class MonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Monitor")

        # Étiquettes d'affichage
        self.ram_label = ttk.Label(root, text="Mémoire: 0%")
        self.ram_label.pack(pady=10)
        self.cpu_label = ttk.Label(root, text="CPU: 0%")
        self.cpu_label.pack(pady=10)

        # Entrées pour les seuils
        self.memory_threshold_var = tk.IntVar()
        self.memory_threshold_var.set(80)  # Valeur par défaut
        self.cpu_threshold_var = tk.IntVar()
        self.cpu_threshold_var.set(80)  # Valeur par défaut

        memory_entry = ttk.Entry(root, textvariable=self.memory_threshold_var, width=5)
        memory_entry.pack(side=tk.LEFT, padx=5)
        ttk.Label(root, text="% RAM").pack(side=tk.LEFT)

        cpu_entry = ttk.Entry(root, textvariable=self.cpu_threshold_var, width=5)
        cpu_entry.pack(side=tk.LEFT, padx=5)
        ttk.Label(root, text="% CPU").pack(side=tk.LEFT)

        # Bouton de mise à jour des seuils
        update_button = ttk.Button(root, text="Mettre à jour les seuils", command=self.update_threshold)
        update_button.pack(pady=10)

        # Étiquette pour afficher les seuils actuels
        self.threshold_label = ttk.Label(root, text=f'Seuil RAM: {self.memory_threshold_var.get()}% | Seuil CPU: {self.cpu_threshold_var.get()}%')
        self.threshold_label.pack()

        # Mise à jour initiale des étiquettes
        self.update_labels()

    def update_labels(self):
        memory_usage = psutil.virtual_memory().percent
        cpu_usage = psutil.cpu_percent(interval=None)
        self.ram_label.config(text=f'Mémoire: {memory_usage}%')
        self.cpu_label.config(text=f'CPU: {cpu_usage}%')

        self.root.after(1000, self.update_labels)  # Met à jour toutes les 1000 ms (1 seconde)

    def update_threshold(self):
        self.threshold_label.config(text=f'Seuil RAM: {self.memory_threshold_var.get()}% | Seuil CPU: {self.cpu_threshold_var.get()}%')


if __name__ == "__main__":
    root = tk.Tk()
    app = MonitorApp(root)
    root.mainloop()