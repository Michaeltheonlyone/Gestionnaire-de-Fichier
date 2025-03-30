import tkinter as tk
from tkinter import Listbox, Entry, messagebox, simpledialog
import os
from PIL import Image, ImageTk
import subprocess
import platform
import time

# --- CONSTANTES ---
ICON_SIZE = 64      # Taille des icônes
ICON_PADDING = 10   # Espace entre les icônes

# --- FONCTIONS DE BASE ---

def load_icons():
    """Charge les icônes pour les différents types de fichiers."""
    icons = {}
    try:
        icons['folder'] = ImageTk.PhotoImage(Image.open("ICONS/folder_icon.png").resize((ICON_SIZE, ICON_SIZE)))
        icons['txt']    = ImageTk.PhotoImage(Image.open("ICONS/txt_icon.png").resize((ICON_SIZE, ICON_SIZE)))
        icons['img']    = ImageTk.PhotoImage(Image.open("ICONS/img_icon.png").resize((ICON_SIZE, ICON_SIZE)))
        icons['pdf']    = ImageTk.PhotoImage(Image.open("ICONS/pdf_icon.png").resize((ICON_SIZE, ICON_SIZE)))
        icons['default']= ImageTk.PhotoImage(Image.open("ICONS/baboosh.png").resize((ICON_SIZE, ICON_SIZE)))
        # Associer explicitement les extensions d'image
        img_icon = icons['img']
        for ext in ['jpg', 'jpeg', 'png', 'gif', 'bmp']:
            icons[ext] = img_icon
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur de chargement des icônes: {e}")
    return icons

def open_item(path):
    """Ouvre un fichier ou charge un dossier."""
    if os.path.isdir(path):
        load_folders(path)
    else:
        try:
            if platform.system() == "Windows":
                os.startfile(path)
            elif platform.system() == "Darwin":  # macOS
                subprocess.Popen(["open", path])
            else:  # Linux
                subprocess.Popen(["xdg-open", path])
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur d'ouverture du fichier: {e}")

def show_context_menu(event, path):
    """Affiche le menu contextuel au clic droit."""
    context_menu = tk.Menu(root, tearoff=0)
    context_menu.add_command(label="Ajouter aux Favoris", command=lambda: add_to_favorites(path))
    context_menu.add_command(label="Supprimer", command=lambda: delete_item(path))
    context_menu.add_command(label="Renommer", command=lambda: rename_item(path))
    context_menu.add_command(label="Afficher les détails", command=lambda: show_file_details(path))
    context_menu.post(event.x_root, event.y_root)

def add_to_favorites(path):
    """Ajoute un élément aux favoris."""
    if path not in favorites:
        favorites.append(path)
        messagebox.showinfo("Favoris", "Ajouté aux favoris.")

def show_favorites():
    """Affiche (ici, charge) le premier favori (à personnaliser selon vos besoins)."""
    if favorites:
        load_folders(favorites[0])
    else:
        messagebox.showinfo("Favoris", "Aucun favori enregistré.")

def delete_item(path):
    """Supprime un fichier ou dossier."""
    try:
        if os.path.isdir(path):
            os.rmdir(path)
        else:
            os.remove(path)
        load_folders(current_path.get())
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur de suppression: {e}")

def rename_item(path):
    """Renomme un fichier ou dossier."""
    new_name = simpledialog.askstring("Renommer", "Entrez le nouveau nom:")
    if new_name:
        try:
            new_path = os.path.join(os.path.dirname(path), new_name)
            os.rename(path, new_path)
            load_folders(current_path.get())
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur de renommage: {e}")

def show_file_details(path):
    """Affiche les détails (taille, date, type) d'un fichier ou dossier dans la zone dédiée."""
    details_text = ""
    try:
        if os.path.isdir(path):
            details_text = f"Type : Dossier\nTaille : N/A\nCréation : {time.ctime(os.path.getctime(path))}"
        else:
            size = os.path.getsize(path)
            details_text = f"Type : Fichier\nTaille : {size} octets\nCréation : {time.ctime(os.path.getctime(path))}"
    except Exception as e:
        details_text = f"Erreur : {e}"
    details_label.config(text=details_text)

def filter_files():
    """Filtre l'affichage des fichiers par extension."""
    ext = simpledialog.askstring("Filtrer les fichiers", "Entrez l'extension (ex: .txt):")
    if ext:
        load_folders(current_path.get(), filter_ext=ext)

def refresh_files():
    """Rafraîchit l'affichage du dossier courant."""
    load_folders(current_path.get())

def search_files():
    """Recherche des fichiers contenant le terme dans le dossier courant."""
    term = search_entry.get().lower().strip()
    if not term:
        messagebox.showinfo("Recherche", "Veuillez entrer un terme de recherche.")
        return
    try:
        items = os.listdir(current_path.get())
        filtered = [item for item in items if term in item.lower()]
        file_canvas.delete("all")
        x, y = ICON_PADDING, ICON_PADDING
        max_width = file_canvas.winfo_width() or 1200
        for item in sorted(filtered):
            full_path = os.path.join(current_path.get(), item)
            ext = item.split('.')[-1].lower() if '.' in item else ''
            icon = icons['folder'] if os.path.isdir(full_path) else icons.get(ext, icons['default'])
            frame = tk.Frame(file_canvas, bd=2, relief="solid")
            window_id = file_canvas.create_window(x, y, window=frame, anchor="nw")
            lbl_icon = tk.Label(frame, image=icon)
            lbl_icon.image = icon
            lbl_icon.pack()
            lbl_name = tk.Label(frame, text=item, wraplength=ICON_SIZE*2, font=("Arial", 10, "bold"))
            lbl_name.pack()
            lbl_name.bind("<Double-Button-1>", lambda e, p=full_path: open_item(p))
            lbl_name.bind("<Button-3>", lambda e, p=full_path: show_context_menu(e, p))
            file_canvas.update_idletasks()
            bbox = file_canvas.bbox(window_id)
            if bbox:
                item_width = bbox[2] - bbox[0]
            else:
                item_width = ICON_SIZE + ICON_PADDING*2
            x += item_width + ICON_PADDING
            if x + item_width + ICON_PADDING > max_width:
                x = ICON_PADDING
                y += ICON_SIZE + ICON_PADDING*2
        file_canvas.configure(scrollregion=file_canvas.bbox("all"))
    except Exception as e:
        messagebox.showerror("Erreur", f"Erreur lors de la recherche : {e}")

# --- Fonction de chargement dynamique dans le canvas ---
def load_folders(path, filter_ext=None):
    file_canvas.delete("all")
    if not os.path.isdir(path):
        messagebox.showerror("Erreur", "Chemin invalide")
        return
    path_display.delete(0, "end")
    path_display.insert(0, path)
    current_path.set(path)
    try:
        items = os.listdir(path)
        items.sort()
        x, y = ICON_PADDING, ICON_PADDING
        max_width = file_canvas.winfo_width() or 1200
        for item in items:
            if filter_ext and not item.endswith(filter_ext):
                continue
            full_path = os.path.join(path, item)
            ext = item.split('.')[-1].lower() if '.' in item else ''
            icon = icons['folder'] if os.path.isdir(full_path) else icons.get(ext, icons['default'])
            frame = tk.Frame(file_canvas, bd=2, relief="solid")
            window_id = file_canvas.create_window(x, y, window=frame, anchor="nw")
            lbl_icon = tk.Label(frame, image=icon)
            lbl_icon.image = icon
            lbl_icon.pack()
            lbl_name = tk.Label(frame, text=item, wraplength=ICON_SIZE*2, font=("Arial", 10, "bold"))
            lbl_name.pack()
            lbl_name.bind("<Double-Button-1>", lambda e, p=full_path: open_item(p))
            lbl_name.bind("<Button-3>", lambda e, p=full_path: show_context_menu(e, p))            
            file_canvas.update_idletasks()
            bbox = file_canvas.bbox(window_id)
            if bbox:
                item_width = bbox[2] - bbox[0]
            else:
                item_width = ICON_SIZE + ICON_PADDING*2
            x += item_width + ICON_PADDING
            if x + item_width + ICON_PADDING > max_width:
                x = ICON_PADDING
                y += ICON_SIZE + ICON_PADDING*2
        file_canvas.configure(scrollregion=file_canvas.bbox("all"))
    except PermissionError:
        pass

def on_path_enter(event):
    load_folders(path_display.get())

def lhs_selection(event):
    selection = lhs_list.curselection()
    if selection:
        selected_item = lhs_list.get(selection[0])
        if selected_item == "Local Disk":
            load_folders("C:/")
        elif selected_item == "Computer":
            drives = [d.strip() for d in os.popen("wmic logicaldisk get name").read().splitlines() if d.strip() and d.strip() != "Name"]
            if drives:
                load_folders(drives[0])
            else:
                messagebox.showerror("Erreur", "Aucun disque trouvé.")
        elif selected_item == "Recent":
            load_folders(os.path.expanduser("~"))
        elif selected_item == "Tags":
            messagebox.showinfo("Tags", "Pas encore implémenté.")
        elif selected_item == "Favorites":
            show_favorites()

def create_new_folder():
    folder_name = simpledialog.askstring("Nouveau dossier", "Entrez le nom du dossier:")
    if folder_name:
        try:
            new_folder_path = os.path.join(current_path.get(), folder_name)
            if not os.path.exists(new_folder_path):
                os.mkdir(new_folder_path)
                load_folders(current_path.get())  # Actualise l'affichage du dossier courant
            else:
                messagebox.showerror("Erreur", "Ce dossier existe déjà.")
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur de création du dossier: {e}")


# --- Interface Graphique ---

root = tk.Tk()
root.title("Gestionnaire de fichiers")
root.geometry("1200x800")  # Fenêtre redimensionnable avec boutons standards
root.config(bg="lightgray")

icons = load_icons()
current_path = tk.StringVar()
current_path.set(os.getcwd())
favorites = []

# Conteneur principal
main_frame = tk.Frame(root, bg="lightgray", bd=5, relief="solid")
main_frame.pack(fill="both", expand=True)

# Barre du haut : chemin + recherche
top_bar = tk.Frame(main_frame, bg="white", bd=5, relief="solid")
top_bar.grid(row=0, column=1, columnspan=2, sticky="ew", padx=10, pady=5)

path_display = Entry(top_bar, font=("Arial", 14), bg="white", bd=1, justify="center")
path_display.pack(side="left", fill="x", expand=True, padx=5, pady=5)
path_display.insert(0, current_path.get())
path_display.bind("<Return>", on_path_enter)

search_entry = tk.Entry(top_bar, font=("Arial", 14), width=20)
search_entry.pack(side="left", padx=5, pady=5)

search_button = tk.Button(top_bar, text="Rechercher", font=("Arial", 14, "bold"), command=search_files)
search_button.pack(side="left", padx=5, pady=5)

# Sidebar (LHS)
sidebar = tk.Frame(main_frame, bg="lightgray", width=200, bd=5, relief="solid")
sidebar.grid(row=1, column=0, sticky="ns", padx=10, pady=5)

lhs_list = Listbox(sidebar, font=("Arial", 12), bd=5, relief="solid")
lhs_list.pack(fill="both", expand=True, padx=5, pady=5)
lhs_list.insert("end", "Recent")
lhs_list.insert("end", "Local Disk")
lhs_list.insert("end", "Computer")
lhs_list.insert("end", "Tags")
lhs_list.insert("end", "Favorites")
lhs_list.bind("<<ListboxSelect>>", lhs_selection)

# Boutons dans la sidebar
button_frame = tk.Frame(sidebar, bg="lightgray", bd=5, relief="solid")
button_frame.pack(fill="x", padx=5, pady=5)
create_button = tk.Button(button_frame, text="Nouveau Dossier", font=("Arial", 12, "bold"), command=create_new_folder)
create_button.pack(fill="x", padx=5, pady=5)
filter_button = tk.Button(button_frame, text="Filtrer", font=("Arial", 12, "bold"), command=filter_files)
filter_button.pack(fill="x", padx=5, pady=5)
refresh_button = tk.Button(button_frame, text="Actualiser", font=("Arial", 12, "bold"), command=refresh_files)
refresh_button.pack(fill="x", padx=5, pady=5)

# Zone d'affichage des fichiers (Canvas)
file_canvas = tk.Canvas(main_frame, bg="white", bd=5, relief="solid")
file_canvas.grid(row=1, column=1, sticky="nsew", padx=10, pady=5)

v_scroll = tk.Scrollbar(main_frame, orient="vertical", command=file_canvas.yview)
v_scroll.grid(row=1, column=2, sticky="ns", padx=5, pady=5)
file_canvas.configure(yscrollcommand=v_scroll.set)

# Utilisation du canvas pour un affichage dynamique
# Les icônes seront créées directement dans le canvas via la fonction load_folders
# (La fonction load_folders redéfinie plus haut effectue ce travail)

# Zone de détails en bas
details_frame = tk.Frame(main_frame, bg="lightgray", bd=5, relief="solid")
details_frame.grid(row=2, column=1, columnspan=2, sticky="ew", padx=10, pady=5)
details_label = tk.Label(details_frame, text="Sélectionnez un fichier pour afficher les détails.", font=("Arial", 12, "bold"), bg="lightgray")
details_label.pack(fill="x", padx=5, pady=5)

# Configuration de la grille principale
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(1, weight=1)

# Charger le dossier initial
load_folders(current_path.get())

root.mainloop()
