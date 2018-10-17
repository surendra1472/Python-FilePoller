import logging
import os

'''
Created on Oct 17, 2018
@author: Surendra
'''


class MainTest:

    def __init__(self):
        print("Je;;p")


    def __configLog(self):
        filename = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'file_poller.log')
        logging.basicConfig(filename=filename, level=logging.DEBUG)
        logging.debug('This message should go to the log file')
        logging.info('So should this')
        logging.warning('And this, too')

    def sayHello(self):
        print("Hello World")


if(__name__=="__main__"):
    main = MainTest()
    main.sayHello()
