import tkinter as tk
import random
import string
import pyperclip

def generate_password_from_text():
    text = text_entry.get()
    length = length_entry.get()
    
    if not text or not length:
        error_label.config(text="Les champs 'Texte de base' et 'Longueur' sont obligatoires.", fg="red")
        return
    
    try:
        length = int(length)
    except ValueError:
        error_label.config(text="La longueur doit être un nombre entier.", fg="red")
        return
    
    include_uppercase = uppercase_var.get()
    include_numbers = numbers_var.get()
    include_symbols = symbols_var.get()
    
    # Utilisation du texte saisi comme base pour le mot de passe
    chars = text
    
    # Ajouter des caractères supplémentaires si nécessaire
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_numbers:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation
    
    # Générer le mot de passe
    generated_password = ''.join(random.choice(chars) for _ in range(length))
    
    # Afficher le mot de passe généré dans le champ de texte
    password_entry.config(state=tk.NORMAL)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, generated_password)
    password_entry.config(state=tk.DISABLED)
    
    # Effacer le message d'erreur
    error_label.config(text="")

def copy_to_clipboard():
    password = password_entry.get()
    pyperclip.copy(password)

def toggle_password_visibility():
    if show_password_var.get():
        password_entry.config(show='')
    else:
        password_entry.config(show='*')

# Création de la fenêtre principale
root = tk.Tk()
root.title("StarLight Complex Password Generator")

# Dimensions de la fenêtre
window_width = 400
window_height = 450

# Obtenir les dimensions de l'écran
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculer les coordonnées pour centrer la fenêtre
position_top = int((screen_height - window_height) / 2)
position_right = int((screen_width - window_width) / 2)

# Ajuster la géométrie de la fenêtre
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")
root.resizable(False, False)  # Désactiver l'agrandissement de la fenêtre

# Interface utilisateur
tk.Label(root, text="Texte de base pour le mot de passe").pack(pady=5)
text_entry = tk.Entry(root, width=40)
text_entry.pack(pady=5)

tk.Label(root, text="Longueur du mot de passe").pack(pady=5)
length_entry = tk.Entry(root, width=10)
length_entry.pack(pady=5)

uppercase_var = tk.BooleanVar()
uppercase_check = tk.Checkbutton(root, text="Inclure majuscules", variable=uppercase_var)
uppercase_check.pack(pady=5)

numbers_var = tk.BooleanVar()
numbers_check = tk.Checkbutton(root, text="Inclure chiffres", variable=numbers_var)
numbers_check.pack(pady=5)

symbols_var = tk.BooleanVar()
symbols_check = tk.Checkbutton(root, text="Inclure caractères spéciaux", variable=symbols_var)
symbols_check.pack(pady=5)

show_password_var = tk.BooleanVar()
show_password_check = tk.Checkbutton(root, text="Afficher le mot de passe", variable=show_password_var, command=toggle_password_visibility)
show_password_check.pack(pady=5)

generate_button = tk.Button(root, text="Générer", command=generate_password_from_text)
generate_button.pack(pady=5)

password_entry = tk.Entry(root, show='*', width=40)
password_entry.pack(pady=5)
password_entry.config(state=tk.DISABLED)

copy_button = tk.Button(root, text="Copier", command=copy_to_clipboard)
copy_button.pack(pady=5)

error_label = tk.Label(root, text="", fg="red")
error_label.pack(pady=5)

root.mainloop()
