from professor import Professor
from escola import Escola

escola1 = Escola("Escola X")
escola2 = Escola("Escola Y")

professor1 = Professor("Lucas")
professor2 = Professor("João")

professor1.adicionar_escola(escola1)
professor1.adicionar_escola(escola2)
professor2.adicionar_escola(escola1)

print(f"{professor1} leciona em: {[str(escola) for escola in professor1.escolas]}")
print(f"{professor2} leciona em: {[str(escola) for escola in professor2.escolas]}")
print(f"Professores da {escola1}: {[str(professor) for professor in escola1.professores]}")
print(f"Professores da {escola2}: {[str(professor) for professor in escola2.professores]}")