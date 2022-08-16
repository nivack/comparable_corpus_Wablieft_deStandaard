"""
Extract meta from stan article xml files to same format as Wablieft meta file
"""

from bs4 import BeautifulSoup
import datetime
import os


# Give rootpath of standaard articles filelocation e.g. data\\standaard\\
root_path = ''

os.chdir(root_path)

# Give list of years you want to extract stanmeta data from
year_maps = ['2013', '2014', '2015', '2016', '2017']

for year in year_maps:
    path = 'stan'+year+'\\xml\\'
    # for file in glob.glob("*.xml"): 
    aantal = 0 # aantal files zonder artikeltitel

    tsv_filename = "stanMeta" + year + ".tsv"
    with open(tsv_filename, "w", encoding='utf-8') as output_file:
        for file in os.listdir(path):
            if file.endswith(".xml"):

                with open(path + file, 'r', encoding='utf-8') as tei:
                    soup = BeautifulSoup(tei, 'xml')

                if soup.title.getText() == "":
                    titel = "No title"
                    aantal += 1
                else: titel = soup.title.getText()

                datum = soup.date.getText()
                datum = datetime.datetime.strptime(datum, "%d-%m-%Y").strftime("%Y" + "%m" + "%d")

                articleclass = soup.find("interpGrp", {"type": "articleClass"})
                category = articleclass.interp["value"]


                if category is None:
                    category=""
                

                output_file.write(file+"   "+titel+"    "+datum+"   "+category+"\n")

        print(aantal, " files without title")
