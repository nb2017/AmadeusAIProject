from AmadeusSound import AmadeusSound

class Amadeus():
    modules = None
    def __init__(self):
        if self.modules is None:
            self.modules = [
                AmadeusSound(),
            ]
            for module in self.modules:
                module.wakeUp()
