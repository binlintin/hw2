import requests
# Set the base URL and credentials
URL = "https://github.com/"
username = "binlintin"
password = "blank"

# Your name for the message
your_name = "An"  # Replace with your actual name

# Prepare the message
postmsg = {"inputtext": f"daily message posted by {your_name}"}

# Headers for the request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
}

# Start a session
with requests.Session() as s:
    # Perform login
    r = s.post(URL + "login_action", data={"username": username, "password": password}, headers=headers, allow_redirects=True)
    
    # Post the message
    r = s.post(URL + "homepage_action", data=postmsg, headers=headers, allow_redirects=True)
    
    # Read back the homepage to verify the message
    r = s.get(URL + "homepage")
    
    # Convert the content to a string
    strcontent = str(r.content)
    
    # Look for the textarea where the message would be
    msgIdx = strcontent.find("textarea id='blogtext'")
    
    # If the textarea is found
    if msgIdx >= 0:
        # Find the closing tag for the textarea
        endIdx = strcontent.find("</textarea>", msgIdx)
        
        # Extract the content in the textarea
        posted_message = strcontent[msgIdx:endIdx]
        
        # Print the extracted message
        print(posted_message)
        
        # Verify if the posted message is the one we sent
        if postmsg["inputtext"] in posted_message:
            print("Most recent post has worked")
        else:
            print("Post Failed")
    else:
        print("Could not find the posted message.")
