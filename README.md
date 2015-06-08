Reminders
=========

This library creates a group reminder system that runs on Google App Engine.

It was originally designed to remind my housemates to take out the trash, on a rotating weekly schedule.

Other than the cost of sending text messages via Twilio (currently < $0.01 per SMS message sent), it's free to run, assuming your group has fewer than 30 people in it.

To set up this system, do the following:

0. Create a Twilio account with API access and put a few $'s into it.  Make a note of the phone number, API user and secret key
0. Create a new Google Project via the [Google Developers Console](https://console.developers.google.com/project)
0. Create a new Gmail account with an email address that will be used to send the reminder messages
0. Register this new Gmail account with your Google Project with "Can Edit" permissions via the Google Developers Console.  This will enable your app to send emails from this address
0. In your favorite code directory, make a new directory called "reminders-project" and cd into it
0. Create a new python virtual environment in the current folder -- `virtualenv .`  There should now be folders for 'bin', 'include', and 'lib'
0. Activate this new virtualenv -- `source bin/activate`
0. Clone the reminders repo into the current directory -- `git clone https://github.com/seriesoftubes/reminders.git`
0. cd into the newly created "reminders" folder  -- `cd reminders`
0. In the current directory, add a new file called "secrets.json" and put the following in it:
```
{
  "twilio": {
    "phone_number": "<Your Twilio phone number prefixed with the country code and no dashes>",
    "api_user": "<Your Twilio API user>",
    "api_secret": "<Your Twilio API secret key>"
  },
  "email_address": "<Your reminders email address (this will send the reminders)>"
}
```
0. Install the required third-party Python libraries to a new subfolder that will be recognized by AppEngine -- `pip install -t lib -r requirements.txt`
0. Edit the cron.yaml file so it meets your needs
0. Download and install the google-cloud-sdk.  You may need to set it up with some authorizations, but the cloud SDK should guide you through that process
0. Deploy your app -- `python /PATH/TO/YOUR/google-cloud-sdk/bin/appcfg.py -A your-appengine-app-id update /PATH/TO/YOUR/reminders-project/reminders`.  To find your AppEngine app's ID, go to the [AppEngine homepage](https://appengine.google.com), navigate to your project, and click on the "Application Settings link".  Look for the "Application Identifier" property.  That is your app ID
0. Add the people in your reminder group via the Datastore Viewer.  To do this, go to your AppEngine app's home page, click on the "Datastore Viewer" link, then click on the "Create" tab and make sure the "Person" entity is selected. This will take your through a guided process of adding each new Person to your group reminders.

Example of 2 Person entities:
```
Namespace: "" (leave it blank)
can_do_trash: "True"
email_address: "bob@bob.com"
full_name: "bob saget"
is_in_house: "True"
phone_number: "+12228675309"
sort_order: 0

Namespace: "" (leave it blank)
can_do_trash: "False"
email_address: "joe@joe.com"
full_name: "joe joseph"
is_in_house: "True"
phone_number: "+18005556677"
sort_order: 1
```
After creating these 2 entities, you will have 2 people in your house, only 1 of whom can do the trash (i.e., Bob).

* Note that for Twilio to work, phone numbers must have no dashes and they must start with the country code (+1 for the US).
* Also note that chosen sort_order fields must start with 0 in ascending order (e.g., 0...1...2...etc).
