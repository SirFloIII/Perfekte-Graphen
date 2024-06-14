Kapitel Introduction:

    Geschichtliches

    Historischer Kontext von Paul Seymour zitieren.

Kapitel Basics:

    Def Graph und die typischen Annahmen für den Kontext (simple, undirected, nicht leer)

    Def Chromatic Number

    Rekursives Schema zum berechnen der chromatischen Zahl via Chromatic Polynom

    ergo O(2^|V|)

    NP-Hardness via Karp's 21 NP-complete problems

    Def Clique

    Def Perfekter Graph

    Reduktionsschema bzw. Induktion nach Knotenanzahl:
        Eine typische Beweisidee: Wir sehen, die gefragte Aussage gilt trivialerweise für den Ein-Knoten-Graph, und nehmen an, das die Aussage schon für alle kleineren Graphen gezeigt ist. Dann wählen wir geschickt einen Knoten oder eine Teilmenge der Knoten aus, die wir aus dem Graphen entfernen. Der übrige Graph erfüllt die Aussage und das wieder hinzufügen der weggenommenen Knoten ist verträglich mit der Aussage. qed

    Beispiele perfekter Graphen + jeweils Beweis dafür
        (bipartite, complete, empty)

    Weak Theorem

    Strong Theorem ohne Beweis


    Ausblick:
        Wir schauen uns spezielle Klassen von perfekten Graphen und Algorithmen darauf an.
            - Triangulated Graphs
            - ...

Kapitel Triangulated Graphs

    Definition: Ein Graph heißt *trianguliert*, wenn jeder Zyklus im Graphen mit Länge >= 4 eine Sehne (Chord) besitzt. Eine Sehne eines Zykluses ist eine Kante, die zwei im Zyklus nicht aufeinanderfolgende Kanten verbindet.

    Beispiel und Gegenbeispiel
        Fig 4.1

    Remark Intuitionfalle:
        Triangulated Graphs sind nicht Triangle-Mesh Graphs
        Gegenbeispiel: Oktaeder-Graph, Equator ist 4 Cyclus ohne Chord

        Anmerkung: Triangulierte Graphen sind nicht Dreieck-Mesh-Graphen zu verwechselen, wie man sie zum Beispiel aus der Computergrafik kennt. Der Oktaeder-Graph (siehe Fig. X) besteht nur aus Dreiecken, ist aber nicht trianguliert, da der farblich markierte 4-Cyclus keine Sehnen besitzt.

    Definition: Simplektischer Knoten: Ein Knoten u heißt *simplektisch* (simplical), wenn seine Nachbaren alle untereinander verbunden sind, i.e. adj(u) ist eine Clique.
    
    Definition: Für einen Graphen $G = (V, E)$ und zwei Knoten $a, b \in V$ nennen wir eine Menge $S \subset V$ einen \emph{Knoten-Seperator} oder \emph{$a$-$b$-Seperator}, wenn der induzierte Subgraph von $V \setminus S$ in zwei (oder mehr) Kompenenten zerfällt und $a$ und $b$ in verschiedenen Komponenten sind. Wenn keine echte Teilmenge von $S$ selbst ein $a$-$b$-Seperator ist, dann nennen wir $S$ einen \emph{minimalen Knoten-Seperator}.

    Thm 4.1 Teil 1
        Sei $G$ ein ungerichteter Graph. $G$ ist trianguliert, genau dann wenn jeder minimale Knoten-Seperator einen vollständigen Teilgraph induziert.

        Bew: "<=": Sei $\[a, x, b, y_1, \hdots, y_k, a\]$ ein Zyklus in $G$. Es ist zu zeigen, das dieser eine Sehne besitzt. Fall 1: $a$ und $b$ sind verbunden, dann ist $ab$ eine Sehne. Fall 2: $a$ und $b$ sind nicht verbunden. Sei $S$ ein minimaler Knoten-Seperator zwischen $a$ und $b$. Der Knoten $x$ muss auf jeden Fall in $S$ sein, da sonst $a$ und $b$ durch $S$ nicht separiert werden. Ebenso muss eines der $y_i$ in $S$ sein. Da $S$ laut Vorraussetzung vollständig ist, sind $x$ und $y_i$ verbunden, und damit ist $xy_i$ die gesuchte Sehne.

        "=>": Sei $S$ ein minmaler $a$-$b$-Seperator und $G_A$ und $G_B$ die Komponenten von $G_{V \setminus S}$, in denen sich $a$ und $b$ jeweils befinden. Seien $x, y \in S$. Es ist zu zeigen, dass $x$ und $y$ verbunden sein. Da $S$ minimal ist, muss jeder Knoten $x \in S$ einen Nachbaren in $A$ und einen Nachbaren in $B$ haben. Man kann also einen Pfad von $x$ nach $y$ durch $A$ finden. Konkret sei $\[x, a_1, \hdots, a_k, y\]$ ein kürzester Pfad in $G_{A \cup S}$ mit $a_i \in A$ für alle $i$. Analog sei $\[x, b_1, \hdots, b_h, y\]$ ein kürzester Pfad in $G_{B \cup S}$ mit $b_i \in B$ für alle $i$. Die beiden Pfade kann man nun zu einem Zyklus in $G$ zusammenbauen: $\[x, a_1, \hdots, a_k, y, b_h, \hdots b_1, x\]$ muss laut Vorraussetzung also eine Sehne besitzen. Wo kann sie sein?
            - Nicht zwischen einem $a_i$ und $b_j$, da $S$ ein Knoten-Seperator ist.
            - Nicht zwischen zwei $a_i$ und $a_j$ oder einem $a_i$ und $x$ oder $y$, da der Pfad in $G_{A \cup S}$ kürzestmöglich ist.
            - Analog für $b_i$ und $b_j$.
        Es bleibt also nur die Möglichkeit zwischen $x$ und $y$, was zu zeigen war. \qed

    Lem 4.2 [Dirac 1961]
        Jeder triangulierter Graph $G = (V, E)$ hat einen simplektischen Knoten. Wenn $G$ nicht vollständig ist, dann hat $G$ sogar zwei nicht benachbarte simplektische Knoten.

        Bew: Wenn G vollständig ist, dann ist jeder Knoten simplektisch und die Aussage ist trivial. Sonst beweisen wir mittels Induktion über die Knoten-Anzahl:

        Induktionsanfang: Ein einzelner Knoten ist als Graph gesehen vollständig.

        Induktionsschritt: Sei also $G$ nicht vollständig, also existieren zwei nicht benachbarte Knoten $a$ und $b$. Sei $S$ ein minimaler Knoten-Seperator für $a$ und $b$. Die Komponenten von $G_{V \setminus S}$, die $a$ und $b$ enthalten jeweils $G_A$ und $G_B$.
    
    
    


    Naiver Algo in O(|V|^4) lol

    Besserer Algo von Fulkerson-Gross

    Dessen Timecomplexity

    Triangulated Graphs are Perfect

    Schneller Algo um Chomatische Zahl und maximale Cliquen zu finden

Kapitel Split Graphs

    Definition

    sonstiges?

Kapitel Interval Graphs

    Definition

    Definition proper Interval Graph (aus kawahara et al)

    Fun Fact: proper <=> unit interval

    Satz: G ist Interval Graph <=> G ist trianguliert und das Komplement von G ist Ordnungsgraph
    (Theorem 8.1 & Corrolary 8.2 aus dem Buch)

    Korollar: Interval => Perfekt

    Algo 1 aus Kawahara et al.:
        Intro Binary Strings (mit L und R)
        Definition BDD
        Definition alternate string
        Definition canonical
        Erkärung Nodes mit State
            - i
            - hL
            - hR
            - F
        L und R State berechnen
        O(n³)
        
    Beispiele

    Anzahl OEIS

    Anzahl geschlossene Form?



