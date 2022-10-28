
import csv
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
	    "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("/home/zec/Downloads/pune-zomato-data-05392526067d.json",scope)
client = gspread.authorize(creds)

sheet = client.open("zomato_pune_data").get_worksheet(1)

# data = sheet.get_all_records()

DATA_SPREADSHEET_ID='1R2A2_vcztq5FLqK8HU7JA6_RlUIGpw3Hi5qLYycFCws'




def append_googlesheet(value1):


    values = [value1]
    service = build('sheets','v4',credentials=creds)
    response = service.spreadsheets().values().append(spreadsheetId= DATA_SPREADSHEET_ID,
     valueInputOption='USER_ENTERED', range="Sheet1!A2:F2", body={"values": values}).execute()


def append_googlesheet2(value1):


    values = [value1]
    service = build('sheets','v4',credentials=creds)
    response = service.spreadsheets().values().append(spreadsheetId= DATA_SPREADSHEET_ID,
     valueInputOption='USER_ENTERED', range="Sheet2!A2:E2", body={"values": values}).execute()



# with open('Zomato_pune_data.csv', newline='') as f:
#     reader = csv.reader(f)
#     values = list(reader)
#     service = build('sheets','v4',credentials=creds)
# response = service.spreadsheets().values().append(spreadsheetId='1R2A2_vcztq5FLqK8HU7JA6_RlUIGpw3Hi5qLYycFCws', valueInputOption='USER_ENTERED', range="Sheet1", body={"values": values}).execute()



