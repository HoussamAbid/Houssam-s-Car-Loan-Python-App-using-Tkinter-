from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from turtle import home
from datetime import date

#1
class Voiture:
    def __init__(self,immatriculation=1, marque="", carburant="", modele=2, puissance=3):
        self.__immatriculation=immatriculation
        self.__marque=marque
        self.__carburant=carburant
        self.__modele=modele
        self.__puissance=puissance     
    @property
    def immatriculation(self):
        return  self.__immatriculation
    @immatriculation.setter
    def immatriculation(self,I):
        self.__immatriculation=I
        
    @property
    def marque(self):
        return  self.__marque
    @marque.setter
    def marque(self,I):
        self.__marque=I
        
    @property
    def carburant(self):
      return self.__carburant
    
    @carburant.setter
    def carburant(self,I):
         self.__carburant=I
        
    @property
    def modele(self):
        return  self.__modele
    @modele.setter
    def modele(self,I):
        self.__modele=I
        
    @property
    def puissance(self):
        return  self.__puissance
    @puissance.setter
    def puissance(self,I):
        self.__puissance=I


    def __str__(self):
        return f"immatriculation:{self.immatriculation} || marque:{self.marque}|| carburant:{self.carburant}|| modele:{self.modele}|| puissance:{self.puissance}"
#2
class VoitureVip(Voiture):
    def __init__(self,immatriculation=111, marque="marque", carburant="gazoile", modele=2000, puissance=33,tupe=""):
        super().__init__(immatriculation,marque,carburant,modele,puissance)
        if tupe=="4*4" or tupe=="SUV"  or tupe=="minibus"  or tupe=="limousine":
            self.__tupe=tupe
        else:
            print("type invalide")
    @property
    def tupe(self):
        return  self.__tupe
    @tupe.setter
    def tupe(self,t):
        if t=="4*4" or t=="SUV"  or t=="minibus"  or t=="limousine":
            self.__tupe=t
        else:
            print("type invalide")
    def __str__(self):
        return f"{super().__str__()},type:{self.tupe}"

#3

class VoitureCitadinne(Voiture):
    def __init__(self,immatriculation=1, marque="", carburant="", modele=2, puissance=3,gamme=""):
        super().__init__(immatriculation,marque,carburant,modele,puissance)
        if gamme=="A" or gamme=="B"  or gamme=="C":
            self.__gamme=gamme
        else:
            print("gamme invalide")
    @property
    def gamme(self):
        return  self.__gamme
    @gamme.setter
    def gamme(self,g):
        if g=="A" or g=="B"  or g=="C":
            self.__gamme=g
        else:
            print("gamme invalide")
    def __str__(self):
        return f"{super().__str__()},gamme:{self.gamme}"
##
class ListeVoiture:
    def __init__(self, lv=[]):
        self.__listevoiture=lv

    @property
    def listevoiture(self):
        return  self.__listevoiture
    @listevoiture.setter
    def listevoiture(self,I):
        self.__listevoiture=I

    def __str__(self):
        return f"Liste DES Voitures:{self.listevoiture}"
    
    def AjouterVoiture(self,voiture):
        if voiture in self.listevoiture:
            print("CETTE VOITURE DEJA LA")
            return False
        else:
            self.listevoiture.append(voiture)
            return True

    def SupprimerVoiture(self,immatriculation):
        for i in self.listevoiture:
            if i.immatriculation==immatriculation:
                self.listevoiture.remove(i)
                return True
        print("CETTE VOITURE NE EXISTE PAS")
        return False
        
    def ModifierVoiture(self,voiture):
        for i in self.listevoiture:
            if i.immatriculation==voiture.immatriculation:
                i.marque=voiture.marque
                i.carburant=voiture.carburant
                i.modele=voiture.modele
                i.puissance=voiture.puissance
                if hasattr(i,"tupe"):
                    i.tupe=voiture.tupe
                else:
                    i.gamme=voiture.gamme
                return True
        print("CETTE VOITURE NE EXISTE PAS")
        return False
#4

class Personne:
    def __init__(self,cin="",nom="",prenom=""):
        self._cin=cin
        self._nom=nom
        self._prenom=prenom
    @property
    def cin(self):
        return  self._cin
    @cin.setter
    def cin(self,I):
        self._cin=I
        
    @property
    def nom(self):
        return  self._nom
    @nom.setter
    def nom(self,I):
        self._nom=I

    @property
    def prenom(self):
        return  self._prenom
    @prenom.setter
    def prenom(self,I):
        self._prenom=I
    

    def __str__(self):
        return f"CIN:{self.cin},Nom:{self.nom},Prenom:{self.prenom}"
per=Personne("H000","Houssam","Eddine")
per.__str__()


#5
class Client(Personne) :
    def __init__(self,cin="",nom="",prenom="",NumPermis=1 , tele=000000000):
        super().__init__(cin,nom,prenom)
        self.__NumPermis=NumPermis
        self.__tele=tele
    @property
    def NumPermis(self):
        return  self.__NumPermis
    @NumPermis.setter
    def NumPermis(self,I):
        self.__NumPermis=I
        
    @property
    def tele(self):
        return  self.__tele
    @tele.setter
    def tele(self,I):
        self.__tele=I

    def __str__(self):
        return f"{super().__str__()},NumPermis:{self.NumPermis},tele:{self.tele}"
        
c=Client("H000","Houssam","Eddine",0000,0000000000)
c.__str__()

#6
class Location:
    auto=0
    def __init__(self,datelocation=date(1,1,1),durelocation=1,prixlocation=2,client=Client(),voiture=Voiture()):
        self.__idLocation=Location.auto
        Location.auto+=1
        self.__datelocation=datelocation
        self.__durelocation=durelocation
        self.__prixlocation=prixlocation
        self.__client=client
        self.__voiture=voiture
    @property
    def idLocation(self):
        return  self.__idLocation
    @property
    def datelocation(self):
        return  self.__datelocation
    @datelocation.setter
    def datelocation(self,I):
        self.__datelocation=I
        
    @property
    def durelocation(self):
        return  self.__durelocation
    @durelocation.setter
    def durelocation(self,I):
        self.__durelocation=I
        
    @property
    def prixlocation(self):
      return self.__prixlocation
    @prixlocation.setter
    def prixlocation(self,I):
         self.__prixlocation=I
        
    @property
    def client(self):
        return  self.__client
    @client.setter
    def client(self,I):
        self.__client=I
        
    @property
    def voiture(self):
        return  self.__voiture
    @voiture.setter
    def voiture(self,I):
        self.__voiture=I
    def __str__(self):
        return f"id Location:{self.idLocation},date de location:{self.datelocation} ,durée de location:{self.prixlocation} ,prix de location:{self.prixlocation} ,Client:{self.client} ,Voiture:{self.voiture}"
#7
class Utilisateur(Personne):
    def __init__(self,cin="H000",nom="",prenom="",login="",motpasse="",email=""):
        super().__init__(cin,nom,prenom)
        self.__login=login
        self.__motpasse=motpasse
        self.__email=email
    @property
    def login(self):
        return  self.__login
    @login.setter
    def login(self,I):
        self.__login=I
        
    @property
    def motpasse(self):
        return  self.__motpasse
    @motpasse.setter
    def motpasse(self,I):
        self.__motpasse=I

    @property
    def email(self):
        return  self.__email
    @email.setter
    def email(self,I):
        self.__email=I
    

    def __str__(self):
        return f"{super().__str__()},LOGIN:{self.login},PASSWORD:{self.motpasse},EMAIL:{self.email}"
#8
class ListeUtilisateur:
    def __init__(self,lU=[]):
        self.__listeUtilisateurs=lU
    @property
    def listeUtilisateurs(self):
        return  self.__listeUtilisateurs
    @listeUtilisateurs.setter
    def listeUtilisateurs(self,I):
        self.__listeUtilisateurs=I

    def __str__(self):
        return f"liste de l'Utilisateurs:{self.listeUtilisateurs}"

    def Authentifier(self,login,mdp):
        for i in self.listeUtilisateurs:
            if i.login==login and i.motpasse==mdp:
                print("Authentification valide")
                return True
        return False                      

    def AjouterUtilisateur(self,utilisateur):
        if utilisateur in self.listeUtilisateurs:
            print("ce Utilisateur déja exciste")
            return False
        else:
            self.listeUtilisateurs.append(utilisateur)
            return True


    def SupprimerUtilisateur(self,login):
        for i in self.listeUtilisateurs:
            if i.login==login:
                self.listeUtilisateurs.remove(i)
                return True
        print("ce Utilisateur n'existe pas")
        return False

    def ModifierUtilisateur(self,utilisateur):
        for i in self.listeUtilisateurs:
            if i.login==utilisateur.login:
                i.cin=utilisateur.cin
                i.nom=utilisateur.nom
                i.prenom=utilisateur.prenom
                i.motpasse=utilisateur.motpasse
                i.email=utilisateur.email
#9
class ListeClient:
    def __init__(self,lc=[]):
        self.__listeclient=lc

    @property
    def listeclient(self):
        return  self.__listeclient
    @listeclient.setter
    def listeclient(self,I):
        self.__listeclient=I

    def __str__(self):
        return f"LISTE DES CLIENT :{self.listeclient}"

    def AjouterClient(self,client):
        if client in self.listeclient:
            print("DEJA EXISTE")
            return False
        else:
            self.listeclient.append(client)
            return True


    def SupprimerClient(self,cin):
        for i in self.listeclient:
            if i.cin==cin:
                self.listeclient.remove(i)
                return True
        print("Ce Client n'existe pas")
        return False

    def ModifierClient(self,client):
        for i in self.listeclient:
            if i.cin==client.cin:
                i.nom=client.nom
                i.prenom=client.prenom
                i.NumPermis=client.NumPermis
                i.tele=client.tele
#10
class ListeLocation:
    def __init__(self,L=[]):
        self.__listeLocation=L

    @property
    def listeLocation(self):
        return  self.__listeLocation
    @listeLocation.setter
    def listeLocation(self,I):
        self.__listeLocation=I

    def __str__(self):
        return f"Liste DES LOCATIONS:{self.listeLocation}"

    def AfficherListeLocation(self):
        for i in self.listeLocation:
            print(i)

    def AfficherListeLocationCitadine(self):
        lvc=[]
        for i in self.listeLocation:
            if isinstance(i.voiture,VoitureCitadinne)==True:
                lvc.append(i)
        return lvc

    def AfficherListeLocationVip(self):
        lvv=[]
        for i in self.listeLocation:
            if isinstance(i.voiture,VoitureVip)==True:
                lvv.append(i)
        return lvv
    def AfficherLocationMarque(self,marque):
        mr=[]
        for i in self.listeLocation:
            if i.voiture.marque==marque:
                mr.append(i)
                print(i)
        return mr

    def AfficherLocationImma(self,Immatriculation):
        imm=[]
        for i in self.listeLocation:
            if i.voiture.immatriculation==Immatriculation:
                imm.append(i)
                print(i)
        return imm
            
    def AjouterLocation(self,location):
        if location in self.listeLocation:
            print("CETTE LOCATION DEJA LA")
            return False
        else:
            self.listeLocation.append(location)
            return True
    def AfficherLocationClient(self,Cin):
        imm=[]
        for i in self.listeLocation:
            if i.client.cin==Cin:
                imm.append(i)
                print(i)
        return imm
        
    def SupprimerLocation(self,idd):
        for i in self.listeLocation:
            if i.idLocation==idd:
                self.listeLocation.remove(i)
                return True
        print("CETTE LOCATIN NE EXISTE PAS")
        return False
    def ModifierLocation(self,location):
         for i in self.listeLocation:
            if i.idLocation==location.idLocation:
                i.datelocation=location.datelocation
                i.durelocation=location.durelocation
                i.prixlocation=location.prixlocation
                i.client=location.client
                i.voiture=location.voiture
        
    def FiltrerLocationDate(self,date):
        fdate=[]
        for i in self.listeLocation:
            if i.datelocation==date:
                fdate.append(i)
        return fdate
#   #   #



ut=Utilisateur("H000","Houssam","Abid","sam","1234","sam@gmail.com")
ut2=Utilisateur("a","a","a","a","a","a")
lut=ListeUtilisateur([ut,ut2])

cl1=Client("H000","Houssam","Abid",000,00000000)
cl2=Client("a","a","a",0,00)
lstcl=ListeClient([cl1,cl2])


vv=VoitureVip("A111","LUXIS","FUEL",2020,1000,"SPORT CAR")
vv2=VoitureVip("B111","LAMBO","FUEL",2019,800,"CASUAL")
vv3=VoitureVip("C111","MERCEDES","essense",2021,1200,"4*4")


vc=VoitureCitadinne("A222","Dacia","Fuel",2007,500,"B")
vc2=VoitureCitadinne("B222","HONDA","Fuel",2011,700,"B")
vc3=VoitureCitadinne("C222","VOLSWAGEN","Fuel",2013,600,"A")
lstvoiture=ListeVoiture([vv,vv2,vv3,vc,vc2,vc3])

loc=Location(date(2020,4,6),52,500,cl1,vc2)
loc1=Location(date(2019,11,5),59,600,cl2,vv2)
lstlocation=ListeLocation([loc,loc1])

Authentification=Tk()
Authentification.title("Bonjour ,Welcome ,مرحبا ,Hola !!")
Authentification.geometry("1080x720")
Authentification.configure(bg="white")


lbltitile=Label(Authentification,text=" FAIT L'AUTHENTIFICATION",font=("Times",25,'bold italic'),fg="black", bg="tomato")
lbltitile.place(x=270,y=40)

login=Label(Authentification,text="Login (username) :", bg="white" ,font=("Times",15,'bold'),fg="black")
login.place(x=100,y=130)
entrylogin=Entry(Authentification,width=15,bd=2,font=("Times",15))
entrylogin.place(x=700,y=130)


mdp=Label(Authentification,text="Mot De Pass (Password) :", bg="white" ,font=("Times",15,'bold'),fg="black")
mdp.place(x=100,y=180)
entrymdp=Entry(Authentification,width=15,bd=2,font=("Times",15),show="*")
entrymdp.place(x=700,y=180)

def authentifier():
    login=entrylogin.get()
    mdp=entrymdp.get()
    valide=lut.Authentifier(login,mdp)
    if valide:
        Authentification.destroy()
    else:
        messagebox.showinfo("UTILISATEUR NEXISTE PAS || USER NOT FOUND")
          
connecter=Button(Authentification,text="CONNECT",font=("Times",15,'bold italic'),fg="black",bg="tomato",command=lambda:authentifier())
connecter.place(x=420,y=400)

Authentification.mainloop()

Accueil=Tk()
Accueil.title("LA PAGE D'ACCEIL || HOME PAGE")
Accueil.geometry("1080x720")
Accueil.configure(bg="tomato")

def child1():
    child=Toplevel(Accueil)
    child.geometry("700x700")
    child.title("Ajouter : Utilisteur")
    child.configure(bg="salmon")

    cin=Label(child,text="CIN",font=("Times",12,'bold'),fg="black",bg="salmon")
    cin.place(x=100,y=80)
    entrycin=Entry(child,width=15,bd=2,font=("Times",12))
    entrycin.place(x=230,y=80)

    nom=Label(child,text="NAME",font=("Times",12,'bold'),fg="black",bg="salmon")
    nom.place(x=100,y=120)
    entrynom=Entry(child,width=15,bd=2,font=("Times",12))
    entrynom.place(x=230,y=120)

    prenon=Label(child,text="LAST NAME:",font=("Times",12,'bold'),fg="black",bg="salmon")
    prenon.place(x=100,y=160)
    entryprenon=Entry(child,width=15,bd=2,font=("Times",12))
    entryprenon.place(x=230,y=160)

    log=Label(child,text="LOGIN :",font=("Times",12,'bold'),fg="black",bg="salmon")
    log.place(x=100,y=200)
    entrylog=Entry(child,width=15,bd=2,font=("Times",12))
    entrylog.place(x=230,y=200)

    mtop=Label(child,text="PASSWORD :",font=("Times",12,'bold'),fg="black",bg="salmon")
    mtop.place(x=100,y=240)
    entrymotp=Entry(child,width=15,bd=2,font=("Times",12),show="*")
    entrymotp.place(x=230,y=240)

    email=Label(child,text="E-MAIL",font=("Times",12,'bold'),fg="black",bg="salmon")
    email.place(x=100,y=280)
    entryemail=Entry(child,width=15,bd=2,font=("Times",12) ,bg="salmon")
    entryemail.place(x=230,y=280)

    def ajouterUtilisateur():
        cin=entrycin.get()
        nom=entrynom.get()
        prenom=entryprenon.get()
        login=entrylog.get()
        mtop=entrymotp.get()
        email=entryemail.get()
        utilisateur=Utilisateur(cin,nom,prenom,login,mtop,email)
        valide=lut.AjouterUtilisateur(utilisateur)
        if valide:
            messagebox.showinfo("UTILISATEUR AJOUTE AVEC SUCCE")
        else:
            messagebox.showinfo("DEJA EXISTE")

    enregistrer=Button(child,text="Enregistrer",font=("Times",12,'bold'),fg="black",bg="tomato",command=lambda:ajouterUtilisateur())
    enregistrer.place(x=500,y=280)
    

def child2():
    child=Toplevel(Accueil)
    child.geometry("1080x720")
    child.title("AFFICHAGE UTILISATEUR")
    child.configure(bg="salmon")
    value=[]

    def selectItem(a):
        curItem = tree.focus()
        value=tree.item(curItem).get("values")
   

    def supprimerUtilisateur():
        curItem = tree.focus()
        value=tree.item(curItem).get("values")
        lut.SupprimerUtilisateur(str(value[3]))
        selected_item = tree.selection()[0] 
        tree.delete(selected_item)

    def modifierUtilisateur():
        curItem = tree.focus()
        value=tree.item(curItem).get("values")
        child2=Toplevel(child)
        child2.geometry("500x500")
        child2.title("Modifier Utilisateur")
        child2.configure(bg="tomato")
        selected_item = tree.selection()[0] 

        cin=Label(child2,text="CIN :",font=("Times",12,'bold'),fg="black",bg="salmon")
        cin.place(x=100,y=80)
        entrycin=Entry(child2,width=15,bd=2,font=("Times",12))
        entrycin.place(x=230,y=80)
        entrycin.insert(END,str(value[0]))
        entrycin.config(state='disabled')

        nom=Label(child2,text="Nom :",font=("Times",12,'bold'),fg="black",bg="salmon")
        nom.place(x=100,y=120)
        entrynom=Entry(child2,width=15,bd=2,font=("Times",12))
        entrynom.place(x=230,y=120)
        entrynom.insert(END,str(value[1]))

        prenon=Label(child2,text="Prenom:",font=("Times",12,'bold'),fg="black",bg="salmon")
        prenon.place(x=100,y=160)
        entryprenon=Entry(child2,width=15,bd=2,font=("Times",12))
        entryprenon.place(x=230,y=160)
        entryprenon.insert(END,str(value[2]))

        log=Label(child2,text="Login :",font=("Times",12,'bold'),fg="black",bg="salmon")
        log.place(x=100,y=200)
        entrylog=Entry(child2,width=15,bd=2,font=("Times",12))
        entrylog.place(x=230,y=200)
        entrylog.insert(END,str(value[3]))

        mtop=Label(child2,text="Mot De Passe :",font=("Times",12,'bold'),fg="black",bg="salmon")
        mtop.place(x=100,y=240)
        entrymotp=Entry(child2,width=15,bd=2,font=("Times",12),show="*")
        entrymotp.place(x=230,y=240)
        entrymotp.insert(END,str(value[4]))

        email=Label(child2,text="Email :",font=("Times",12,'bold'),fg="black",bg="salmon")
        email.place(x=100,y=280)
        entryemail=Entry(child2,width=15,bd=2,font=("Times",12))
        entryemail.place(x=230,y=280)
        entryemail.insert(END,str(value[5]))
        def modifier():
            cin=entrycin.get()
            nom=entrynom.get()
            prenom=entryprenon.get()
            login=entrylog.get()
            mtop=entrymotp.get()
            email=entryemail.get()
            utilisateur=Utilisateur(cin,nom,prenom,login,mtop,email)
            lut.ModifierUtilisateur(utilisateur)
            tree.delete(selected_item)
            row = [cin,nom,prenom,login,mtop,email]
            tree.insert('', END, values= row)         

        Modifier=Button(child2,text="MODIFY",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:modifier())
        Modifier.place(x=330,y=330)
 

    modifier=Button(child,text="MODIFY",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:modifierUtilisateur())
    modifier.place(x=270,y=360)
    supprimer=Button(child,text="DELETE",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:supprimerUtilisateur())
    supprimer.place(x=370,y=360)

    tree=ttk.Treeview(child,columns=(1,2,3,4,5,6),heigh=5,show="headings")
    tree.place(x=50,y=50,width=750,height=225)

    tree.heading(1,text="CIN")
    tree.heading(2,text="Nom")
    tree.heading(3,text="Prenon")
    tree.heading(4,text="Login")
    tree.heading(5,text="Mot De Passe")
    tree.heading(6,text="Email")

    tree.column(1,width=100)
    tree.column(2,width=100)
    tree.column(3,width=100)
    tree.column(4,width=100)
    tree.column(5,width=100)
    tree.column(6,width=250)

    for i in lut.listeUtilisateurs:
        row = [i.cin,i.nom,i.prenom,i.login,i.motpasse,i.email]
        tree.insert('', END, values= row)

    tree.bind('<ButtonRelease-1>', selectItem)


def child3():
    child=Toplevel(Accueil)
    child.geometry("500x500")
    child.title("Ajouter Client")
    child.configure(bg="tomato")

    cin=Label(child,text="CIN :",font=("Times",12,'bold'),fg="black",bg="salmon")
    cin.place(x=100,y=80)
    entrycin=Entry(child,width=15,bd=2,font=("Times",12))
    entrycin.place(x=220,y=80)

    nom=Label(child,text="NAME",font=("Times",12,'bold'),fg="black",bg="salmon")
    nom.place(x=100,y=120)
    entrynom=Entry(child,width=15,bd=2,font=("Times",12))
    entrynom.place(x=220,y=120)

    prenon=Label(child,text="LAST NAME",font=("Times",12,'bold'),fg="black",bg="salmon")
    prenon.place(x=100,y=160)
    entryprenon=Entry(child,width=15,bd=2,font=("Times",12))
    entryprenon.place(x=220,y=160)

    nump=Label(child,text="NUMERO DE PERMIS:",font=("Times",12,'bold'),fg="black",bg="salmon")
    nump.place(x=100,y=200)
    entrynump=Entry(child,width=15,bd=2,font=("Times",12))
    entrynump.place(x=220,y=200)

    tele=Label(child,text="TETEPHONE :",font=("Times",12,'bold'),fg="black",bg="salmon")
    tele.place(x=100,y=240)
    entrytele=Entry(child,width=15,bd=2,font=("Times",12))
    entrytele.place(x=220,y=240)
    def ajouterClient():
        cin=entrycin.get()
        nom=entrynom.get()
        prenom=entryprenon.get()
        permi=entrynump.get()
        tele=entrytele.get()
        client=Client(cin,nom,prenom,permi,tele)
        valide=lstcl.AjouterClient(client)
        if valide:
            messagebox.showinfo("AJOUTER AVEC SUCCEE")
        else:
            messagebox.showinfo("CLIENT ALREADY EXIST")

    enregistrer=Button(child,text="S'enregister",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:ajouterClient())
    enregistrer.place(x=330,y=330)
    

def child4():
    child=Toplevel(Accueil)
    child.geometry("1080x720")
    child.title("CLIENTV AFFICHAGEt")
    child.configure(bg="tomato")
    value=[]

    def selectItem(a):
        curItem = tree.focus()
        value=tree.item(curItem).get("values")
   

    def supprimerClient():
        curItem = tree.focus()
        value=tree.item(curItem).get("values")
        lstcl.SupprimerClient(str(value[0]))
        selected_item = tree.selection()[0] 
        tree.delete(selected_item)

    def modifierClient():
        curItem = tree.focus()
        value=tree.item(curItem).get("values")
        child2=Toplevel(child)
        child2.geometry("500x500")
        child2.title("Modifier l'tilisateur")
        child2.configure(bg="tomato")
        selected_item = tree.selection()[0] 

        cin=Label(child2,text="CIN :",font=("Times",12,'bold'),fg="black",bg="salmon")
        cin.place(x=100,y=80)
        entrycin=Entry(child2,width=15,bd=2,font=("Times",12))
        entrycin.place(x=220,y=80)
        entrycin.insert(END,str(value[0]))
        entrycin.config(state='disabled')

        nom=Label(child2,text="NAME",font=("Times",12,'bold'),fg="black",bg="salmon")
        nom.place(x=100,y=120)
        entrynom=Entry(child2,width=15,bd=2,font=("Times",12))
        entrynom.place(x=220,y=120)
        entrynom.insert(END,str(value[1]))

        prenon=Label(child2,text="LAST NAME",font=("Times",12,'bold'),fg="black",bg="salmon")
        prenon.place(x=100,y=160)
        entryprenon=Entry(child2,width=15,bd=2,font=("Times",12))
        entryprenon.place(x=220,y=160)
        entryprenon.insert(END,str(value[2]))

        
        nump=Label(child2,text="NMR PERMIS",font=("Times",12,'bold'),fg="black",bg="salmon")
        nump.place(x=100,y=200)
        entrynump=Entry(child2,width=15,bd=2,font=("Times",12))
        entrynump.place(x=220,y=200)
        entrynump.insert(END,str(value[3]))

        tele=Label(child2,text="TELEPHONE",font=("Times",12,'bold'),fg="black",bg="salmon")
        tele.place(x=100,y=240)
        entrytele=Entry(child2,width=15,bd=2,font=("Times",12))
        entrytele.place(x=220,y=240)
        entrytele.insert(END,str(value[4]))

        def modifier():
            cin=entrycin.get()
            nom=entrynom.get()
            prenom=entryprenon.get()
            numpermis=entrynump.get()
            tele=entrytele.get()
            client=Client(cin,nom,prenom,numpermis,tele)
            lstcl.ModifierClient(client)
            tree.delete(selected_item)
            row = [cin,nom,prenom,numpermis,tele]
            tree.insert('', END, values= row)

            

        Modifier=Button(child2,text="MODIFY",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:modifier())
        Modifier.place(x=330,y=330)
        
        
    modifier=Button(child,text="MODUFY",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:modifierClient())
    modifier.place(x=270,y=360)
    supprimer=Button(child,text="DELETE",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:supprimerClient())
    supprimer.place(x=370,y=360)

    tree=ttk.Treeview(child,columns=(1,2,3,4,5),heigh=5,show="headings")
    tree.place(x=50,y=50,width=500,height=225)

    tree.heading(1,text="CIN")
    tree.heading(2,text="NAME")
    tree.heading(3,text="LASTE NAME")
    tree.heading(4,text="CAR LICENSE NUMBER")
    tree.heading(5,text="PHONE NUMBER")

    tree.column(1,width=100)
    tree.column(2,width=100)
    tree.column(3,width=100)
    tree.column(4,width=100)
    tree.column(5,width=100)
   

    for i in lstcl.listeclient:
        row = [i.cin,i.nom,i.prenom,i.NumPermis,i.tele]
        tree.insert('', END, values= row)

    tree.bind('<ButtonRelease-1>', selectItem)


def child5():
    child=Toplevel(Accueil)
    child.geometry("500x500")
    child.title("Ajouter Voiture VIP :")
    child.configure(bg="tomato")

    im=Label(child,text="Immatriculation",font=("Times",12,'bold'),fg="black",bg="salmon")
    im.place(x=100,y=80)
    entryim=Entry(child,width=15,bd=2,font=("Times",12))
    entryim.place(x=260,y=80)

    mar=Label(child,text="Voiture Marque:",font=("Times",12,'bold'),fg="black",bg="salmon")
    mar.place(x=100,y=120)
    entrymar=Entry(child,width=15,bd=2,font=("Times",12))
    entrymar.place(x=260,y=120)

    car=Label(child,text="CARBURANT",font=("Times",12,'bold'),fg="black",bg="salmon")
    car.place(x=100,y=160)
    entrycar=Entry(child,width=15,bd=2,font=("Times",12))
    entrycar.place(x=260,y=160)

    mod=Label(child,text="YEAR MODEL",font=("Times",12,'bold'),fg="black",bg="salmon")
    mod.place(x=100,y=200)
    entrymod=Entry(child,width=15,bd=2,font=("Times",12))
    entrymod.place(x=260,y=200)

    pss=Label(child,text="PUISSANCE FISCALE",font=("Times",12,'bold'),fg="black",bg="salmon")
    pss.place(x=100,y=240)
    entrypss=Entry(child,width=15,bd=2,font=("Times",12))
    entrypss.place(x=260,y=240)

    tp=Label(child,text="TYPE",font=("Times",12,'bold'),fg="black",bg="salmon")
    tp.place(x=100,y=280)
    entrytp=Entry(child,width=15,bd=2,font=("Times",12))
    entrytp.place(x=260,y=280)

    def ajouterVoiture():
        Immatriculation=entryim.get()
        Marque=entrymar.get()
        Carburant=entrycar.get()
        Modele=entrymod.get()
        puissance=entrypss.get()
        Type=entrytp.get()
        voiture=VoitureVip(Immatriculation,Marque,Carburant,Modele,puissance,Type)
        valide=lstvoiture.AjouterVoiture(voiture)
        if valide:
            messagebox.showinfo("VOITURE AJOUTEE AVEC SUCCE")
        else:
            messagebox.showinfo("VOITURE DEJA EXISTE")

    enregistrer=Button(child,text="Enregistrer",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:ajouterVoiture())
    enregistrer.place(x=330,y=330)
   

def child7():
    child=Toplevel(Accueil)
    child.geometry("1080x720")
    child.title("Aficher Voiture Vip")
    child.configure(bg="tomato")
    value=[]

    def selectItem(a):
        curItem = tree.focus()
        value=tree.item(curItem).get("values")
   

    def supprimerVoitureVip():
        curItem = tree.focus()
        value=tree.item(curItem).get("values")
        lstvoiture.SupprimerVoiture(value[0])
        selected_item = tree.selection()[0] 
        tree.delete(selected_item)

    def modifierVoitureVip():
        curItem = tree.focus()
        value=tree.item(curItem).get("values")
        child2=Toplevel(child)
        child2.geometry("500x500")
        child2.title("Modifier Voiture Vip")
        child2.configure(bg="tomato")
        selected_item = tree.selection()[0] 
        
        im=Label(child2,text="Immatriculation :",font=("Times",12,'bold'),fg="black",bg="salmon")
        im.place(x=100,y=80)
        entryim=Entry(child2,width=15,bd=2,font=("Times",12))
        entryim.place(x=260,y=80)
        entryim.insert(END,value[0])
        entryim.config(state='disabled')

        mar=Label(child2,text="Marque Voiture",font=("Times",12,'bold'),fg="black",bg="salmon")
        mar.place(x=100,y=120)
        entrymar=Entry(child2,width=15,bd=2,font=("Times",12))
        entrymar.place(x=260,y=120)
        entrymar.insert(END,str(value[1]))

        car=Label(child2,text="Carburant",font=("Times",12,'bold'),fg="black",bg="salmon")
        car.place(x=100,y=160)
        entrycar=Entry(child2,width=15,bd=2,font=("Times",12))
        entrycar.place(x=260,y=160)
        entrycar.insert(END,str(value[2]))

        mod=Label(child2,text="CAR MODEL",font=("Times",12,'bold'),fg="black",bg="salmon")
        mod.place(x=100,y=200)
        entrymod=Entry(child2,width=15,bd=2,font=("Times",12))
        entrymod.place(x=260,y=200)
        entrymod.insert(END,value[3])
        

        pss=Label(child2,text="puissance fiscale",font=("Times",12,'bold'),fg="black",bg="salmon")
        pss.place(x=100,y=240)
        entrypss=Entry(child2,width=15,bd=2,font=("Times",12))
        entrypss.place(x=260,y=240)
        entrypss.insert(END,value[4])

        tp=Label(child2,text="TYPE",font=("Times",12,'bold'),fg="black",bg="salmon")
        tp.place(x=100,y=280)
        entrytp=Entry(child2,width=15,bd=2,font=("Times",12))
        entrytp.place(x=260,y=280)
        entrytp.insert(END,str(value[5]))

        def modifier():
            Immatriculation=entryim.get()
            Marque=entrymar.get()
            Carburant=entrycar.get()
            Modele=entrymod.get()
            puissance=entrypss.get()
            Type=entrytp.get()
            voiture=VoitureVip(int(Immatriculation),Marque,Carburant,int(Modele),int(puissance),Type)
            lstvoiture.ModifierVoiture(voiture)
            tree.delete(selected_item)
            row = [Immatriculation,Marque,Carburant,Modele,puissance,Type]
            tree.insert('', END, values= row)

        Modifier=Button(child2,text="MODIFY",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:modifier())
        Modifier.place(x=330,y=330)
 

    modifier=Button(child,text="MODIFY",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:modifierVoitureVip())
    modifier.place(x=270,y=360)
    supprimer=Button(child,text="DELETE",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:supprimerVoitureVip())
    supprimer.place(x=370,y=360)

    tree=ttk.Treeview(child,columns=(1,2,3,4,5,6),heigh=5,show="headings")
    tree.place(x=50,y=50,width=600,height=225)

    tree.heading(1,text="Immatriculation")
    tree.heading(2,text="MARQUE VOITURE")
    tree.heading(3,text="CARBURANT")
    tree.heading(4,text="MODEL YEAR")
    tree.heading(5,text="PUISSANCE FISCALE")
    tree.heading(6,text="TYPE")
    

    tree.column(1,width=100)
    tree.column(2,width=100)
    tree.column(3,width=100)
    tree.column(4,width=100)
    tree.column(5,width=100)
    tree.column(6,width=100)
   

    for i in lstvoiture.listevoiture:
        if hasattr(i,"TYPE"):
            row = [i.immatriculation,i.marque,i.carburant,i.modele,i.puissance,i.tupe]
            tree.insert('', END, values= row)

    tree.bind('<ButtonRelease-1>', selectItem)   

def child6():
    child=Toplevel(home)
    child.geometry("1080x720")
    child.title("Ajouter Voiture Citadinne")
    child.configure(bg="tomato")
    

    im=Label(child,text="Immatriculation :",font=("Times",12,'bold'),fg="black",bg="salmon")
    im.place(x=100,y=80)
    entryim=Entry(child,width=15,bd=2,font=("Times",12))
    entryim.place(x=260,y=80)

    mar=Label(child,text="MARQUE",font=("Times",12,'bold'),fg="black",bg="salmon")
    mar.place(x=100,y=120)
    entrymar=Entry(child,width=15,bd=2,font=("Times",12))
    entrymar.place(x=260,y=120)

    car=Label(child,text="CARBURANT :",font=("Times",12,'bold'),fg="black",bg="salmon")
    car.place(x=100,y=160)
    entrycar=Entry(child,width=15,bd=2,font=("Times",12))
    entrycar.place(x=260,y=160)

    mod=Label(child,text="MODEL YEAR :",font=("Times",12,'bold'),fg="black",bg="salmon")
    mod.place(x=100,y=200)
    entrymod=Entry(child,width=15,bd=2,font=("Times",12))
    entrymod.place(x=260,y=200)

    pss=Label(child,text="puissance fiscale :",font=("Times",12,'bold'),fg="black",bg="salmon")
    pss.place(x=100,y=240)
    entrypss=Entry(child,width=15,bd=2,font=("Times",12))
    entrypss.place(x=260,y=240)

    gm=Label(child,text="GAMME:",font=("Times",12,'bold'),fg="black",bg="salmon")
    gm.place(x=100,y=280)
    entrygm=Entry(child,width=15,bd=2,font=("Times",12))
    entrygm.place(x=260,y=280)
    def ajouterVoiture():
        Immatriculation=entryim.get()
        Marque=entrymar.get()
        Carburant=entrycar.get()
        Modele=entrymod.get()
        puissance=entrypss.get()
        gamme=entrygm.get()
        voiture=VoitureCitadinne(Immatriculation,Marque,Carburant,Modele,puissance,gamme)
        valide=lstvoiture.AjouterVoiture(voiture)
        if valide:
            messagebox.showinfo('Message succes',"Cette Voiture a bien été ajouté!!")
        else:
            messagebox.showinfo('Message D’Erreur',"Cette Voiture existe déjà")

    enregistrer=Button(child,text="Enregistrer",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:ajouterVoiture())
    enregistrer.place(x=330,y=330)
   

def child8():
    child=Toplevel(Accueil)
    child.geometry("1080x720")
    child.title("Aficher Voiture Citadinne")
    child.configure(bg="tomato")
    value=[]

    def selectItem(a):
        curItem = tree.focus()
        value=tree.item(curItem).get("values")
   

    def supprimerVoitureCitadinne():
        curItem = tree.focus()
        value=tree.item(curItem).get("values")
        lstvoiture.SupprimerVoiture(value[0])
        selected_item = tree.selection()[0] 
        tree.delete(selected_item)

    def modifierVoitureCitadinne():
        curItem = tree.focus()
        value=tree.item(curItem).get("values")
        child2=Toplevel(child)
        child2.geometry("1080x720")
        child2.title("Modifier Voiture Citadinne")
        child2.configure(bg="tomato")
        selected_item = tree.selection()[0] 
        
        im=Label(child2,text="Immatriculation :",font=("Times",12,'bold'),fg="black",bg="salmon")
        im.place(x=100,y=80)
        entryim=Entry(child2,width=15,bd=2,font=("Times",12))
        entryim.place(x=260,y=80)
        entryim.insert(END,value[0])
        entryim.config(state='disabled')

        mar=Label(child2,text="MARQUE",font=("Times",12,'bold'),fg="black",bg="salmon")
        mar.place(x=100,y=120)
        entrymar=Entry(child2,width=15,bd=2,font=("Times",12))
        entrymar.place(x=260,y=120)
        entrymar.insert(END,str(value[1]))

        car=Label(child2,text="Carburant :",font=("Times",12,'bold'),fg="black",bg="salmon")
        car.place(x=100,y=160)
        entrycar=Entry(child2,width=15,bd=2,font=("Times",12))
        entrycar.place(x=260,y=160)
        entrycar.insert(END,str(value[2]))

        mod=Label(child2,text="YEAR MODEL :",font=("Times",12,'bold'),fg="black",bg="salmon")
        mod.place(x=100,y=200)
        entrymod=Entry(child2,width=15,bd=2,font=("Times",12))
        entrymod.place(x=260,y=200)
        entrymod.insert(END,value[3])
        

        pss=Label(child2,text="puissance fiscale :",font=("Times",12,'bold'),fg="black",bg="salmon")
        pss.place(x=100,y=240)
        entrypss=Entry(child2,width=15,bd=2,font=("Times",12))
        entrypss.place(x=260,y=240)
        entrypss.insert(END,value[4])

        gm=Label(child2,text="GAMME",font=("Times",12,'bold'),fg="black",bg="salmon")
        gm.place(x=100,y=280)
        entrygm=Entry(child2,width=15,bd=2,font=("Times",12))
        entrygm.place(x=260,y=280)
        entrygm.insert(END,str(value[5]))

        def modifier():
            Immatriculation=entryim.get()
            Marque=entrymar.get()
            Carburant=entrycar.get()
            Modele=entrymod.get()
            puissance=entrypss.get()
            gamme=entrygm.get()
            voiture=VoitureCitadinne(int(Immatriculation),Marque,Carburant,int(Modele),int(puissance),gamme)
            lstvoiture.ModifierVoiture(voiture)
            tree.delete(selected_item)
            row = [Immatriculation,Marque,Carburant,Modele,puissance,gamme]
            tree.insert('', END, values= row)

        Modifier=Button(child2,text="MODIFY",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:modifier())
        Modifier.place(x=330,y=330)
 

    modifier=Button(child,text="MODIFY",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:modifierVoitureCitadinne())
    modifier.place(x=270,y=360)
    supprimer=Button(child,text="DELETE",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:supprimerVoitureCitadinne())
    supprimer.place(x=370,y=360)

    tree=ttk.Treeview(child,columns=(1,2,3,4,5,6),heigh=5,show="headings")
    tree.place(x=50,y=50,width=600,height=225)

    tree.heading(1,text="Immatriculation")
    tree.heading(2,text="MARQUE")
    tree.heading(3,text="Carburant")
    tree.heading(4,text="YEAR MODEL")
    tree.heading(5,text="Puissance fiscale")
    tree.heading(6,text="GAMME")
    

    tree.column(1,width=100)
    tree.column(2,width=100)
    tree.column(3,width=100)
    tree.column(4,width=100)
    tree.column(5,width=100)
    tree.column(6,width=100)
   

    for i in lstvoiture.listevoiture:
        if hasattr(i,"gamme"):
            row = [i.immatriculation,i.marque,i.carburant,i.modele,i.puissance,i.gamme]
            tree.insert('', END, values= row)

    tree.bind('<ButtonRelease-1>', selectItem)   


def child9():
    child=Toplevel(Accueil)
    child.geometry("1080x720")
    child.title("location ajout")
    child.configure(bg="tomato")

    ddl=Label(child,text="LOCATION DATE :",font=("Times",12,'bold'),fg="black",bg="salmon")
    ddl.place(x=100,y=80)
    entryddl=Entry(child,width=15,bd=2,font=("Times",12))
    entryddl.place(x=270,y=80)

    drl=Label(child,text="Durée :",font=("Times",12,'bold'),fg="black",bg="salmon")
    drl.place(x=100,y=120)
    entrydrl=Entry(child,width=15,bd=2,font=("Times",12))
    entrydrl.place(x=270,y=120)

    pdl=Label(child,text="Prix :",font=("Times",12,'bold'),fg="black",bg="salmon")
    pdl.place(x=100,y=160)
    entrypdl=Entry(child,width=15,bd=2,font=("Times",12))
    entrypdl.place(x=270,y=160)

    clt=Label(child,text="CIN:",font=("Times",12,'bold'),fg="black",bg="salmon")
    clt.place(x=100,y=200)
    entryclt=Entry(child,width=15,bd=2,font=("Times",12))
    entryclt.place(x=270,y=200)


    vt=Label(child,text="Immetricilation :",font=("Times",12,'bold'),fg="black",bg="salmon")
    vt.place(x=100,y=240)
    entryvt=Entry(child,width=15,bd=2,font=("Times",12))
    entryvt.place(x=270,y=240)

    def ajouterLocation():
        Date=entryddl.get()
        Dure=entrydrl.get()
        Prix=entrypdl.get()
        Client=entryclt.get()
        Voiture=entryvt.get()
        location=Location(Date,Dure,Prix,Client,Voiture)
        valide=lstlocation.AjouterLocation(location)
        if valide:
            messagebox.showinfo("location avec succe")
        else:
            messagebox.showinfo("LOCATION EXIST")

    enregistrer=Button(child,text="S'enregister",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:ajouterLocation())
    enregistrer.place(x=330,y=290)
    
def child10():
    child=Toplevel(Accueil)
    child.geometry("1080x720")
    child.title("LOCATION AFFICHAGE")
    child.configure(bg="tomato")
    value=[]

    def selectItem(a):
        curItem = tree.focus()
        value=tree.item(curItem).get("values")
   
    def supprimerLocation():
        curItem = tree.focus()
        value=tree.item(curItem).get("values")
        lstlocation.SupprimerLocation(int(value[0]))
        selected_item = tree.selection()[0] 
        tree.delete(selected_item)

    def modifierLocation():
        curItem = tree.focus()
        value=tree.item(curItem).get("values")
        child2=Toplevel(child)
        child2.geometry("1080x720")
        child2.title("Modifier la Location")
        child2.configure(bg="tomato")
        selected_item = tree.selection()[0]

        idd=Label(child2,text="De location:",font=("Times",12,'bold'),fg="black",bg="salmon")
        idd.place(x=100,y=80)
        entryidd=Entry(child2,width=15,bd=2,font=("Times",12))
        entryidd.place(x=270,y=80)
        entryidd.insert(END,value[0])
        entryidd.config(state='disabled')

        ddl=Label(child2,text="LOCATION DATE:",font=("Times",12,'bold'),fg="black",bg="salmon")
        ddl.place(x=100,y=120)
        entryddl=Entry(child2,width=15,bd=2,font=("Times",12))
        entryddl.place(x=270,y=120)
        entryddl.insert(END,value[1])

        drl=Label(child2,text="Durée",font=("Times",12,'bold'),fg="black",bg="salmon")
        drl.place(x=100,y=160)
        entrydrl=Entry(child2,width=15,bd=2,font=("Times",12))
        entrydrl.place(x=270,y=160)
        entrydrl.insert(END,value[2])

        pdl=Label(child2,text="Prix:",font=("Times",12,'bold'),fg="black",bg="salmon")
        pdl.place(x=100,y=200)
        entrypdl=Entry(child2,width=15,bd=2,font=("Times",12))
        entrypdl.place(x=270,y=200)
        entrypdl.insert(END,value[3])

        clt=Label(child2,text="cin",font=("Times",12,'bold'),fg="black",bg="salmon")
        clt.place(x=100,y=240)
        entryclt=Entry(child2,width=15,bd=2,font=("Times",12))
        entryclt.place(x=270,y=240)
        entryclt.insert(END,value[4])


        vt=Label(child2,text="Immatriculation :",font=("Times",12,'bold'),fg="black",bg="salmon")
        vt.place(x=100,y=280)
        entryvt=Entry(child2,width=15,bd=2,font=("Times",12))
        entryvt.place(x=270,y=280)
        entryvt.insert(END,value[5])
        
        def modifier():
            idd=entryidd.get()
            ddl=entryddl.get()
            drl=entrydrl.get()
            pdl=entrypdl.get()
            numcin=entryclt.get()
            vt=entryvt.get()
            trouver=False
            for i in lstcl.listeclient:
                if i.cin==str(numcin):
                    trouver=True
                    break
            if not(trouver):
                messagebox.showinfo("client NEXISTE PAS")

            
            trouverV=False
            for i in lstvoiture.listevoiture:
                if i.immatriculation==int(vt):
                    trouverV=True
                    break
            if not(trouverV):
                messagebox.showinfo("voiture NEXISTE PAS")
            if trouver and trouverV:
                for i in lstlocation.listeLocation:
                    if i.idLocation==int(idd):
                        location=i
                        break
                lstlocation.ModifierLocation(location)
                tree.delete(selected_item)
                row = [idd,ddl,drl,pdl,numcin,vt]
                tree.insert('', END, values= row) 

        Modifier=Button(child2,text="MODIFY",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:modifier())
        Modifier.place(x=330,y=330)

    modifier=Button(child,text="MODIFY ",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:modifierLocation())
    modifier.place(x=270,y=300)
    supprimer=Button(child,text="DELETE",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:supprimerLocation())
    supprimer.place(x=370,y=300)

    tree=ttk.Treeview(child,columns=(1,2,3,4,5,6),heigh=5,show="headings")
    tree.place(x=50,y=50,width=1050,height=225)

    tree.heading(1,text="ID")
    tree.heading(2,text="LOCATION DATE")
    tree.heading(3,text="Duree")
    tree.heading(4,text="Prix")
    tree.heading(5,text="CIN)")
    tree.heading(6,text="Immatriculation")

    tree.column(1,width=150)
    tree.column(2,width=150)
    tree.column(3,width=150)
    tree.column(4,width=150)
    tree.column(5,width=150)
    tree.column(6,width=300)
   
    for i in lstlocation.listeLocation:
        row = [i.idLocation,i.datelocation,i.durelocation,i.prixlocation,i.client.cin,i.voiture.immatriculation]
        tree.insert('', END, values= row)

    tree.bind('<ButtonRelease-1>', selectItem)


    txt=Label(child,text="CAR TYPE :",font=("Times",12,'bold'),fg="black",bg="salmon")
    
    txt.place(x=110,y=360)
    
    selectedType=StringVar()
    box=ttk.Combobox(child,textvariable=selectedType)
    box['values']=["ALL THE CARS","CITADINNE","VIP CARS"]
    box['state']='readonly'
    
    box.place(x=320,y=360)

    def type_change(e):
        Type=selectedType.get()
        if Type=="Tout":
            tree.delete(*tree.get_children())
            for i in lstlocation.listeLocation:
                row = [i.idLocation,i.datelocation,i.durelocation,i.prixlocation,i.client.cin,i.voiture.immatriculation]
                tree.insert('', END, values= row)
        if Type=="Citadinne":
            tree.delete(*tree.get_children())
            for i in lstlocation.AfficherListeLocationCitadine():
                row = [i.idLocation,i.datelocation,i.durelocation,i.prixlocation,i.client.cin,i.voiture.immatriculation]
                tree.insert('', END, values= row)
        if Type=="Vip":
            tree.delete(*tree.get_children())
            for i in lstlocation.AfficherListeLocationVip():
                row = [i.idLocation,i.datelocation,i.durelocation,i.prixlocation,i.client.cin,i.voiture.immatriculation]
                tree.insert('', END, values= row)
              
    box.bind('<<ComboboxSelected>>',type_change)
    

    
    mar=Label(child,text="MARQUE DE VOITURE :",font=("Times",12,'bold'),fg="black",bg="salmon")
    mar.place(x=100,y=430)
    entrymar=Entry(child,width=25,bd=2,font=("Times",12))
    entrymar.place(x=190,y=430)
    def locationParMarque():
        marque=entrymar.get()
        tree.delete(*tree.get_children())
        for i in lstlocation.AfficherLocationMarque(marque):
            row = [i.idLocation,i.datelocation,i.durelocation,i.prixlocation,i.client.cin,i.voiture.immatriculation]
            tree.insert('', END, values= row)
        
    afficherlocationmarque=Button(child,text="AFFICHER PAR LA MARQUE DU VOITURE",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:locationParMarque())
    afficherlocationmarque.place(x=470,y=430)


    ima=Label(child,text="IMMAT :",font=("Times",12,'bold'),fg="black",bg="salmon")
    ima.place(x=100,y=470)
    entryima=Entry(child,width=25,bd=2,font=("Times",12))
    entryima.place(x=250,y=470)
    
    def locationParImmatriculation():
        immatriculation=int(entryima.get())
        tree.delete(*tree.get_children())
        for i in lstlocation.AfficherLocationImma(immatriculation):
            row = [i.idLocation,i.datelocation,i.durelocation,i.prixlocation,i.client.cin,i.voiture.immatriculation]
            tree.insert('', END, values= row)
            
    afficherlocationimmatriculation=Button(child,text="AFFICHER PAR IMMATRICULATION ICI :",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:locationParImmatriculation())
    afficherlocationimmatriculation.place(x=530,y=470)


    clcin=Label(child,text="CIN ",font=("Times",12,'bold'),fg="black",bg="salmon")
    clcin.place(x=100,y=510)
    entryclcin=Entry(child,width=25,bd=2,font=("Times",12))
    entryclcin.place(x=190,y=510)

    def locationParCin():
        cin=entryclcin.get()
        tree.delete(*tree.get_children())
        for i in lstlocation.AfficherLocationClient(cin):
            row = [i.idLocation,i.datelocation,i.durelocation,i.prixlocation,i.client.cin,i.voiture.immatriculation]
            tree.insert('', END, values= row)
    afficherlocationclient=Button(child,text="AFFICHER AVEC LA CIN",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:locationParCin())
    afficherlocationclient.place(x=470,y=510)

    dt=Label(child,text="DATE",font=("Times",12,'bold'),fg="black",bg="salmon")
    dt.place(x=100,y=550)
    entrydt=Entry(child,width=25,bd=2,font=("Times",12))
    entrydt.insert(END, 'aaaa-mm-jj')
    entrydt.place(x=190,y=550)

    def locationParDate():
        Listedate=entrydt.get().split('-')
        datex=date(int(Listedate[0]),int(Listedate[1]),int(Listedate[2]))
        tree.delete(*tree.get_children())
        for i in lstlocation.FiltrerLocationDate(datex):
            row = [i.idLocation,i.datelocation,i.durelocation,i.prixlocation,i.client.cin,i.voiture.immatriculation]
            tree.insert('', END, values= row)
    FiltrerLocationDate=Button(child,text="AFFICHER PAR LA DATE ICI :",font=("Times",12,'bold'),fg="black",bg="salmon",command=lambda:locationParDate())
    FiltrerLocationDate.place(x=470,y=550)


   
menubar = Menu(Accueil)

menu1=Menu(menubar,font=("Times",20,'bold'),fg="black",bg="salmon", tearoff=0)
menubar.add_cascade(label="GESTION : Utilisateur", menu=menu1)
menu1.add_command(label="AJOUTER : Utilisateur", command=lambda:child1())
menu1.add_command(label="AFFICHER : Utilisateurs", command=lambda:child2())
menu1.add_separator()
menu1.add_command(label="QUITTER LE PROGRAMME", command=Accueil.quit)


menu2=Menu(menubar,font=("Times",20,'bold'),fg="black",bg="salmon", tearoff=0)
menubar.add_cascade(label="GESTION : Client", menu=menu2)
menu2.add_command(label="AJOUTER : Client", command=lambda:child3())
menu2.add_command(label="AFFICHER :Clients", command=lambda:child4())
menu2.add_separator()
menu2.add_command(label="QUITTER LE PROGRAMME", command=Accueil.quit)


menu3=Menu(menubar,font=("Times",20,'bold'),fg="black",bg="salmon", tearoff=0)
menubar.add_cascade(label="GESTION : Voiture", menu=menu3)

menuaj=Menu(menu3,font=("Times",20,'bold'),fg="black",bg="salmon",tearoff=0)
menu3.add_cascade(label="AJOUTER : Voiture",menu=menuaj)
menuaj.add_command(label="AJOUTER : Voiture Vip",command=lambda:child5())
menuaj.add_command(label="AJOUTER : Voiture Citadinne",command=lambda:child6())

menuaff=Menu(menu3,font=("Times",20,'bold'),fg="black",bg="salmon",tearoff=0)
menu3.add_cascade(label="AFFICHER : Voitures",menu=menuaff)
menuaff.add_command(label="AFFICHER : Voiture Vip",command=lambda:child7())
menuaff.add_command(label="AFFICHER : Voiture Citadinne",command=lambda:child8())

menu3.add_separator()
menu3.add_command(label="QUITTER LE PROGRAMME", command=Accueil.quit)


menu4=Menu(menubar,font=("Times",20,'bold'),fg="black",bg="salmon", tearoff=0)
menubar.add_cascade(label="GESTION : Locations", menu=menu4)
menu4.add_command(label="AJOUTER : Location", command=lambda:child9())
menu4.add_command(label="AFFICHER : Locations", command=lambda:child10())
menu4.add_separator()
menu4.add_command(label="QUITTER LE PROGRAMME", command=Accueil.quit)

Accueil.config(menu=menubar)
Accueil.mainloop()
