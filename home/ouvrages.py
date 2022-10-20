import datetime
import logging
from typing import NamedTuple


class OuvrageFile(NamedTuple):
    name: str
    url: str
    date: datetime.date

    @classmethod
    def from_json(cls, name, json: dict):
        if not json:
            return None
        date = datetime.datetime.fromisoformat(
            # Le problème du Z est corrigé dans Python 3.11 : https://docs.python.org/3.11/whatsnew/3.11.html#datetime
            json["date"].replace("Z", "+00:00")
        ).date()
        return cls(name, json["url"], date)


class Ouvrage(NamedTuple):
    name: str
    document: OuvrageFile
    vignette: OuvrageFile | None = None
    metadata: OuvrageFile | None = None

    @classmethod
    def from_json(cls, name, json: dict):
        if "document.pdf" not in json:
            return None

        document = OuvrageFile.from_json("document.pdf", json["document.pdf"])
        vignette = OuvrageFile.from_json("vignette.jpg", json.get("vignette.jpg"))
        metadata_file_instances = [
            (x, y)
            for x, y in json.items()
            if x.startswith("OUVNAUT_") and x.endswith(".xml")
        ]
        metadata = None
        if len(metadata_file_instances) == 1:
            metadata_name, metadata_json = metadata_file_instances[0]
            metadata = OuvrageFile.from_json(metadata_name, metadata_json)
        else:
            logging.warning("No metadata found for ouvrage named `%s`", name)
        return cls(name, document, vignette, metadata)

    @property
    def date(self):
        return self.document.date
