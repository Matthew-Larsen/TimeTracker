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


def forceLoad():
    model.load()


def get_data():
    return model.get_data()


def get_data_with_tag(tag):
    return model.get_data_with_tag(tag)


def get_data_with_tag_after(tag, date):
    return model.get_tagged_after(tag, date)


def get_data_after(date):
    return model.get_data_after(date)


if __name__ == "__main__":
    start()
