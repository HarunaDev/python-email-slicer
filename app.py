def app():
    print("Welcome to my awesome email slicer app \n")

    # def get_input():
    #     email_input = input("Type in your email here: ")

    #     while "@" and "." not in email_input:
    #         get_input()
    
    # get_input()

    email_input = input("Type in your email here: ")
    
    def check_input(input_data):
        if "@" and "." not in input_data:
            while "@" and "." not in input_data:
                input_data = input("Type your email here: ")
    
    check_input(email_input)

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")
    
    output = {"username": username, "domain": domain, "extension": extension} 
    print(output)
            

app()