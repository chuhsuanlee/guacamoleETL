# -*- coding: utf-8 -*-
import guacamoleETL


if __name__ == "__main__":
    guacamoleETL.load('Challenge_me.txt')
    result = guacamoleETL.transform('Challenge_me.txt')
    print(result)
