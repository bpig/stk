import sys
import pandas as pd
from futu import *

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)


class Logger:
    def __init__(self, filename='default.log'):
        self.terminal = sys.stdout
        sys.stdout = self
        self.log = open(filename, "w")

    def write(self, msg):
        self.terminal.write(msg)
        self.log.write(msg)

    def reset(self):
        self.log.close()
        sys.stdin = self.terminal

    def flush(self):
        self.log.flush()
        pass


class Connect:
    def __enter__(self):
        self.conn = OpenQuoteContext(host='127.0.0.1', port=11111)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()
