# You have to extract a portion of the file name as follows:

# Assume it will start with date represented as long number
# Followed by an underscore
# You'll have then a filename with an extension
# it will always have an extra extension at the end


import re

class FileNameExtractor:
    @staticmethod
    def extract_file_name(dirty_file_name):
        return re.findall(r'(\d+_)(.+)\.(\w+|\d+)', dirty_file_name)[0][1]
    