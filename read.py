print("start")

globalClf = 0
try:
    import nfc
    import time


    while True:
        clf = nfc.ContactlessFrontend()
        assert clf.open('usb:001:011') is True 
        globalClf = clf

        from nfc.clf import RemoteTarget
        target = clf.sense(RemoteTarget('106A'), RemoteTarget('106B'), RemoteTarget('212F'))

        if target != None:
            print(target)
            try:
                tag = nfc.tag.activate(clf, target)
                print(tag)
            except:
                print('could not activate')
        clf.close()
        time.sleep(2)
except:
    print("An exception occurred")
    globalClf.close()
