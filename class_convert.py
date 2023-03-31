class converter:
    def __init__(self,data_from,data_to,value):
        self.data_from = data_from
        self.data_to = data_to
        self.value = value

    def __convert_gr(self):
        res = 0
        if self.data_to == 'Gram':
            res = self.value
        elif self.data_to == 'Kg':
            res = self.value / 1000
        elif self.data_to == 'Ton':
            res = self.value / 1000 / 1000
        return res

    def __convert_kg(self):
        res = 0
        if self.data_to == 'Gram':
            res = self.value * 1000
        elif self.data_to == 'Kg':
            res = self.value
        elif self.data_to == 'Ton':
            res = self.value / 1000
        return res

    def __convert_ton(self):
        res = 0
        if self.data_to == 'Gram':
            res = self.value * 1000 * 1000
        elif self.data_to == 'Kg':
            res = self.value * 1000
        elif self.data_to == 'Ton':
            res = self.value
        return res



    def convert(self):
        if self.data_from == "Gram":
            return self.__convert_gr()
        elif self.data_from == "Kg":
            return self.__convert_kg()
        elif self.data_from == "Ton":
            return self.__convert_ton()