# py regex-string.py

message=" Hello welcome to the devops world! "

# 1.Remove leading and trailing spaces (start and end)
print("1.Strip():",message.strip())

#2.Convert to upper case
print("2.upper-", message.upper())

#3.Convert to lower case
print("3.lower-", message.lower())

#4.Replace a word
print("4.replace-", message.replace("devops", "python"))

#5.Check if string starts with a word
print("5.startswith-", message.strip().startswith("Hello"))

#6.Check if string ends with a word
print("6.endswith-", message.strip().endswith("world!"))

#7.To find the positionn of a word
print("7.find(devops)-", message.find("devops"))

#8. tO Count a word
print("8.Count(o)-", message.count("o"))

#9.Split the string into list
words=message.strip().split(" ")
print("9.Split-",words)

#10.Join the list back into string with ("-")
print("10.jOIN-", "-".join(words))

#11.Capitalized - depreciated

#12.Check all the characters is alphabet
print("12.isalpha-", message.isalpha())

#12.Check all the characters is digit
print("12.isdigit-", message.isdigit())


