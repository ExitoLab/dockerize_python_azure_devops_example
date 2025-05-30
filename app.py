from flask import Flask

class Greeting:
    def __init__(self, message="Hello, Cloud Summit!"):
        self._message = message

    # Getter method
    def get_message(self):
        return self._message

    # Setter method
    def set_message(self, message):
        self._message = message

class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.greeting = Greeting()

        # Define a route to fetch the greeting message
        @self.app.route('/')
        def hello_world():
            return self.greeting.get_message()

        # Define a route to update the greeting message
        @self.app.route('/update/<message>', methods=['GET', 'POST'])
        def update_message(message):
            self.greeting.set_message(message)
            return f"Greeting updated to: {message}"

# Create the app instance
app_instance = App()
app = app_instance.app

# This makes the app importable by a WSGI server
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
