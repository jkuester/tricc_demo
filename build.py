# pip install tricc_oo lxml html2text pydantic babel xlsxwriter pandas polib StrEnum fhir.resources antlr4-python3-runtime antlr-ast
from tricc_oo.strategies.input.drawio import DrawioStrategy
from tricc_oo.strategies.output.xls_form import XLSFormStrategy
from tricc_oo.strategies.output.xlsform_cdss import XLSFormCDSSStrategy
from tricc_oo.strategies.output.xlsform_cht import XLSFormCHTStrategy
from tricc_oo.strategies.output.xlsform_cht_hf import XLSFormCHTHFStrategy
from tricc_oo.models.lang import SingletonLangClass
import os
import logging

# logging.basicConfig(
#    level=logging.INFO,
#    format="%(asctime)s - %(levelname)s - %(message)s",
#    handlers=[
#        logging.StreamHandler(),
#    ],
# )


class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = (
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    )

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


# logger = logging.getLogger("default")


# set up logging to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
console.setFormatter(CustomFormatter())
# add the handler to the root logger
logging.getLogger("default").addHandler(console)


langs = SingletonLangClass()
in_filepath = "./L2"
file_content = []
files = []
if os.path.isdir(in_filepath):
    files = [
        os.path.join(in_filepath, f)
        for f in os.listdir(in_filepath)
        if f.endswith(".drawio")
    ]
elif os.path.isfile(in_filepath) and in_filepath.endswith(".drawio"):
    files = [in_filepath]

for f in files:
    print(f)
    with open(f, "r", encoding="utf8") as s:
        file_content.append(s.read())
if not file_content:
    print(
        f"{in_filepath} is neither a drawio file nor a directory containing drawio files"
    )
    exit(-1)
input_strategy = DrawioStrategy(file_content)
media_path = os.path.join("./L3", "media-tmp")
project = input_strategy.execute(file_content, media_path)
# Strategy can be changed here
output_strategy = XLSFormCHTHFStrategy(project, "./L3")
# start_page, pages, images = input_strategy.execute(file_content, media_path)
output = output_strategy.execute()
