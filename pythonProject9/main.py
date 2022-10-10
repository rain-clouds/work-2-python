import random
random.seed(0)
e=2.7182818284

def CreareMatrice(N, J, nr=0.0):  # crearea matricei de dimensiuni N
    M = []
    for i in range(N):
        M.append([nr]*J)
    return M


def sigmoid(x):   # functia sigmoida la care utilizam 1/(1+e^-x)
    return 1.0/(1.0+e**(-1.0*x))


def dsigmoid(y):  # derivata functiei sigmoide
    return 1.0 - y**2

def Random(a, b):
    return (b-a)*random.random() + a

class IA:
    def __init__(self, NI, NH, NO):

        self.NI = NI + 1 # +1 pentru bias
        self.NH = NH
        self.NO = NO

        # activarea nodurilor
        self.AI = [1.0]*self.NI
        self.AH = [1.0]*self.NH
        self.AO = [1.0]*self.NO

        # crearea de weights
        self.WI = CreareMatrice(self.NI, self.NH)
        self.WO = CreareMatrice(self.NH, self.NO)


        for i in range(self.NI):       # le setam valori random
            for j in range(self.NH):
                self.WI[i][j] = Random(-0.2, 0.2)

        for i in range(self.NH):
            for j in range(self.NO):
                self.WO[i][j] = Random(-2.0, 2.0)

        # ultima modificare a weight-ului pentru momentum M
        self.CI = CreareMatrice(self.NI, self.NH)
        self.CO = CreareMatrice(self.NH, self.NO)

    def test(self, M_AND):
        for p in M_AND:
            print(p[0], '->', self.update(p[0]))

    def update(self, inputs):


        for i in range(self.NI-1):  #activarea inputului
            self.AI[i] = inputs[i]

        for j in range(self.NH):  # activarea pentru hidden
            S = 0.0
            for i in range(self.NI):
                S = S + self.AI[i] * self.WI[i][j]
            self.AH[j] = sigmoid(S)


        for i in range(self.NO):  # activarea pentru output
            S = 0.0
            for j in range(self.NH):
                S = S + self.AH[j] * self.WO[j][i]
            self.AO[i] = sigmoid(S)

        return self.AO[:]


    def BackPropagate(self, target, L,M):

        output_deltas = [0.0] * self.NO   #eroarea pt output
        for i in range(self.NO):
            error = target[i]-self.AO[i]
            output_deltas[i] = dsigmoid(self.AO[i]) * error

        # calculate error terms for hidden
        hidden_deltas = [0.0] * self.NH
        for j in range(self.NH):
            error = 0.0
            for i in range(self.NO):
                error = error + output_deltas[i]*self.WO[j][i]
            hidden_deltas[j] = dsigmoid(self.AH[j]) * error


        for j in range(self.NH):  # reactualizam weight-ul de la output
            for i in range(self.NO):
                change = output_deltas[i]*self.AH[j]
                self.WO[j][i] = self.WO[j][i] + L*change + M*self.CO[j][i]
                self.CO[j][i] = change


        for i in range(self.NI):  # reactualizam weight-ul de la input
            for j in range(self.NH):
                change = hidden_deltas[j]*self.AI[i]
                self.WI[i][j] = self.WI[i][j] + L*change + M*self.CI[i][j]
                self.CI[i][j] = change

        # calcularea erorii
        error = 0.0
        for i in range(len(target)):
            error = error + 0.5*(target[i]-self.AO[i])**2
        return error



    def iteratii(self, M_AND, EP, L, M=0.0):
        # L: learning rate
        # M: momentum factor
        for i in range(EP):
            error = 0.0
            for p in M_AND:
                input = p[0]
                target = p[1]
                self.update(input)
                error = error + self.BackPropagate(target, L, M)
            if i % 200 == 0:
                print('error',error)

        print('Acuratetea ->',1-error)


def rezolvare():

    MatriceAND = [
        [[0,0], [0]],
        [[0,1], [0]],
        [[1,0], [0]],
        [[1,1], [1]]
    ]

    m = IA(2, 2, 1) # creare retea cu 2 inputuri, 2 hidden si un output
    print("Numar epoci de antrenare:")
    EP = int(input())
    print("Rata de invatare:")
    L = float(input())
    m.iteratii(MatriceAND,EP,L)
    m.test(MatriceAND)


rezolvare()