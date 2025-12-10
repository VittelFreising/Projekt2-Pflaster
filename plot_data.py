import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSV-Dateien laden (mit Semikolon als Trennzeichen, deutsche Dezimaltrennzeichen)
df1 = pd.read_csv('/workspaces/Projekt2-Pflaster/Zugversuch_Pflaster1.csv', 
                    sep=';', decimal=',', skiprows=5)
df2 = pd.read_csv('/workspaces/Projekt2-Pflaster/Zugversuch_Pflaster2.csv', 
                    sep=';', decimal=',', skiprows=5)

# Kraft-Spalte bereinigen (NaN-Werte entfernen und in positive Werte umwandeln)
df1['Force'] = pd.to_numeric(df1['Force'], errors='coerce')
df2['Force'] = pd.to_numeric(df2['Force'], errors='coerce')
df1 = df1.dropna(subset=['Force'])
df2 = df2.dropna(subset=['Force'])
df1['Force'] = df1['Force'].abs()
df2['Force'] = df2['Force'].abs()

# Visualisierung erstellen
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Plot 1: Zugversuch Pflaster 1
axes[0].plot(df1.index, df1['Force'], linewidth=1.5, color='blue')
axes[0].set_title('Zugversuch Pflaster 1', fontsize=12, fontweight='bold')
axes[0].set_xlabel('Messwert Nr.', fontsize=10)
axes[0].set_ylabel('Kraft (N)', fontsize=10)
axes[0].grid(True, alpha=0.3)
axes[0].set_xlim(0, len(df1))

# Plot 2: Zugversuch Pflaster 2
axes[1].plot(df2.index, df2['Force'], linewidth=1.5, color='green')
axes[1].set_title('Zugversuch Pflaster 2', fontsize=12, fontweight='bold')
axes[1].set_xlabel('Messwert Nr.', fontsize=10)
axes[1].set_ylabel('Kraft (N)', fontsize=10)
axes[1].grid(True, alpha=0.3)
axes[1].set_xlim(0, len(df2))

plt.tight_layout()
plt.savefig('/workspaces/Projekt2-Pflaster/Zugversuch_Vergleich.png', dpi=300, bbox_inches='tight')
print("Grafik erstellt und gespeichert: Zugversuch_Vergleich.png")

# Auch einzelne Grafiken erstellen
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(df1.index, df1['Force'], linewidth=1.5, color='blue')
ax1.set_title('Zugversuch Pflaster 1 - Kraft vs. Zeit', fontsize=14, fontweight='bold')
ax1.set_xlabel('Messwert Nr.', fontsize=12)
ax1.set_ylabel('Kraft (N)', fontsize=12)
ax1.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('/workspaces/Projekt2-Pflaster/Zugversuch_Pflaster1.png', dpi=300, bbox_inches='tight')
print("Grafik erstellt und gespeichert: Zugversuch_Pflaster1.png")

fig2, ax2 = plt.subplots(figsize=(10, 6))
ax2.plot(df2.index, df2['Force'], linewidth=1.5, color='green')
ax2.set_title('Zugversuch Pflaster 2 - Kraft vs. Zeit', fontsize=14, fontweight='bold')
ax2.set_xlabel('Messwert Nr.', fontsize=12)
ax2.set_ylabel('Kraft (N)', fontsize=12)
ax2.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('/workspaces/Projekt2-Pflaster/Zugversuch_Pflaster2.png', dpi=300, bbox_inches='tight')
print("Grafik erstellt und gespeichert: Zugversuch_Pflaster2.png")

# Statistiken ausgeben
print("\n--- Statistiken Pflaster 1 ---")
print(f"Anzahl Datenpunkte: {len(df1)}")
print(f"Max. Kraft: {df1['Force'].max():.2f} N")
print(f"Min. Kraft: {df1['Force'].min():.2f} N")
print(f"Durchschnitt: {df1['Force'].mean():.2f} N")

print("\n--- Statistiken Pflaster 2 ---")
print(f"Anzahl Datenpunkte: {len(df2)}")
print(f"Max. Kraft: {df2['Force'].max():.2f} N")
print(f"Min. Kraft: {df2['Force'].min():.2f} N")
print(f"Durchschnitt: {df2['Force'].mean():.2f} N")
