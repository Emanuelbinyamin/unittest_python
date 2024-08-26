# Chat Server and Client

Welcome to the Chat Server and Client project!
 This application provides a basic chat system implemented in Python using sockets.
 The server handles multiple client connections, broadcasts messages to all clients, and manages client disconnections.
 The client connects to the server, sends and receives messages, and allows users to participate in real-time chat.

## 📦 Overview

- **Server**: Manages client connections, broadcasts messages, and handles disconnections.
- **Client**: Connects to the server, sends and receives messages, and handles user input.

## 🚀 Getting Started

### Requirements

- Python 3.x

### Running the Server

1. **Start the Server**: Run the server script to initialize and start listening for incoming connections.
2. **View Logs**: The server will display logs of connected clients and incoming messages.

### Running the Client

1. **Run the Client**: Execute the client script to connect to the server.
2. **Enter Nickname**: Provide a nickname when prompted.
3. **Start Chatting**: Send and receive messages in real-time.

## 🧩 Function Details

### `adds(num=0)`

This function performs a basic addition operation with input validation.

**Parameters:**
- `num`: An optional parameter (default is 0) that is the input to be processed.

**Returns:**
- An integer result of `num + 5` if `num` is a valid number.
- A string message `"please enter a number"` if `num` is `None` or an empty string.
- A `ValueError` if `num` cannot be converted to an integer.

**Example:**

```python
print(adds(6))  # Output: 11
print(adds("10"))  # Output: 15
print(adds("asdfg"))  # Output: ValueError
print(adds(None))  # Output: please enter a number
print(adds(""))  # Output: please enter a number
```
**🧪 Testing**

The project includes unit tests to verify the functionality of the `adds` function.

### Test Cases

- **`test_A`**: Verifies that `adds(10)` returns `15`.
- **`test_B`**: Checks that `adds("asdfg")` returns a `ValueError`.
- **`test_C`**: Confirms that `adds("10")` returns `15`.
- **`test_D`**: Ensures that `adds(None)` returns `"please enter a number"`.
- **`test_E`**: Validates that `adds("")` returns `"please enter a number"`.
