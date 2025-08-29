"""
Educational Resource Hub - Tanzania Curriculum
Full-featured Tkinter app with:
- Subject tabs with resources (open / download)
- Dark / Light mode
- Downloads manager (open / rename / delete / add file)
- Search (global resources + downloads)
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import webbrowser
import requests
import os
import shutil
import subprocess
import sys

class EducationalHub:
    def __init__(self, root):
        self.root = root
        self.root.title("Educational Resource Hub - Tanzania Curriculum")
        self.root.geometry("1000x700")
        # Downloads folder
        self.downloads_dir = os.path.join(os.getcwd(), "downloads")
        os.makedirs(self.downloads_dir, exist_ok=True)

        # Themes
        self.light_theme = {
            "bg": "#f4f6f7", "fg": "#2c3e50", "title_bg": "#2c3e50",
            "title_fg": "white", "button_bg": "#3498db", "button_fg": "white",
            "accent": "#8e44ad"
        }
        self.dark_theme = {
            "bg": "#1f2933", "fg": "white", "title_bg": "#0b1220",
            "title_fg": "#f1c40f", "button_bg": "#9b59b6", "button_fg": "white",
            "accent": "#8e44ad"
        }
        self.theme = self.light_theme.copy()
        self.is_dark = False

        # Resources (Tanzania curriculum focused links)
        self.resources = {
            "Mathematics": [
                {"name": "Khan Academy Math", "url": "https://www.khanacademy.org/math"},
                {"name": "NECTA Past Papers (Math)", "url": "https://www.necta.go.tz"},
                {"name": "TIE Math Textbooks", "url": "https://ol.tie.go.tz/subjects/mathematics"}
            ],
            "Science": [
                {"name": "PhET Simulations", "url": "https://phet.colorado.edu/"},
                {"name": "NECTA Past Papers (Science)", "url": "https://www.necta.go.tz"},
                {"name": "TIE Science Books", "url": "https://ol.tie.go.tz/subjects/science"}
            ],
            "Geography": [
                {"name": "TIE Geography Books", "url": "https://ol.tie.go.tz/subjects/geography"},
                {"name": "NECTA Geography Past Papers", "url": "https://www.necta.go.tz"},
                {"name": "YouTube: Tanzania Geography Lessons", "url": "https://www.youtube.com/results?search_query=tanzania+geography+lessons"}
            ],
            "Kiswahili": [
                {"name": "TIE Kiswahili Books", "url": "https://ol.tie.go.tz/subjects/kiswahili"},
                {"name": "NECTA Kiswahili Papers", "url": "https://www.necta.go.tz"},
                {"name": "YouTube: Mashairi ya Kiswahili", "url": "https://www.youtube.com/results?search_query=shairi+za+kiswahili"}
            ],
            "Civics": [
                {"name": "TIE Civics Books", "url": "https://ol.tie.go.tz/subjects/civics"},
                {"name": "NECTA Civics Past Papers", "url": "https://www.necta.go.tz"},
                {"name": "YouTube Civics Lessons", "url": "https://www.youtube.com/results?search_query=civics+tanzania+lessons"}
            ],
            "History": [
                {"name": "TIE History Books", "url": "https://ol.tie.go.tz/subjects/history"},
                {"name": "NECTA History Past Papers", "url": "https://www.necta.go.tz"},
                {"name": "YouTube: Tanzania History Lessons", "url": "https://www.youtube.com/results?search_query=history+tanzania+lessons"}
            ],
            "English": [
                {"name": "British Council Learn English", "url": "https://learnenglish.britishcouncil.org/"},
                {"name": "NECTA English Past Papers", "url": "https://www.necta.go.tz"},
                {"name": "YouTube English Lessons", "url": "https://www.youtube.com/results?search_query=english+tanzania+lessons"}
            ]
        }

        # Build UI
        self.build_header()
        self.build_search()
        self.build_notebook()
        self.populate_resource_tabs()
        self.build_downloads_tab()
        self.apply_theme_to_widgets()

    # ---------- UI build ----------

    def build_header(self):
        self.header = tk.Frame(self.root, bg=self.theme["title_bg"], height=70)
        self.header.pack(fill=tk.X)
        self.title_label = tk.Label(self.header, text="📚 Tanzanian Educational Resource Hub",
                                    font=("Arial", 20, "bold"),
                                    bg=self.theme["title_bg"], fg=self.theme["title_fg"])
        self.title_label.pack(side=tk.LEFT, padx=15, pady=12)
        self.theme_btn = tk.Button(self.header, text="🌙 Dark Mode", command=self.toggle_theme,
                                   bg=self.theme["button_bg"], fg=self.theme["button_fg"], font=("Arial", 11))
        self.theme_btn.pack(side=tk.RIGHT, padx=12)

    def build_search(self):
        search_frame = tk.Frame(self.root, bg=self.theme["bg"])
        search_frame.pack(fill=tk.X, padx=12, pady=(12, 6))
        tk.Label(search_frame, text="🔍 Search resources:", bg=self.theme["bg"], fg=self.theme["fg"],
                 font=("Arial", 11)).pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        self.search_entry = tk.Entry(search_frame, textvariable=self.search_var, font=("Arial", 11), width=40)
        self.search_entry.pack(side=tk.LEFT, padx=8)
        tk.Button(search_frame, text="Go", command=self.search_resources, bg="#27ae60", fg="white").pack(side=tk.LEFT)
        tk.Button(search_frame, text="Clear", command=self.clear_search).pack(side=tk.LEFT, padx=6)

    def build_notebook(self):
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)
        self.tab_frames = {}

    def populate_resource_tabs(self):
        # Make a tab per subject and add resource rows
        for subject, links in self.resources.items():
            frame = tk.Frame(self.notebook, bg=self.theme["bg"])
            self.notebook.add(frame, text=subject)
            self.tab_frames[subject] = frame

            header = tk.Label(frame, text=f"{subject} resources", font=("Arial", 14, "bold"),
                              bg=self.theme["bg"], fg=self.theme["fg"])
            header.pack(anchor="w", padx=12, pady=(10, 6))

            for res in links:
                row = tk.Frame(frame, bg=self.theme["bg"])
                row.pack(anchor="w", fill=tk.X, padx=12, pady=6)

                name_lbl = tk.Label(row, text=res["name"], font=("Arial", 11),
                                    bg=self.theme["bg"], fg=self.theme["fg"], anchor="w")
                name_lbl.pack(side=tk.LEFT, padx=(0, 8), fill=tk.X, expand=True)

                open_btn = tk.Button(row, text="🌐 Open", command=lambda url=res["url"]: self.open_link(url),
                                     bg=self.theme["button_bg"], fg=self.theme["button_fg"], width=12)
                open_btn.pack(side=tk.RIGHT, padx=4)

                dl_btn = tk.Button(row, text="⬇ Download", command=lambda url=res["url"]: self.download_file(url),
                                   bg="#16a085", fg="white", width=12)
                dl_btn.pack(side=tk.RIGHT, padx=4)

    def build_downloads_tab(self):
        # Add the Downloads tab at the end
        self.downloads_tab = tk.Frame(self.notebook, bg=self.theme["bg"])
        self.notebook.add(self.downloads_tab, text="📂 My Downloads")

        top_frame = tk.Frame(self.downloads_tab, bg=self.theme["bg"])
        top_frame.pack(fill=tk.X, padx=10, pady=8)

        add_btn = tk.Button(top_frame, text="➕ Add File", command=self.add_file,
                            bg="#2980b9", fg="white", width=12)
        add_btn.pack(side=tk.LEFT, padx=(0, 6))

        # Search inside downloads
        tk.Label(top_frame, text="🔎 Search my files:", bg=self.theme["bg"], fg=self.theme["fg"]).pack(side=tk.LEFT, padx=(10,4))
        self.download_search_var = tk.StringVar()
        self.download_search_entry = tk.Entry(top_frame, textvariable=self.download_search_var, width=30)
        self.download_search_entry.pack(side=tk.LEFT, padx=6)
        tk.Button(top_frame, text="Find", command=self.search_downloads).pack(side=tk.LEFT, padx=4)
        tk.Button(top_frame, text="Clear", command=self.clear_download_search).pack(side=tk.LEFT, padx=4)

        # Frame for list of files
        self.files_list_frame = tk.Frame(self.downloads_tab, bg=self.theme["bg"])
        self.files_list_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(6,10))
        self.refresh_downloads()

    # ---------- Theme handling ----------

    def apply_theme_to_widgets(self):
        # Apply colors to main widgets (some widgets are recreated when refresh_downloads is called)
        self.root.configure(bg=self.theme["bg"])
        self.header.configure(bg=self.theme["title_bg"])
        self.title_label.configure(bg=self.theme["title_bg"], fg=self.theme["title_fg"])
        self.theme_btn.configure(bg=self.theme["button_bg"], fg=self.theme["button_fg"])
        # Notebook's tab background is managed by ttk, but inner frames will use theme colors
        for subject, frame in self.tab_frames.items():
            frame.configure(bg=self.theme["bg"])
            for child in frame.winfo_children():
                try:
                    child.configure(bg=self.theme["bg"], fg=self.theme["fg"])
                except Exception:
                    pass
        # Downloads tab
        try:
            self.downloads_tab.configure(bg=self.theme["bg"])
            self.files_list_frame.configure(bg=self.theme["bg"])
        except Exception:
            pass

    def toggle_theme(self):
        if not self.is_dark:
            self.theme = self.dark_theme.copy()
            self.is_dark = True
            self.theme_btn.configure(text="☀ Light Mode")
        else:
            self.theme = self.light_theme.copy()
            self.is_dark = False
            self.theme_btn.configure(text="🌙 Dark Mode")
        # Reapply colors
        self.apply_theme_to_widgets()
        # Rebuild dynamic parts (downloads list) so colors apply
        self.refresh_downloads()

    # ---------- Resource actions ----------

    def open_link(self, url):
        try:
            webbrowser.open(url)
        except Exception as e:
            messagebox.showerror("Error", f"Could not open link:\n{e}")

    def download_file(self, url):
        # Ask user where to save (default into downloads_dir)
        suggested_name = os.path.basename(url) or "resource.pdf"
        initial = os.path.join(self.downloads_dir, suggested_name)
        save_path = filedialog.asksaveasfilename(title="Save resource as",
                                                 initialdir=self.downloads_dir,
                                                 initialfile=suggested_name,
                                                 defaultextension="",
                                                 filetypes=[("All files", "*.*")])
        if not save_path:
            return  # cancelled

        try:
            # Support common simple HTTP downloads
            resp = requests.get(url, stream=True, timeout=30)
            resp.raise_for_status()
            with open(save_path, "wb") as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            messagebox.showinfo("Download Complete", f"Saved to:\n{save_path}")
            self.refresh_downloads()
        except Exception as e:
            messagebox.showerror("Download Failed", f"Could not download:\n{e}")

    # ---------- Downloads manager ----------

    def refresh_downloads(self, filter_text: str = ""):
        # Clear the frame
        for w in self.files_list_frame.winfo_children():
            w.destroy()

        files = sorted(os.listdir(self.downloads_dir))
        if filter_text:
            files = [f for f in files if filter_text.lower() in f.lower()]

        if not files:
            tk.Label(self.files_list_frame, text="No downloads or uploaded files yet.",
                     font=("Arial", 12), bg=self.theme["bg"], fg=self.theme["fg"]).pack(pady=20)
            return

        for filename in files:
            filepath = os.path.join(self.downloads_dir, filename)
            row = tk.Frame(self.files_list_frame, bg=self.theme["bg"])
            row.pack(fill=tk.X, pady=4)

            lbl = tk.Label(row, text=filename, font=("Arial", 11), anchor="w",
                           bg=self.theme["bg"], fg=self.theme["fg"], width=60)
            lbl.pack(side=tk.LEFT, padx=6)

            open_btn = tk.Button(row, text="📖 Open", command=lambda f=filepath: self.open_offline(f),
                                 bg=self.theme["button_bg"], fg=self.theme["button_fg"], width=10)
            open_btn.pack(side=tk.RIGHT, padx=4)

            del_btn = tk.Button(row, text="🗑 Delete", command=lambda f=filepath: self.delete_file(f),
                                bg="#c0392b", fg="white", width=10)
            del_btn.pack(side=tk.RIGHT, padx=4)

            rename_btn = tk.Button(row, text="✏ Rename", command=lambda f=filepath: self.rename_file(f),
                                   bg="#2980b9", fg="white", width=10)
            rename_btn.pack(side=tk.RIGHT, padx=4)

    def open_offline(self, filepath):
        if not os.path.exists(filepath):
            messagebox.showerror("File not found", "The selected file does not exist.")
            self.refresh_downloads()
            return
        try:
            if sys.platform.startswith("win"):
                os.startfile(filepath)
            elif sys.platform.startswith("darwin"):
                subprocess.Popen(["open", filepath])
            else:
                # linux
                subprocess.Popen(["xdg-open", filepath])
        except Exception:
            try:
                webbrowser.open(f"file://{os.path.abspath(filepath)}")
            except Exception as e:
                messagebox.showerror("Open failed", f"Could not open file:\n{e}")

    def delete_file(self, filepath):
        if not os.path.exists(filepath):
            messagebox.showerror("File not found", "The selected file does not exist.")
            self.refresh_downloads()
            return
        confirm = messagebox.askyesno("Confirm Delete", f"Are you sure you want to delete:\n{os.path.basename(filepath)} ?")
        if not confirm:
            return
        try:
            os.remove(filepath)
            messagebox.showinfo("Deleted", f"Removed: {os.path.basename(filepath)}")
            self.refresh_downloads()
        except Exception as e:
            messagebox.showerror("Error", f"Could not delete file:\n{e}")

    def rename_file(self, filepath):
        if not os.path.exists(filepath):
            messagebox.showerror("File not found", "The selected file does not exist.")
            self.refresh_downloads()
            return

        rename_win = tk.Toplevel(self.root)
        rename_win.title("Rename file")
        rename_win.geometry("420x150")
        rename_win.transient(self.root)

        tk.Label(rename_win, text="Current name:", font=("Arial", 10)).pack(pady=(8,0))
        tk.Label(rename_win, text=os.path.basename(filepath), font=("Arial", 10, "bold")).pack(pady=(0,8))

        new_name_var = tk.StringVar()
        entry = tk.Entry(rename_win, textvariable=new_name_var, width=50)
        entry.pack(pady=6)
        entry.insert(0, os.path.basename(filepath))

        def apply_rename():
            new_name = new_name_var.get().strip()
            if not new_name:
                messagebox.showwarning("Invalid name", "Please enter a valid file name.")
                return
            new_path = os.path.join(self.downloads_dir, new_name)
            if os.path.exists(new_path):
                messagebox.showwarning("Exists", "A file with that name already exists.")
                return
            try:
                os.rename(filepath, new_path)
                messagebox.showinfo("Renamed", f"Renamed to:\n{new_name}")
                rename_win.destroy()
                self.refresh_downloads()
            except Exception as e:
                messagebox.showerror("Error", f"Could not rename file:\n{e}")

        tk.Button(rename_win, text="Apply", command=apply_rename, bg="#27ae60", fg="white").pack(pady=6)

    def add_file(self):
        file_path = filedialog.askopenfilename(title="Select a file to add",
                                               filetypes=[("Documents", "*.pdf *.docx *.txt *.pptx"), ("All files", "*.*")])
        if not file_path:
            return
        try:
            dest = os.path.join(self.downloads_dir, os.path.basename(file_path))
            # If same name exists, ask to overwrite or rename
            if os.path.exists(dest):
                overwrite = messagebox.askyesno("File exists", "A file with that name already exists. Overwrite?")
                if not overwrite:
                    return
            shutil.copy2(file_path, dest)
            messagebox.showinfo("Added", f"Copied to library:\n{dest}")
            self.refresh_downloads()
        except Exception as e:
            messagebox.showerror("Error", f"Could not add file:\n{e}")

    # ---------- Search ----------

    def search_resources(self):
        q = self.search_var.get().strip().lower()
        if not q:
            messagebox.showinfo("Search", "Enter a search term.")
            return
        matches = []
        for subject, links in self.resources.items():
            for res in links:
                if q in res["name"].lower() or q in subject.lower():
                    matches.append((res["name"], res["url"], subject))
        if not matches:
            messagebox.showinfo("Search Results", "No matching resources found.")
            return
        # show simple choice list and open all matches (or just present)
        # We'll present the list and open the ones the user confirms
        msg = "Found:\n\n" + "\n".join([f"{name} ({subj})" for name, _, subj in matches])
        open_all = messagebox.askyesno("Search Results", msg + "\n\nOpen all results in browser?")
        if open_all:
            for _, url, _ in matches:
                webbrowser.open(url)

    def clear_search(self):
        self.search_var.set("")

    # Downloads search
    def search_downloads(self):
        q = self.download_search_var.get().strip()
        self.refresh_downloads(filter_text=q)

    def clear_download_search(self):
        self.download_search_var.set("")
        self.refresh_downloads()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = EducationalHub(root)
    root.mainloop()
