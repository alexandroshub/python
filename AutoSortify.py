==============================

🔹 AutoSortify Project Structure

==============================

Περιλαμβάνει 3 εκδόσεις του ίδιου project:

1. CLI (Console Version)

2. Tkinter GUI (Desktop Version)

3. Kivy GUI (Mobile/Android Version)

==============================

=============================================================

1️⃣ autosortify_cli.py (Console Version)

=============================================================

import os import shutil from datetime import datetime

SOURCE_FOLDER = "./downloads" DEST_FOLDER = "./organized_files" LOG_FILE = "automation_log.txt"

FILE_CATEGORIES = { "Images": [".jpg", ".jpeg", ".png", ".gif"], "Documents": [".pdf", ".docx", ".txt", ".xlsx"], "Videos": [".mp4", ".avi", ".mov"], "Archives": [".zip", ".rar", ".tar"] }

def write_log(message: str): with open(LOG_FILE, "a", encoding="utf-8") as log: log.write(f"[{datetime.now()}] {message}\n")

class FileOrganizerCLI: def init(self, source, destination, log_callback=None): self.source = source self.destination = destination self.log_callback = log_callback if log_callback else print

def create_folders(self):
    for category in FILE_CATEGORIES.keys():
        os.makedirs(os.path.join(self.destination, category), exist_ok=True)
    self.log_callback("✅ Created category folders.")

def organize_files(self):
    try:
        for filename in os.listdir(self.source):
            file_path = os.path.join(self.source, filename)
            if os.path.isfile(file_path):
                moved = False
                for category, extensions in FILE_CATEGORIES.items():
                    if any(filename.lower().endswith(ext) for ext in extensions):
                        shutil.move(file_path, os.path.join(self.destination, category, filename))
                        self.log_callback(f"📂 Moved {filename} → {category}")
                        moved = True
                        break
                if not moved:
                    other_path = os.path.join(self.destination, "Other")
                    os.makedirs(other_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(other_path, filename))
                    self.log_callback(f"📦 Moved {filename} → Other")
    except Exception as e:
        self.log_callback(f"❌ Error: {e}")
        print("Κάτι πήγε στραβά! Δες το log.")

def main_cli(): print("🚀 File Organizer Automation ξεκίνησε...") organizer = FileOrganizerCLI(SOURCE_FOLDER, DEST_FOLDER) organizer.create_folders() organizer.organize_files() print("✨ Οργάνωση ολοκληρώθηκε!")

=============================================================

2️⃣ autosortify_gui.py (Desktop GUI with Tkinter)

=============================================================

import tkinter as tk from tkinter import filedialog, messagebox, scrolledtext

class FileOrganizer: def init(self, source: str, destination: str, log_callback): self.source = source self.destination = destination self.log_callback = log_callback

def create_folders(self):
    for category in FILE_CATEGORIES.keys():
        os.makedirs(os.path.join(self.destination, category), exist_ok=True)
    self.log_callback("✅ Created category folders.")

def organize_files(self):
    try:
        for filename in os.listdir(self.source):
            file_path = os.path.join(self.source, filename)
            if os.path.isfile(file_path):
                moved = False
                for category, extensions in FILE_CATEGORIES.items():
                    if any(filename.lower().endswith(ext) for ext in extensions):
                        shutil.move(file_path, os.path.join(self.destination, category, filename))
                        self.log_callback(f"📂 Moved {filename} → {category}")
                        moved = True
                        break
                if not moved:
                    other_path = os.path.join(self.destination, "Other")
                    os.makedirs(other_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(other_path, filename))
                    self.log_callback(f"📦 Moved {filename} → Other")
    except Exception as e:
        self.log_callback(f"❌ Error: {e}")
        messagebox.showerror("Error", f"Κάτι πήγε στραβά! {e}")

class AutoSortifyApp: def init(self, root): self.root = root self.root.title("AutoSortify - File Organizer") self.root.geometry("600x400") self.root.resizable(False, False) self.source_folder = "" self.dest_folder = ""

tk.Label(root, text="AutoSortify", font=("Arial", 18, "bold"), fg="#4CAF50").pack(pady=10)
    tk.Button(root, text="Επιλογή Φακέλου Πηγής", command=self.select_source, width=30).pack(pady=5)
    self.source_label = tk.Label(root, text="Πηγή: -", fg="gray")
    self.source_label.pack()
    tk.Button(root, text="Επιλογή Φακέλου Προορισμού", command=self.select_destination, width=30).pack(pady=5)
    self.dest_label = tk.Label(root, text="Προορισμός: -", fg="gray")
    self.dest_label.pack()
    tk.Button(root, text="Οργάνωση Αρχείων", command=self.run_organizer, bg="#4CAF50", fg="white", width=30).pack(pady=15)
    self.log_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=10, state="disabled")
    self.log_area.pack(pady=10)

def select_source(self):
    folder = filedialog.askdirectory()
    if folder:
        self.source_folder = folder
        self.source_label.config(text=f"Πηγή: {folder}", fg="black")

def select_destination(self):
    folder = filedialog.askdirectory()
    if folder:
        self.dest_folder = folder
        self.dest_label.config(text=f"Προορισμός: {folder}", fg="black")

def log_message(self, message):
    self.log_area.config(state="normal")
    self.log_area.insert(tk.END, message + "\n")
    self.log_area.yview(tk.END)
    self.log_area.config(state="disabled")

def run_organizer(self):
    if not self.source_folder or not self.dest_folder:
        messagebox.showwarning("Missing Folders", "Παρακαλώ επίλεξε φακέλους πηγής και προορισμού.")
        return
    organizer = FileOrganizer(self.source_folder, self.dest_folder, self.log_message)
    organizer.create_folders()
    organizer.organize_files()
    messagebox.showinfo("Ολοκληρώθηκε", "Η οργάνωση ολοκληρώθηκε με επιτυχία!")

def main_gui(): root = tk.Tk() app = AutoSortifyApp(root) root.mainloop()

=============================================================

3️⃣ autosortify_mobile.py (Mobile GUI with Kivy)

=============================================================

from kivy.app import App from kivy.uix.boxlayout import BoxLayout from kivy.uix.button import Button from kivy.uix.label import Label from kivy.uix.scrollview import ScrollView from kivy.uix.textinput import TextInput from kivy.uix.popup import Popup from kivy.uix.filechooser import FileChooserListView

class AutoSortifyUI(BoxLayout): def init(self, **kwargs): super().init(orientation="vertical", **kwargs) self.source_folder = "" self.dest_folder = "" self.add_widget(Label(text="AutoSortify (Mobile)", font_size=24, size_hint=(1, 0.1))) self.btn_source = Button(text="Select Source Folder", size_hint=(1, 0.1)) self.btn_source.bind(on_press=lambda x: self.open_filechooser("source")) self.add_widget(self.btn_source) self.lbl_source = Label(text="Source: -", size_hint=(1, 0.05)) self.add_widget(self.lbl_source) self.btn_dest = Button(text="Select Destination Folder", size_hint=(1, 0.1)) self.btn_dest.bind(on_press=lambda x: self.open_filechooser("dest")) self.add_widget(self.btn_dest) self.lbl_dest = Label(text="Destination: -", size_hint=(1, 0.05)) self.add_widget(self.lbl_dest) self.btn_organize = Button(text="Organize Files", size_hint=(1, 0.1), background_color=(0, 1, 0, 1)) self.btn_organize.bind(on_press=lambda x: self.run_organizer()) self.add_widget(self.btn_organize) self.log_area = TextInput(text="", readonly=True, size_hint=(1, 0.5)) scroll = ScrollView(size_hint=(1, 0.5)) scroll.add_widget(self.log_area) self.add_widget(scroll)

def open_filechooser(self, target):
    chooser = FileChooserListView(path="/", dirselect=True)
    def select_path(instance):
        if chooser.selection:
            folder = chooser.selection[0]
            if target == "source":
                self.source_folder = folder
                self.lbl_source.text = f"Source: {folder}"
            else:
                self.dest_folder = folder
                self.lbl_dest.text = f"Destination: {folder}"
            popup.dismiss()
    popup = Popup(title="Select Folder", content=chooser, size_hint=(0.9, 0.9))
    chooser.bind(on_submit=lambda c, s, t: select_path(c))
    popup.open()

def log_message(self, message):
    self.log_area.text += message + "\n"
    self.log_area.cursor = (0, len(self.log_area.text))

def run_organizer(self):
    if not self.source_folder or not self.dest_folder:
        self.log_message("⚠ Please select source and destination folders.")
        return
    organizer = FileOrganizerCLI(self.source_folder, self.dest_folder, self.log_message)
    organizer.create_folders()
    organizer.organize_files()
    self.log_message("✨ Organization Completed!")

class AutoSortifyApp(App): def build(self): return AutoSortifyUI()

def main_mobile(): AutoSortifyApp().run()

=============================================================

4️⃣ main.py (Launcher for all versions)

=============================================================

if name == "main": print(""" ============================== 🚀 AutoSortify Launcher ============================== 1. CLI Version (Console) 2. GUI Version (Desktop - Tkinter) 3. Mobile Version (Kivy - Android) ============================== """)

choice = input("Επίλεξε ποια έκδοση θέλεις να τρέξεις (1/2/3): ").strip()

if choice == "1":
    main_cli()
elif choice == "2":
    main_gui()
elif choice == "3":
    main_mobile()
else:
    print("❌ Μη έγκυρη επιλογή.")

