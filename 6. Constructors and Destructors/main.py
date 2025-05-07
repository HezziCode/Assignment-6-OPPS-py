class Logger:
    def __init__(self):
        print("\nLogger created.")

    def __del__(self):
        print("Logger Destroyed.")

log = Logger()