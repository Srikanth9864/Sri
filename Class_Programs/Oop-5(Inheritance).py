class ConsoleLogger:
    def log(self, message):
        print(message)  # prints something in the console

class TextFileLogger:
    def __init__(self, file_object):
        self.file_object = file_object
    
    def log(self, message):
        self.file_object.write(message.strip())
        self.file_object.write("\n")
        self.file_object.flush()

# ------------------------------------------------------------------------------------
# BAD DESIGN
# ------------------------------------------------------------------------------------
class CSVLogger:
    def __init__(self, file_object):
        self.file_object = file_object
    
    def log(self, message):
        words = message.split()
        from csv import writer
        csv_writer = writer(self.file_object)
        csv_writer.writerow(words)
        self.file_object.flush()

# Inheritance (IS-A relationship)
class FilteredConsoleLogger(ConsoleLogger):
    def __init__(self, pattern):
        self.pattern = pattern
    
    # overriding the log method present in Parent class
    def log(self, message):
        if self.pattern in message:     # adding extra functionality (filtering the messages)
            super().log(message)    # reusing the existing functionality of parent class

class FilteredTextFileLogger(TextFileLogger):
    def __init__(self, pattern, file_object):
        self.pattern = pattern
        super().__init__(file_object)
    
    def log(self, message):
        if self.pattern in message:
            super().log(message)

class FilteredCSVLogger(CSVLogger):
    def __init__(self, pattern, file_object):
        self.pattern = pattern
        super().__init__(file_object)
    
    def log(self, message):
        if self.pattern in message:
            super().log(message)

class FilteredLogger:
    def __init__(self, pattern):
        self.pattern = pattern
    
    def log(self, message):
        if self.pattern in message:
            super().log(message)
# ------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------
# USING MULTIPLE INHERITANCE
# ------------------------------------------------------------------------------------
class FilteredConsoleLogger(FilteredLogger, ConsoleLogger):
    def __init__(self, pattern):
        FilteredLogger.__init__(self, pattern)

class FilteredTextFileLogger(FilteredLogger, TextFileLogger):
    def __init__(self, pattern, file_object):
        FilteredLogger.__init__(self, pattern)
        TextFileLogger.__init__(self, file_object)

class FilteredCSVLogger(FilteredLogger, CSVLogger):
    def __init__(self, pattern, file_object):
        FilteredLogger.__init__(self, pattern)
        CSVLogger.__init__(self, file_object)
# ------------------------------------------------------------------------------------
# Composition (HAS-A relationship)
class FilteredLogger:
    def __init__(self, pattern, logger_type):
        self.pattern = pattern
        self.logger_type = logger_type
    # Polymorphic behavior or it is also called as Duck Typing    
    def log(self, message):
        if self.pattern in message:
            self.logger_type.log(message)

with open('./data_files/sample.log') as f:
    with open("events.csv", "w") as fw:
        text_logger = TextFileLogger(fw)
        logger = FilteredLogger("INFO", text_logger)
        for line in f:
            logger.log(line)
# ------------------------------------------------------------------------------------