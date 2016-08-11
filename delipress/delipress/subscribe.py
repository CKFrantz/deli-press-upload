# Latest MailChimp Python Package can be downloaded with the following command:
# pip install git+git://github.com/charlesthk/python-mailchimp.git
# Documentation is Here: github.com/charlesthk/python-mailchimp
# Email page I learned from is here: http://stackoverflow.com/questions/6270782/how-to-send-an-email-with-python

from mailchimp3 import MailChimp
#import requests

#
#	Test Variables
#
sEmail = 'dominic@vpmedia.us'
sFname = 'Dominic'
sLname = 'Olivas'
sTitle = 'Creative'
sCompany = 'Vantage Point Media'
sSegment = 'Media'


#
#  Subscribe Users
#
#  API Settings   client = MailChimp([USERNAME] , [API KEY])
#
client = MailChimp('delimarketnews', 'e060fca52424795d9c49cde144ce21c4-us11')

# add subscriber to list matching id on mailchimp
client.member.create('baf3851622', {
    'email_address': sEmail,
    'status': 'subscribed',
    'merge_fields': {
        'FNAME': sFname,
        'LNAME': sLname,
        'MMERGE3': sTitle,
        'MMERGE4': sCompany,
        'MMERGE7': sSegment,
    },
})

