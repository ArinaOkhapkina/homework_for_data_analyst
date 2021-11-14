def is_valid(t1, t2, t3, t4, t5, t6):
    rolled_sectors = [t1, t2, t3, t4, t5, t6] 
    sectors = [1, 1, 1, 1, 1, 1]
    
    for rolled_sector in rolled_sectors:
        choosed_sector = rolled_sector
        while(choosed_sector < 7):
            if sectors[choosed_sector - 1] == 0: # сектор уже выбран
                choosed_sector += 1 # проверяем следующий сектор
            else:
                sectors[choosed_sector - 1] = 0 # помечаем сектор выбранным
                break
        if(choosed_sector == 7):
            return False
    return True
    

valid_count = 0;
for t1 in range(1, 7):
    for t2 in range(1, 7):
        for t3 in range(1, 7):
            for t4 in range(1, 7):
                for t5 in range(1, 7):
                    for t6 in range(1, 7):
                        if is_valid(t1, t2, t3, t4, t5, t6):
                            valid_count +=1
valid_count