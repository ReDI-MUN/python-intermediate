class FileHandler:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        with open(self.filename, 'r') as file:
            return file.read()

    def write_file(self, content):
        with open(self.filename, 'w') as file:
            file.write(content)

    def append_file(self, content):
        with open(self.filename, 'a') as file:
            file.write(content)


class FileStatistics(FileHandler):
    def count_lines(self):
        content = self.read_file()
        return len(content.split('\n'))

    def count_words(self):
        content = self.read_file()
        return len(content.split(' '))


def main():
    # Initialize file with some content
    handler = FileHandler("example.txt")
    handler.write_file("Line 1\nLine 2\nLine 3")

    # Perform read and append operations
    print(f"Initial Content:\n{handler.read_file()}")

    handler.append_file("Line 4")
    print(f"Content after appending 'Line 4':\n{handler.read_file()}")

    # File statistics
    stats = FileStatistics("example.txt")
    print(f"Number of lines: {stats.count_lines()}")
    print(f"Number of words: {stats.count_words()}")


if __name__ == "__main__":
    main()
