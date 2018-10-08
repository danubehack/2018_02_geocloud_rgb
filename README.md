# Geocloud RGB for SK
authors: Jakub Kocica, Tomas Kliment
## Motivation
- test data, service and tools provided by ONDA DIAS provider
- create a cloud free mosaic dataset from S2MSI2A products

## Target user groups
- Future ONDA DIAS platform users
- Big data managers
- Big data user products creators 

## Methodology
- Product location selection using ONDA Catalog API
- Data preparations for further processing (GDAL tools)
- Tiles selection for a cloudfree composite
- Final Virtual Raster generation
- Publication

## Results
### Overal
- script to query ONDA catalogue API and return paths to BAND files defined by user (e.g. B2,B3,B4)
- "cloudfree" RGB composite for Slovakia

### Copernicus data and platforms utilization
- ONDA data storage for S2MSI2A
- ONDA VPS hardware
- ONDA Catalogue API

## Experienced problems
- Ran out of "project" space during the dataset preparation (gdal_merge)
- Perofrmance issues in browsing data in ENS mounted in VPS
