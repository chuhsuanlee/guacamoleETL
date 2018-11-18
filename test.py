# -*- coding: utf-8 -*-
import guacamoleETL


if __name__ == "__main__":
    guacamoleETL.load('./guacamoleETL/raw_data/Challenge_me.txt')
    result = guacamoleETL.transform('./guacamoleETL/raw_data/Challenge_me.txt')
    print(result)
