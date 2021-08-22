Zc = [0.9976, 0.9901, 0.9785, 0.9645, 0.9591, 0.9496, 0.9396, 0.9331, 0.8898, 0.9933, 0.9995]
r_eps = [1000, 640, 600, 480]

A = [{'k': 0,
      'l': 0,
      'vals': [1.0245130e1, 3.3539090e1, 1.0169140e1, 1.0777610e1]},
     {'k': 1,
      'l': 0,
      'vals': [8.5906610e-2,
               -1.0282240e-1,
               4.3666120e-1,
               1.6474900e-1]},
     {'k': 0,
      'l': 1,
      'vals': [1.4982130e-1,
               2.0683750e-1,
               3.8170960e-2,
               -1.4050070e-1,
               -3.1156360e-1]},
     {'k': 2,
      'l': 0,
      'vals': [7.3843960e-3,
               2.3981410e-2,
               -8.7264540e-2,
               -5.1987300e-2,
               7.6359480e-1]},
     {'k': 1,
      'l': 1,
      'vals': [9.5705040e-3,
               3.3161370e-3,
               -7.9478640e-3,
               -7.0448690e-3,
               4.5480690e-2]},
     {'k': 0,
      'l': 2,
      'vals': [5.1369710e-3,
               -3.5536890e-3,
               1.0365010e-2,
               1.6154370e-2,
               1.1230410e-2]},
     {'k': 3,
      'l': 0,
      'vals': [-1.0036620e-4,
               -9.5847460e-4,
               5.9397950e-3,
               3.9913150e-3,
               -2.3762630e-2]},
     {'k': 2,
      'l': 1,
      'vals': [-2.0203270e-4,
               -2.4096040e-4,
               3.2678860e-4,
               1.4794820e-4,
               -7.8562940e-4]},
     {'k': 1,
      'l': 2,
      'vals': [-4.5802770e-5,
               3.9418400e-5,
               2.3714910e-4,
               3.3848030e-4,
               6.5557090e-4]},
     {'k': 0,
      'l': 3,
      'vals': [-5.6856150e-5,
               5.0018560e-5,
               -1.6152150e-4,
               -1.7546700e-4,
               -2.1468550e-3]},
     {'k': 4,
      'l': 0,
      'vals': [4.1273050e-7,
               2.0052880e-5,
               -1.8541270e-4,
               -1.2774870e-4,
               4.3554940e-4]},
     {'k': 3,
      'l': 1,
      'vals': [1.2511380e-6,
               3.4585100e-6,
               -3.3085860e-7,
               2.7564440e-6,
               3.8606680e-6]},
     {'k': 2,
      'l': 2,
      'vals': [3.1147030e-7,
               8.0364540e-7,
               -4.9758630e-6,
               -4.0416670e-6,
               -1.3816990e-6]},
     {'k': 1,
      'l': 3,
      'vals': [-3.1401570e-7,
               -4.3338760e-7,
               -8.7822910e-7,
               -1.9710210e-6,
               -7.9339020e-6]},
     {'k': 0,
      'l': 4,
      'vals': [2.4039480e-7,
               -2.5042560e-7,
               7.7408400e-7,
               6.0752130e-7,
               6.6993640e-5]},
     {'k': 5,
      'l': 0,
      'vals': [0.0000000e0,
               -2.1154170e-7,
               2.9565980e-6,
               2.0157030e-6,
               -4.6077260e-6]},
     {'k': 6,
      'l': 0,
      'vals': [0.0000000e0,
               9.0540200E-10,
               -2.3370740e-8,
               -1.5580170e-8,
               2.6105700e-8]},
     {'k': 7,
      'l': 0,
      'vals': [0,
               0,
               7.3223480e-11,
               4.7976930e-11,
               -6.1439140e-11]},
     {'k': 0,
      'l': 5,
      'vals': [0,
               0,
               0,
               0,
               -8.3693870e-7]},
     {'k': 0,
      'l': 6,
      'vals': [0,
               0,
               0,
               0,
               3.9280730e-9]}]


class Mix(object):
    def __init__(self, name, type, r):
        """
        Класс смеси
        :param name: Имя
        :type name: str
        :param type: 1, 2, 3, 4
        :type type: int
        :param r: массив с r Нормализованными
        :type r: list
        """
        self.name = name
        self.type = type
        self.rn = r
        self.r = []
        self.rmax = None
        self.first_comp = None
        self.second_comp = None
        self.MN = 0
        # Эти извращенцы не могли по нормальному в ГОСТе смеси ввести?
        # Почему у 2-й смеси зануляется 3-й компонент?!
        if type == 1:
            self.rmax = [0, 100, 100, 100]
            self.first_comp = 2
            self.second_comp = 1
        elif type == 2:
            self.rmax = [100, 100, 100, 0]
            self.first_comp = 0
            self.second_comp = 1
        elif type == 3:
            self.rmax = [100, 0, 100, 100]
            self.first_comp = 0
            self.second_comp = 2
        elif type == 4:
            self.rmax = [100, 100, 0, 100]
            self.first_comp = 0
            self.second_comp = 1
        self.w = sum([self.rn[i] * self.rmax[i] / r_eps[i] for i in range(4)])

    def normalize(self):
        s = sum(self.r)
        self.rn = []
        for i in range(len(self.r)):
            self.rn.append(self.r[i] * 100 / s)

    def get_MN(self):
        self.MN = 0
        for k in range(7):
            s = 0
            for l in range(6):
                try:
                    rec = next(item for item in A if item["k"] == k and item["l"] == l)
                    s += rec['vals'][self.type-1] * (self.rn[self.first_comp]) ** k * (self.rn[self.second_comp]) ** l
                except StopIteration:
                    continue
            self.MN += s


class Component(object):
    def __init__(self, name, mol, index):
        """
        Создание элемента компонента смеси
        :type index: int
        :type mol: float
        :param name: имя
        :param mol: молярная доля
        :param index: индекс элемента в последовательности, как в таблице 1, с нуля.
        """
        self.name = name
        self.mol = mol
        self.index = index
        self.r = None

    def get_weight(self):
        return self.mol * Zc[self.index]

    def set_r(self, sum):
        self.r = self.mol * Zc[self.index] * 100 / sum
        return self.r


class Gas(object):
    def __init__(self, C1, C2, C3, iC4, nC4, neoC5, iC5, nC5, C6, CO2, N2, N=3):
        # количество смесей
        self.N = N
        self.components = []
        self.components.append(Component("C1", C1, 0))
        self.components.append(Component("C2", C2, 1))
        self.components.append(Component("C3", C3, 2))
        self.components.append(Component("iC4", iC4, 3))
        self.components.append(Component("nC4", nC4, 4))
        self.components.append(Component("neoC5", neoC5, 5))
        self.components.append(Component("iC5", iC5, 6))
        self.components.append(Component("nC5", nC5, 7))
        self.components.append(Component("C6", C6, 8))
        self.components.append(Component("CO2", CO2, 9))
        self.components.append(Component("N2", N2, 10))
        self.sum = 0
        self.mixes = None
        self.r = None
        self.rc4p = None
        self.rs = None
        self.rsn = None
        self.process_mixes()
        self.set_init_values()
        for mix in self.mixes:
            mix.get_MN()
        print(self.mixes)

    def process_mixes(self):
        for component in self.components:
            self.sum += component.get_weight()
        self.r = [comp.set_r(self.sum) for comp in self.components]
        self.rc4p = sum(self.r[3:5]) + 2.3 * (sum(self.r[5:8])) + 5.3 * self.r[8]
        self.rs = self.r[:3]
        self.rs.append(self.rc4p)
        # Вычисление r для нормализовнаной упрощенной смеси
        self.rsn = [i * 100 / sum(self.rs) for i in self.rs]
        mix1 = Mix('mix1', 1, self.rsn)
        mix2 = Mix('mix2', 2, self.rsn)
        mix3 = Mix('mix3', 3, self.rsn)
        mix4 = Mix('mix4', 4, self.rsn)
        self.mixes = [mix1, mix2, mix3, mix4]
        self.mixes.sort(key=lambda x: x.w, reverse=True)
        self.mixes = self.mixes[:self.N]

    def set_init_values(self):
        for i in range(4):
            s = 0
            for mix in self.mixes:
                s += mix.rmax[i]
            for mix in self.mixes:
                mix.r.append(self.rsn[i] / s * mix.rmax[i])
        for mix in self.mixes:
            mix.normalize()

    def calc_sum_r(self):
        self.sum = self.C1 * 0.9976


if __name__ == "__main__":
    g = Gas(97.064, 1.6758, 0.2453, 0.0356, 0.0253, 0.0011, 0.0076, 0.0132, 0.0091, 0.053, 0.87)
