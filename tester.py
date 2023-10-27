import datetime

days = int(input("Days = "))
hours = int(input("Hours = "))
minutes = int(input("Minutes = "))
weeks = int(input("Weeks = "))

ts = datetime.datetime.now() + datetime.timedelta(minutes=days) + datetime.timedelta(hours=hours) + datetime.timedelta(days=minutes) + datetime.timedelta(weeks=weeks)
ts = int(ts.timestamp())
message = ""
# I'm aware that discord.utils.format_dt exists, but I prefer this layout
# for readability purposes (and its more efficient for this specific use case)
for i in "fdt":
    message += f"`<t:{ts}:{i.upper()}>`: <t:{ts}:{i.upper()}>\n"
    message += f"`<t:{ts}:{i.lower()}>`: <t:{ts}:{i.lower()}>\n"
message += f"`<t:{ts}:R>`: <t:{ts}:R>\n"

print(message)