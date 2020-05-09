from datetime import datetime
import calendar
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
from pprint import pprint
import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
CREDENTIALS_FILE = 'credentials.json'  #  ← имя скаченного файла с закрытым ключом
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_FILE, ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

spreadsheetId = '1UCAw3PTluEKc3noSBrMcLlfCU1WHhpraLd8Zwh9z9Lg'
range_name = 'Лист1!A:G'
table = service.spreadsheets().values().get(spreadsheetId=spreadsheetId, range=range_name).execute()
spread_sheet_values = table['values']
print(spread_sheet_values[0][0])



cell = 'A1'
value = '1,618'
body_to_write = {"valueInputOption": "USER_ENTERED",
                 "data": [{"range": 'Лист1' + "!" + cell,
                           "majorDimension": "ROWS",
                           "values": [[value]]}]
                 }
service.spreadsheets().values().batchUpdate(spreadsheetId=spreadsheetId, body=body_to_write).execute()
