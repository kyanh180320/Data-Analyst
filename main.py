from subName import process,printMsg
def main():
    emails = ['adfafd@gafaf' , 'adfafafafff@ffff' , '24324@ffff']
    for email in emails :
        email_user, domain_user = process(email)
        printMsg(email_user, domain_user)
    
if __name__ == "__main__":
 main()
     