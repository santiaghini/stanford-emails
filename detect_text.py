import json
import io
import os
import re
from os import listdir
from os.path import isfile, join
from pdf2image import convert_from_path
# install google package: https://cloud.google.com/vision/docs/libraries
from google.cloud import vision
from google.oauth2 import service_account
from google.protobuf.json_format import MessageToJson

# TODO: You need to have the photonos.json keys in the same folder where you run the script
credentials = service_account.Credentials.from_service_account_file(
    "photonos.json")
vision_client = vision.ImageAnnotatorClient(credentials=credentials)

# TODO: add absolute or relative path to folder where you want to extract files
# Folder has to have three subfolders: pdfs, imgs and extracted_text
root_path = '/Users/tiagohernan/Documents/Stanford/ClassPresident/emails/'
files_path = 'pdfs/'
imgs_path = 'imgs/'
extracted_texts_folder = 'text/'


def detect_document(path, filename):
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    print('\tSent to Google')
    response = vision_client.document_text_detection(image=image)
    print('\tGoogle Responded')
    # print(response)
    serialized = MessageToJson(response)
    json_obj = json.loads(serialized)

    json_filename = root_path + extracted_texts_folder + filename + ".json"

    with open(json_filename, 'w') as fp:
        # json.dump(json_obj, fp, sort_keys=True, indent=3, separators=(',', ': ')) # pretty
        json.dump(json_obj['textAnnotations'][0]['description'], fp, indent=None,
                  separators=(',', ':'))  # compressed


def delete_extension(n):
    return n.split('.')[0]


def add_extension(n):
    return n + '.pdf'


files = os.listdir(root_path + files_path)
print(files)
files.sort()
print(files)

# files = list(map(delete_extension, files))
# print(files)
#
# files.sort(key=int)
# print(files)
#
# files = list(map(add_extension, files))

i = 0
for file in files:
    i += 1
    print(f'File {str(i)} of {len(files)}')
    if not file.endswith(".pdf"):
        continue

    pdf_path = root_path + files_path + file
    print(pdf_path)
    pages = convert_from_path(pdf_path, 300)
    for j, page in enumerate(pages):
        print(f'\tPage {str(j+1)} of {len(pages)}')
        page_name = "{}-{}".format(file.split('.')[0], j+1)
        img_path = root_path + imgs_path + page_name + ".jpg"
        print('\timg_path:', img_path)
        page.save(img_path, "jpeg")
        print("\t" + page_name + ".json")
        detect_document(img_path, page_name)
