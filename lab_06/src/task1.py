from matplotlib import pyplot as plt

from parameters import params_table, project_modes


class Task1():
    def __init__(self, mode, size):
        self.mode = mode
        self.RELY = 1
        self.DATA = 1
        self.CPLX = 1
        self.TIME = 1
        self.STOR = 1
        self.VIRT = 1
        self.TURN = 1
        self.ACAP = 1
        self.AEXP = 1
        self.PCAP = 1
        self.VEXP = 1
        self.LEXP = 1
        self.MODP = 1
        self.TOOL = 1
        self.SCED = 1
        self.SIZE = size
    
    
    def EAF(self):
        return self.RELY * self.DATA * self.CPLX * self.TIME * self.STOR * \
               self.VIRT * self.TURN * self.ACAP * self.AEXP * self.PCAP * \
               self.VEXP * self.LEXP * self.MODP * self.TOOL * self.SCED
    
    
    def PM(self):
        return project_modes['c1'][self.mode] * self.EAF() * (self.SIZE ** project_modes['p1'][self.mode])


    def TM(self):
        return project_modes['c2'][self.mode] * (self.PM() ** project_modes['p2'][self.mode])
    

    def getComplexity(self, levelComplexity):
        if levelComplexity == 0:
            complexity = "очень низкая"
        elif levelComplexity == 4:
            complexity = "очень высокая"
        else:
            complexity = "номинальная"

        return complexity
    

    def buildGraph(self, x, y_pm, y_tm, levelComplexity):
        plt.figure(figsize=(14, 6))
        plt.suptitle("Исследование влияния атрибутов персонала на "
                     "трудозатраты и время разработки (Сложность: {})"\
                        .format(self.getComplexity(levelComplexity)))
        
        plt.subplot(121)
        plt.plot(x, y_pm[0], label='ACAP')
        plt.plot(x, y_pm[1], label='PCAP')
        plt.plot(x, y_pm[2], label='AEXP')
        plt.plot(x, y_pm[3], label='LEXP')
        plt.ylabel('Трудозатраты')
        plt.xlabel('Уровень фактора')
        plt.legend()
        plt.grid(True)

        plt.subplot(122)
        plt.plot(x, y_tm[0], label='ACAP')
        plt.plot(x, y_tm[1], label='PCAP')
        plt.plot(x, y_tm[2], label='AEXP')
        plt.plot(x, y_tm[3], label='LEXP')
        plt.ylabel('Время разработки')
        plt.xlabel('Уровень фактора')
        plt.legend()
        plt.grid(True)
        plt.show()


    def exploreAttributes(self):
        for i in [0, 2, 4]: # уровень сложности проекта
            self.CPLX = params_table['CPLX'][i]

            y_pm_acap = []
            y_pm_pcap = []
            y_pm_aexp = []
            y_pm_lexp = []

            y_tm_acap = []
            y_tm_pcap = []
            y_tm_aexp = []
            y_tm_lexp = []
            
            for j in range(4):
                self.ACAP = params_table['ACAP'][j]
                y_pm_acap.append(self.PM())
                y_tm_acap.append(self.TM())
            self.ACAP = 1

            for j in range(4):
                self.PCAP = params_table['PCAP'][j]
                y_pm_pcap.append(self.PM())
                y_tm_pcap.append(self.TM())
            self.PCAP = 1

            for j in range(4):
                self.AEXP = params_table['AEXP'][j]
                y_pm_aexp.append(self.PM())
                y_tm_aexp.append(self.TM())
            self.AEXP = 1

            for j in range(4):
                self.LEXP = params_table['LEXP'][j]
                y_pm_lexp.append(self.PM())
                y_tm_lexp.append(self.TM())
            self.LEXP = 1

            x = ['Очень низкий', 'Низкий', 'Номинальный', 'Высокий']
            y_pm = [y_pm_acap, y_pm_pcap, y_pm_aexp, y_pm_lexp]
            y_tm = [y_tm_acap, y_tm_pcap, y_tm_aexp, y_tm_lexp]
            
            self.buildGraph(x, y_pm, y_tm, i)
