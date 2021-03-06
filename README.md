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
- Video: https://youtu.be/JbnP5g9a2M8
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

## Sample usage
### MSIL1C
```bash
python search.py -wkt 'POLYGON((17.66543704555818 48.47776455545619,18.55258304165193 48.47776455545619,18.55258304165193 48.08846410187011,17.66543704555818 48.08846410187011,17.66543704555818 48.47776455545619))' -cloud 50 -from 2018-10-01 -to 2018-10-10 -product 'MSIL1C'
https://catalogue.onda-dias.eu/dias-catalogue/Products?$search=%22((name:*MSIL1C*) AND cloudCoverPercentage:[0 TO 50])%20AND%20((beginPosition:[2018-10-01T00:00:00.000Z%20TO%202018-10-10T23:59:00.000Z]))%20AND%20footprint:%22Intersects(POLYGON((17.66543704555818 48.47776455545619,18.55258304165193 48.47776455545619,18.55258304165193 48.08846410187011,17.66543704555818 48.08846410187011,17.66543704555818 48.47776455545619)))%22%22&$orderby=creationDate%20asc&$format=json&$skip=0&$top=10
Found 10 products. Starting the process.
Product pseudopath is /mnt/data/S2/2A/MSI/LEVEL-1C/S2MSI1C/2018/10/01/S2A_MSIL1C_20181001T230901_N0206_R101_T58KFB_20181002T002651.zip/S2A_MSIL1C_20181001T230901_N0206_R101_T58KFB_20181002T002651.SAFE
Product pseudopath is /mnt/data/S2/2A/MSI/LEVEL-1C/S2MSI1C/2018/10/01/S2A_MSIL1C_20181001T230901_N0206_R101_T59LKH_20181002T002651.zip/S2A_MSIL1C_20181001T230901_N0206_R101_T59LKH_20181002T002651.SAFE
Product pseudopath is /mnt/data/S2/2A/MSI/LEVEL-1C/S2MSI1C/2018/10/01/S2A_MSIL1C_20181001T224531_N0206_R101_T03WWR_20181002T002948.zip/S2A_MSIL1C_20181001T224531_N0206_R101_T03WWR_20181002T002948.SAFE
Product pseudopath is /mnt/data/S2/2B/MSI/LEVEL-1C/S2MSI1C/2018/10/01/S2B_MSIL1C_20181001T235259_N0206_R030_T57PYQ_20181002T011218.zip/S2B_MSIL1C_20181001T235259_N0206_R030_T57PYQ_20181002T011218.SAFE
Product pseudopath is /mnt/data/S2/2B/MSI/LEVEL-1C/S2MSI1C/2018/10/01/S2B_MSIL1C_20181001T233649_N0206_R030_T60VVN_20181002T011425.zip/S2B_MSIL1C_20181001T233649_N0206_R030_T60VVN_20181002T011425.SAFE
Product pseudopath is /mnt/data/S2/2B/MSI/LEVEL-1C/S2MSI1C/2018/10/02/S2B_MSIL1C_20181002T230529_N0206_R044_T03WWS_20181003T004834.zip/S2B_MSIL1C_20181002T230529_N0206_R044_T03WWS_20181003T004834.SAFE
Product pseudopath is /mnt/data/S2/2B/MSI/LEVEL-1C/S2MSI1C/2018/10/05/S2B_MSIL1C_20181005T095029_N0206_R079_T33UYP_20181005T133546.zip/S2B_MSIL1C_20181005T095029_N0206_R079_T33UYP_20181005T133546.SAFE
Product pseudopath is /mnt/data/S2/2B/MSI/LEVEL-1C/S2MSI1C/2018/10/05/S2B_MSIL1C_20181005T095029_N0206_R079_T33UXP_20181005T133546.zip/S2B_MSIL1C_20181005T095029_N0206_R079_T33UXP_20181005T133546.SAFE
Product pseudopath is /mnt/data/S2/2B/MSI/LEVEL-1C/S2MSI1C/2018/10/05/S2B_MSIL1C_20181005T095029_N0206_R079_T34UCU_20181005T133546.zip/S2B_MSIL1C_20181005T095029_N0206_R079_T34UCU_20181005T133546.SAFE
Product pseudopath is /mnt/data/S2/2A/MSI/LEVEL-1C/S2MSI1C/2018/10/10/S2A_MSIL1C_20181010T095031_N0206_R079_T33UYP_20181010T115600.zip/S2A_MSIL1C_20181010T095031_N0206_R079_T33UYP_20181010T115600.SAFE
```

### MSIL2A
```bash
python search.py -wkt 'POLYGON((17.66543704555818 48.47776455545619,18.55258304165193 48.47776455545619,18.55258304165193 48.08846410187011,17.66543704555818 48.08846410187011,17.66543704555818 48.47776455545619))' -cloud 50 -from 2018-10-01 -to 2018-10-10 -product 'MSIL2A'
https://catalogue.onda-dias.eu/dias-catalogue/Products?$search=%22((name:*MSIL2A*) AND cloudCoverPercentage:[0 TO 50])%20AND%20((beginPosition:[2018-10-01T00:00:00.000Z%20TO%202018-10-10T23:59:00.000Z]))%20AND%20footprint:%22Intersects(POLYGON((17.66543704555818 48.47776455545619,18.55258304165193 48.47776455545619,18.55258304165193 48.08846410187011,17.66543704555818 48.08846410187011,17.66543704555818 48.47776455545619)))%22%22&$orderby=creationDate%20asc&$format=json&$skip=0&$top=10
Found 6 products. Starting the process.
Product pseudopath is /mnt/data/S2/2B/MSI/LEVEL-2A/S2MSI2A/2018/10/05/S2B_MSIL2A_20181005T095029_N0208_R079_T33UYP_20181005T142530.zip/S2B_MSIL2A_20181005T095029_N0208_R079_T33UYP_20181005T142530.SAFE
Product pseudopath is /mnt/data/S2/2B/MSI/LEVEL-2A/S2MSI2A/2018/10/05/S2B_MSIL2A_20181005T095029_N0208_R079_T33UXP_20181005T142530.zip/S2B_MSIL2A_20181005T095029_N0208_R079_T33UXP_20181005T142530.SAFE
Product pseudopath is /mnt/data/S2/2B/MSI/LEVEL-2A/S2MSI2A/2018/10/05/S2B_MSIL2A_20181005T095029_N0208_R079_T34UCU_20181005T142530.zip/S2B_MSIL2A_20181005T095029_N0208_R079_T34UCU_20181005T142530.SAFE
Product pseudopath is /mnt/data/S2/2A/MSI/LEVEL-2A/S2MSI2A/2018/10/10/S2A_MSIL2A_20181010T095031_N0209_R079_T34UCU_20181010T122839.zip/S2A_MSIL2A_20181010T095031_N0209_R079_T34UCU_20181010T122839.SAFE
Product pseudopath is /mnt/data/S2/2A/MSI/LEVEL-2A/S2MSI2A/2018/10/10/S2A_MSIL2A_20181010T095031_N0209_R079_T33UYP_20181010T122839.zip/S2A_MSIL2A_20181010T095031_N0209_R079_T33UYP_20181010T122839.SAFE
Product pseudopath is /mnt/data/S2/2A/MSI/LEVEL-2A/S2MSI2A/2018/10/10/S2A_MSIL2A_20181010T095031_N0209_R079_T33UXP_20181010T122839.zip/S2A_MSIL2A_20181010T095031_N0209_R079_T33UXP_20181010T122839.SAFE

```

