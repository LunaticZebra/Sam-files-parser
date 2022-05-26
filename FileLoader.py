import re


class FileLoader:

    def __init__(self, filename):
        self.filename = filename
        self.gtf_records = {}

    def gtf_extract_record(self, line):
        gene_id = re.split("; ", line[len(line) - 1])
        gene_id = re.split(" ", gene_id[0])
        gene_id = gene_id[1].strip('"')
        if line[2] == "gene":
            gtf_record = {"gene_id": gene_id, "start": line[3], "stop": line[4]}
        else:
            gtf_record = {}
        return gtf_record

    def gtf_reader(self):
        with open(self.filename) as file:
            for line in file:
                line = re.split("\t", file.readline())
                gtf_record = self.gtf_extract_record(line)
                if len(gtf_record) > 0:
                    self.gtf_records[gtf_record['gene_id']] = gtf_record
                    print(gtf_record)



if __name__ == '__main__':
    fl = FileLoader("test.txt")
    fl.gtf_reader()
