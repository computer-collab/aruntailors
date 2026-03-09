print("Hello world")
if __name__ == "__main__":
    class ThisObject:
        def __init__ (self, value):
            self.ex = value;
        def __call__(self):
            self.ex
            print(self.ex)
    
    blueprint = ThisObject(5)
    blueprint()