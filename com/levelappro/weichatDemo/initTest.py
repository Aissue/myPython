import itchat


if __name__=="__main__":
    itchat.login()
    friends = itchat.get_friends(update=False)[0:]
    for i in friends[1:]:
        # print(i["UserName"])
        print(i["NickName"]+":"+i["Signature"])