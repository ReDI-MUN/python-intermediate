# Logging Exercises 
### Exercise 1: Basic Logging Setup
- **Objective**: Set up basic logging to log messages into a file.
- **Task**: Create a Python script that logs messages of different severity levels (INFO, WARNING, ERROR, CRITICAL) into a file called `basic_log.log`.

### Exercise 2: Log Formatting
- **Objective**: Customize the log format.
- **Task**: Modify the logger from Exercise 1 to include the timestamp, the level of the log, and the message in this format: `[TIMESTAMP] [LEVEL] - MESSAGE`.

### Exercise 3: Multiple Handlers
- **Objective**: Use multiple handlers for logging.
- **Task**: Extend the logger from Exercise 2 to also output log messages to the console (stdout), in addition to the log file.

### Exercise 4: Logging Exceptions
- **Objective**: Log exceptions in a try-except block.
- **Task**: Create a function that performs division of two numbers. Use a try-except block to catch the ZeroDivisionError and log it.

### Exercise 5: Rotating Log Files
- **Objective**: Implement log rotation.
- **Task**: Extend the logger from Exercise 3 to use a `RotatingFileHandler` that creates a new log file after reaching 1MB in size.

### Exercise 6: Advanced Filtering
- **Objective**: Use filters to control logging.
- **Task**: Create a custom filter that only logs messages containing the word "error".

### Exercise 7: Performance Analysis
- **Objective**: Analyze the performance of logging.
- **Task**: Use the `time` module to measure the time taken for logging 1000 messages with and without logging enabled. Compare the results.

Feel free to ask if you need sample solutions for any of these exercises.