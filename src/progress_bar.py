import sys

class Progbar:
    def __init__(self, period=100, bars=32):
        self._period  = period
        self.bars     = bars
        self.active   = True
    def __del__(self):
        self.dispose()
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        self.dispose()

    def dispose(self):
        if self.active:
            self.active = False
            self.update(self._period, "")
            sys.stdout.write("\n")
    def update(self, tick, status: str):
        rate = tick / self._period
        # progress rate
        str = "{0:7d}% ".format(int(rate*100))
        # progress bar
        bar_prog = int(rate * self.bars)
        str += "|"
        str += "#" * (            bar_prog)
        str += "-" * (self.bars - bar_prog)
        str += "|"
        str += status
        str += "\r"
        sys.stdout.write(str)
