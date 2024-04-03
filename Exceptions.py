class Platform_Error(Exception):
    def __init__(self, message: str):
        super().__init__(f"An error occured when loading the chosen platform - {message}")

class No_STOP_Error(Exception):
    def __init__(self):
        super().__init__("No STOP provided.")

class Dont_Steal(Exception):
    def __init__(self):
        super().__init__("Please do not steal my code. seriously. Don't.")