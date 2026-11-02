# Einfacher PDF Text Editor für Windows 11

Dieses Programm erlaubt das Öffnen von PDF-Dateien, das Extrahieren und Bearbeiten des Textes und das Speichern als neues PDF.

**Hinweis:** Es ist ein einfacher Versuch. Das originale Layout (Bilder, Formatierung) wird beim Speichern nicht beibehalten – nur der Text der aktuellen Seite wird in ein neues PDF geschrieben.

## Installation

1. Python 3.10 oder höher installieren (https://www.python.org/downloads/)
2. Im Ordner ausführen:
   ```
   pip install -r requirements.txt
   ```

## Starten

```
python pdf_editor.py
```

## Funktionen

- PDF öffnen
- Text der aktuellen Seite anzeigen und bearbeiten
- Seiten vor/zurück navigieren
- Bearbeiteten Text als neues PDF speichern

## EXE erstellen (optional)

```
pip install pyinstaller
pyinstaller --onefile --windowed pdf_editor.py
```

Die EXE liegt dann in `dist/`.

## ZIP und Email

Den Ordner oder die EXE zippen und an s.grosser61@gmx.de senden.

---

Gebaut als einfacher Versuch mit PyMuPDF und ReportLab.
