import csv
import statistics


def read_line(reader):
    fields = next(reader)
    print(" | ".join(fields))
    return fields


def slice(coffe_list, start, end):
    coffe_list.seek(0)
    reader = csv.reader(coffe_list, delimiter=",")
    for i in range(end):
        if i >= start:
            read_line(reader)
        else:
            next(reader)


def find_popular(coffe_list):
    coffe_list.seek(0)
    reader = csv.DictReader(coffe_list, delimiter=",")
    drinks = []
    for r in reader:
        drinks.append(r["coffee_name"])

    res = statistics.mode(drinks)
    print(res)
    # counter = {d: 0 for d in drinks}

    # for d in drinks:
    #     counter[d] += 1
    # print(counter)
    # print(max(counter, key=lambda k: counter[k]))


def income_month(coffe_list):
    month = min(max(int(input("1-12 ")), 1), 12)
    coffe_list.seek(0)
    reader = csv.DictReader(coffe_list, delimiter=",")
    income = 0
    for r in reader:
        if r["Monthsort"] == str(month):
            income += float(r["money"])
    print(income)
    return income



if __name__ == '__main__':
    with open("Coffe_sales.csv") as coffe_list:
        #reader = csv.reader(coffe_list, delimiter=",")
        # read_line(reader)
        #slice(coffe_list, 8, 14)
        #find_popular(coffe_list)
        income_month(coffe_list)