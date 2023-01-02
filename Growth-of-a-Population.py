p0      = 1500000
percent = 2.5
aug     = 10000
p       = 2000000

n_years = 0
while p0 < p:
    p0 = int(p0+p0*(percent/100)+aug)
    n_years += 1


# Forma pro

# def nb_year(p0, percent, aug, p, years = 0):
#     if p0 < p:
#         return nb_year(p0 + int(p0 * percent / 100) + aug, percent, aug, p, years + 1)
#     return years

