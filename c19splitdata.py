#!/usr/bin/env python3

"""
Covid-19 Dataset Splitter
"""

import logging
import sys

from src.covid19 import DataSplitterApp


# Path to source dataset
PATH_DATASET = "./data/obec.csv"

# Path to output directory
PATH_OUTPUTDIR = "/home/camlost/public_html/Covid19_obce"

# Log file path
PATH_LOG = "./log/c19splitdata.log"


try:
    logging.basicConfig(
        filename=PATH_LOG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO)
    logging.info("Started.")

    app = DataSplitterApp(100)
    app.run(PATH_DATASET, PATH_OUTPUTDIR)

    logging.info("Finished.")
except KeyboardInterrupt:
    print("Terminated by user. Exiting.", file=sys.stderr)
