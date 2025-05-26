import ansys.dynamicreporting.core as adr

ansys_loc = r"C:\Program Files\ANSYS Inc\v251"
db_dir = r"C:\Users\rbiswas\Development\pydr-example\example_db_queries"
adr_service = adr.Service(ansys_installation=ansys_loc, db_directory=db_dir)
adr_service.start(create_db=True)

for i in range(100):
    if i % 3 == 0:
        my_text = adr_service.create_item(obj_name=f"Name {str(i % 20)}", source="Application X")
    elif i % 3 == 1:
        my_text = adr_service.create_item(obj_name=f"Name {str(i % 20)}", source="Application Y")
    elif i % 3 == 2:
        my_text = adr_service.create_item(obj_name=f"Name {str(i % 20)}", source="Application Z")
    my_text.item_text = "Any text. Does not matter the actual payload"
    if i % 4 == 0:
        my_text.set_tags("var=pressure")
    elif i % 4 == 1:
        my_text.set_tags("var=energy")
    elif i % 4 == 2:
        my_text.set_tags("var=temperature")
    elif i % 4 == 3:
        my_text.set_tags("var=vorticity")
    my_text.add_tag(tag="dp", value=str(i % 50))

all_items = adr_service.query()
test_one = len(all_items) == 100
app_x = adr_service.query(item_filter="A|i_src|cont|Application X")
app_y = adr_service.query(item_filter="A|i_src|cont|Application Y")
app_z = adr_service.query(item_filter="A|i_src|cont|Application Z")
test_two = len(app_x) == 34
test_three = len(app_y) == len(app_z) == 33
name_0 = adr_service.query(item_filter="A|i_name|cont|Name 0")
name_11 = adr_service.query(item_filter="A|i_name|cont|Name 11")
name_7 = adr_service.query(item_filter="A|i_name|cont|Name 7")
test_four = len(name_7) == len(name_0) == len(name_11) == 5
dp0_items = adr_service.query(item_filter="A|i_tags|cont|dp=0")
dp10_items = adr_service.query(item_filter="A|i_tags|cont|dp=10")
dp33_items = adr_service.query(item_filter="A|i_tags|cont|dp=33")
test_five = len(dp0_items) == len(dp10_items) == len(dp33_items) == 2

adr_service.stop()