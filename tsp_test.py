from tsp_bitshift import tsp_bitshift
from tsp_normal import tsp_normal
from nose.tools import assert_equal
import time

"""
TSP Städte
13
18
25
"""

test_files = ["short_cities.txt", "middle_cities.txt", "long_cities.txt"]


def test_tsp(file, tsp_len):

    # short_cities
    if file == test_files[0]:
        print("--------------------------------------")
        print("Meilen (Kurze Städte):", tsp_len)
        assert_equal(7293, tsp_len)

    # middle_cities
    if file == test_files[1]:
        print("--------------------------------------")
        print("Meilen (Mittlere Städte):", tsp_len)
        assert_equal(285, tsp_len)

    # long_cities
    if file == test_files[2]:
        print("--------------------------------------")
        print("Meilen (Lange Städte):", tsp_len)
        assert_equal(1978, tsp_len)


def test():
    # Durch alle Testdaten files durchiterieren, welche oben angegeben sind
    for file in test_files:
        with open("Testdaten/" + file, "r") as input:
            cities = []
            for line in input.readlines():
                line = line.replace("\n", "")

                cities.append(line)

            data = [cities[row].split(" ") for row in range(len(cities))]
            data = [[int(data[row][col]) for col in range(len(data))] for row in range(len(data))]

            # Laufzeitmessung für TSP_BITSHIFT
            start = time.time()
            test_tsp(file, tsp_bitshift(data))
            ende = time.time()
            print('{:5.10f}s'.format(ende - start))

            # Laufzeitmessung für TSP_NORMAL
            start = time.time()
            test_tsp(file, tsp_normal(data))
            ende = time.time()
            print('{:5.10f}s'.format(ende - start))


if __name__ == '__main__':
    test()

