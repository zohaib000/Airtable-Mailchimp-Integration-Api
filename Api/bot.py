from airtable import Airtable
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
import time


client = MailchimpMarketing.Client()
client.set_config({
    "api_key": "93d6138d5d64a0a717dcc6ce8eddd762-us21",
    "server": "us21"
})
        
def insertIntoMailchimp(data_object):
    email=data_object.get("Email","")
    fname=data_object.get("Prénom","")
    lname=data_object.get("Nom","")
    print(email,fname,lname)
    try:
        data={
            "email_address":email,
            "status": "unsubscribed",
            "merge_fields": {
                "FNAME": fname,
                "LNAME": lname,
                # "ADDRESS": "chak 7 nb sargodha",
                # "PHONE": "03057896585",
            },
        }
        
        response = client.lists.add_list_member("182ac8cf01", data)
        print(response)
    except ApiClientError as error:
        print("Error: {}".format(error.text))
    
    
    
def check_new_airtable_record():
        apikey="patN8LvvnujXB3er6.a4bf93fab875bdec59a11b9a0bdaa9c8914e1ea3c0e92ea4b132134aa81bc2cd"
        baseId="appzq0aKpzmM4Zzfs"
        tableID="Clients"

        headers={
            "Authorization": f"Bearer {apikey}"
        }
        # r=requests.get(f"https://api.airtable.com/v0/{baseId}/{tableID}",headers=headers)
        # total_records=r.json()["records"]
        # print(len(total_records))

        previous_records=0
        while True:
            airtable = Airtable(baseId, tableID,api_key=apikey)
            records=airtable.get_all(view='Grid view',sort='Id')
            new_records=len(airtable.get_all())
            if new_records!=previous_records:
               print("---Airtable New Record Found----")
               print(records[-1])
               insertIntoMailchimp(records[-1]["fields"])
               previous_records=new_records
            time.sleep(5)

