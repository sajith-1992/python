import sys
names = ["sajith","lakshmikuti","okperfect","aliyan","kuppikannan","pazhamgowdham","kavutaaliyan","parishkari","sikorajan","appyteam"]
name = input("Name:")
if name in names:
    print("found")
    sys.exit(0)
print("not found")
sys.exit(1)