from math import *

"""
Классификация ошибок
!xx - критическая ошибка. обязательно нужно поправить
@xx - ошибка. не очень важная, но поправить нужно
&xx - ошибка с потерей точности. некритично, но нежелательно
"""

DIVISION_DENOM_LIMIT = 20

class Number:
    numer, denom = [1], [0]
    len1, len2 = 1, 1
    sign = 1

    def __init__(self, *args, **kwargs):
        if args:
            if str(float(args[0]))[0] != "-":
                self.sign = 1
                snum = str(float(args[0])).split(".")
            else:
                snum = str(float(args[0]))[1:].split(".")
                self.sign = -1
            self.numer, self.denom = list(map(int, snum[0])), list(map(int, snum[1])) #Возможна ошибка IndexError, если число слишком большое
            self.len1, self.len2 = len(snum[0]), len(snum[1])                         #и представляется в виде ke+x "@01"
        else:
            self.numer, self.denom = list(map(int, kwargs["numer"])), list(map(int, kwargs["denom"]))
            self.len1, self.len2 = len(self.numer), len(self.denom)
            if "sign" in kwargs:
                self.sign = kwargs["sign"]

    def __repr__(self):
        return ("-" if self.sign == -1 else "") + "".join(map(str, self.numer)) + "." + "".join(map(str, self.denom))

    def __str__(self):
        return self.__repr__()

    def __add__(self, other):
        if not isinstance(other, Number):
            other = Number(other)
        if self.sign == -1 and other.sign == 1:
            return other - self
        if self.sign == 1 and other.sign == -1:
            return self - Number(numer=other.numer, denom = other.denom)
        if self.sign == -1 and other.sign == -1:
            self_copy = self.copy()
            self_copy.sign = 1
            other_copy = other.copy()
            other_copy.sign = -1
            result = self.copy + other.copy
            result.sign = -1
            return result
        maxlen1, maxlen2 = max(self.len1, other.len1), max(self.len2, other.len2)
        self_numer = [0] * (maxlen1 - self.len1) + self.numer
        other_numer = [0] * (maxlen1 - other.len1) + other.numer
        self_denom = self.denom + [0] * (maxlen2 - self.len2)
        other_denom = other.denom + [0] * (maxlen2 - other.len2)
        numer_new, denom_new = [0] * maxlen1, [0] * maxlen2
        mind = 0
        for i in range(max(self.len2, other.len2) - 1, -1, -1):
            denom_new[i] = (int(self_denom[i]) + int(other_denom[i]) + mind) % 10
            mind = (int(self_denom[i]) + int(other_denom[i]) + mind) // 10
        for i in range(max(self.len1, other.len1) - 1, -1, -1):
            numer_new[i] = (int(self_numer[i]) + int(other_numer[i]) + mind) % 10
            mind = (int(self_numer[i]) + int(other_numer[i]) + mind) // 10
        if mind:
            numer_new = [mind] + numer_new
        if not numer_new:
            numer_new = [0]
        if not denom_new:
            denom_new = [0]
        while numer_new[0] == 0 and len(numer_new) > 1:
            numer_new.pop(0)
        while denom_new[-1] == 0 and len(denom_new) > 1:
            denom_new.pop(-1)
        return Number(numer=numer_new, denom=denom_new)
    
    def __sub__(self, other):
        if not isinstance(other, Number):
            other = Number(other)
        if self < other:
            return -(other - self)
        if self.sign == -1 and other.sign == -1:
            return other - self
        if self.sign == 1 and other.sign == -1:
            return self + other
        if self.sign == -1 and other.sign == 1:
            self_copy = self.copy()
            self_copy.sign = 1
            other_copy = other.copy()
            other_copy.sign = -1
            result = self.copy + other.copy
            result.sign = -1
        maxlen1, maxlen2 = max(self.len1, other.len1), max(self.len2, other.len2)
        self_numer = [0] * (maxlen1 - self.len1) + self.numer
        other_numer = [0] * (maxlen1 - other.len1) + other.numer
        self_denom = self.denom + [0] * (maxlen2 - self.len2)
        other_denom = other.denom + [0] * (maxlen2 - other.len2)
        numer_new, denom_new = [0] * maxlen1, [0] * maxlen2
        if not numer_new:
            numer_new = [0]
        if not denom_new:
            denom_new = [0]
        mind = 0
        for i in range(max(self.len2, other.len2) - 1, -1, -1):
            denom_new[i] = (int(self_denom[i]) - int(other_denom[i]) + mind) % 10
            mind = (int(self_denom[i]) - int(other_denom[i]) + mind) // 10
        for i in range(max(self.len1, other.len1) - 1, -1, -1):
            numer_new[i] = (int(self_numer[i]) - int(other_numer[i]) + mind) % 10
            mind = (int(self_numer[i]) - int(other_numer[i]) + mind) // 10
        if mind:
            numer_new = [mind] + numer_new
        if not numer_new:
            numer_new = [0]
        if not denom_new:
            denom_new = [0]
        while numer_new[0] == 0 and len(numer_new) > 1:
            numer_new.pop(0)
        while denom_new[-1] == 0 and len(denom_new) > 1:
            denom_new.pop(-1)
        return Number(numer=numer_new, denom=denom_new)

    def __mul__(self, other):
        if not isinstance(other, Number):
            other = Number(other)
        raw_self = self.numer + (self.denom if self.denom != [0] else [])
        raw_other = other.numer + (other.denom if other.denom != [0] else [])
        po = self.len2 + other.len2 - (1 if self.denom == [0] else 0) - (1 if other.denom == [0] else 0)
        self.listm = []
        raw_sum = Number(0)
        for i in range(len(raw_other)):
            raw_tek = Number(0)
            for j in range(int(raw_other[i])):
                raw_tek += Number(numer=raw_self, denom=[0])
            self.listm.append(Number(numer=raw_tek.numer + [0] * (len(raw_other)-i-1), denom=[0]))
            raw_sum += Number(numer=raw_tek.numer + [0] * (len(raw_other)-i-1), denom=[0])
        numer = raw_sum.numer[:-po] if po != 0 else raw_sum.numer
        denom = raw_sum.numer[-po:] if po != 0 else [0]
        if not numer:
            numer = [0]
        if not denom:
            denom = [0]
        while numer[0] == 0 and len(numer) > 1:
            numer.pop(0)
        while denom[-1] == 0 and len(denom) > 1:
            denom.pop(-1)
        result = Number(numer=numer, denom=denom)
        return -result if self.sign != other.sign else result

    def __truediv__(self, other):         #При делении больших чисел в конце из ниоткуда образуется
        if not isinstance(other, Number): #цифра 1 "&02"
            other = Number(other)     #Вроде бы пофиксил. Проблема заключалась в том, что при переходе в крайний разряд
        assert other != 0                 #проверка срабатывает после прибавления единицы к общему счетчику и обнаруживает выход за границы только в этот момент
        maxlen2 = max(self.len2, other.len2)
        raw_self = Number(numer = self.numer + (self.denom if self.denom != [0] else []) + [0] * (maxlen2 - self.len2), denom = [0])
        raw_other = Number(numer = other.numer + (other.denom if other.denom != [0] else []) + [0] * (maxlen2 - other.len2), denom = [0])
        result = Number(0)

        while raw_self != 0:
            if raw_self >= raw_other:
                raw_self -= raw_other
                result += 1
            else:
                break
        raw_self *= 10
        deep = 1
        while raw_self != 0 and len(result.denom) < DIVISION_DENOM_LIMIT:
            if raw_self >= raw_other:
                raw_self -= raw_other
                if len((result + Number(numer=[0], denom = [0] * (deep - 1) + [1])).denom) >= DIVISION_DENOM_LIMIT:
                    break
                result += Number(numer=[0], denom = [0] * (deep - 1) + [1])
            else:
                deep += 1
                raw_self *= 10
        if not result.numer:
            result.numer = [0]
        if not result.denom:
            result.denom = [0]
        while result.numer[0] == 0 and len(result.numer) > 1:
            result.numer.pop(0)
        while result.denom[-1] == 0 and len(result.denom) > 1:
            result.denom.pop(-1)
        return -result if self.sign != other.sign else result
        #print(n // dn)
        #tn = n % dn * 10;
        #while True:
        #    print(tn // dn)
        #    if (tn % dn == 0): break
        #    tn = tn % dn * 10
        #

    def __floordiv__(self, other):
        if not isinstance(other, Number):
            other = Number(other)
        assert other != 0
        maxlen2 = max(self.len2, other.len2)
        raw_self = Number(numer = self.numer + (self.denom if self.denom != [0] else []) + [0] * (maxlen2 - self.len2), denom = [0])
        raw_other = Number(numer = other.numer + (other.denom if other.denom != [0] else []) + [0] * (maxlen2 - other.len2), denom = [0])
        result = Number(0)

        while raw_self != 0:
            if raw_self >= raw_other:
                raw_self -= raw_other
                result += 1
            else:
                break
        if not result.numer:
            result.numer = [0]
        if not result.denom:
            result.denom = [0]
        while result.numer[0] == 0 and len(result.numer) > 1:
            result.numer.pop(0)
        while result.denom[-1] == 0 and len(result.denom) > 1:
            result.denom.pop(-1)
        return -result if self.sign != other.sign else result

    def __mod__(self, other):
        assert other != 0
        return self - (self // other) * other

    def __divmod__(self, other):
        return (self // other, self % other)

    def copy(self):
        return Number(numer = self.numer, denom = self.denom, sign = self.sign)

    def __lt__(self, other):
        return float(str(self)) < float(str(other))

    def __le__(self, other):
        return float(str(self)) <= float(str(other))

    def __rt__(self, other):
        return float(str(self)) > float(str(other))

    def __re__(self, other):
        return float(str(self)) >= float(str(other))

    def __eq__(self, other):
        return float(str(self)) == float(str(other))

    def __ne__(self, other):
        return float(str(self)) != float(str(other))

    def __neg__(self):
        self_copy = self.copy()
        self_copy.sign = -1
        return self_copy
    
    def __bool__(self):
        return str(self) != "0.0"
    
    def __abs__(self):
        self_copy = self.copy()
        self_copy.sign = 1
        return self_copy
    
    def __int__(self):
        self_copy = self.copy()
        self_copy.denom = [0]
        return int(float(str(self_copy)))
    
    def __float__(self):
        return float(str(self))
    
    #TODO:
    #Возведение в рациональную степень, извлечение корня рациональной степени и логарифм

__all__ = ["Number", "DIVISION_DENOM_LIMIT"]

if __name__ == "__main__":
    a = Number(2)
    b = Number(numer = [1, 2, 3], denom = [1, 9])
    c = Number(-3)
    d = Number(3)

    a + b
    c - d
    a / b + c - d
    d * 2 - c / 3 + a
