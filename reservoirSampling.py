## reservoir sampling

class ReservoirSampling:
    def __init__(self, k):
        self.samples = []
        self.maxSize = k
        self.index = 0

    def add(self):
        element = self.get_next_number()
        if self.index >= self.maxSize:
            num = random.randint(1, self.index+1)
            if num < self.maxSize:
                self.samples[num-1] = element
        else:
            self.samples.append(element)
        self.index += 1


class RandomSampling:
    def randomSampling(self, arr, k):
        n = len(arr)
        picked = [False]*n
        res = []
        i = 0

        while i < k:
            idx = random.randint(0, n-1)
            if picked[idx] == False:
                res.append(arr[idx])
                picked[idx] = True
                i += 1
        return res
