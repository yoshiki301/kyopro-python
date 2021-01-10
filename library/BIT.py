class BinaryIndexedTree():
    # LSBの計算を容易にするため, 1-indexedとする
    def __init__(self, size: int, func=lambda a, b: a + b):
        self.bit = [0] * (size+1)
        self.size = size
        self.func = func

    # i番目にxだけ加算
    def add(self, _i: int, _x):
        _i += 1 # 1-indexed
        while _i <= self.size:
            self.bit[_i] = self.func(self.bit[_i], _x)
            _i += _i & -_i # LSB加算

    # 1番目からi番目までの総和
    def sum(self, _i: int):
        _i += 1 # 1-indexed
        s = 0
        while _i > 0:
            s = self.func(s, self.bit[_i])
            _i -= _i & -_i # LSB減算
        return s