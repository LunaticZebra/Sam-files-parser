import re


class SamReader:

    def __init__(self, filename, chromosome, start, stop):
        self.filename = filename
        self.chromosome = str(chromosome)
        self.start = start
        self.stop = stop
        self.sam_records = []

    def check_line(self, line):
        line_split = re.split("\t", line)
        if line_split[2] == self.chromosome:
            position = int(line_split[3])
            if self.start <= position <= self.stop:
                return True
            return False
        return False

    def read_file(self):
        with open(self.filename) as file:
            for line in file:
                if self.check_line(line):
                    self.sam_records.append(line)
                    print(line)

    def show_lines(self):
        for record in self.sam_records:
            print(record)

    def save_file(self):
        with open("result.sam", "w") as file:
            for record in self.sam_records:
                file.write(record)


if __name__ == "__main__":
    sr = SamReader("test.sam", 1, 51, 206)
    sr.read_file()
    sr.save_file()
