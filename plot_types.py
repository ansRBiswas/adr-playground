import ansys.dynamicreporting.core as adr
import numpy as np

ansys_loc = r"C:\Program Files\ANSYS Inc\v251"
db_dir = r"C:\Users\rbiswas\Development\pydr-example\example_db_plot_types"
adr_service = adr.Service(ansys_installation=ansys_loc, db_directory=db_dir)

adr_service.start(create_db=True)

simple_table = adr_service.create_item(obj_name="Simple Table", source="Documentation")
simple_table.item_table = np.array(
    [[0, 1, 2, 3, 4], [0, 3, 6, 9, 12], [0, 1, 4, 9, 16]], dtype="|S20"
)
simple_table.labels_row = ["X", "line", "square"]

line_plot = adr_service.create_item(obj_name="Line Plot", source="Documentation")
line_plot.item_table = np.array(
    [[0, 1, 2, 3, 4], [0, 3, 6, 9, 12], [0, 1, 4, 9, 16], [0, 0.25, 2, 6.75, 16]], dtype="|S20"
)
line_plot.labels_row = ["X", "line", "square", "cube"]
line_plot.plot = "line"
line_plot.xaxis = "X"
line_plot.yaxis_format = "floatdot0"
line_plot.xaxis_format = "floatdot1"
line_plot.xtitle = "x"
line_plot.ytitle = "y = f(x)"
line_plot.visualize()

bar_plot = adr_service.create_item(obj_name="Bar Plot", source="Documentation")
bar_plot.item_table = np.array([[0, 1, 2, 3, 4], [0.3, 0.5, 0.7, 0.6, 0.3]], dtype="|S20")
bar_plot.plot = "bar"
bar_plot.labels_row = ["ics", "my variable"]
bar_plot.xaxis_format = "floatdot0"
bar_plot.yaxis_format = "floatdot2"
bar_plot.xaxis = "ics"
bar_plot.yaxis = "my variable"
bar_plot.visualize()

pie_plot = adr_service.create_item(obj_name="Pie Plot", source="Documentation")
pie_plot.item_table = np.array([[10, 20, 50, 20]], dtype="|S20")
pie_plot.plot = "pie"
pie_plot.labels_column = ["Bar", "Triangle", "Quad", "Penta"]
pie_plot.visualize()

heatmap = adr_service.create_item(obj_name="Heatmap", source="Documentation")
heatmap.item_table = np.array(
    [
        [0.00291, 0.01306, 0.02153, 0.01306, 0.00291],
        [0.01306, 0.05854, 0.09653, 0.05854, 0.01306],
        [0.02153, 0.09653, np.nan, 0.09653, 0.02153],
        [0.01306, 0.05854, 0.09653, 0.05854, 0.01306],
        [0.00291, 0.01306, 0.02153, 0.01306, 0.00291],
    ],
    dtype="|S20",
)
heatmap.plot = "heatmap"
heatmap.format = "floatdot0"
heatmap.visualize()

surface = adr_service.create_item()
# We can use the same data as we use to visualize heatmap
surface.item_table = np.array(
    [
        [0.00291, 0.01306, 0.02153, 0.01306, 0.00291],
        [0.01306, 0.05854, 0.09653, 0.05854, 0.01306],
        [0.02153, 0.09653, np.nan, 0.09653, 0.02153],
        [0.01306, 0.05854, 0.09653, 0.05854, 0.01306],
        [0.00291, 0.01306, 0.02153, 0.01306, 0.00291],
    ],
    dtype="|S20",
)
surface.plot = "3d surface"
surface.format = "floatdot0"
surface.visualize()

parallel = adr_service.create_item()
parallel.item_table = np.array(
    [
        [54.2, 12.3, 1.45e5],
        [72.3, 9.3, 4.34e5],
        [45.4, 10.8, 8.45e4],
        [67.4, 12.2, 2.56e5],
        [44.8, 13.5, 9.87e4],
    ],
    dtype="|S20",
)
parallel.labels_column = ["Temperature", "Max. Pressure", "Max. Work"]
parallel.plot = "parallel"
parallel.visualize()

histo_data = adr_service.create_item()
histo_data.item_table = np.random.normal(0, 0.1, 100)
histo_data.plot = "histogram"
histo_data.histogram_normalized = 1
histo_data.histogram_bin_size = 0.03
histo_data.visualize()

sankey_plot = adr_service.create_item()
sankey_plot.item_table = np.array(
    [
        [0, 0, 8, 2, 0, 0],
        [0, 0, 0, 4, 0, 0],
        [0, 0, 0, 0, 8, 0],
        [0, 0, 0, 0, 5, 1],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ],
    dtype="|S20",
)
sankey_plot.labels_row = ["A", "B", "C", "D", "E", "F"]
sankey_plot.labels_column = ["A", "B", "C", "D", "E", "F"]
sankey_plot.plot = "sankey"
sankey_plot.visualize()

scatter_plot_3d = adr_service.create_item()
scatter_plot_3d.item_table = np.random.uniform(1.0, 50.0, size=(6, 20))
scatter_plot_3d.labels_row = ["X1", "Y1", "Z1", "X2", "Y2", "Z2"]
scatter_plot_3d.plot = "line"
# specified the 3D scatter's line style (default is markers+lines)
scatter_plot_3d.line_style = "none"
# specified the 3D scatter's symbol (default is solid circle)
# supportive: diamond, cross, x, circle, square (open & solid)
scatter_plot_3d.xaxis = ["X1", "X2"]
scatter_plot_3d.yaxis = ["Y1", "Y2"]
scatter_plot_3d.zaxis = ["Z1", "Z2"]
scatter_plot_3d.zaxis_format = "floatdot0"
scatter_plot_3d.yaxis_format = "floatdot0"
scatter_plot_3d.xaxis_format = "floatdot1"
scatter_plot_3d.xtitle = "x"
scatter_plot_3d.ytitle = "f(x)"
scatter_plot_3d.ztitle = "f(x,y)"
# opacity
scatter_plot_3d.line_marker_opacity = 0.7
# vis
scatter_plot_3d.visualize()

polar = adr_service.create_item()
# We can use the same data as we use to visualize heatmap
polar.item_table = np.array(
    [
        ["-180", "-135", "-90", "-45", "0", "45", "90", "135", "180"],
        [8.2, 7.3, 10.6, 5.6, 5.9, 9.1, 2.4, 1.6, 4.8],
    ],
    dtype="|S20",
)
polar.plot = "polar"
polar.format = "floatdot0"
polar.xaxis = 0
polar.format_row = "str"
polar.labels_row = ["theta", "r"]
polar.visualize()

adr_service.stop()