import json
import logging

'''
Created on Oct 17, 2018
@author: Surendra
'''


class JsonReaderTest:

    def __init__(self, file_path):
        self.filePath = file_path


    def getData(self):
        try:
            json.loads(open(self.filePath).read())
        except Exception as e:
            logging.exception("Got Exception : ", e)


if(__name__=="__main__"):
    json_parser = JsonReaderTest("sdfsd")
    json_parser.getData()