def FibbionaciSequence(n):
    if n <= 1:
        return n
    else:
        return FibbionaciSequence(n-1) + FibbionaciSequence(n-2)
n_terms = 20;

for i in range(n_terms):
    print(FibbionaciSequence(i))