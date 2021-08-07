from gui import Window

def main():
    window = Window(700, 400, "Endangered Species")
    window.create_submit_page()
    window.display()

if __name__ == '__main__':
    main()
