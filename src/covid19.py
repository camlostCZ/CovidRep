"""
CZ0633-
"""

import csv
import datetime
import logging
import pathlib
import sys

from typing import Dict


class DataSplitterApp:
    """
    Main application class.

    Attributes:
        history: Number of days to include in output.

    Methods:
        split_datafile: Split source CSV into files - one per city.
        run: Execute the application.
    """

    def __init__(self, history=31) -> None:
        """
        Constructor.

        Args:
            history: Number of days to include in output.
        """

        self.history = history


    def split_datafile(self, data_path: str, out_dir: str) -> None:
        """
        Split CSV file into smaller ones - one per city.
        Only records younger then `history` days are included.
        Output files will be stored in `out_dir`.

        Args:
            data_path: Path to source CSV file.
            out_dir: Path to output directory.
        """

        now = datetime.datetime.now()
        try:
            with open(data_path, "r", encoding="utf8", newline="") as datafile:
                reader = csv.DictReader(datafile, delimiter=";")
                row_count = 0
                for row in reader:
                    row_count += 1
                    row_date = datetime.datetime.strptime(row["datum"], "%Y-%m-%d")
                    delta = now - row_date
                    if delta.days < self.history:
                        self._save_datarow(row, out_dir)
                logging.info("Number of rows processed: %d", row_count)
        except FileNotFoundError:
            logging.error("Unabled to open '%s'.", data_path)
            print(f"Unable to open '{data_path}'.", file=sys.stderr)


    def _save_datarow(self, datarow: Dict[str, str], out_dir: str) -> None:
        """
        Save data row to a CSV file.

        Args:
            datarow: A dictionary of columns and their values (CSV row).
            out_dir: Output directory.
        """

        filename = f"{datarow['okres_kod']}-{datarow['obec_nazev']}.csv".replace("/", "_")
        path = pathlib.Path(out_dir) / filename
        with open(path, mode="a", encoding="utf8") as outfile:
            writer = csv.DictWriter(
                outfile,
                delimiter=",",
                fieldnames=["datum", "obec_kod", "obec_nazev",
                    "nove_pripady", "aktualne_nemocnych"],
                extrasaction="ignore")
            writer.writerow(datarow)


    def run(self, data_path: str, out_dir: str) -> None:
        """
        Run the splitting procedure.

        Args:
            data_path: Path to source CSV file.
            out_dir: Path to output directory.
        """

        logging.debug("Executed with the following params:")
        logging.debug("  data_path: %s", data_path)
        logging.debug("  out_dir: %s", out_dir)
        self.split_datafile(data_path, out_dir)
