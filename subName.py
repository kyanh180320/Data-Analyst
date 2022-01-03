def process(email): 
    email_user = email[0:email.index('@')]
    domain_user = email[email.index('@')+1:]
    return [email_user , domain_user]
   
def printMsg(email_user, domain_user):
    print(f'User name  : {email_user} , Domain user name  : {domain_user}')    
    
def main():
    email = input("please input email : ").strip()
    email_user, domain_user = process(email)
    printMsg(email_user, domain_user)
if  __name__ == "__main__":
 main()
     