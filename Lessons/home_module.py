import true_math as tm
import fake_math as fm


def main():
    first_mt = input("first = ")
    second_mt = input("second = ")
# проверить что ввели верные данные
    if first_mt.strip().isdigit() and second_mt.strip().isdigit():
        tm.divide(int(first_mt), int(second_mt))

    first_mf = input("first_f = ")
    second_mf = input("second_f = ")
# проверить что ввели верные данные
    if first_mf.strip().isdigit() and second_mf.strip().isdigit():
        fm.divide(int(first_mf), int(second_mf))


if __name__ == '__main__':
    main()

