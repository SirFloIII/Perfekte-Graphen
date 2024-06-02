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

    Definition

    Beispiel und Gegenbeispiel
        Fig 4.1

    Remark Intuitionfalle:
        Triangulated Graphs sind nicht Triangle-Mesh Graphs
        Gegenbeispiel: Oktaeder-Graph, Equator ist 4 Cyclus ohne Chord

    Thm 4.1 und Lem 4.2 bringen

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



