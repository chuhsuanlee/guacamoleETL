# -*- coding: utf-8 -*-
import guacamoleETL


if __name__ == "__main__":
    guacamoleETL.load()
    result = guacamoleETL.transform()
    print (result)
