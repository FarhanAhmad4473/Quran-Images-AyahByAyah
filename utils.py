import pandas as pd
import xml.etree.cElementTree as ET

def Xml_to_pd(xml_path):
    tree = ET.parse(xml_path)
    All_data = []
    for form in tree.getroot().findall("sura"):
        attributes = form.attrib

        Surah_No,Surah_Name = attributes['index'],attributes['name']
        All_ayats = form.findall('aya')

        for aya_meta in All_ayats:
            aya = aya_meta.attrib
            Ayat_no,Aya_text = aya['index'],aya['text']
            All_data.append([Surah_No,Surah_Name,Ayat_no,Aya_text])
    #     print('*******************************************')
    print(f"Total no of ayats:{len(All_data)}")
    return pd.DataFrame(All_data,columns=['Surah_No','Surah_Name','Ayat_no','Aya_text'])