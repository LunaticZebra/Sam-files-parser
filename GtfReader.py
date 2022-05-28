import re
import json
import time
import FileReader
import file_type


class GtfReader(FileReader.FileReader):

    def __init__(self):
        super(FileReader, self).__init__()
        self.gtf_records = {}

    def extract_record(self, line):
        if line[2] == "gene":
            attributes_list = re.split("; ", line[len(line) - 1])
            gene_name = ""
            for attribute in attributes_list:
                if "gene_name" in attribute:
                    gene_name = re.split(" ", attribute)[1].strip('"')
                    break

            gene_id = re.split(" ", attributes_list[0])
            gene_id = gene_id[1].strip('"')
            gtf_record = {"gene_id": gene_id, "gene_name": gene_name, "chromosome": line[0], "start": line[3], "stop": line[4]}
        else:
            gtf_record = {}
        return gtf_record

    def create_dict(self):
        with open(self.filepath) as file:
            for line in file:
                if "##" in line:
                    continue
                line_split = re.split("\t", file.readline())
                gtf_record = self.extract_record(line_split)
                if len(gtf_record) > 0:
                    self.gtf_records[gtf_record['gene_id']] = gtf_record

    def save_to_json(self):
        json_str = json.dumps(self.gtf_records)
        with open("gtf_records.json", "w") as json_file:
            json_file.write(json_str)


if __name__ == '__main__':
    start_time = time.time()
    #fl = GtfReader("gencode.v40.annotation.gtf")
    #fl.create_dict()
    #fl.save_to_json()
    #print(time.time()-start_time)
