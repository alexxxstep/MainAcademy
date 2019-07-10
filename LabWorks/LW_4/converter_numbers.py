class Converter:
    R = {0: '', 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M',
         4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}
    RO = {0: '', 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    RO_M = {4: 'IV', 9: 'IX', 40: 'XL', 90: 'XC', 400: 'CD', 900: 'CM'}

    def __init__(self, number):
        self.number = number
        self.nList = []
        self.romList = []

    def convert(self):
        if self.is_arabs():
            return self.to_roman()
        elif self.is_roms():
            return self.to_arab()
        else:
            return None

    def is_arabs(self):
        try:
            return isinstance(int(self.number), int)
        except:
            return False

    def is_roms(self):
        ro_list = Converter.RO.values()
        for i in str(self.number):
            if i in ro_list:
                continue
            else:
                return False
        return True

    def to_roman(self):
        if int(self.number) > 0 and int(self.number) <= 3999:
            arList = self.get_numbs_list()
            # [1000, 100, 10 , 1]
            # [0,1,2,3]
            romList = []

            s = 3
            for x in range(4):
                n_tuple = self.get_numbs_tuple(arList[x])
                for n in n_tuple:
                    if n > 0 and n <= 3:
                        st = 10 ** s
                        val = Converter.R.get(st)
                        r_s = val * n
                    else:
                        st = 10 ** s
                        val = Converter.R.get(n * st)
                        r_s = val
                    self.romList.append(r_s)
                s -= 1

            return ''.join(self.romList)

    def get_numbs_list(self):
        n = int(self.number)
        d = 10
        s = 3
        m_list = []
        d_list = []

        while n > 0:
            m = n // (d ** s)
            m_list.append(m)
            md = m * (d ** s)
            d_list.append(md)
            n -= md
            s -= 1
        return m_list

    def get_numbs_tuple(self, n):
        if n > 5 and n <= 8:
            ost = n % 5
            return (n - ost, ost)
        else:
            return (n,)

    def to_arab(self):

        n_list = list(self.number)
        l_st = len(n_list)

        while l_st > 0:

            srez = n_list[:l_st]

            twice = srez[l_st-2:]
            twice_val = ''.join(twice)
            ones = srez[l_st-1:]
            ones_val = ''.join(ones)

            k_twice = self.get_key(Converter.RO_M, twice_val)
            if k_twice:
                self.nList.append(k_twice)
                l_st -= 2
                continue

            k_ones = self.get_key(Converter.RO, ones_val)
            if k_ones:
                self.nList.append(k_ones)
                l_st -= 1

        # print(self.nList)
        return sum(self.nList)

    def get_key(self, d, value):
        for k, v in d.items():
            if v == value:
                return k
        else:
            return None


# con = Converter('1087')
# print(con.convert())

ar = Converter('MLXXXVII')
print(ar.convert())
