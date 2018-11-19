# -*- coding: utf-8 -*-
import guacamoleETL

dataFile = 'Challenge_me.txt'

if __name__ == "__main__":
    guacamoleETL.load(dataFile)
    result = guacamoleETL.transform(dataFile)
    print(result)
