# ⋆˚꩜｡ AutoArch ｡✮⋆˙

> `Fast • Minimal • Powerful`

`ᰔ` A small Textual-powered Arch Linux installer prototype with a calm terminal UI.

## 🪼 ⋆｡ What It Is

AutoArch is an early-stage terminal installer interface for Arch Linux.

Right now, it focuses on one clean step:

- discovering available disks with `lsblk`
- showing them in a Textual list view
- returning the disk the user selects

It is currently a UI foundation, not a full installer yet.

## 𖦹° How It Looks

The app opens a centered screen with:

- a styled header
- a bordered disk picker
- a simple, focused selection flow

The current interface is built in [ui/screens/disk_screen.py](/home/void/autoarch/ui/screens/disk_screen.py) and launched from [main.py](/home/void/autoarch/main.py).

## 🫧 ⋆.ೃ࿔*:･ Stack

- Python
- [Textual](https://textual.textualize.io/)
- `lsblk` for disk discovery on Linux

## ₊⊹ Running It

```bash
source venv/bin/activate
python main.py
```

If Textual is not installed in your environment:

```bash
pip install textual
```

## ✮⋆˙ Current Flow

```text
launch app
   ↓
read disks via lsblk
   ↓
render selectable list
   ↓
exit with selected disk path
```

## ⋆˚⊹ Project Shape

```text
autoarch/
├── main.py
├── core/
│   └── disk.py
├── ui/
│   ├── app.py
│   └── screens/
│       └── disk_screen.py
├── config/
└── scripts/
```

## ｡✮⋆˙ What’s Next

- partition selection
- filesystem setup
- mount workflow
- package/bootstrap steps
- post-install automation

## ᰔ Notes

- This project is Linux-specific.
- Disk discovery depends on `lsblk` being available.
- The repository currently contains the UI scaffold for a larger installer workflow.

---

`⋆˚꩜｡✮⋆˙₊⊹₊˚⊹ᰔ🪼⋆｡𖦹°🫧⋆.ೃ࿔*:･`
