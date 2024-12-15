class Bin:
     def start(self):
        cont = self.check()
        require = self
        if cont != "NONE":
            require = []
        start(require)
        if require:
            with open(self.stat,"w") as f:
                f.write("None")