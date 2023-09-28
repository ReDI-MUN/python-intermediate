# Running this script will cause an error. Find the error using the debugger and fix it.
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def divide(self):
        return self.a / self.b


class AdvancedCalculator(Calculator):
    def power(self):
        return self.a ** self.b

    def modulo(self):
        return self.a % self.b


def main():
    calc1 = Calculator(10, 5)
    calc2 = AdvancedCalculator(10, 0)

    print(f"Basic Calculator: ")
    print(f"Adding: {calc1.add()}")
    print(f"Subtracting: {calc1.subtract()}")
    print(f"Multiplying: {calc1.multiply()}")
    print(f"Dividing: {calc1.divide()}")  # Should work fine

    print(f"\nAdvanced Calculator: ")
    print(f"Adding: {calc2.add()}")
    print(f"Subtracting: {calc2.subtract()}")
    print(f"Multiplying: {calc2.multiply()}")
    print(f"Power: {calc2.power()}")

    # Trigger the bugs
    print(f"Dividing: {calc2.divide()}")
    print(f"Modulo: {calc2.modulo()}")


if __name__ == "__main__":
    main()
