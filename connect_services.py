import ansys.dynamicreporting.core as adr
import os
from pathlib import Path


if "WSL_DISTRO_NAME" in os.environ:
  # Running in WSL
  db_dir = Path("/mnt/c/Users/rbiswas/Development/pydr-example/example_db_docker")
else:
  # Native Windows or Linux
  db_dir = Path.home() / "Development" / "adr-playground" / "new_db_docker"

print(str(db_dir))

adr_service = adr.Service(ansys_installation=r"docker", db_directory=str(db_dir))
session_guid = adr_service.start(create_db=True)


adr_service.stop()