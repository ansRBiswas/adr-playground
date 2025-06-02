from random import random as r
import numpy as np

import ansys.dynamicreporting.core as adr
from ansys.dynamicreporting.core.utils import report_utils

# find a random open port for the ADR service and define the ADR root domain
adr_port = report_utils.find_unused_ports(1)
if not adr_port:
    raise RuntimeError("No open ports found for the ADR service.")
adr_port = adr_port[0]
root = f"http://127.0.0.1:{adr_port}/"

# start an ADR server
adr_service = adr.Service(
    ansys_installation=r"C:\Program Files\Ansys Inc\251",
    db_directory=r"C:\Users\rbiswas\Development\pydr-example\example_db_embed",
    port=adr_port,
)

adr_service.start()

# select report based on the matched report name
my_report = adr_service.get_report(report_name="Top Level Report")