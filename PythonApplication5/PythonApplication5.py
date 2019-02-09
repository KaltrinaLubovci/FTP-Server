import sys
import chilkat
import os

ftp = chilkat.CkFtp2()

success = ftp.UnlockComponent("Anything for 30-day trial")
if (success != True):
    print(ftp.lastErrorText())
    sys.exit()

ftp.put_Hostname("192.168.56.1")
ftp.put_Username("FTPuser1")
ftp.put_Password("ftpuser")

#  Connect and login to the FTP server.
success = ftp.Connect()
if (success != True):
    #print(ftp.lastErrorText())
    #sys.exit()
    print("************************************************ FTP Server is offline *************************************************")
    print("")
else:
    #  FTP serveri ne Active mode:
    #ftp.put_Passive(False)

    ftp.put_Passive(False)
    
    #funksioni per ngarkim te fajllave
    def ngarko():
        filepath =raw_input("Filepath:")
        filee=raw_input("Filename:")
        if filepath == "" or filee == "":
            print("Fushat \'Filepath\' dhe \'Filename\' duhet te plotesohen!")
            filepath =raw_input("Filepath:")
            filee=raw_input("Filename:")
            name, ext = os.path.splitext(filee)
            if ext==".doc" or ext == ".docx" or ext == ".xls" or ext == ".xlsx": 
                success = ftp.PutFile(filepath,filee)
                if (success != True):
                    print(ftp.lastErrorText())
                success = ftp.Disconnect()
                print("Fajlli u ngarkua!")
            else:
                print("Nuk lejohet ngarkimi i fajlleve me extension \"" + ext + "\" ! ")
                print("Mund te ngarkohen vetem fajllat me extension \".doc\", \".docx\", \".xls\" ose \".xlsx\" !")
        else:
            name, ext = os.path.splitext(filee)
            if ext==".doc" or ext == ".docx" or ext == ".xls" or ext == ".xlsx": 
                success = ftp.PutFile(filepath,filee)
                if (success != True):
                    print(ftp.lastErrorText())
                success = ftp.Disconnect()
                print("Fajlli u ngarkua!")
            else:
                print("Nuk lejohet ngarkimi i fajlleve me extension \"" + ext + "\" ! ")
                print("Mund te ngarkohen vetem fajllat me extension \".doc\", \".docx\", \".xls\" ose \".xlsx!\"")
    
    #funksioni per fshirje te fajllave
    def fshij():
        filee=raw_input("Shenoni fajllin per t\'u fshire:")
        success = ftp.DeleteRemoteFile(filee)
        if (success != True):
            print("Fajlli nuk mund te fshihet, pasiqe mund te mos gjendet ne kete direktorium!")
        else:
            print("Fajlli u fshi me sukses!")

    #funksioni per te krijuar follder te ri
    def krijoDir():
        folder=raw_input("Shenoni emrin e follderit qe doni t\'a krijoni:")
        success = ftp.CreateRemoteDir(folder)
        if (success != True):
            print("Follderit nuk mund te krijohet!")
        else:
            print("Follderi u krijua me sukses!")
        success = ftp.ChangeRemoteDir(folder)
        if (success != True):
            print(ftp.lastErrorText())
        else:
            print("Fajllat do te ruhen ne follderin " + folder)

    #funnksioni per te fshire ndonje follder
    def fshijDir():
        folder=raw_input("Shenoni emrin e follderit qe doni t\'a fshini:")
        success = ftp.ChangeRemoteDir(folder)
        if (success != True):
            print(ftp.lastErrorText())
        success = ftp.DeleteTree()
        if (success != True):
            print(ftp.lastErrorText())
        success = ftp.ChangeRemoteDir("..")
        if (success != True):
            print(ftp.lastErrorText())
        success = ftp.RemoveRemoteDir(folder)
        if (success != True):
            print("Follderi nuk mund te fshihet!")
        else:
            print("Follderi u fshi me sukses")
    
     #funksioni per ndryshim te lokacionit te ruajtses se fajllave
    def ndryshoDir():
        folder=raw_input("Shenoni emrin e follderit ku doni te operoni:")
        success = ftp.ChangeRemoteDir(folder)
        if (success != True):
            print("Ky follder nuk ekziston!")
        else:
            print("Tani gjendeni ne follderin "+folder)



        

    print("************************************************ FTP Server is online **************************************************")
    print("")
    print("Shtyp --i per informata rreth aplikacionit. Shtyp ndonje nga karakteret tjera per t\'a tejkaluar kete hap! ")
    string = raw_input(">>")
    print("")
    if string == "--i":
        print("=======================================================================================================================")
        print("Ky aplikacion sherben per ngarkim(upload) dhe fshirje te fajllave me extension .doc, .docx, .xls apo .xlsx ne FTP Server.")
        print("")
        print("Filepath:          Ne seksionin \"Filepath:\" kerkohet shtegu(path) i fajllit qe duam t\'a ngarkojm,")
        print("                   duke perfshire edhe emrin e fajllit.")
        print("Filename:          Ne seksionin \"Filename:\" kerkohet emri i fajllit(se bashku me extension) qe duam t\'a ngarkojme. ")
        print("=======================================================================================================================")
        print("--f                Komanda per t\'a filluar procesin e ngarkimit.")
        print("--d                Komanda per te fshire ndonje fajll. ")
        print("--k                Komanda per te krijuar follder te ri.")
        print("--e                Komanda per te fshire ndonje follder.")
        print("=======================================================================================================================")
        st=raw_input("Deshironi t\'a nderroni direktoriumin? [Po/Jo] ")
        if st == "Po":
            ndryshoDir()
            print("Shtyp njeren nga komandat per te vazhduar me tutje!")
            string1=raw_input(">>")
            if string1 == "--f":
                ngarko()
            elif string1 == "--d":
                 fshij()
            elif string1 == "--k":
                  krijoDir()
            elif string1 == "--e":
                  fshijDir()
            else:
                print("Ju nuk keni shtypur komanden e duhur! Ju lutem, shtypni njeren nga komandat me siper!")
                string1=raw_input(">>")
                if string1== "--f":
                    ngarko()
                elif string1 == "--d":
                      fshij()
                elif string1 == "--k":
                      krijoDir()
                elif string1 == "--e":
                      fshijDir()
                else:
                    print("                                              -------------------------")
                    print("                                              |Rifilloje aplikacionin!|")
                    print("                                              -------------------------")
        
        elif st == "Jo":
            print("Operimet e radhes do te kryhen ne follderin aktual!")
            print("Shtyp njeren nga komandat per te vazhduar me tutje!")
            string1=raw_input(">>")
            if string1 == "--f":
                ngarko()
            elif string1 == "--d":
                  fshij()
            elif string1 == "--k":
                  krijoDir()
            elif string1 == "--e":
                  fshijDir()
            else:
                print("Ju nuk keni shtypur komanden e duhur! Ju lutem, shtypni njeren nga komandat me siper!")
                string1=raw_input(">>")
                if string1== "--f":
                    ngarko()
                elif string1 == "--d":
                      fshij()
                elif string1 == "--k":
                     krijoDir()
                elif string1 == "--e":
                      fshijDir()
                else:
                    print("                                              -------------------------")
                    print("                                              |Rifilloje aplikacionin!|")
                    print("                                              -------------------------")
        
        
    else:
        print("=======================================================================================================================")
        print("--f                Komanda per t\'a filluar procesin e ngarkimit.")
        print("--d                Komanda per te fshire ndonje fajll. ")
        print("--k                Komanda per te krijuar follder te ri.")
        print("--e                Komanda per te fshire ndonje follder.")
        print("=======================================================================================================================")
        st=raw_input("Deshironi t\'a nderroni direktoriumin? [Po/Jo]")
        if st == "Po":
            ndryshoDir()
            print("Shtyp njeren nga komandat per te vazhduar me tutje!")
            string1=raw_input(">>")
            if string1 == "--f":
                ngarko()
            elif string1 == "--d":
                 fshij()
            elif string1 == "--k":
                  krijoDir()
            elif string1 == "--e":
                  fshijDir()
            else:
                print("Ju nuk keni shtypur komanden e duhur! Ju lutem, shtypni njeren nga komandat me siper!")
                string1=raw_input(">>")
                if string1== "--f":
                    ngarko()
                elif string1 == "--d":
                      fshij()
                elif string1 == "--k":
                      krijoDir()
                elif string1 == "--e":
                      fshijDir()
                else:
                    print("                                              -------------------------")
                    print("                                              |Rifilloje aplikacionin!|")
                    print("                                              -------------------------")
        
        elif st == "Jo":
            print("Operimet e radhes do te kryhen ne follderin aktual!")
            print("Shtyp njeren nga komandat per te vazhduar me tutje!")
            string1=raw_input(">>")
            if string1 == "--f":
                ngarko()
            elif string1 == "--d":
                  fshij()
            elif string1 == "--k":
                  krijoDir()
            elif string1 == "--e":
                  fshijDir()
            else:
                print("Ju nuk keni shtypur komanden e duhur! Ju lutem, shtypni njeren nga komandat me siper!")
                string1=raw_input(">>")
                if string1== "--f":
                    ngarko()
                elif string1 == "--d":
                      fshij()
                elif string1 == "--k":
                     krijoDir()
                elif string1 == "--e":
                      fshijDir()
                else:
                    print("                                              -------------------------")
                    print("                                              |Rifilloje aplikacionin!|")
                    print("                                              -------------------------")
        
        