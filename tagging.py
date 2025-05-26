import ansys.dynamicreporting.core as adr

ansys_loc = r"C:\Program Files\ANSYS Inc\v251"
db_dir = r"C:\Users\rbiswas\Development\pydr-example\example_db_tagging"
adr_service = adr.Service(ansys_installation=ansys_loc, db_directory=db_dir)
adr_service.start(create_db=True)

my_text = adr_service.create_item(obj_name="text")
my_text.item_text = "<p style=\"font-weight: bold; font-size: 12px; color: red\">My paragraph</p>"
my_text.set_tags("var=pressure unit=Pa time=0.34")
my_text.get_tags()
my_text.add_tag(tag="dp", value="0.01")
my_text.rem_tag("time")
my_text.get_tags()

my_second_text = adr_service.create_item(obj_name="second text")
my_second_text.item_text = "<p style=\"font-weight: bold; font-size: 12px; color: green\">My second paragraph</p>"
my_second_text.set_tags("var=temperature dp=3")
my_third_text = adr_service.create_item(obj_name="third text")
my_second_text.set_tags("var=temperature dp=2")
dp3_items = adr_service.query(item_filter="A|i_tags|cont|dp=2")
for item in dp3_items:
    print(f"Item: {item.obj_name}, Tags: {item.get_tags()}")

adr_service.stop()