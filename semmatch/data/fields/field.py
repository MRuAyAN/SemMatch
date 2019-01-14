class Field(object):
    def __init__(self):
        pass

    def count_vocab(self, counter):
        raise NotImplementedError

    def index(self, vocab):
        raise NotImplementedError

    def to_example(self):
        raise NotImplementedError

    def get_example(self):
        raise NotImplementedError
