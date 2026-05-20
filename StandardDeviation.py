import statistics


class StandardDeviation:
    def __init__(self) -> None:
        pass

    def mean(self, data):
        return statistics.mean(data)

    def stdev(self, data):
        return statistics.stdev(data)

    def test1(self):
        data = [1, 2, 3]
        print(f"data: {data}")
        print(f"mean: {self.mean(data)}")
        print(f"standard deviation: {self.stdev(data)}")
    def test2(self):
        data=[-101,6,101]
        print(f"data: {data}")
        print(f"mean: {self.mean(data)}")
        print(f"standard deviation: {self.stdev(data)}")

def main():
    std = StandardDeviation()
    std.test1()
    std.test2()


if __name__ == "__main__":
    main()
