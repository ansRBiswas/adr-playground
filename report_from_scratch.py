import ansys.dynamicreporting.core as adr
import numpy as np

ansys_loc = r"C:\Program Files\ANSYS Inc\v251"
db_dir = r"C:\Users\rbiswas\Development\pydr-example\example_db_report"
port = 8080
adr_service = adr.Service(ansys_installation=ansys_loc, db_directory=db_dir, port=port)
session_guid = adr_service.start(create_db=True)

adr_service.connect(url=f"http://localhost:{port}")
server = adr_service.serverobj

if server is None:
    raise RuntimeError("Failed to connect to the Dynamic Reporting server.")

template_003 = server.create_template(
    name="Solution Analysis from Multiphysics simulation",
    parent=None,
    report_type="Layout:basic"
)
template_003.params = (
    '{"HTML": "<h1>Solution Report</h1><p>hello!</p>"}'
)
template_003.set_filter("A|i_tags|cont|solution=solverA;")
server.put_objects(template_003)

template_011 = server.create_template(
    name="Project Details",
    parent=template_003,
    report_type="Layout:basic"
)
template_011.params = (
    '{"TOCitems": 1, "HTML": "<h2>Project Details</h2>", "properties": {"justification": "left"}}'
)
template_011.set_filter("A|i_type|cont|html,string;A|i_tags|cont|text=project_details;")
server.put_objects(template_011)
server.put_objects(template_003)

template_000 = server.create_template(name="TOC", parent=template_003, report_type="Layout:toc")
template_000.params = '{"TOCitems": 1, "HTML": "<h2>Table of Contents</h2>"}'
template_000.set_filter("A|i_name|eq|__NonexistantName__;")
server.put_objects(template_000)
server.put_objects(template_003)

template_004 = server.create_template(
    name="TOC Figures", parent=template_003, report_type="Layout:toc"
)
template_004.params = (
    '{"TOCitems": 0, "TOCfigures": 1, "HTML": "<h2>List of Figures</h2>", "TOCtables": 0}'
)
template_004.set_filter("A|i_name|eq|__NonexistantName__;")
server.put_objects(template_004)
server.put_objects(template_003)

template_014 = server.create_template(
    name="Introduction", parent=template_003, report_type="Layout:panel"
)
template_014.params = '{"TOCitems": 1, "HTML": "<h2>Introduction</h2>", "properties": {"TOCItem": "1", "TOCLevel": "0"}}'
template_014.set_filter("A|i_tags|cont|section=intro;")
server.put_objects(template_014)
server.put_objects(template_003)

template_015 = server.create_template(name="text", parent=template_014, report_type="Layout:basic")
template_015.params = '{"properties": {"TOCItem": "0", "justification": "left"}}'
template_015.set_filter("A|i_type|cont|html,string;")
server.put_objects(template_015)
server.put_objects(template_014)
server.put_objects(template_003)

template_016 = server.create_template(name="img", parent=template_014, report_type="Layout:basic")
template_016.params = (
    '{"properties": {"TOCName": "Multiphysics Workflow", "TOCItem": "", "TOCFigure": "1"}}'
)
template_016.set_filter("A|i_type|cont|image;")
server.put_objects(template_016)
server.put_objects(template_014)
server.put_objects(template_003)

template_005 = server.create_template(
    name="CAD Model Summary", parent=template_003, report_type="Layout:panel"
)
template_005.params = '{"TOCitems": 1, "HTML": "<h2>CAD Model Summary</h2>", "properties": {"TOCItem": "1", "TOCLevel": "0"}}'
template_005.set_filter("A|i_tags|cont|section=cad_summary;")
server.put_objects(template_005)
server.put_objects(template_003)

template_010 = server.create_template(
    name="Summary of the Design Analysis", parent=template_005, report_type="Layout:basic"
)
template_010.params = (
    '{"HTML": "<h3>Summary of the Design Analysis</h3>", "properties": {"TOCLevel": "1"}}'
)
server.put_objects(template_010)
server.put_objects(template_005)
server.put_objects(template_003)

template_018 = server.create_template(
    name="table_params", parent=template_010, report_type="Layout:basic"
)
template_018.params = '{"properties": {"TOCItem": "2"}}'
template_018.set_filter("A|i_type|cont|table;")
server.put_objects(template_018)
server.put_objects(template_010)
server.put_objects(template_005)
server.put_objects(template_003)

template_017 = server.create_template(name="img", parent=template_010, report_type="Layout:basic")
template_017.params = (
    '{"properties": {"TOCItem": "0", "TOCName": "CAD Configuration", "TOCFigure": "1"}}'
)
template_017.set_filter("A|i_type|cont|image;")
server.put_objects(template_017)
server.put_objects(template_010)
server.put_objects(template_005)
server.put_objects(template_003)

template_006 = server.create_template(
    name="Preliminary Analysis Summary", parent=template_003, report_type="Layout:panel"
)
template_006.params = '{"TOCitems": 1, "HTML": "<h2>Preliminary Analysis Summary</h2>", "properties": {"TOCItem": "1", "TOCLevel": "0"}}'
template_006.set_filter("A|i_tags|cont|section=preliminar_summary;")
server.put_objects(template_006)
server.put_objects(template_003)

template_012 = server.create_template(
    name="Results Summary for Preliminary Analysis", parent=template_006, report_type="Layout:basic"
)
template_012.params = (
    '{"HTML": "<h3>Result summary for Preliminar Analysis</h3>", "properties": {"TOCLevel": "1"}}'
)
server.put_objects(template_012)
server.put_objects(template_006)
server.put_objects(template_003)

template_019 = server.create_template(name="img", parent=template_012, report_type="Layout:basic")
template_019.params = (
    '{"properties": {"TOCItem": "0", "TOCName": "Discovery CAD", "TOCFigure": "1"}}'
)
template_019.set_filter("A|i_type|cont|image;")
server.put_objects(template_019)
server.put_objects(template_012)
server.put_objects(template_006)
server.put_objects(template_003)

template_002 = server.create_template(
    name="table_params", parent=template_012, report_type="Layout:basic"
)
template_002.params = '{"properties": {"TOCItem": "2"}}'
template_002.set_filter("A|i_type|cont|table;")
server.put_objects(template_002)
server.put_objects(template_012)
server.put_objects(template_006)
server.put_objects(template_003)

template_007 = server.create_template(
    name="Detailed Analysis Summary", parent=template_003, report_type="Layout:panel"
)
template_007.params = '{"TOCitems": 1, "HTML": "<h2>Detailedy Analysis Summary</h2>\\nDetailed analysis constitutes detailed CFD (Computational Fluid Dynamics) analysis workflow with fluid solver and required data is transferred back to the CAD calibration.", "properties": {"TOCItem": "1", "TOCLevel": "0"}}'
template_007.set_filter("A|i_tags|cont|section=detailed_summary;")
server.put_objects(template_007)
server.put_objects(template_003)

template_020 = server.create_template(name="img", parent=template_007, report_type="Layout:basic")
template_020.params = '{"properties": {"TOCItem": "0", "TOCName": "Mesh Review", "TOCFigure": "1"}}'
template_020.set_filter("A|i_type|cont|image;")
server.put_objects(template_020)
server.put_objects(template_007)
server.put_objects(template_003)

template_013 = server.create_template(
    name="Mesh Summary", parent=template_007, report_type="Layout:basic"
)
template_013.params = (
    '{"properties": {"TOCItem": "1", "TOCLevel": "1"}, "HTML": "<h3>Mesh Summary</h3>"}'
)
template_013.set_filter("A|i_type|cont|table;A|i_tags|cont|table=meshsummary;")
server.put_objects(template_013)
server.put_objects(template_007)
server.put_objects(template_003)

template_021 = server.create_template(
    name="Results Summary of Detailed Analysis", parent=template_007, report_type="Layout:basic"
)
template_021.params = '{"properties": {"TOCItem": "1", "TOCLevel": "1"}, "HTML": "<h3>Results Summary of Detailed Analysis</h3>", "column_count": 1, "column_widths": [1.0]}'
template_021.set_filter("A|i_type|cont|table;A|i_tags|cont|table=results;")
server.put_objects(template_021)
server.put_objects(template_007)
server.put_objects(template_003)

template_001 = server.create_template(name="table", parent=template_021, report_type="Layout:basic")
template_001.params = '{"properties": {"TOCItem": ""}}'
template_001.set_filter("A|i_tags|cont|show=table;")
server.put_objects(template_001)
server.put_objects(template_021)
server.put_objects(template_007)
server.put_objects(template_003)

template_022 = server.create_template(name="plots", parent=template_021, report_type="Layout:basic")
template_022.params = '{"properties": {"TOCItem": "0", "plot": "line", "TOCFigure": "2", "xaxis": "0", "format": "floatdot0"}, "column_count": 2, "column_widths": [1.0, 1.0]}'
template_022.set_filter("A|i_tags|cont|show=plot;")
server.put_objects(template_022)
server.put_objects(template_021)
server.put_objects(template_007)
server.put_objects(template_003)

template_008 = server.create_template(
    name="Results & Conclusion", parent=template_003, report_type="Layout:panel"
)
template_008.params = '{"TOCitems": 1, "HTML": "<h2>Results & Conclusion</h2>", "properties": {"TOCItem": "1", "TOCLevel": "0"}}'
template_008.set_filter("A|i_tags|cont|section=results;")
server.put_objects(template_008)
server.put_objects(template_003)

template_009 = server.create_template(
    name="Results", parent=template_008, report_type="Layout:basic"
)
template_009.params = '{"properties": {"TOCItem": "1", "TOCLevel": "1"}, "HTML": "<h3>Results</h3>\\nResults are feedback for model calibrarion and detailed summary of results as below."}'
template_009.set_filter("A|i_type|cont|image;")
server.put_objects(template_009)
server.put_objects(template_008)
server.put_objects(template_003)

template_023 = server.create_template(
    name="References", parent=template_003, report_type="Layout:basic"
)
template_023.params = '{"TOCitems": 1, "HTML": "<h3>References</h3>", "properties": {"TOCItem": "1", "TOCLevel": "0", "justification": "left"}}'
template_023.set_filter("A|i_tags|cont|section=references;")
server.put_objects(template_023)
server.put_objects(template_003)

adr_service.get_list_reports()
adr_service.stop()