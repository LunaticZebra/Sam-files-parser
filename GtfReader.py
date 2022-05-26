import re
import json


class GtfReader:

    def __init__(self, filename):
        self.filename = filename
        self.gtf_records = {}

    def gtf_extract_record(self, line):
        if line[2] == "gene":
            attributes_list = re.split("; ", line[len(line) - 1])
            gene_name = ""
            for attribute in attributes_list:
                if "gene_name" in attribute:
                    gene_name = re.split(" ", attribute)[1].strip('"')
                    break

            gene_id = re.split(" ", attributes_list[0])
            gene_id = gene_id[1].strip('"')
            gtf_record = {"gene_id": gene_id, "chromosome": line[0], "start": line[3], "stop": line[4]}
            gtf_record["gene_name"] = gene_name
        else:
            gtf_record = {}
        return gtf_record

    def gtf_create_dict(self):
        with open(self.filename) as file:
            for _ in file:
                line_split = re.split("\t", file.readline())
                gtf_record = self.gtf_extract_record(line_split)
                if len(gtf_record) > 0:
                    self.gtf_records[gtf_record['gene_id']] = gtf_record
                    print(gtf_record)

    def gtf_save_to_json(self):
        json_str = json.dumps(self.gtf_records)
        with open("gtf_records.json","w") as json_file:
            json_file.write(json_str)


if __name__ == '__main__':
    fl = GtfReader("test.txt")
    fl.gtf_create_dict()
    fl.gtf_save_to_json()
