import re


class SamReader:

    def __init__(self):
        self.chromosome = ""
        self.start = -1
        self.stop = -1
        self.sam_records = []
        self.gene_list = []
        self.chromosome_found = False
        self.stop_reading = False
        self.filepath = ""
        self.different_file = True

    def set_genes(self, genes):
        self.gene_list = genes

    def __set_gene(self, gene):
        self.chromosome = gene["chromosome"]
        self.start = int(gene["start"])
        self.stop = int(gene["stop"])

    def check_line(self, line):
        line_split = re.split("\t", line)
        if "@" in line_split[0] and self.different_file:
            return True
        self.different_file = False
        if line_split[2] == self.chromosome:
            self.chromosome_found = True
            position = int(line_split[3])
            if self.start <= position <= self.stop:
                return True
            return False
        elif self.chromosome_found:
            self.stop_reading = True
        return False

    def __read_file(self):
        with open(self.filepath) as file:
            for line in file:
                if self.check_line(line):
                    self.sam_records.append(line)
                elif self.stop_reading:
                    break

    def read_file(self):
        for gene in self.gene_list:
            self.__set_gene(gene)
            self.__read_file()
            self.chromosome_found = False
            self.stop_reading = False

    def save_file(self, path):
        with open(path, "w") as file:
            for record in self.sam_records:
                file.write(record)

    def clear(self):
        self.sam_records = []
        self.chromosome_found = False
        self.stop_reading = False
        self.filepath = ""
        self.different_file = True

    def set_filepath(self, filepath):
        self.filepath = filepath
