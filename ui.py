# ui.py
import tkinter as tk
from tkinter import ttk
from almanax_api import fetch_almanax
from utils import format_date_fr
from datetime import datetime

class AlmanaxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🌿 Almanax Dofus - Guide Journalier")
        self.root.geometry("750x600")
        self.root.configure(bg="#2b2a24")  # fond sombre vert/brun
        self.root.resizable(False, False)

        self.style = ttk.Style()
        self.apply_custom_theme()
        self.create_widgets()
        self.load_data()

    def apply_custom_theme(self):
        """Applique un thème Dofus-like"""
        self.style.theme_use("clam")

        self.style.configure("TFrame", background="#2b2a24")
        self.style.configure("TLabelframe", background="#3b3a30", foreground="#f4e4b0", relief="ridge", borderwidth=3)
        self.style.configure("TLabelframe.Label", background="#3b3a30", foreground="#f4e4b0", font=("Georgia", 14, "bold"))
        self.style.configure("TLabel", background="#3b3a30", foreground="#e8e3c5", font=("Georgia", 12))
        self.style.configure("Treeview", background="#423f35", foreground="#f9f6e5", fieldbackground="#423f35", font=("Consolas", 11))
        self.style.configure("Treeview.Heading", background="#b6a05b", foreground="#2b2a24", font=("Georgia", 12, "bold"))
        self.style.map("Treeview", background=[("selected", "#8ca934")])
        self.style.configure("TButton", background="#a58f48", foreground="#2b2a24", font=("Georgia", 12, "bold"), padding=6)
        self.style.map("TButton", background=[("active", "#c9b56d")])

    def create_widgets(self):
        # Bannière
        title_frame = tk.Frame(self.root, bg="#2b2a24")
        title_frame.pack(pady=10)
        title_label = tk.Label(
            title_frame,
            text="⚜️ Almanax Dofus ⚜️",
            font=("Georgia", 28, "bold"),
            fg="#f4e4b0",
            bg="#2b2a24"
        )
        title_label.pack()

        subtitle_label = tk.Label(
            title_frame,
            text="Les offrandes et bonus journaliers des Douze",
            font=("Georgia", 13, "italic"),
            fg="#c9b56d",
            bg="#2b2a24"
        )
        subtitle_label.pack(pady=2)

        # Frame du jour
        self.current_frame = ttk.LabelFrame(self.root, text="📅 Aujourd’hui", padding=15)
        self.current_frame.pack(fill="x", padx=15, pady=10)

        self.lbl_date = ttk.Label(self.current_frame, text="Date : ")
        self.lbl_date.grid(row=0, column=0, sticky="w", pady=2)
        self.lbl_resource = ttk.Label(self.current_frame, text="Ressource : ")
        self.lbl_resource.grid(row=1, column=0, sticky="w", pady=2)
        self.lbl_quantity = ttk.Label(self.current_frame, text="Quantité : ")
        self.lbl_quantity.grid(row=2, column=0, sticky="w", pady=2)
        self.lbl_bonus = ttk.Label(self.current_frame, text="Bonus : ")
        self.lbl_bonus.grid(row=3, column=0, sticky="w", pady=2)

        # Ligne de séparation
        sep = ttk.Separator(self.root, orient="horizontal")
        sep.pack(fill="x", padx=20, pady=10)

        # Frame des prochains jours
        self.upcoming_frame = ttk.LabelFrame(self.root, text="🗓️ Prochains jours", padding=15)
        self.upcoming_frame.pack(fill="both", expand=True, padx=15, pady=5)

        self.tree = ttk.Treeview(
            self.upcoming_frame,
            columns=("date", "resource", "quantity", "bonus"),
            show="headings",
            height=8
        )
        self.tree.heading("date", text="Date")
        self.tree.heading("resource", text="Ressource demandée")
        self.tree.heading("quantity", text="Qté")
        self.tree.heading("bonus", text="Bonus du jour")
        self.tree.column("date", width=80, anchor="center")
        self.tree.column("resource", width=220)
        self.tree.column("quantity", width=60, anchor="center")
        self.tree.column("bonus", width=300)

        self.tree.pack(fill="both", expand=True, pady=5)

        # Bouton refresh stylé
        self.btn_refresh = ttk.Button(self.root, text="🔄 Rafraîchir les données", command=self.load_data)
        self.btn_refresh.pack(pady=12)

        # Footer
        footer = tk.Label(
            self.root,
            text=f"Mis à jour : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}",
            font=("Georgia", 9, "italic"),
            bg="#2b2a24",
            fg="#a58f48"
        )
        footer.pack(side="bottom", pady=5)
        self.footer = footer

    def load_data(self):
        """Charge les données du jour et des prochains jours."""
        today = fetch_almanax(0)
        if today:
            self.lbl_date.config(text=f"📆 Date : {format_date_fr(today['date'])}")
            self.lbl_resource.config(text=f"🪶 Ressource : {today['resource']}")
            self.lbl_quantity.config(text=f"📦 Quantité : {today['quantity']}")
            self.lbl_bonus.config(text=f"✨ Bonus : {today['bonus']}")
        else:
            self.lbl_date.config(text="📆 Date : –")
            self.lbl_resource.config(text="🪶 Ressource : –")
            self.lbl_quantity.config(text="📦 Quantité : –")
            self.lbl_bonus.config(text="✨ Bonus : –")

        # Nettoyer le tableau
        for row in self.tree.get_children():
            self.tree.delete(row)

        # Ajouter les jours à venir
        for offset in range(1, 7):
            entry = fetch_almanax(offset)
            if entry:
                date_fr = format_date_fr(entry["date"])
                self.tree.insert("", "end", values=(date_fr, entry["resource"], entry["quantity"], entry["bonus"]))

        self.footer.config(text=f"Mis à jour : {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
