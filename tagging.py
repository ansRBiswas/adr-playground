import ansys.dynamicreporting.core as adr

ansys_loc = r"C:\Program Files\ANSYS Inc\v251"
db_dir = r"C:\Users\rbiswas\Development\pydr-example\example_db_tagging"
adr_service = adr.Service(ansys_installation=ansys_loc, db_directory=db_dir)
adr_service.start(create_db=True)
adr_service.stop()