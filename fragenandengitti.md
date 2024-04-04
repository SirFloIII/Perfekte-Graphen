Komplexitätstheorie:
Soll ich den Spass mit Laufzeitanalyse, P und NP, NP-Hardness usw. als bekannt annehmen oder in einem (Unter)-Kapitel ausführen?
    + Es kommt im Mathebacc nur ein bissi in Panholzer III vor.
    - Es kommt im Infomaster vor, in einem Fach das ich bereits gemacht hab.

Als Vergleich die Chromatische Zahl in O(2^n * n) für allgemeine Graphen (rekursive Formel für chromatisches Polynom, kleinster !=0 Koeffizient) auch herzeigen, oder nur auf Subklassen perfekter Graphen fokusieren?

Selbiges für Cliquenzahl in Worst Case O(2^n * n²) (jede Teilmenge durchprobieren)

Nakamara Paper: Man kann also dir BDDs schnell bauen, aber wenn man tatsächlich die Graphen enumerieren will, wie geht das? Alle Strings durchgehen und mit dem BDD testen ist wieder O(4^n). Depth First Seach durch den BDD? Wie kann ich da die Laufzeit analysieren?