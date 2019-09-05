import MainPageGui as view
import Model as model


def button_pressed(event):
    print(event.widget["text"])


def start():
    try:
        print("stuck in gui")
        view.init_gui()
        print("made it")
        model.load()
        view.show_data(model.get_data())
    except Exception:
        view.show_no_data()


if __name__ == "__main__":
    start()
