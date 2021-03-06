from pyrogram import Client, filters
import json
import os
'''
{"list":[]}
'''


@Client.on_message(filters.command("listadd", prefixes="%") & filters.me)
async def creadd(client, message):
    maintext = message.text
    creation = maintext.replace("%listadd ", "")
    os.chdir("configs")
    conf = open("PCTList.json", "r")
    resdict = json.load(conf)
    conf = open("PCTlist.json", "w")
    if resdict["list"].count(creation) == 0:
        resdict["list"].append(creation)
        json.dump(resdict, conf)
        await message.edit_text("Competed")
    else:
        await message.edit_text(f"\"{creation}\" exist")
    conf.close()
    os.chdir("../")


@Client.on_message(filters.command("listlist", prefixes="%") & filters.me)
async def creationlist(client, message):
    os.chdir("configs")
    conf = open("PCTList.json", "r")
    resdict = json.load(conf)
    crelist = resdict["list"]
    head = "List:\n"
    body = ""
    if len(crelist) == 0:
        body = "empty"
    else:
        for i in range(len(crelist)):
            body += f"{str(i+1)}){crelist[i]}\n"
    conf.close()
    os.chdir("../")
    await message.edit_text(head+body)


@Client.on_message(filters.command("listremove", prefixes="%") & filters.me)
async def creationrem(client, message):
    id = int(message.text.replace("%listremove ", ""))-1
    os.chdir("configs")
    conf = open("PCTList.json", "r")
    resdict = json.load(conf)
    conf = open("PCTList.json", "w")
    try:
        creation = resdict["list"].pop(id)
        json.dump(resdict, conf)
        await message.edit_text(f"\"{creation}\" has been deleted.")
    except IndexError:
        await message.edit_text(f"\"{creation}\" does not exist")
    conf.close()
    os.chdir("../")
