import math

class NormalDistribution():

    def __init__(self) -> str:
        return print("This class implements Normal distribution in statistics and probality.\n")
    
    def z_score(self,x:int,mu:int,sigma: int)-> float:
        self.z_score = (x-mu)/sigma

        if self.z_score < 0:
            return print(f'z-score is {self.z_score}. {x} is {self.z_score} steps from the mean {mu}.')
        
        else:
            return print(f'z-score is {self.z_score}. {x} is {self.z_score} steps from the mean {mu}.')
        

    def impericalRule(self):
        self.notes = """
        If X is a random variable and has a normal distribution with mean µ and standard deviation σ, then the Empirical Rule states that:\n
            • About 68% of the x values lie between –1σ and +1σ of the mean µ (within one standard deviation of the mean).\n
            • About 95% of the x values lie between –2σ and +2σ of the mean µ (within two standard deviations of the mean).\n
            • About 99.7% of the x values lie between –3σ and +3σ of the mean µ (within three standard deviations of the mean).\n
        

            Notice that almost all the x values lie within three standard deviations of the mean.\n
            • The z-scores for +1σ and –1σ are +1 and –1, respectively.\n
            • The z-scores for +2σ and –2σ are +2 and –2, respectively.\n
            • The z-scores for +3σ and –3σ are +3 and –3 respectively.\n
        The empirical rule is also known as the 68-95-99.7 rule."""

        return print(self.notes)
    
    def z_prob(self):
        pass


class Geometric:
    def __init__(self,data):
        self.data = data
        
    def geometricMean(self):
        for num in self.data:
            pass


class ArithmeticMean:
    def __init__(self,X)->list:
        self.__x_sum = 0
        self.X = X
        
    def mean(self)->float:
        for i in range(len(self.X)):
            self.__x_sum += self.X[i]
        return self.__x_sum/len(self.X)




