# ui.py
import tkinter as tk
from tkinter import ttk
from almanax_api import fetch_almanax
from utils import format_date_fr

class AlmanaxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("📅 Almanax DOFUS")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        self.create_widgets()
        self.load_data()

    def create_widgets(self):
        # --- Section du jour actuel ---
        self.current_frame = ttk.LabelFrame(self.root, text="📆 Aujourd’hui", padding=10)
        self.current_frame.pack(fill="x", padx=10, pady=10)

        self.lbl_date = ttk.Label(self.current_frame, text="Date : ")
        self.lbl_date.grid(row=0, column=0, sticky="w", pady=2)
        self.lbl_resource = ttk.Label(self.current_frame, text="Ressource : ")
        self.lbl_resource.grid(row=1, column=0, sticky="w", pady=2)
        self.lbl_quantity = ttk.Label(self.current_frame, text="Quantité : ")
        self.lbl_quantity.grid(row=2, column=0, sticky="w", pady=2)
        self.lbl_bonus = ttk.Label(self.current_frame, text="Bonus : ")
        self.lbl_bonus.grid(row=3, column=0, sticky="w", pady=2)

        # --- Section prochains jours ---
        self.upcoming_frame = ttk.LabelFrame(self.root, text="🗓️ Prochains jours", padding=10)
        self.upcoming_frame.pack(fill="both", expand=True, padx=10, pady=5)

        self.tree = ttk.Treeview(self.upcoming_frame, columns=("date", "resource", "quantity", "bonus"), show="headings", height=7)
        self.tree.heading("date", text="Date")
        self.tree.heading("resource", text="Ressource")
        self.tree.heading("quantity", text="Quantité")
        self.tree.heading("bonus", text="Bonus")
        self.tree.pack(fill="both", expand=True)

        # --- Bouton refresh ---
        self.btn_refresh = ttk.Button(self.root, text="🔄 Rafraîchir", command=self.load_data)
        self.btn_refresh.pack(pady=10)

    def load_data(self):
        """Charge les données du jour et de la semaine à venir."""
        # Jour actuel
        today = fetch_almanax(0)
        if today:
            self.lbl_date.config(text=f"Date : {format_date_fr(today['date'])}")
            self.lbl_resource.config(text=f"Ressource : {today['resource']}")
            self.lbl_quantity.config(text=f"Quantité : {today['quantity']}")
            self.lbl_bonus.config(text=f"Bonus : {today['bonus']}")
        else:
            self.lbl_date.config(text="Date : –")
            self.lbl_resource.config(text="Ressource : –")
            self.lbl_quantity.config(text="Quantité : –")
            self.lbl_bonus.config(text="Bonus : –")

        # Prochains jours
        for row in self.tree.get_children():
            self.tree.delete(row)

        for offset in range(1, 7):  # 6 prochains jours
            entry = fetch_almanax(offset)
            if entry:
                date_fr = format_date_fr(entry["date"])
                self.tree.insert("", "end", values=(date_fr, entry["resource"], entry["quantity"], entry["bonus"]))
