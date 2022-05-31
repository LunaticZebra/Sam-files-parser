import re
import FileReader
import time

class SamReader(FileReader.FileReader):

    def __init__(self, chromosome, start, stop):
        super(SamReader, self).__init__()
        self.chromosome = str(chromosome)
        self.start = start
        self.stop = stop
        self.sam_records = []

    def check_line(self, line):
        line_split = re.split("\t", line)
        if "@" in line_split[0]:
            return True
        if line_split[2] == self.chromosome:
            position = int(line_split[3])
            if self.start <= position <= self.stop:
                return True
            return False
        return False

    def read_file(self):
        with open(self.filepath) as file:
            for line in file:
                if self.check_line(line):
                    self.sam_records.append(line)

    def show_lines(self):
        for record in self.sam_records:
            print(record)

    def save_file(self):
        with open("result.sam", "w") as file:
            for record in self.sam_records:
                file.write(record)


if __name__ == "__main__":
    start_time = time.time()
    sr = SamReader(1, 10942648, 10944727)
    sr.set_filepath("C:\\Users\\macie\\OneDrive\\Desktop\\Python-app_resources\\APIT-20-1.sam")
    sr.read_file()
    sr.save_file()
    print(time.time()-start_time)
