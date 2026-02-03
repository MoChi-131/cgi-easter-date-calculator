# 🐣 Easter Date Calculator (Python CGI)

A lightweight Python CGI web application that calculates the date of Easter for any given year.  
The backend uses the Meeus/Jones/Butcher algorithm and supports multiple output formats, making it a simple but effective demonstration of server‑side processing with Python.

---

## ✨ Features

- Input any valid year
- Calculates Easter Sunday using a well‑known algorithm
- Output formats:
  - **Numerical** (dd/mm/yyyy)
  - **Verbose** (e.g., 12ᵗʰ April 2020)
  - **Both formats together**
- Clean HTML form interface
- No external libraries required

---

## 🚀 How to Run Locally

You can test the CGI script using Python’s built‑in HTTP server:

1. Open a terminal in the project folder  
2. Run: python -m http.server  --cgi 8000
3. Ensure the CGI script is inside a `cgi-bin` directory  
4. Open your browser and visit: http://localhost:8000

---

## 🧮 Algorithm

This project uses the **Meeus/Jones/Butcher algorithm**, a widely accepted method for calculating the date of Easter in the Gregorian calendar.

---






