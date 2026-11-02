import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import fitz  # PyMuPDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import os

class PDFTextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Text Editor für Windows 11")
        self.root.geometry("900x700")
        self.doc = None
        self.filepath = None
        self.current_page = 0

        # Toolbar
        toolbar = tk.Frame(root)
        toolbar.pack(side=tk.TOP, fill=tk.X, padx=5, pady=5)

        tk.Button(toolbar, text="Öffnen", command=self.open_pdf).pack(side=tk.LEFT, padx=2)
        tk.Button(toolbar, text="Speichern als...", command=self.save_as).pack(side=tk.LEFT, padx=2)
        tk.Button(toolbar, text="Vorherige Seite", command=self.prev_page).pack(side=tk.LEFT, padx=2)
        tk.Button(toolbar, text="Nächste Seite", command=self.next_page).pack(side=tk.LEFT, padx=2)

        self.page_label = tk.Label(toolbar, text="Seite: - / -")
        self.page_label.pack(side=tk.LEFT, padx=10)

        # Text editor
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier New", 11))
        self.text_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Status bar
        self.status = tk.Label(root, text="Bereit. Öffne eine PDF-Datei.", bd=1, relief=tk.SUNKEN, anchor=tk.W)
        self.status.pack(side=tk.BOTTOM, fill=tk.X)

    def open_pdf(self):
        path = filedialog.askopenfilename(title="PDF öffnen", filetypes=[("PDF Dateien", "*.pdf")])
        if not path:
            return
        try:
            if self.doc:
                self.doc.close()
            self.doc = fitz.open(path)
            self.filepath = path
            self.current_page = 0
            self.load_current_page()
            self.status.config(text=f"Geladen: {os.path.basename(path)}")
        except Exception as e:
            messagebox.showerror("Fehler beim Öffnen", str(e))

    def load_current_page(self):
        if not self.doc:
            return
        page = self.doc[self.current_page]
        text = page.get_text("text") or "(Kein Text auf dieser Seite)"
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, text)
        self.page_label.config(text=f"Seite: {self.current_page + 1} / {len(self.doc)}")

    def prev_page(self):
        if self.doc and self.current_page > 0:
            self.current_page -= 1
            self.load_current_page()

    def next_page(self):
        if self.doc and self.current_page < len(self.doc) - 1:
            self.current_page += 1
            self.load_current_page()

    def save_as(self):
        if not self.doc:
            messagebox.showwarning("Keine Datei", "Bitte zuerst eine PDF öffnen.")
            return
        save_path = filedialog.asksaveasfilename(
            title="PDF speichern als",
            defaultextension=".pdf",
            filetypes=[("PDF Dateien", "*.pdf")]
        )
        if not save_path:
            return
        try:
            edited_text = self.text_area.get("1.0", tk.END).strip()
            c = canvas.Canvas(save_path, pagesize=A4)
            width, height = A4
            y = height - 50
            c.setFont("Helvetica", 12)
            for line in edited_text.split("\n"):
                if y < 50:
                    c.showPage()
                    y = height - 50
                    c.setFont("Helvetica", 12)
                c.drawString(50, y, line[:120])  # max Länge pro Zeile
                y -= 15
            c.save()
            messagebox.showinfo("Gespeichert", f"Datei gespeichert:\n{save_path}\n\nHinweis: Nur der Text der aktuellen Seite wurde als neues PDF exportiert. Original-Layout wird nicht beibehalten.")
        except Exception as e:
            messagebox.showerror("Fehler beim Speichern", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFTextEditor(root)
    root.mainloop()
