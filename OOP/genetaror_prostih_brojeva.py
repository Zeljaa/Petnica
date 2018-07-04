class PrimeGenerator: 
    def __init__(self):
        self.Sito(30)
    
    def get(self):
        return self.primes[self.index]
 
    def next(self):
        self.index += 1
 
    def Sito(self, rng):
        sieve = [True for _ in range(rng+1)]
        sieve[0:1] = [False, False]
        for start in range(2, rng+1):
            if sieve[start]:
                for i in range(2 * start, rng + 1, start):
                    sieve[i] = False
        primes = []
        for i in range(2, rng+1):
            if sieve[i]:
                primes.append(i)
        self.primes = primes
        self.index = 0
 
t = PrimeGenerator()

for i in range(10):
    t.next()
    print(t.get())
