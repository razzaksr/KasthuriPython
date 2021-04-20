class KasthuriError(RuntimeError):
    def __init__(self):
        self.msg="StockNotFound"
        super(KasthuriError, self).__init__()
    def __str__(self):
        return self.msg