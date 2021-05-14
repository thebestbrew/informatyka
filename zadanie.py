import geopandas
import numpy as np
import matplotlib.pyplot as plt



#TO ODPALIC NAJPIERW

gdf = geopandas.read_file('shp/PD_STAT_GRID_CELL_2011.shp')

gdf = gdf.to_crs("EPSG:4326")
gdf['centroid'] = gdf.centroid
#%%

import shapely
#
xmin, ymin, xmax, ymax= [13 ,48 , 25, 56]
#
n_cells=30
cell_size = (xmax-xmin)/n_cells
#
grid_cells = []

for x0 in np.arange(xmin, xmax+cell_size, cell_size ):
    for y0 in np.arange(ymin, ymax+cell_size, cell_size):
        # bounds
        x1 = x0-cell_size
        y1 = y0+cell_size
        grid_cells.append( shapely.geometry.box(x0, y0, x1, y1) )
cell = geopandas.GeoDataFrame(grid_cells, columns=['geometry'])


ax = gdf.plot(markersize=.1, figsize=(12, 8), column='TOT', cmap='jet')

plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("off")


merged = geopandas.sjoin(gdf, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index, 'TOT'] = dissolve.TOT.values
ax = cell.plot(column='TOT', figsize=(12, 8), cmap='viridis', vmax=700000, edgecolor="grey", legend = True)
plt.autoscale(False)
ax.set_axis_off()
plt.axis('equal');
plt.title('liczba ludności w siatce')

#gdf.plot('TOT', legend = True)

#%%



gdf_w = geopandas.read_file('shp/Województwa.shp')
gdf_w = gdf_w.to_crs('EPSG:4326')

#
cell = geopandas.GeoDataFrame(gdf_w, columns=['geometry'])


ax = gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_0_14', cmap='jet')

plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("off")


merged = geopandas.sjoin(gdf, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index, 'TOT_0_14'] = dissolve.TOT_0_14.values
ax = cell.plot(column='TOT_0_14', figsize=(12, 8), cmap='viridis', vmax=700000, edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_off()
plt.axis('equal');
plt.title('liczba ludności w województwach w wieku 0-14')


#%%
gdf_w = geopandas.read_file('shp/Województwa.shp')
gdf_w = gdf_w.to_crs('EPSG:4326')

#
cell = geopandas.GeoDataFrame(gdf_w, columns=['geometry'])


ax = gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_15_64', cmap='jet')

plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("off")


merged = geopandas.sjoin(gdf, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index, 'TOT_15_64'] = dissolve.TOT_15_64.values
ax = cell.plot(column='TOT_15_64', figsize=(12, 8), cmap='viridis', vmax=700000, edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_off()
plt.axis('equal');
plt.title('liczba ludności w województwach w wieku 15-64')


#%%
gdf_w = geopandas.read_file('shp/Województwa.shp')
gdf_w = gdf_w.to_crs('EPSG:4326')

#
cell = geopandas.GeoDataFrame(gdf_w, columns=['geometry'])


ax = gdf.plot(markersize=.1, figsize=(12, 8), column='TOT_65__', cmap='jet')

plt.autoscale(False)
cell.plot(ax=ax, facecolor="none", edgecolor='grey')
ax.axis("off")


merged = geopandas.sjoin(gdf, cell, how='left', op='within')
dissolve = merged.dissolve(by="index_right", aggfunc="sum")
cell.loc[dissolve.index, 'TOT_65__'] = dissolve.TOT_65__.values
ax = cell.plot(column='TOT_65__', figsize=(12, 8), cmap='viridis', vmax=700000, edgecolor="grey", legend = True)
plt.autoscale(True)
ax.set_axis_off()
plt.axis('equal');
plt.title('liczba ludności w województwach w wieku >65')