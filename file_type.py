import GtfReader
import SamReader


def get_reader(filename):
    if ".gtf" in filename:
        return GtfReader
    elif ".sam" in filename:
        return SamReader
    else:
        raise TypeError("Expected .gtf or .sam file")
