from random import *
from time import *
from sys import *

def Intro_prolog():
    clear()
    print(" _____                               _                                _    _   ") 
    print("|  __ \                             | |                              | |  | |  ")
    print("| |  | |  ___   ___  ___  _ __ ___  | |__    ___  _ __  _ __    __ _ | |_ | |_ ")
    print("| |  | | / _ \ / __|/ _ \| '_ ` _ \ | '_ \  / _ \| '__|| '_ \  / _` || __|| __|")
    print("| |__| ||  __/| (__|  __/| | | | | || |_) ||  __/| |   | | | || (_| || |_ | |_ ")
    print("|_____/  \___| \___|\___||_| |_| |_||_.__/  \___||_|   |_| |_| \__,_| \__| \__|")
    sleep(2)
    print("")
    print("Decembernatt utspelar sig i en alternativ framtid.")
    sleep(2)
    print("Efter det stora prankkriget 2020 som kulminerade i")
    sleep(2)
    print("vattenbombningen av Norrlands Nation har ")
    sleep(2)
    print("studentnationerna legat i konstant spexkrig. Stridigheterna")
    sleep(2)
    print("manifesterar sig igenom gatustrider där studentrepresentanter")
    sleep(2)
    print("från olika nationer spex slåss om rättigheterna att kalla sig den bästa nationen")
    print("")
    sleep(4)
    print("Efter sluttentorna i December bestämmer sig du och några kurskambrater er för att gå ut på Nation.")
    print("")
    sleep(2)
    print("5 öl, 3 toabesök, och 1 stukad fot senare är det dags att röra sig hemåt.")
    print("")
    sleep(2)
    print("Du", username,",tar ett par stappligt steg ut i decemberkylan. Ner på den lätt puderbeklädda trottoaren.")
    print("")
    sleep(2)
    print("Från den mörka natthimlen faller knallvita snöflingor upplysta av fullmånen. Du känner att du vill ta dig hem!")
    print("")
    sleep (2)
    
    
    


### Slut på intro ###

#Story



def Game_over():
    print("  ██╗  ██╗██╗  ██╗     ██████╗  █████╗ ███╗   ███╗███████╗     ██████╗ ██╗   ██╗███████╗██████╗     ██╗  ██╗██╗  ██╗ ")
    print("  ╚██╗██╔╝╚██╗██╔╝    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔═══██╗██║   ██║██╔════╝██╔══██╗    ╚██╗██╔╝╚██╗██╔╝ ")
    print("   ╚███╔╝  ╚███╔╝     ██║  ███╗███████║██╔████╔██║█████╗      ██║   ██║██║   ██║█████╗  ██████╔╝     ╚███╔╝  ╚███╔╝  ")
    print("   ██╔██╗  ██╔██╗     ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ██║   ██║╚██╗ ██╔╝██╔══╝  ██╔══██╗     ██╔██╗  ██╔██╗  ")
    print("  ██╔╝ ██╗██╔╝ ██╗    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ╚██████╔╝ ╚████╔╝ ███████╗██║  ██║    ██╔╝ ██╗██╔╝ ██╗ ")
    print("  ╚═╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝   ╚═══╝  ╚══════╝╚═╝  ╚═╝    ╚═╝  ╚═╝╚═╝  ╚═╝ ")
                                                                                                 

def Del_1(val_1,Hero):
    if val_1 == "höger":
        print("")
        sleep(2)
        print("Du följer trottoaren och kommer fram till en överfrusen ankdam, i ditt berusade tillstånd får du för dig att det är en bra ide att gå ut på isen. ")
        print("")
        sleep(2)
        val_2 = input("Vill du gå ut på isen? (ja/nej): ")
        if val_2 == "ja":
            sleep(2)
            print("")
            print("Isen knakar när du med stappliga steg rör dig ut på isen. Efter ca 3 meter öppnas marken upp under dig och du glider med ett plums ner i det iskalla vattnet.")
            sleep(2)
            print("")
            Game_over()
            return
        elif val_2 == "nej":
            sleep(2)
            print("")
            print("Du inser att det inte är ett smart beslut att gå ut på isen, speciellt inte i ditt tillstånd. ")
            sleep(2)
            print("")
            print("Du rör dig framåt en bit men stannar kvikt när du ser en anka sittandes på en skateboard intill iskanten. Ankan kollar med en ondsint blick på dig och väser. ")
            sleep(2)
            print("")
            val_3 = input ("Vill du utmana ankan för prospektet att få skateboarden eller tar du höger och går runt ankan? (attack/höger): ")
            if val_3 == "attack":
                sleep(2)
                print("")
                print("ATTACK")
                anka1 = Anka()
                combat(Hero,anka1,"Ankan biter dig på smalbenet!")
                sleep(2)
                clear()
                print("Efter striden med ankan hittar du en skateboard liggandes! Du plockar upp den, man vet aldrig när man kan behöva") 
                print("en sådan! (+1 attack och kanske någon annan fördel??).")
                Hero.attack_Damage += 1
                input("press any key to continue")
                clear()
                
            elif val_3 == "höger": #randomise attack ändå?
                sleep(2)
                print("")
                print("Du går över vägen och runt ankan. Han följer dig med blicken men lämnar dig ifred.")
                sleep(2)

                
def Del_2(Hero):
    sleep(2)
    print("")
    print("Du går in i den mörka gränden, en oroskänsla sprider sig i dig som du rör dig framåt.")
    sleep(2)
    print("")
    val_5 = input("Du ser en skugga röra sig i mörkret. Vad gör du? Chansa och spring förbi hotet, stå på dig och möt hotet, eller vänder du om? (framåt/bakåt/stanna): ")
    if val_5 == "framåt":
        print("")
        sleep(2)
        print("Du snubblar till och slår huvudet på gatstenen")
        sleep(4)
        print("")
        Game_over()
        return
    elif val_5 == "bakåt":
        print("")
        sleep(2)
        print("Du springer tillbaks till Nationen")
        val_1 = input ("Till höger har du fortfarande den upplysta trottoaren. Vilket håll vill du gå åt? (höger): ")
        Del_1(val_1, Hero)
    elif val_5 == "stanna":
        print("")
        sleep(2)
        print("En tunn figur träder fram ur skuggorna. Figuren tar gestalten av en gammal kvinna.")
        sleep(2)
        print("")
        print("Kvinnan har krokig rygg, hennes skrovliga ansikte tycks olikt det av en människa och huden tycks obeskrivigt torr i det dunkla skenet.")
        sleep(2)
        print("")
        print("Nästan som att den skulle brista vid minsta beröring.")
        sleep(2)
        print("")
        print ("Med en klar och stark röst olikt dina förväntningar tar kvinnan till orda. Hon säger, lös min gåta och ta del av belöningen: ")
        print("")
        svargåta1 = ""
        n=0
        förmångaförsök = False
        while svargåta1 != "n":
            svargåta1 = input("Med vad börjar natten och slutar dagen? Du har 3 försök(_): ")
            n += 1
            if n > 3:
                förmångaförsök = True
                break
        else :
            print("")
            print("Utmärkt unge man! Här är din belöning")
            print("")
            sleep(2)
            print ("Gumman sträcker fram en underlig glasflaska med en klar röd, svagt skimrande vätska inuti. Flaskan är förseglad med en kork som mörknat.")
            print("")
            sleep(2)
            val_6 = input (" Vill du dricka innehållet i flaskan eller inte? (ja/nej): ")
            if val_6 == "ja" :
                print ("")
                Hero.max_health +=10
                Hero.health +=10
                print("Health increased by 10!")
                print("")
            elif val_6 == "nej" :
                print ("Du litar inte på innehållet och slänger flaskan i första bästa soptunna.")
                print("")
                sleep(2)
                        
        if förmångaförsök == True :
            print("Bättre lycka nästa gång! Svaret var n!")
            print("")
            sleep(2)
        print ("Den underliga figuren ger dig en sista blick innan du försvinner bort runt nästa huskrök. Du går nu på en gata som leder dig bort mot din lägenhet.")
        print("")
        sleep(2)
        val_7= input("Vill du fortsätta framåt? (ja/nej): ")
        if val_7 == "ja":
            print("")
            sleep(2)
            print("Snyggt! Smart beslut! Du ville ju gå hem!")
        elif val_7 == "nej":
            print("")
            sleep(2)
            print("Varför inte? Du ville ju gå hem! Du går hemåt ändå...")
            print("Mot dig på trottoaren kommer en annan student! Hon har på sig en vikt hatt i papper och ser ut att vara i din ålder, hon kollar lurigt på dig.")
            print("")
            sleep(2)
            print("Hon brister ut, Jahaja, en spexkrigare från", nation, "nation!")
            print("")
            sleep(2)
            if nation in{"norrlands", "kalmars", "stockholms", "västmalands"}: 
                print("Men vi är ju från samma nation! WOW! Lycka till på vägen hem. Tjejen ger dig ett lock till en soptunna med ett handtag på toppen")
                print("")
                sleep(2)
                print("Soptunnelocket liknar en sköld och du känner dig plötsligt starkare.")
                #Ge lite Armour Albin
                Hero.armor +=1
                print("armor increased by 1!")

            else :
                val_8 = input("vad sägs om en Spexstrid? (ja/nej): ")
                if val_8 == "ja" :
                    print("")
                    sleep(2)
                    print ("abc")
                    spex_krigare1 = Spex_krigare()
                    combat(Hero,spex_krigare1,"Spexkrigaren slår dig hårt med sitt ballongsvärd!")
                    #Do strid against spexkrigare
                elif val_8 == "nej" :
                    print("")
                    sleep(2)
                    print ("Spexkrigaren från den andra nationen kollar stint på dig, men låter dig passera till slut.")
        
            print("Du går fundersamt gatan fram och funderar på det skumma mötet med studenten.")
        
        
def kapitel_2(Hero):    
    print("Du kommer till en korsning i vägen.") #"fortsätt här"
    print("")
    sleep(2)
    print("Snabbaste vägen hem är att ta den mindre stigen igenom skogen till höger, men den är inte upplyst! Den asfalterande vägen till vänster är större och upplyst men tar längre tid.")
    print("")
    sleep(2)
    val_4 = input("Tar du vänster eller rakt fram? (framåt/vänster): ")
    if val_4 == "framåt":
        print("")
        sleep(2)
        print("Du tar stigen igenom skogen. Halvvägs igenom skogen ser du 3 personer med ov-ar närma sig.")
        sleep(2)
        print("")
        val_5 = input("Vad gör du? (fly/strid): ")
        if val_5 == "fly":
            sleep(2)
            print ("Du försöker fly men studenterna omringar dig och uppmanar dig att anta utmaningen om spexstrid")
            print("")
            sleep(2)
            student_goons1 = Student_Goons()
            combat(Hero,student_goons1,"Studenterna turas om att slå dig!")
            print("")
        elif val_5 == "strid" :
            print("strid")
            student_goons1 = Student_Goons()
            combat(Hero,student_goons1,"Studenterna turas om att slå dig!")
            #DO STRID AGAINST GOONS

    elif val_4 == "vänster" :
        print("")
        sleep(2)
        print("Du går längs med den väl upplysta vägen runt den skog som du annars hade korsat.")
        print("")
        sleep(2)
        print("Under en gatlyckta en bit fram ser du vad som ser ut att vara en tant.")
        print("")
        sleep(2)
        print("Kvinnan har en märklig uppsyn, hennes ansikt tycks hårdnat, torrt och skrovligt.")
        print("")
        sleep(2)
        print("Som att det är många hundra år. I det dunkla skenet från gatlycktan ser hon nästintill dammig ut.")
        print("")
        sleep(2)
        print("Tanten känns obeskrivligt bekant. Hon stirrar på dig som du närmar dig på den kyliga asfalten")
        print("")
        sleep(2)
        print("Hon utbrister i en klar och stark stämma som du är på väg att gå förbi henne!..")
        print("")
        sleep(2)
        print("Vill du vara så vänlig och svara på min gåta så skall jag belöna dig rikigt unge hern!")
        print("")
        sleep(2)
        svargåta2 = ""
        n=0
        förmångaförsök2 = False
        while svargåta2 != "trappan":
            svargåta2 = input("Vad går upp och ner utan att röra på sig? Du har 3 försök att gissa rätt...(_._._._._._._): ")
            n += 1
            if n > 2:
                förmångaförsök2 = True
                break
        else :
            print("")
            sleep(2)
            print("Bra jobbat min vän, för dina besvär skall du ha en påse guldpengar!")
            print("")
            sleep(2)
            print("gumman sträcker över en skinnsäck men något tungt innuti.")
            print("")
            sleep(2)
            print("Du tar emot säcken och tackar gumman som när du några steg senare vänder dig om för att ge en sista blick är bort!")

        if förmångaförsök2 == True :
            print("Bättre lycka nästa gång min vän")
        print("")
        sleep(2)
    print("Du går vidare och kommer fram till punkten där den snabbare skogsvägen möter den väl upplysta vägen. Nu är det nära hem.")
    print("")
    sleep(2)
    print("Du ser nu din lägenhetsport i fjärran. Ett leende sprider sig på dina läppar.")
    print("")
    sleep(2)
    print("Du rör dig mot den lilla fyrkantiga dörren som växer och växer som du kommer närmare")
    print("")
    sleep(2)
    print("Men plötsligtkänner du skugga falla över dig. Håret i nacken reser sig och du känner en iskall blixt ståla längsmed ryggraden.")
    print("")
    sleep(2)
    print("Du får en akut känsla av att något eller någon övervakar dig.")
    print("")
    sleep(2)
    val_9 = input("Vad gör du? Bryt ut i spurt och ta dig till säkerheten av lägenhetsporten, eller vänder du dig om och möter hotet som du misstänker är dig tätt i hälarna. (framåt/stanna): ")
    if val_9 == "stanna" :
        print("Du vänder dig om och med ens känner du hur mörkret sluter sig kring dig. Ett motstötande dödskrik urskiljer ur tystnaden, och ökar i intencitet tills det är olidligt högt")
        print("Du känner hur benen sviker  dig och du faller ner på knä. Mörkret är nu tatalt och du känner dig trött. Skallbenet krasar när det träffar trotoarkanten.")
        Game_over()
        return
    elif val_9 == "framåt":
        print("Du sprintar mot lägenhetsdörren och kastar dig innanför den skyddande dörren som slår igen med en duns.")
        print ("GRATTIS DU HAR KLARAT SPELET!")
        sleep(5)
######## Chapter 2




###
### Combat CODE!
###



def clear():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
class Hero:
    name = "You"
    max_health = 30
    health = 30
    attack_Damage = 3
    armor = 1
    healing = 10
    
    def take_damage(self,damage):
        self.health -= damage
        return self.health
    def options(self):
        print(f"1) Attack \n2) heal \n3) run")
    def check_dead(self):
        if self.health <=0:
            clear()
            print("GAME OVER NOOBA")
            exit()

class Anka:
    name = "Anka"
    health = 15
    attack_Damage = 2
    armor = 1

    def take_damage(self,damage):
        self.health -= damage
        return self.health
class Student_Goons:
    name = "Student Goons"
    health = 20
    attack_Damage = 3
    armor = 1

    def take_damage(self,damage):
        self.health -= damage
        return self.health

class Spex_krigare:
    name = "Spex Krigare"
    health = 25
    attack_Damage = 3
    armor = 1

    def take_damage(self,damage):
        self.health -= damage
        return self.health

    
    
def combat_hud(char):
    print(char.name)
    print(" __________________")
    print(f" Health Points: {char.health} \n Attack Damage: {char.attack_Damage}  \n Defense: {char.armor}   ")
    print(" __________________")

def combat(hero,enemy,enemy_prompt):
    val = ""
    clear()
    while enemy.health > 0:
        combat_hud(hero)
        combat_hud(enemy)
        hero.options()
        dmg_taken_hero_calc = 0
        dmg_taken_enemy_calc = 0
        
        val = input("Choose action: ")
        if val == "1":
            if randint(0,1) == 1:
                dmg_taken_enemy_calc = 2*hero.attack_Damage-enemy.armor
                enemy.take_damage(dmg_taken_enemy_calc)
            else:
                dmg_taken_enemy_calc = hero.attack_Damage-enemy.armor
                enemy.take_damage(dmg_taken_enemy_calc)
                
        elif val == "2":
            if hero.max_health - hero.health <= hero.healing:
                Healprompt = "Du healar till max hp"
                hero.health = hero.max_health
            else:
                hero.health += hero.healing
                Healprompt = f"du healar upp ditt hp med {hero.healing}"
        ### Enemies time to hit back (can fix so it can do special attacks if time is left over.
        if randint(1,3) == 3:
            dmg_taken_hero_calc = enemy.attack_Damage*2-hero.armor
            hero.take_damage(dmg_taken_hero_calc)
        else:
            dmg_taken_hero_calc = enemy.attack_Damage-hero.armor
            hero.take_damage(dmg_taken_hero_calc)
        hero.check_dead()
            
        clear()
        
        if val =="1":
            print(f"Du anfaller och gör {dmg_taken_enemy_calc} skada!")
        elif val == "2":
            print(Healprompt)
        print(f"\n{enemy_prompt} för {dmg_taken_hero_calc} skada!")
    clear()
    print(f"You won the fight! holy poggers")







                
#Spelkoden börjar

print("Formatet på spelet är sådant att du endast kommer svara med små bokstäver dvs: RÄTT=abc apa, gris, FEL=ABC, Apa, Gris. DETTA ÄR EN VIKTIG ASPEKT AV SPELET!")
print("Ofta ges tips på vad svaret borde vara i en ruta med formatet (svar1/svar2) ibland kommer vi vilja ha ett input från dig.")
print("Det kan se ut såhär: skriv ditt namn (______ efternamn) svaret skall då vara ditt namn, tillexempel, tomas med små bokstäver!")
print("")
sleep(6)

huvud_karaktär = Hero()



username = input("Vad är ditt namn: ")
print("")
print ("Välkommen",username)
print("")
nation = input("Vilken Studentnation vill du spela för ( _____ nation) ")
print("")
print (nation, "nation")
print("")
startgame = input("Starta Spelet? (ja/nej) ")


if startgame == "ja":
    PrologYN = input("Vill du läsa Prologen? (Rekomenderas vid första genomspelningen(ja/nej)): ")
    if PrologYN == "ja":
        print (Intro_prolog())  
else:
    print ("OK, Bye")

clear()               
val_1 = input ("Till höger ser du en upplyst trottoar, och rakt fram en mörk gränd. Vilket håll vill du gå åt? (framåt/höger): ")
if val_1 == "höger":
    Del_1(val_1,huvud_karaktär)
    
elif val_1 == "framåt":
    Del_2(huvud_karaktär)

kapitel_2(huvud_karaktär)

    

