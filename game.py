class Game:
    """
    A class used to represent games with certain attributes.
    """

    CIC = 1.96  # Confidence interval coefficient

    def __init__(self, RTP, variance):
        self.RTP = RTP
        self.variance = variance

    def __standard_dev(self):
        return self.variance ** 0.5

    def __volatility_index(self):
        return self.CIC * self.__standard_dev()

    def min_RTP(self, spin_count):
        return self.RTP - self.__volatility_index() / (spin_count ** 0.5)

    def max_RTP(self, spin_count):
        return self.RTP + self.__volatility_index() / (spin_count ** 0.5)

    def house_edge(self):
        edge_counter = 1
        while self.max_RTP(edge_counter) >= 1.00:
            edge_counter += 1
        return edge_counter
