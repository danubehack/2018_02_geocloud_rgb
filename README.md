# Geocloud RGB for SK
## Motivation
- test data, service and tools provided by ONDA DIAS provider
- create a cloud free mosaic dataset from S2MSI2A products

## Target user groups
- Future ONDA DIAS platform users
-

## Methodology
- Product location selection using ONDA Catalog API
- Data preparations for further processing (GDAL tools)
- Manual selection of 


-vhodné dlaždice boli vyberané manuálne
-celkovo bolo vybratých 12 dlaždíc, ktoré bolo možné nakombinovať tak, aby bolo územie bezoblačné
-územie SR je v dvoch UTM pásmach 33 a 34, čo komplikovalo mergovanie dlaždíc
-dlaždice boli kombinované funkciu Build virtual raster. Toto bolo nutné robiť osobitne pre vrstvy ktoré sú v rovnakom SRS. Následne boli .vrt súbory exportované vo formáte .tiff so SRS 4326
-nasledne boli mergnute
