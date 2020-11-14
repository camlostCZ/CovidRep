"""
Covid-19 Dataset Splitter
"""

import logging
import sys

from src.covid19 import DataSplitterApp


# Path to source dataset
PATH_DATASET = "./data/obec.csv"

# Path to output directory
PATH_DATADIR = "./data"

# Log file path
PATH_LOG = "./log/c19splitdata.log"


try:
    logging.basicConfig(
        filename=PATH_LOG,
        format="%(asctime)s %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG)
    logging.info("Started.")

    app = DataSplitterApp(
        data_path=PATH_DATASET,
        out_dir=PATH_DATADIR)
    app.run()

    logging.info("Finished.")
except KeyboardInterrupt:
    print("Terminated by user. Exiting.", file=sys.stderr)
