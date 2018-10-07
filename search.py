import requests,os,glob,argparse,datetime
#https://catalogue.onda-dias.eu/dias-catalogue/Products?$search=%22((name:*MSIL2A*)%20AND%20cloudCoverPercentage:[0%20TO%2050])%20AND%20((beginPosition:[2018-01-01T00:00:00.000Z%20TO%20NOW]))%20AND%20footprint:%22Intersects(POLYGON((16.42658889596646%2049.90175259992773,23.01838577096646%2049.90175259992773,23.01838577096646%2047.62842332702383,16.42658889596646%2047.62842332702383,16.42658889596646%2049.90175259992773)))%22%22&$orderby=creationDate%20desc&$top=15&$skip=0&$format=json
endpoint=""
polygon="POLYGON((16.066461784422813 48.64375673661302,17.560602409422813 48.64375673661302,17.560602409422813 47.720806778039126,16.066461784422813 47.720806778039126,16.066461784422813 48.64375673661302))"
polygon="POLYGON((16.340941706389003 49.799613029108414,23.284301081389003 49.799613029108414,23.284301081389003 47.6549321486175,16.340941706389003 47.6549321486175,16.340941706389003 49.799613029108414))"
baspath = "/mnt/data/"
inputpath = "/home/klimeto/slovakeye/l2a"
ap = argparse.ArgumentParser()
ap.add_argument("-from",required=False,dest="from",help="e.g. 2018-08-01")
ap.add_argument("-to",required=False,dest="to",help="e.g. 2018-09-01, default now")
ap.add_argument("-bands",required=False,dest="bands",help="Bands to be filtered.", type=list)
ap.add_argument("-wkt",required=False,dest="bands",help="Spatial extend in WKT")
ap.add_argument("-cloud",required=False,dest="cloud",help="Cloud cover upper extent, e.g. 50")
ap.add_argument("-mask",required=False,dest="mask",help="Mask", type=bool)
args = vars(ap.parse_args())
if args['from']:
    FROM = args['from']
else:
    FROM = datetime.datetime.now() - datetime.timedelta(30)
if args['to']:
    TO = args['to']
else:
    TO = datetime.datetime.today().strftime("%Y-%m-%d")
if args['bands']:
    BANDS = args['bands']
else:
    BANDS = ['B04','B02','B03']

if args['mask']:
    MASK = True
top='10'
cloud = '30'
url = "https://catalogue.onda-dias.eu/dias-catalogue/Products?$search=%22((name:*MSIL2A*) AND cloudCoverPercentage:[0 TO "+cloud+"])" \
      "%20AND%20((beginPosition:["+FROM+"T00:00:00.000Z%20TO%20"+TO+"T23:59:00.000Z]))%20AND%20" \
      "footprint:%22Intersects("+polygon+")%22%22&$orderby=creationDate%20asc&$format=json&$skip=0&$top=" + top
print(url)
resp = requests.get(url=url)
data = resp.json()
proc_input = []
for key, value in data.items():
    if key == 'value':
        if len(value) == 0:
            print("No data found. Exiting")
            exit()
        print("Found {} products. Starting the process.".format(len(value)))
        for r in value:
            product = {}
            pseudo = (r['pseudopath']).split(", ")
            pseudoProduct = pseudo[1]
            idecko = (r['name'])
            safename = idecko.replace('.zip','.SAFE')
            prefix = safename.split(".SAFE")[0]
            mgrs = safename.split("_")[5]
            product['name'] = safename
            safePath = (os.path.join(baspath,pseudoProduct,idecko,safename)).replace('\\', '/')
            if not os.path.exists(os.path.join(inputpath,mgrs)):
                os.system('mkdir -p {}'.format(os.path.join(inputpath,mgrs)))
            img_data_pattern = ((os.path.join(safePath,'GRANULE','*','IMG_DATA','*')).replace('\\', '/'))
            files_grabbed = [glob.glob(os.path.join(img_data_pattern,'*'+e+'_10m.jp2')) for e in BANDS]
            grabbed_bands = [val for sublist in files_grabbed for val in sublist]
            if MASK:
                mask_file = glob.glob(os.path.join(img_data_pattern,'*SCL_60m.jp2'))
                if len(mask_file) > 0:
                    os.system('ls -l %s %s' % (mask_file[0],os.path.join(inputpath,mgrs,"mask_"+prefix+".jp2")))
                else:
                    print("Mask file not found")
            if len(grabbed_bands) == 3:
                os.system('gdal_merge.py -separate -of GTiff -o %s %s' % (os.path.join(inputpath, mgrs, prefix + '.tiff'), ' '.join(grabbed_bands)))
