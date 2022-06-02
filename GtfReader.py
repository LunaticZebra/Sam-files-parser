import re


class GtfReader:

    def __init__(self):
        self.gtf_records = {}
        self.filepath = ""

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
            gtf_record = {"gene_id": gene_id, "gene_name": gene_name, "chromosome": line[0],
                          "start": line[3], "stop": line[4]}
        else:
            gtf_record = {}
        return gtf_record

    def create_dict(self):
        with open(self.filepath) as file:
            for line in file:
                if "#" in line:
                    continue
                line_split = re.split("\t", line)
                gtf_record = self.extract_record(line_split)
                if len(gtf_record) > 0:
                    self.gtf_records[gtf_record['gene_id']] = gtf_record

        return self.gtf_records

    def set_filepath(self, filepath):
        self.filepath = filepath
