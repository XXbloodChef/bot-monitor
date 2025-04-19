import tkinter as tk
from tkinter import ttk, scrolledtext

class MonitorApp:
    def __init__(self, root):
        root.title("Bot Monitor - Interface Graphique")
        root.geometry("1000x700")

        tab_control = ttk.Notebook(root)

        self.dashboard_tab = ttk.Frame(tab_control)
        self.settings_tab = ttk.Frame(tab_control)
        self.filters_tab = ttk.Frame(tab_control)
        self.logs_tab = ttk.Frame(tab_control)
        self.live_tab = ttk.Frame(tab_control)

        tab_control.add(self.dashboard_tab, text='📊 Tableau de bord')
        tab_control.add(self.settings_tab, text='⚙️ Paramètres')
        tab_control.add(self.filters_tab, text='🛠️ Filtres')
        tab_control.add(self.live_tab, text='📡 Articles en live')
        tab_control.add(self.logs_tab, text='📄 Logs')
        tab_control.pack(expand=1, fill="both")

        # DASHBOARD
        ttk.Label(self.dashboard_tab, text="Bienvenue dans le Monitor Bot", font=("Arial", 16)).pack(pady=10)
        ttk.Label(self.dashboard_tab, text="Statut global : OK", foreground="green").pack()

        # PARAMÈTRES
        ttk.Label(self.settings_tab, text="Configuration générale", font=("Arial", 14)).pack(pady=5)
        ttk.Label(self.settings_tab, text="Scan interval (s)").pack()
        ttk.Entry(self.settings_tab).pack()
        ttk.Label(self.settings_tab, text="Mode :").pack()
        ttk.Combobox(self.settings_tab, values=["production", "simulation"]).pack()

        # FILTRES
        ttk.Label(self.filters_tab, text="Filtres actifs", font=("Arial", 14)).pack(pady=5)
        ttk.Label(self.filters_tab, text="Exemple :").pack()
        sample_filter = tk.Text(self.filters_tab, height=10, width=100)
        sample_filter.insert("1.0", "- filtre: pokemon-coffret
  mots-clés: coffret, ultra premium
  ping: @elite")
        sample_filter.pack()

        # LIVE ARTICLES
        ttk.Label(self.live_tab, text="Articles détectés en temps réel", font=("Arial", 14)).pack(pady=5)
        self.live_box = scrolledtext.ScrolledText(self.live_tab, wrap=tk.WORD, width=100, height=25)
        self.live_box.pack(padx=10, pady=5)
        self.live_box.insert(tk.END, "[Live Feed démarré...]
")

        # LOGS
        ttk.Label(self.logs_tab, text="Logs d'exécution", font=("Arial", 14)).pack(pady=5)
        self.log_box = scrolledtext.ScrolledText(self.logs_tab, wrap=tk.WORD, width=100, height=20)
        self.log_box.pack(padx=10, pady=5)
        self.log_box.insert(tk.END, "[Logs en attente...]
")

if __name__ == '__main__':
    root = tk.Tk()
    app = MonitorApp(root)
    root.mainloop()
