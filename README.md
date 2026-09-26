# -SISTEMA-DE-RESERVAS-DE-HOTEL

```mermaid
    classDiagram
        class Quarto {
            +numero
        }

    class QuartoLuxo{
        +temBanheira
        +servicoQuarto()
    }

    Quarto <|-- QuartoLuxo

```