from calendar import mdays, month_name


print('Meses com 31 dias')
for mes in range(1,13):
    if mdays[mes]==31:
        print(f'-{month_name[mes]}')