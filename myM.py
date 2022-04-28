class MyMethods:

    @staticmethod
    def arithmetic_mean(my_list):
        s = 0
        for num in my_list:
            s += num
        return s/len(my_list)
        
    @staticmethod
    def my_max(my_list):
        my_max = my_list[0]
        for el in my_list:
            if el > my_max:
                my_max = el
        return my_max

    @staticmethod
    def my_min(my_list):
        my_min = my_list[0]
        for el in my_list:
            if el < my_min:
                my_min = el
        return my_min

    @staticmethod
    def repeated_el(my_list,el_test):
        rep = 0
        i = 0
        while i < len(my_list):
            if my_list[i] == el_test:
                rep += 1
            i += 1
        return rep

    @staticmethod
    def repeated_most_often(my_list):
        max_rep = 0
        el_max_rep = None
        for el in my_list: 
            rep = MyMethods.repeated_el(my_list,el)
            if rep > max_rep:
                max_rep = rep
                el_max_rep = el
        return el_max_rep

    @staticmethod
    def is_it_a_prime_number(inp):
        prime = True
        if inp <= 0:
            prime = False
        if inp == 1:
            prime = False
        if inp == 2:
            prime = True
        i = 2
        while i < inp: 
            if inp % i == 0:
                prime = False
            i += 1
        return prime


    @staticmethod
    def leibniz_formula_for_pi(n):
        a = 3
        suma_c = 0
        while n > 0:
            suma_c += 1/a*(-1)**n
            a += 2
            n -= 1
        PI = (1 - suma_c)*4
        return PI

# print("=="*50)
# print(f"MyMethods.arithmetic_mean([5,4,5]) \t\t {MyMethods.arithmetic_mean([5,4,5])}")
# print(f"MyMethods.my_max([-1,5,7,4,5]) \t\t\t {MyMethods.my_max([-1,5,7,4,5])}")
# print(f"MyMethods.my_min([-1,5,7,4,5]) \t\t\t {MyMethods.my_min([-1,5,7,4,5])}")
# print(f"MyMethods.repeated_el([1,1,1,5,5,5,7],1) \t {MyMethods.repeated_el([1,1,1,5,5,5,7],1)}")
# print(f"MyMethods.repeated_most_often([1,1,1,1,5,5,1]) \t {MyMethods.repeated_most_often([1,1,1,1,5,5,1])}")
# print(f"MyMethods.leibniz_formula_for_pi(1000) \t\t {MyMethods.leibniz_formula_for_pi(1000)}")
# print(f"MyMethods.is_it_a_prime_number(7) \t\t {MyMethods.is_it_a_prime_number(7)}")
# print(f"MyMethods.is_it_a_prime_number(22) \t\t {MyMethods.is_it_a_prime_number(22)}")
# print("=="*50)