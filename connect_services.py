import ansys.dynamicreporting.core as adr

db_dir = r"C:\Users\rbiswas\Development\adr-playground\new_db_docker"
adr_service = adr.Service(ansys_installation=r"C:\Program Files\ANSYS Inc\v251", db_directory=db_dir)
session_guid = adr_service.start(create_db=True)

adr_service.stop()