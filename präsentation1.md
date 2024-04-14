---
marp: true
math: mathjax
theme: default
class: invert
---

# Perfekte Graphen

## und Algorithmen für bestimmte Teilklassen davon

---

### Wir betrachten folgende Graphen:

- endlich
- ungerichtet
- einfach, i.e. keine Doppelkanten oder Schleifen

---

### Das Komplement eines Graphen $G = (V, E)$:


### $\bar G := \left(V, \left\{ ab | a \neq b \in V, ab\not\in E\right\}\right)$

todo: grafik

---

## Chromatische Zahl $\chi(G)$:

Wie viele Farben braucht es, die Knoten von $G$ einzufärben, sodass keine Kante zwei gleichfarbige Knoten verbindet?

## Clique-Cover Zahl $k(G)$:

Wie viele Cliquen braucht es, um den ganzen Graphen zu überdecken?

### Es gilt: $\chi(G) = k(\bar G)$

---

## Cliquenzahl $\omega(G)$:

Wie groß ist die größte Clique in $G$?

## Stabilitätszahl $\alpha(G)$:

Wie groß ist die größte stabilste Menge (Anti-Clique) in $G$?

### Es gilt: $\omega(G) = \alpha(\bar G)$

---

## Es gilt: $\chi(G) \geq \omega(G)$

## Sowie: $k(G) \geq \alpha(G)$

todo: grafik

---

## $G$ ist ein perfekter Graph $:\Leftrightarrow$

## $\forall A \subset V: \chi(G_A) = \omega(G_A)$

---

\> Animation 1 <

---

## Schwacher Perfekte-Graphen-Satz

---

## Beispiele für Klassen von perfekten Graphen:

- Vollständige Graphen
- Bipartite Graphen
- Triangulierte Graphen
- Interval-Schnitt Graphen

---

## Triangulierte Graphen

Todo: Def

---

## $v \in V$ heißt simplektischer Knoten $:\Leftrightarrow$

## $Adj(v) \cong K_n$ für $n$ passend

### Lemma 1: Ein triangulierter Graph hat mindestens 2 simplektische Knoten.

### Lemma 2: Wenn $v$ ein simplektischer Knoten von $G$ ist und $G - v$ trianguliert ist, dann ist $G$ trianguliert.

---

### Erster (Naiver) Erkennungsalgorithmus für triangulierbare Graphen:

Iterativ simplektische Knoten entfernen:
- Wenn man alle Knoten entfernen kann, ist der Graph trianguliert
- Wenn man in einem Schritt keine findet, dann nicht, wegen Lemma 1

Reihenfolge der Knoten nennt man Perfektes Knoten-Eliminations-Schema.

Laufzeit $O(|V|^3|E|)$ ist schlecht

---

### Algorithmus von Rose, Tarjan und Leuker:

Aufbau des perfekten Knoten-Eliminations-Schemas rückwärts

Lineare Laufzeit $O(|V| + |E|)$

\> Animation 2 <

---

## Interval-Schnitt Graph

todo: Def

Todo: def proper

---

Nakamara et al