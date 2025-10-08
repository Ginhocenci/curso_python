# Precedências na ordem abaixo
# 1. (n + n)
# 2. **
# 3. * / // %
# 4. + -

#conta_1 = 1 + 1 ** 5 + 5. Deu 7.
conta_1 = (1 + 1) ** (5 + 5) # Deu 1024
conta_1 = (1 + (0.5 + 0.5)) ** (5 + 5) # Deu 1024
print(conta_1)