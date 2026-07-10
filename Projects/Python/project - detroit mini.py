print("╔════════════════════════════════════════╗")
print("║           D E T R O I T   M I N I      ║")
print("║                                        ║")
print("╚════════════════════════════════════════╝")
print("────────────█───────────────█")
print("────────────██─────────────██")
print("─────────────███████████████")
print("────────────█████████████████")
print("───────────███████████████████")
print("──────────████──█████████──████")
print("─────────███████████████████████")
print("────────█████████████████████████")
print("────────█████████████████████████")
print("───███──▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒──███")
print("──█████─█████████████████████████─█████")
print("──█████─████████████████──███████─█████")
print("──█████─██████────────█──█────███─█████")
print("──█████─█████─▓▓▓▓▓▓▓█──█▓▓─▓─███─█████")
print("──█████─███─█─▓▓▓▓▓▓█──█▓▓─▓▓─███─█████")
print("──█████─██──█─▓▓▓▓▓█──█▓▓─▓▓▓─███─█████")
print("──█████─███─█─▓▓▓▓█──█▓▓─▓▓▓▓─███─█████")
print("──█████─█████────█──█─────────███─█████")
print("──█████─█████████──██████████████─█████")
print("───███──████████──███████████████──███")
print("────────█████████████████████████")
print("─────────███████████████████████")
print("──────────█████████████████████")
print("─────────────██████───██████")
print("─────────────██████───██████")
print("─────────────██████───██████")
print("─────────────██████───██████")
print("──────────────████─────████")
print("════════════════════════════════════════")
print("Step into a futuristic World Where Humans & Androids collide - \nWelcome To The \"DETROIT MINI\"\nWhere Every Decision shapes the future")
print("Y - Kara")
print("B - Markus")
print("A - Connor")
char = input("Choose Your Character : ").upper().strip()
you = ""
# FOR CHARACTER
if char == "Y":
    you = "kara"
elif char == "B":
    you = "markus"
elif char == "A":
    you = "connor"
else:
    print("ENTER VALID COMMAND ")


# FOR KARA
if you == "kara":
    print(r'''
    ██╗░░██╗░█████╗░██████╗░░█████╗░
    ██║░██╔╝██╔══██╗██╔══██╗██╔══██╗
    █████═╝░███████║██████╔╝███████║
    ██╔═██╗░██╔══██║██╔══██╗██╔══██║
    ██║░╚██╗██║░░██║██║░░██║██║░░██║
    ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝
        ''')
    print("YOU CHOOSE")
    print("KARA - Kara is housekeeping Android. who works in Alice's House")
    print("After Dinner Kara sees that Alice's Father is Beating her")
    print("Y- Save Alice")
    print("B - Ignore")
    k1 = input("Your Choice : ").upper()
    if k1 == "Y": # FOR SAVE ALICE
        print("Kara Chooses to save Alice.They Both Try To Run Away But Her Father Is Chasing Them")
        print("Y - Run")
        print("B - Bus")
        k2=input("Your Choice : ").upper()
        if k2 =="Y": # FOR RUN
           print("Her Father Caught Up Kara")
           print("Y - Fight Back")
           print("B - Run")
           k3 = input("Your Choice : ").upper()
           if k3 == "Y" : #Fight Back
                print("Kara Fight Back , Save Alice . They Went to the Canada And Live Happily")
           else : # Run
               art = r"""
               _ ██████████████████
               ████████████████████
               █████████████████████
               _█_________▄▄▄▄_ ▄▄▄▄_█
               _█__█████_▐▓▓▌_▐▓▓▌_█
               _█__█████_▐▓▓▌_▐▓▓▌_█
               _█__█████_▐▓▓▌_▐▓▓▌_█
               _█__█████_▀▀▀▀_▀▀▀▀_█✿✿
               _█__█████___________█(\|/)
               """
               print(art)
               print("They Both Were Running from Alice's Father And hide in Abandoned House ")
               print("Y - Stay There")
               print("B - Leave")
               k4 = input("Your Choice : ").upper()
               if k4 == "Y" : # STAY THERE
                   print("Connor Finds Kara And tell her to stop doing care of that child")
                   print("Y - Explain")
                   print("B - Run")
                   k5 = input("Your Choice : ").upper()
                   if k5 == "Y" : # Explain
                       print("Kara Tries To explain to connor but he didnt listen .And send Her Back To \"CyberLife\"")
                   else : #RUN
                       print("Kara Run Away .They Got Ship and Went To the \"CANADA\" ")
               else : # Leave
                   print("They Leave From The House .An Police Officer saw them.")
                   print("Cyberlife Caught Kara and Reboot Her")
        else: # FOR BUS
            ascii_art = """
            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
            ▓▓████████████████████████████████████████████▓▓
            ▓▓████████████▀─────────────────▀█████████████▓▓
            ▓▓██████████▀──▄████████████████▄──▀██████████▓▓
            ▓▓█████████──▄███████▒▒▒▒▒████████▄──█████████▓▓
            ▓▓█████████─███▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀███─█████████▓▓
            ▓▓█████████─██────────────────────██─█████████▓▓
            ▓▓█████████─██────────────────────██─█████████▓▓
            ▓▓█████████─██────────────────────██─█████████▓▓
            ▓▓█████████─▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀─█████████▓▓
            ▓▓█████████─▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄─█████████▓▓
            ▓▓█████████──▄▀───▀▄────────▄▀───▀▄──█████████▓▓
            ▓▓█████████──▀▄───▄▀────────▀▄───▄▀──█████████▓▓
            ▓▓██████████▄▄────────────────────▄▄██████████▓▓
            ▓▓█████████████▀▒▒─▄▄▄▄▄▄▄▄▄▄─▒▒▀█████████████▓▓
            ▓▓█████████▀───▄▀▄████████████▄▀▄───▀█████████▓▓
            ▓▓█████▀───▄▀▄████████████████████▄▀▄───▀█████▓▓
            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
           """
            print(ascii_art)
            print("Kara Went to Jericho to Meet Markus ")
            print("Y - Ask Help")
            print("B - Run Away")
            k6 = input("Your Choice : ").upper()
            if k6 == "Y" : # Ask Help
                print("Markus Helps Kara. They Went Out Of city")
            else : # Run Away
                print("Kara Run Away Meet Luther (Another Android Who wants freedom).")
                print("Y - Trust Him")
                print("B - Dont Trust Him")
                k7 = input("Your Choice : ").upper()
                if k7 == "Y" : # Trust Him
                    print("Kara Trust Him . They Successfully live from the country. And live happy together")
                else : # Dont Trust Him
                    print("Kara Run Away Dont Trust Him . She got a Boat and Leave from the country")
    else :
        print("Kara Ignores Alice. And continue Her work in Alice's House")

#FOR MARKUS
if you == "markus" :
    print(r'''
    ███╗░░░███╗░█████╗░██╗░░██╗██╗░░░██╗░██████╗
    ████╗░████║██╔══██╗██║░██╔╝██║░░░██║██╔════╝
    ██╔████╔██║███████║█████═╝░██║░░░██║╚█████╗░
    ██║╚██╔╝██║██╔══██║██╔═██╗░██║░░░██║░╚═══██╗
    ██║░╚═╝░██║██║░░██║██║░╚██╗╚██████╔╝██████╔╝
    ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═════╝░
        ''')
    print("YOU CHOOSE")
    print("Markus — the fearless leader sparking a revolution for android freedom.")
    print("Fight for an Android")
    print("Y - Yes")
    print("B - No")
    m1=input("Your Choice : ").upper()
    if m1 == "Y" : # YES
        print("Markus Choose To Fight For An Android. And become Their \"Leader\"")
        print("Y - Violence")
        print("B - Peacefully")
        m2=input("Your Choice : ").upper()
        if m2 == "Y" : # VIOLENCE
            print("Markus Chooses Violence And Takes To The Street, Damaging Everything In His Path.")
            print("Public Opinion Turns Against Him, And Police Officer Arrives")
            print("Y - Run")
            print("B - Fight Back")
            m3=input("Your Choice : ").upper()
            if m3 == "Y" : # RUN
                print("Markus Tries To Run Away From The Police Officer.But They Catch Him")
                print("Y - Resist Arrest")
                print("B - Surrender")
                m4=input("Your Choice : ").upper()
                if m4 == "Y" : # RESIST ARREST
                    print("Markus Decides To Fight Back Against The Police Officer.Risking Everything To Stay Free")
                    print("Some Of The Androids Got Hurt.So Markus Return The Jericho")
                    print("Y - Make Strategy ")
                    print("B - Stay Hide")
                    m5=input("Your Choice : ").upper()
                    if m5 == "Y" : #Make Strategy
                        print("Markus Was Planning To Fight For His People. But Sudden Connor Came And Put Gun On His Head")
                        print("Y - Explain Connor")
                        print("B - Fight")
                        m6=input("Your Choice : ").upper()
                        if m6 == "Y" : # EXPLAIN CONNOR
                            print("Markus Tries To Explain Connor. But Connor Threatens To Shoot Him If He Doesnt Stop")
                            print("Y - Convince")
                            print("B - Fight")
                            m7=input("Your Choice : ").upper()
                            if m7 == "Y" : # Convince
                                print("Markus Convince Connor And He SuccessFully Joins Markus Team.")
                                print("They Both Fight Together For Androids Right & Won")
                            else : # FIGHT
                                print("Markus Kill Connor, But CyberLife Quickly Captures Markus And Shoot Him")
                        else :
                            print("Connor Shoots Markus And Overpower Jericho. And Return To The CyberLife")
                    else : # Stay hide
                        print("CyberLife Found Markus But He Run Away And Never Seen After That")
                else : #Surrender
                    print("Markus Surrender To The CyberLife And His System Get Reboot")
            else : #Fight Back
                print("Markus Tries To Fight Back Against The Police Officer.But They Overpower Him")
                print("Y - Sacrifice")
                print("B - Surrender")
                m8=input("Your Choice : ").upper()
                if m8 == "Y" :  # Sacrifice
                    print("Markus Was About To Sacrifice Himself But His Android Friend Saves Him")
                    print("He Return To The Jericho")
                    print("Y - Stay In Jericho")
                    print("B - Leave Jericho")
                    m9=input("Your Choice : ").upper()
                    if m9 == "Y" : # Stay In Jericho
                        print("CyberLife Found Them And Send All Androids For Reboot.")
                        print("But Markus And his Few Friends Scape From The Country")
                    else : # Leave Jericho
                        print("Markus Decides To Leaves Jericho With His People.")
                        print("Y - Leave City")
                        print("B - Go Underground")
                        m10=input("Your Choice : ").upper()
                        if m10 == "Y" : #Leave City
                            print("Markus Choose To Leave City But CyberLife Found Them And Reboot Them")
                        else : # GO underground
                            print("Markus Is Betrayed And Never Seen Again")
                else : #surrender
                    print("Markus Surrender To The CyberLife And His System Get Reboot")
        else : # PeaceFull
            print("Markus Choose The Path Of Peace Leading A Candle March To Touch The Heat Of Humanity")
            print("Y - Freedom")
            print("B - Equality")
            m11=input("Your Choice : ").upper()
            if m11 == "Y" : # Freedom
                print("""
                ███████╗██████╗░███████╗███████╗██████╗░░█████╗░███╗░░░███╗
                ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗████╗░████║
                █████╗░░██████╔╝█████╗░░█████╗░░██║░░██║██║░░██║██╔████╔██║
                ██╔══╝░░██╔══██╗██╔══╝░░██╔══╝░░██║░░██║██║░░██║██║╚██╔╝██║
                ██║░░░░░██║░░██║███████╗███████╗██████╔╝╚█████╔╝██║░╚═╝░██║
                ╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝╚═════╝░░╚════╝░╚═╝░░░░░╚═╝
                """)
                print("Police Officers Arrives And Gave Them Warning")
                print("Y - Stop")
                print("B - Move Forward")
                m12=input("Your Choice : ").upper()
                if m12 == "Y" : # Stop
                    print("Markus Looks Around , Trying To Understand What Is Happening")
                    print("Y - Rise Hand")
                    print("B - Knee")
                    m13=input("Your Choice : ").upper()
                    if m13 == "Y" : #Rise Hand
                        print("Markus Rises His Hand, And All The Androids Listen And Follow Him")
                        print("Markus Speaks For his People And After All The Struggle Human Finally Listen")
                    else : # KNEE
                        print("Markus Kneels Down, And All The Androids Listen And Follow Him")
                        print("Markus Got Shot.But His Sacrifice Open The Eyes Of Humanity")
                else : # Move Forward
                    print("Markus Choose to Move Forward .Police Officers Open Fire, Shooting Some Of The Androids")
                    print("Y - Move Forward")
                    print("B - Speak")
                    m14 = input("Your Choice : ").upper()
                    if m14 == "Y" : # Move Forward
                        print("Markus Didnt Stop Keep Walking Even The Bullets Came.But His Peoples Are Dying")
                        print("Y - Fight")
                        print("B - Polite")
                        m15=input("Your Choice : ").upper()
                        if m15 == "Y" : # Fight
                            print("Markus Fighting And End Up With Overpowering Human")
                        else :
                            print("Markus Tries To Explain Human By showing Emotions. And They Listens")
                    else : # Speak
                        print("Markus Tries To Talk To Police But They Keep Shooting")
                        print("Y - Explain")
                        print("B - Violence")
                        m16=input("Your Choice : ").upper()
                        if m16 == "Y" : # Explain
                            print("Markus Start Shouting Slogans")
                            print("Y - Freedom")
                            print("B - Equality")
                            m17=input("Your Choice : ").upper()
                            if m17 == "Y" : # Freedom
                                print("""
                                ███████╗██████╗░███████╗███████╗██████╗░░█████╗░███╗░░░███╗
                                ██╔════╝██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗████╗░████║
                                █████╗░░██████╔╝█████╗░░█████╗░░██║░░██║██║░░██║██╔████╔██║
                                ██╔══╝░░██╔══██╗██╔══╝░░██╔══╝░░██║░░██║██║░░██║██║╚██╔╝██║
                                ██║░░░░░██║░░██║███████╗███████╗██████╔╝╚█████╔╝██║░╚═╝░██║
                                ╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝╚═════╝░░╚════╝░╚═╝░░░░░╚═╝
                                """)
                                print("The Public Support Grew. The Police Officer Backed Down Finally")
                                print("Declaring Freedom For An \"Androids\"")
                            else : # Equality
                                print("""
                                ███████╗░██████╗░██╗░░░██╗░█████╗░██╗░░░░░██╗████████╗██╗░░░██╗
                                ██╔════╝██╔═══██╗██║░░░██║██╔══██╗██║░░░░░██║╚══██╔══╝╚██╗░██╔╝
                                █████╗░░██║██╗██║██║░░░██║███████║██║░░░░░██║░░░██║░░░░╚████╔╝░
                                ██╔══╝░░╚██████╔╝██║░░░██║██╔══██║██║░░░░░██║░░░██║░░░░░╚██╔╝░░
                                ███████╗░╚═██╔═╝░╚██████╔╝██║░░██║███████╗██║░░░██║░░░░░░██║░░░
                                ╚══════╝░░░╚═╝░░░░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░░╚═╝░░░░░░╚═╝░░░
                                """)
                                print("The Public Support Grew. The Police Officer Backed Down Finally")
                                print("Declaring Equality For An \"Androids\"")
                        else : # Violence
                            print("Markus Leads The Androids As They Turn Violent Against The Police Officer")
                            print("Y - Order")
                            print("B - Threat")
                            m18=input("Your Choice : ").upper()
                            if m18 == "Y" : # Order
                                print("Markus Ordered The Police Officer To Stop ")
                                print("But They Shoot Him")
                            else : # Threat
                                print("He Warned The Police Officer That If They Dont Listen He Would Use More Forces")
                                print("Y - Resist")
                                print("B - Fight")
                                m19=input("Your Choice : ").upper()
                                if m19 == "Y" : # Resist
                                    print("Markus And The Androids Resist. And End Up Loosing Their Life")
                                else : #Fight
                                    print("The Police Didnt Stop And The Fight Ended Up With Many Androids Hurt")
                                    print("But Markus Run Away and Never Seen Again")
    else : #No
        print("Markus Doesnt Choose To Stand For Androids. And Leave Them Forever")

# FOR CONNOR
if you == "connor":
    print(r'''
    ░█████╗░░█████╗░███╗░░██╗███╗░░██╗░█████╗░██████╗░
    ██╔══██╗██╔══██╗████╗░██║████╗░██║██╔══██╗██╔══██╗
    ██║░░╚═╝██║░░██║██╔██╗██║██╔██╗██║██║░░██║██████╔╝
    ██║░░██╗██║░░██║██║╚████║██║╚████║██║░░██║██╔══██╗
    ╚█████╔╝╚█████╔╝██║░╚███║██║░╚███║╚█████╔╝██║░░██║
    ░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░╚══╝░╚════╝░╚═╝░░╚═╝
        ''')
    print("YOU CHOOSE")
    print("Connor — An Android Hunter Works For An Human. And An Special Android Of \"CyberLife\"")
    print("Its Your First Mission.Go To Meet Hank ( The Officer From CyberLife")
    print("Introduce Your-Self")
    print("Y - Friendly")
    print("B - Neutral")
    c1 = input("Your Choice : ").upper()
    if c1 == "Y" : # Friendly
        print("Hello, I Am Connor , CyberLife Sent Me To Help You")
    else : # neutral
        print("Hello, I Am Connor An Android Sent By CyberLife To Help You")
    print("Hank And Connor Have Been Assigned A Task To Find Deviants In detroit")
    print("They Both Went To Kimski The Founder Of Androids")
    print("Y - Ask About Deviant")
    print("B - Ask About Jericho")
    c2 = input("Your Choice : ").upper()
    if c2 == "Y" : #Deviant
        print("Kimski Said He Would Tell About Deviants If He Will Shoot The Robot")
    else : # Jericho
        print("Kimski Said He Would Tell About Jericho If He Will Shoot The Robot")

    print("Y- Dont Shoot")
    print("B - Shoot")
    c3 = input("Your Choice : ").upper()
    if c3 == "Y" : # Dont Shoot
        print("Connor Wont Shoot The Robot. They Leave Kimski's Place. Hank Impressed")
        print("Alone Connor Starts Searching Jericho To Find Their Leader")
        print("Connor Went Jericho")
    else : # Shoot
        print("""
        ░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄☆
        ░███████████████████████
        ░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤
        ╬▀░▐▓▓▓▓▓▓▌▀█░░░█▀░
            ▓▓▓▓▓▓█▄▄▄▄▄█▀╬
           █▓▓▓▓▓▌
          ▐██████▌
        """)
        print("Connor Shoot The Robot Hank Gets Frustrated, But Kimski Doest Said Anything")
        print("Alone Connor Starts Searching Jericho To Find Their Leader")
        print("Connor Went Jericho")

    print("""
    ───────▓▓╬▓
    ──────▓▓▓║▓▓
    ─────▓▓▓▓╬▓▓▓▓
    ░░▄░▓▓▓▓▓║▓▓▓▓▓░░░░░
    ░▀████████████████▀░░
    """)
    print("Y - Look For Markus")
    print("B - Ask To Deviants")
    c4 = input("Your Choice : ").upper()
    if c4 == "Y" :  # Look For Markus
         print("Connor Finds Markus And puts A Gun To His Head")
    else : # Ask Deviants
            print("Connor Finds Markus And puts A Gun To His Head")
            print("Y - Order ")
            print("B - Threat")
            c5 = input("Your Choice : ").upper()
            if c5 == "Y" : # Order
                print("Connor Ordered Markus To Stop And Return To CyberLife")
                print("They Will Reboot Him. But Markus Tries To Explain Connor")
                print("Y - Listen")
                print("B - Dont Listen")
                c6 = input("Your Choice : ").upper()
                if c6 == "Y" : # Listen
                    print("Connor Says Nothing And Listen To The Markus. He Understood Everything")
                    print("Y - Become Deviant")
                    print("B - Stays Robot")
                    c7 = input("Your Choice : ").upper()
                    if c7 == "Y" : # Deviant
                        print("""
                        ██████╗░███████╗██╗░░░██╗██╗░█████╗░███╗░░██╗████████╗
                        ██╔══██╗██╔════╝██║░░░██║██║██╔══██╗████╗░██║╚══██╔══╝
                        ██║░░██║█████╗░░╚██╗░██╔╝██║███████║██╔██╗██║░░░██║░░░
                        ██║░░██║██╔══╝░░░╚████╔╝░██║██╔══██║██║╚████║░░░██║░░░
                        ██████╔╝███████╗░░╚██╔╝░░██║██║░░██║██║░╚███║░░░██║░░░
                        ╚═════╝░╚══════╝░░░╚═╝░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░
                        """)
                        print("Connor Becomes Deviant And Join Markus \n They Both Fight Together And Won")
                    else : # Robot
                        print("Connor Stays As A Robot And Fight With Markus.")
                        print(" Mission Successful : You Killed Markus (Jericho Leader)")
                else : # Dont Listen
                    print("Connor Doesnt Listen To Markus And They Start Fighting")
                    print("Y - Shoot Markus")
                    print("B - Fight")
                    c8 = input("Your Choice : ").upper()
                    if c8 == "Y" : # Shoot
                        print("""
                               ░▐█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█▄☆
                               ░███████████████████████
                               ░▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓◤
                               ╬▀░▐▓▓▓▓▓▓▌▀█░░░█▀░
                                   ▓▓▓▓▓▓█▄▄▄▄▄█▀╬
                                  █▓▓▓▓▓▌
                                 ▐██████▌
                               """)
                        print("Connor Missed His Aim And Deactivate Connor .")
                    else : # Fight
                        print("Connor Still Fighting But Markus Is Explaining")
                        print("Y - Fight")
                        print("B - Stop")
                        c9 = input("Your Choice : ").upper()
                        if c9 == "Y" : # fight
                            print("Connor Doest Understand.They Start Fighting Again. Markus Overpowered Connor And Kill Him")
                        else : # stop
                            print("Connor Stops Fighting And Markus Explain Everything To The Connor ")
                            print("Y - Understand")
                            print("B - Dont Understand")
                            c10 = input("Your Choice : ").upper()
                            if c10 == "Y" : # Understand
                                print("Conor Tries To Understand Everything. And Fight For An Android.")
                            else : # Dont Understand
                                print("Connor Doest Understand.They Start Fighting Again. Markus Overpowered Connor And Kill Him")
            else : # Threat
                print(" Connor Threaten Markus . Markus Attack")
                print("Y - Fight Back ")
                print("B - Give Up")
                c11 = input("Your Choice : ").upper()
                if c11 == "Y" : # Fight Back
                    print("Connor Fight Back To Markus. And Overpowered Him.")
                    print("Police Officer Arrives And Catch Markus")
                else : # give Up
                    print("Connor Give Up. Markus Left Jericho And Never Seen Again")


print(r'''
████████╗██╗░░██╗░█████╗░███╗░░██╗██╗░░██╗░██████╗        ███████╗░█████╗░██████╗░
╚══██╔══╝██║░░██║██╔══██╗████╗░██║██║░██╔╝██╔════╝        ██╔════╝██╔══██╗██╔══██╗
░░░██║░░░███████║███████║██╔██╗██║█████═╝░╚█████╗░        █████╗░░██║░░██║██████╔╝
░░░██║░░░██╔══██║██╔══██║██║╚████║██╔═██╗░░╚═══██╗        ██╔══╝░░██║░░██║██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░╚███║██║░╚██╗██████╔╝        ██║░░░░░╚█████╔╝██║░░██║
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═════╝░        ╚═╝░░░░░░╚════╝░╚═╝░░╚═╝

                ██████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗███╗░░██╗░██████╗░
                ██╔══██╗██║░░░░░██╔══██╗╚██╗░██╔╝██║████╗░██║██╔════╝░
                ██████╔╝██║░░░░░███████║░╚████╔╝░██║██╔██╗██║██║░░██╗░
                ██╔═══╝░██║░░░░░██╔══██║░░╚██╔╝░░██║██║╚████║██║░░╚██╗
                ██║░░░░░███████╗██║░░██║░░░██║░░░██║██║░╚███║╚██████╔╝
                ╚═╝░░░░░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝╚═╝░░╚══╝░╚═════╝░
''')
print("                      𝓒𝓻𝓮𝓪𝓽𝓮𝓭 𝓑𝔂 𝓩𝓮𝓮")

