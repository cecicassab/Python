from calendar import mdays, month_name
from functools import reduce


meses_31 = filter(lambda m: mdays[m] == 31, range(1,13))
mes_nome = map(lambda m: month_name[m], meses_31)
meses = reduce(lambda inicio, meses: f'{inicio}\n-{meses}', mes_nome, 'Meses com 31 dias')

print(meses)
