class al:
    def aaa(self):
        print("a")
        self.bbb()

    def bbb(self):
        print("b")

a = al()
a.aaa()