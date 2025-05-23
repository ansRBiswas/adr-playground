import ansys.dynamicreporting.core as adr

db_dir = r"C:\Users\rbiswas\Development\adr-playground\new_db_docker"
adr_service = adr.Service(db_directory=db_dir)
session_guid = adr_service.start(create_db=True)

adr_service.stop()