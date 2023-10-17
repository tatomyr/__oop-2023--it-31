from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def open(self):
        pass

    @abstractmethod
    def close(self):
        pass


class OpenState(State):
    def open(self):
        print("Вікно вже відкрите.")
        return self

    def close(self):
        print("Закриваємо вікно...")
        return ClosedState()


class ClosedState(State):
    def open(self):
        print("Відкриваємо вікно...")
        return OpenState()

    def close(self):
        print("Вікно вже закрите.")
        return self


class Window:
    def __init__(self):
        self.current_state = ClosedState()

    def open(self):
        self.current_state = self.current_state.open()

    def close(self):
        self.current_state = self.current_state.close()


# Код для первірки роботи патерну.

window = Window()

window.close() #Закриваємо закрите вікно.
window.open() #Відкриваємо відкрите вікно.
window.open() #Відкриваємо відкрите вікно.
window.close() #Закриваємо відкрите відкно.
