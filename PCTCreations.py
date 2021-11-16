from pyrogram import Client, filters
import json
import os
'''
{"creationlist":[]}
'''


@Client.on_message(filters.command("creationadd", prefixes="%") & filters.me)
async def creadd(client, message):
    maintext = message.text
    creation = maintext.replace("%creationadd ", "")
    os.chdir("configs")
    conf = open("PCTCreations.json", "r")
    resdict = json.load(conf)
    conf = open("PCTCreations.json", "w")
    if resdict["creationlist"].count(creation) == 0:
        resdict["creationlist"].append(creation)
        json.dump(resdict, conf)
        await message.edit_text("Competed")
    else:
        await message.edit_text(f"\"{creation}\" exist")
    conf.close()
    os.chdir("../")


@Client.on_message(filters.command("creationlist", prefixes="%") & filters.me)
async def creationlist(client, message):
    os.chdir("configs")
    conf = open("PCTCreations.json", "r")
    resdict = json.load(conf)
    crelist = resdict["creationlist"]
    head = "Creation list:\n"
    body = ""
    if len(crelist) == 0:
        body = "empty"
    else:
        for i in range(len(crelist)):
            body += f"{str(i+1)}){crelist[i]}\n"
    conf.close()
    os.chdir("../")
    await message.edit_text(head+body)


@Client.on_message(filters.command("creationremove", prefixes="%") & filters.me)
async def creationrem(client, message):
    id = int(message.text.replace("%creationremove ", ""))-1
    os.chdir("configs")
    conf = open("PCTCreations.json", "r")
    resdict = json.load(conf)
    conf = open("PCTCreations.json", "w")
    try:
        creation = json["creationlist"].pop(id)
        json.dump(resdict, conf)
        await message.edit_text(f"Creation \"{creation}\" has been deleted.")
    except IndexError:
        await message.edit_text(f"\"{creation}\" does not exist")
    conf.close()
    os.chdir("../")
