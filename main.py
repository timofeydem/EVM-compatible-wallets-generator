from eth_account import Account
import secrets

number = int(input("Number of wallets you need: "))
choose_type = int(input("Choose type of writing:\n 1 - address | private_key \n 2 - address \n     private key: "))
choose_array = input("Do you need to print array format at the end of your file? (y/n): ")
addresses = []
private_keys = []

f = open('wallets.txt', 'w')

while number > 0:
    private_key = "0x" + secrets.token_hex(32)
    acct = Account.from_key(private_key)
    acct = acct.address
    addresses.append(acct)
    private_keys.append(private_key)
    number -= 1

if choose_type == 1:
    for x in range(0, len(addresses)):
        f.write(addresses[x] + " | " + private_keys[x] + "\n")
if choose_type == 2:
    for x in range(0, len(addresses)):
        f.write(addresses[x] + "\n" + private_keys[x] + "\n")
if choose_array == "y":
    f.write("\nAddresses array:\n")
    f.write("[")
    for x in addresses:
        f.write("'" + x + "'" + ",")
    f.write("]")

    f.write("\nPrivate keys array:\n")
    f.write("[")
    for x in private_keys:
        f.write("'" + x + "'" + ",")
    f.write("]")
