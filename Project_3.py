## Email Slicer

# we will take the email id and strip
email = input("Enter your email id: ").strip()

# For extracting the username we slice down the name before "@"
username = email[:email.index("@")]
# Here we slice down the remaining portion after "@" as domain name. We use +1 so as to not include the "@" within our username.
domain_name = email[email.index("@") + 1:]

format_ = ("Your username is {} and your domain is {}".format(username, domain_name))
print(format_)