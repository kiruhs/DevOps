# ================================================================================================
lst = {3, 8, -8,"hello", 0, -17, 5, 'a'} # <<3, 8, -8, 0, -17, 5>>
lst2 = [30, 2, -5,0, -2, 8]
class My_arr(list):
    "This class inherits from list and sorts all elements and more.."

    def __init__(self, it):
        a = []
        for i in it:
            if isinstance(i, (int,float,bool)):
                a.append(i)
        it = a
        super().__init__(sorted(it))
        self.index = 0

    def __str__(self):

        return f"<<{', '.join(str(item) for item in self)}>>"

    def append(self, object):
        super().append(object)
        self.sort()

    def __len__(self):
        cnt = 0
        # if isinstance(self, str):
        #     self = self.split()
        for i in self:
            if i >= 0:
                cnt += 1
        return cnt
    @property
    def length(self):
        return super().__len__()

    def __getitem__(self, item):
        it = super().__getitem__(item)
        if isinstance(item, slice):
            return My_arr([i for i in it])
            # return f"<<{', '.join(str(i) for i in it)}>>"

        return it
        # if isinstance(item, slice):
        #     return My_arr[item]
        # return item
    @property
    def even(self):
        it = [i for i in self if i % 2 == 0]
        return My_arr(it)
    # @property
    def __call__(self):
        return self

    def __sub__(self, other):
        if other > self.length:
            print("The number is greater than list length")
            return None
        for i in range(other):
            self.pop()
        return self

    def __pow__(self, power, modulo=None):
        if not isinstance(power, int):
            return NotImplementedError
        new = My_arr([])
        for i in self:
            for j in range(power):
                new.append(i)
        return new

    def __next__(self):
        if self.index >= self.length:
            raise StopIteration
        value = self[self.index]
        self.index += 1
        return value

    def __neg__(self):
        rev = [-i for i in self]
        return My_arr(rev)

    def map_(self, func):
        return iter(My_arr(map(func, self)))

    @property
    def dif(self):
        return self[-1] - self[0]

    def __gt__(self, other):
        if not isinstance(other, My_arr):
            return
        return self.dif > other.dif

    def __lt__(self, other):
        if not isinstance(other, My_arr):
            return
        return self.dif < other.dif


    def __ge__(self, other):
        if not isinstance(other, My_arr):
            return
        return self.dif >= other.dif

    # def __del__(self):
    #     return
        # raise NotImplementedError

    def dct(self):
        return {k:self[k] for k in range(self.length)}



new_list = My_arr(lst)
new_list2 = My_arr(lst2)
print(new_list == new_list2)
print(new_list)
# print(My_arr.mro())
new_list.append(-100)
print(new_list)
print((new_list.length))
# print(len(new_list[2:4]))

print(new_list.even)

# print(new_list - 2)

# lst = [3,5,6,7,8,8]
# print(new_list[2:7])
# print(new_list[2:7].length)
#
# print(new_list + [2, 4, 5])

# print(new_list**1)
# print(next(new_list))
# print(new_list)
# print(new_list2)
# buildin_map = map(lambda x: x**2, new_list)
# my_map = new_list.map_(lambda x: x**2)
# print(My_arr(buildin_map))
# print(next(buildin_map))
# print(next(buildin_map))
# print(My_arr(my_map))
# print(next(my_map))
# print(new_list < new_list2)

# list = 5
# print = 5
# print(list((3,4,5)))

# del new_list
# print(new_list)


# print(new_list.dct())

