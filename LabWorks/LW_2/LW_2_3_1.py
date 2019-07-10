import string as st

# Generate string with lowercase and uppercase alphabet plus numbers
az = st.ascii_lowercase
AZ = st.ascii_uppercase
ns = st.digits

# Print 1st symbol of string
print(az[0])

# Print last symbol
print(az[-1])

# Print 3rd from start and 3rd from the end
print(az[2])
print(az[-3])

# Slice first 8 symbols
sl = az[0:8]
print(sl)

# Print only symbols with index, which divides on 3 without remaining
print(az[2::3])

# Print the symbol of the middle of the string text
print(az[len(az)//2])

#Reverse text using slice
print(az[::-1])





