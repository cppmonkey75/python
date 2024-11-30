class Parent:
    def __init__(self) -> None:
        print("From base class")
    def speak(self):
        print("From parent speak")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("From child init ")
    def speak(self):
        super.speak()
        print("Now child")

p1=Parent()
p2=Child()
p1.speak()
p2.speak()