from rich import print
from rich.console import Console
from rich.table import Table
import numpy as np

table  = Table(title="Polinomios")
table.add_column("Nombre")
table.add_column("Valor buscado")
table.add_column("Valor actual")


skey = np.array(([-3,-3,-3],[-3,-3,-3]))
A = np.array([[0,0,0],[0,0,0]])
table.add_row("Matriz S",str(A))
table.add_row("Llave Privada",str(skey))
table.add_row("Llave Publica",str(A*skey))

console = Console()
console.print(table)
