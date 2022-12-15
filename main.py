def find_index(num_of_str, max_freq_signal, signals_longitude, signals_latitude):
    freq_signals_latitude = []                                                  #создаем список широт сигналов
    for i in range(int(num_of_str)):                                            #проходим по всем элементам
        if signals_longitude[i] == str(max_freq_signal):                        #проверяем на то, что долгота равняется найденной максимальной
            tmp = int(signals_latitude[i])                                      #временная переменная для хранения широты
            if tmp < 0:                                                         #проверяем на отрицательность
                tmp = (abs(tmp) // 10) * -1                                     #находим остаток от деления на 10 модуля и умножаем на 1
            else:                                                               #если не отрицательное, то
                tmp = tmp//10                                                   #просто находим остаток от деления на 10
            freq_signals_latitude.append(tmp)                                   #добовляем результат в список
    return freq_signals_latitude                                                #возвращаем результат


def strList_to_intList(freq_signals):
    freq_signals = list(freq_signals)                                           #переводим мнржество в список
    for i in range(len(freq_signals)):                                          #проходимся по массиву
        freq_signals[i] = int(freq_signals[i])                                  #переводим все строки в числа
    return freq_signals                                                         #возвращаем результат


def find_max_freq(signals_longitude_set, signals_longitude):
    freq_max = 0                                                                # переменная для хранения максимальной частоты
    for i in range(len(signals_longitude_set)):                                 # проходимся по уникальным долготам
        freq = signals_longitude.count((signals_longitude_set[i]))              # считаем сколько раз встречается каждая
        if freq > freq_max:                                                     # проверяем на то, что частота больше максимальной
            freq_max = freq                                                     # обновляем максимальную частоту
    return freq_max


def main():
    signals_latitude = []                                                       #создаем массив широт
    signals_longitude = []                                                      #создаем массив долгот
    with open('26.txt', 'r') as file:                                           #считываем данные
        num_of_str = file.readline()                                            #записываем
        for i in range(int(num_of_str)):                                        #проходим по всем данным
            tmp = file.readline().split()                                       #временная переменная для хранения списка [широта, долгота]
            signals_latitude.append(tmp[0])                                     #записываем широты
            signals_longitude.append(tmp[1])                                    #записываем долготы

    signals_longitude_set = set()                                               #создаем множество долгот
    for i in range(len(signals_longitude)):                                     #проходимся по всем долготам
        signals_longitude_set.add(signals_longitude[i])                         #записываем их в множество

    signals_longitude_set = list(signals_longitude_set)                         #переводим множество в список

    freq_max = find_max_freq(signals_longitude_set, signals_longitude)          #переменная для хранения максимальной частоты

    freq_signals = set()                                                        #создаем множество самых частых долгот
    for i in range(len(signals_longitude_set)):                                 #проходимся по множеству уникальных долгот
        if signals_longitude.count((signals_longitude_set[i])) == freq_max:     #проверяем на то, что частоты долгот максимальна
            freq_signals.add(signals_longitude_set[i])                          #если так, то записываем в множество самых частых долго

    freq_signals = strList_to_intList(freq_signals)                             #переводим все элементы в числа
    freq_signals.sort()                                                         #сортируем получившийся массив
    max_freq_signal = freq_signals[-1]                                          #берем максимальный элемент

    # создаем список широт сигналов
    freq_signals_latitude = find_index(num_of_str, max_freq_signal, signals_longitude, signals_latitude)

    print(max_freq_signal, len(set(freq_signals_latitude)))                     #выводим получившийся результат


if __name__ == "__main__":
    main()
