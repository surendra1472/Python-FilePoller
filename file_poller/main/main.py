import logging
import os

from file_poller.data.constants import LOG_FILE_PATH

'''
Created on Oct 17, 2018
@author: Surendra
'''


class Main:

    def __init__(self):
        self.__configLog__()
        logging.info("Starting FilePoller")

    def __configLog__(self):
        logging.basicConfig(filename=LOG_FILE_PATH, level=logging.DEBUG)


    def sayHello(self):
        print("Hello World")


if(__name__=="__main__"):
    main = Main()
    main.sayHello()
