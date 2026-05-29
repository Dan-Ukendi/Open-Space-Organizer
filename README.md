# 🪑 OpenSpace Organiser

A Python CLI tool to automatically organize colleagues' seating in an open space, with neighbourhood constraint management.

---

## 📁 Project Structure

```
openspace-organiser/
├── main.py
├── utils/
│   ├── openspace.py
│   └── tables.py
├── txt/
│   └── new_colleagues.txt
└── seating_arrangement.txt
```

---

## ▶️ Usage

```bash
python main.py
```

The program will guide you step by step through interactive prompts:

1. **Path to the file** containing colleagues' names
2. **Number of tables** and **size of each table**
3. Option to **add people manually**
4. Automatic check that there are **enough seats** (option to add tables if not)
5. **Random seating assignment** for all colleagues
6. Display of free seats, number of people, and total seats
7. Apply **constraints** :
   - Person alone at a table → moved automatically
   - Two people **cannot** sit together
   - Two people **must** sit together
8. **Save** the seating arrangement to `seating_arrangement.txt` and display it

---

## 📄 Input File Format

The input file must contain **one name per line**, for example:

```
Alice
Bob
Charlie
Diana
```

---

## 🧩 Architecture

### `Seat`
Represents a seat linked to a table. Attributes: `free` (boolean), `occupant` (name).

### `Table`
Array of `Seat`. Handles assigning, freeing, and moving occupants.

### `OpenSpace`
Array of `Table`. Orchestrates random seating, neighbourhood constraints, and file saving.

---

## ⚙️ Requirements

- Python 3.x
- No external dependencies

---

## 📝 Output Example (`seating_arrangement.txt`)

```
Alice, Table 0
Bob, Table 0
Charlie, Table 1
Diana, Table 1
```