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

## Induzierter Teilgraph von G:

## für $A \subset V$ definiere $G_A := (A, \{vw \in E|v, w \in A\})$

---

## $G$ ist ein perfekter Graph $:\Leftrightarrow$

## $\forall A \subset V: \chi(G_A) = \omega(G_A)$

---

\> Animation 1 <

---

## Schwacher Perfekte-Graphen-Satz [Lovász 1972]

### Graph $G$ ist genau dann perfekt, wenn $\bar G$ perfekt ist.
 
### Alternative Formulierung: Diese 3 Aussagen sind equivalent:

- $\forall A \subset V: \chi(G_A) = \omega(G_A)$
- $\forall A \subset V: k(G_A) = \alpha(G_A)$
- $\forall A \subset V: \omega(G_A)\cdot\alpha(G_A) \geq |A|$

---

## Beispiele für Klassen von perfekten Graphen:

- Vollständige Graphen
- Bipartite Graphen
- Triangulierte Graphen
- Interval-Schnitt Graphen

---

## Triangulierte Graphen

### Definition: Ein Graph $G$ heißt trianguliert $:\Leftrightarrow$

Jeder Kreis in $G$ mit Länge $\geq 4$ besitzt eine Kante, die zwei im Kreis nicht benachbarte Knoten verbindet.

todo: skizze

---

### $v \in V$ heißt simplektischer Knoten $:\Leftrightarrow$

### $Adj(v)$ ist vollständiger Teilgraph von $G$

###

Lemma 1: Ein triangulierter Graph hat mindestens 2 simplektische Knoten.

Lemma 2: Wenn $v$ ein simplektischer Knoten von $G$ ist und $G - v$ trianguliert ist, dann ist $G$ trianguliert.

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

## Ausblick:

### Interval-Schnitt-Graph

Ein Graph heißt Interval-Schnitt-Graph, wenn es eine Familie von (reellen) Intervallen gibt, die in bijektiv auf die Knoten abgebildet werden und eine Kante zwischen 2 Knoten existiert gdw. die zugehörigen Intervalle überlappen.

todo: grafik

Ein Interval-Schnitt-Graph heißt proper, wenn keines der Intervalle ganz in einem anderen ist.

---

## Aufzählungsschema für Proper Interval-Schnitt-Graphen

Paper von Kawahara et al

Gewisse Binärstrings $\cong$ Proper Interval-Schnitt-Graphen

Bau eines Binary-Decision-Diagrams

---

# Danke für Ihre Aufmerksamkeit

