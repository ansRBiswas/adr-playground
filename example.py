import numpy as np
import ansys.dynamicreporting.core as adr

# point to the location of your Ansys installation
ansys_loc = r"C:\Program Files\ANSYS Inc\v251"
# point to the location of your database
# (this will be created if it does not exist)
db_dir = r"C:\Users\rbiswas\Development\pydr-example\example_db"

# initialize an ADR service
# class Service(
#     ansys_version: int = None,
#     docker_image: str = DOCKER_REPO_URL,
#     data_directory: str = None,
#     db_directory: str = None,
#     port: int = DOCKER_DEFAULT_PORT,
#     logfile: str = None,
#     ansys_installation: str | None = None
# )
adr_service = adr.Service(ansys_installation=ansys_loc, db_directory=db_dir)

# start the ADR service
# (method) def start(
#     username: str = "nexus",
#     password: str = "cei",
#     create_db: bool = False,
#     error_if_create_db_exists: bool = False,
#     exit_on_close: bool = False,
#     delete_db: bool = False
# ) -> str
adr_service.start()

# create an item in the database
# (method) def create_item(
#     obj_name: str | None = "default",
#     source: str | None = "ADR"
# ) -> Item
my_heading = adr_service.create_item(obj_name="heading")
my_heading.item_text = "<h1 style=\"color: blue\">My Heading</h1>"

my_text = adr_service.create_item(obj_name="text")
my_text.item_text = "<p style=\"font-weight: bold; font-size: 12px; color: red\">My paragraph</p>"

my_table = adr_service.create_item(obj_name="table")
my_table.table_dict["rowlbls"] = ["Row 1", "Row 2"]
my_table.item_table = np.array([["1", "2", "3", "4"], ["1", "8", "27", "64"]], dtype="|S20") # type: ignore

# render the report
# (method) def visualize_report(
#     report_name: str | None = "",
#     new_tab: bool | None = False,
#     filter: str | None = "",
#     item_filter: str | None = ""
# ) -> None
adr_service.visualize_report()

my_plot = adr_service.create_item(obj_name="plot")
my_plot.item_table = np.array([[1, 2, 3, 4, 5, 6], [1, 4, 9, 16, 25, 36]], dtype="|S20") # type: ignore
my_plot.labels_row = ["First", "Second"] # type: ignore

leaves = []
for i in range(1, 7):
    leaves.append({"key": "leaves", "name": f"leaf {i}", "value": i})
children = []
children.append({"key": "child", "name": "Boolean example", "value": True})
children.append({"key": "child", "name": "String example", "value": "Hello World"})
children.append({"key": "child", "name": "Integer example", "value": 42})
children.append({"key": "child", "name": "Float example", "value": 3.14})
children.append(
    {
        "key": "child_parent",
        "name": "a child parent",
        "value": "parents can also have values",
        "children": leaves,
        "state": "collapsed"
    }
)

tree = []
tree.append(
    {
        "key": "root",
        "name": "top level",
        "value": None,
        "children": children,
        "state": "expanded"
    }
)

my_tree = adr_service.create_item(obj_name="tree")
my_tree.item_tree = tree

adr_service.visualize_report()

# stop the ADR service
# (method) def stop() -> None
adr_service.stop()