class ProgressBar:
    def __init__(self, name:str, cur:int, total:int) -> None:
        self.reset(name, cur, total)

    def reset(self, name:str, cur:int, total:int):
        self.name = name
        self.cur = cur
        self.total = total

    def print(self):
        self.cur += 1
        if self.cur <= self.total:
            percentage = int(100 * self.cur // self.total)
            fill = "█" * percentage
            empty = " " * (100 - percentage)
            print(f"\r {self.name}: {fill}{empty} {self.cur} / {self.total}", end="\r")
        if self.cur == self.total:
            print()
