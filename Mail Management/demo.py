from imap_tools import MailBox, AND
from datetime import date

MAIL_PASSWORD = "itppfwrrcvrcbhae"  # Use an app password or environment variables
MAIL_USERNAME = "infraonsupport@everestims.com"  # Use your actual Gmail account

# Connect to the Gmail IMAP server and log in
with MailBox("imap.gmail.com").login(MAIL_USERNAME, MAIL_PASSWORD, "INBOX") as mb:
    count = 0
    unanswered_emails = []

    # Fetch emails, limit to 5
    for msg in mb.fetch(limit=5):
        subject = msg.subject
        time = msg.date
        body = msg.text
        from_addr = msg.from_

        # Print email details
        
        print(f"from : {from_addr}")
        print("\n")
        print(f"time : {time}")
        print("\n")
        print(f"subject : {subject}")
        #print(f"body : {body}")
        print("\n--------------------------------------- \n")

        # Define a specific email address that is considered "answered"
        support_emails = 'infraonsupport@everestims.com'

        # If the email is not from the support address, it is considered unanswered
        if from_addr != support_emails:
            unanswered_email = {'subject': subject, 'from': from_addr, 'time': time}
            #print(f"Found unanswered email: {unanswered_email}")
            unanswered_emails.append(unanswered_email)
            count += 1
    #print(f"Found unanswered email: {unanswered_email}")
    
    # Print the count and the list of unanswered emails
    print(f'Count of unanswered emails: {count}')
    print("---------------------------\n")
    for i in unanswered_emails:
        print(f"List of all unanswered emails: {i} \n")
