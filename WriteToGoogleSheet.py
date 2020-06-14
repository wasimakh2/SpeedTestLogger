import gspread
from oauth2client.service_account import ServiceAccountCredentials
from _datetime import datetime

def AddSpeedResutltToGoogleSheet(parameter_list):

    # use creds to create a client to interact with the Google Drive API
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    # Find a workbook by name and open the first sheet
    # Make sure you use the right name here.
    sheet = client.open("SpeedTestCLI_Report").sheet1

    # Extract and print all of the values
    #list_of_hashes = sheet.get_all_records()
    #print(list_of_hashes)

    sheet.append_row([
        str(datetime.now()),
        parameter_list['client']['isp'],
        (parameter_list['download']//1000000),
        (parameter_list['upload']/1000000),
        parameter_list['server']['sponsor'],
        parameter_list['ping'],
        parameter_list['share']
        ])