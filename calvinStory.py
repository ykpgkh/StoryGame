'''
Text based game; Calvin Story 
Created Fall 2018
author: Young Kwang Park
'''

class Game:
    
    def __init__(self):
        '''Initialize the basics of the game'''
        self.counter_a = 0
        self.counter_b = 0
        self.education = 0
        self.social = 0
        self.love = 0
        self.name = "yk"

    def get_name(self):
        return self.name

    def get_education(self):
        return self.education    
        
    def get_love(self):
        '''Error 404: Love not found'''
        return self.love
    
    def get_social(self):
        return self.social
    
    def update_education(self):
        self.education = self.education + 17
        return self.education
    
    def update_love(self):
        self.love = self.love + 15
        return self.love
        
    def update_social(self):
        self.social = self.social + 16
        
    def get_a(self):

        self.counter_a = self.counter_a + 1
        if self.counter_a == 1:
            return "Orientation Assistant: Hello everyone! How are all of you doing?"
        if self.counter_a == 2:
            return "Orientation Assistant: I'm your Orientation Assistant, Steve! Pleasure to meet all of you"
        if self.counter_a == 3:
            return "Steve: How about we go around and introduce ourselves! Can you share your name and something fun about yourself!"
        if self.counter_a == 4:
            self.update_social()
            return "YK: Hi, my name is YK and I am NOT the creator of this game"
        if self.counter_a == 5:
            return "Catalina: Hello everyone! My name is Catalina and I like to play sports!"
        if self.counter_a == 6:
            return "Jane Doe: Does it matter? I'm never going to appear in the story again until there is a patch to include me more..."
        if self.counter_a == 7:
            return "Steve: Yikes..."
        if self.counter_a == 8:
            return "Steve: Anyhow, how about we play some team-building games! "
        if self.counter_a == 9:
            return "Press A to continue"
        if self.counter_a == 10:
            return "Steve: Hey, YK! How are you doing? Classes going well I hope?"
        if self.counter_a == 11:
            return "YK: I think they have been going pretty decently. I think I might end up getting an A in my Intro to CS class"
        if self.counter_a == 12:
            return "Steve: Nice, nice. Hey, Joe invited me to a house party he is hosting. Wanna come? It should be a good break from studying all the time"
        if self.counter_a == 13:
            return "YK: A house party?     A) Sounds fun. I\'m down     B) Nah, I got midterms coming up"
        if self.counter_a == 14 and self.counter_b == 1:
            self.update_social()
            return "Steve: Nice. Let's uber together"
        #decided to not go to the party
        if self.counter_a == 14 and self.counter_b == 2:
            self.counter_a = self.counter_a + 1
            return "Press A to continue"
        #decided to go to the party
        if self.counter_a == 15:
            return "***At the party*** \nSteve: Wow, look at all these people! I didn't realize so many people at Calvin liked to party!"
        if self.counter_a == 16:
            return "Catalina: STEVE! YK! HI! it's so good to see you guys here. How are you guys enjoying the party?"
        if self.counter_a == 17:
            return "Steve: Well, we just got here so not sure. But I know what will make it better. I'll go get some drinks for us."
        if self.counter_a == 18:
            return "Catalina: Steve sure does seem to know how to party hahaha. How have you been YK? "
        if self.counter_a == 19:
            return "YK:     A) Not bad. I tried the rock climbing recently. It's pretty fun but I suck.     B) good. You?"
        if self.counter_a == 20:
            return "Catalina: Dude, me too. I tried it a couple of times with my roommate but I freaking suck hahaha. We should go together some time!"
        if self.counter_a == 21:
            self.update_love()
            return "Press A to continue"
        #finals are approaching
        if self.counter_a == 22:
            self.update_education()
            return "Press A to continue"
        if self.counter_a == 23:
            return "Steve: Sup YK. How is studying for finals going?"
        if self.counter_a == 24:
            return "YK: Not good... I've been wasting too much time on Instagram"
        if self.counter_a == 25:
            return "Steve: Do you know what that means? MOVIE TIME!!!"
        if self.counter_a == 26:   
            return "YK:     A) ...Sure. What movie?     B) Nah dude. I really should study"
        if self.counter_a == 27:
            self.update_social()
            return "Steve: That's the spirit. LEGGO"
        if self.counter_a == 28:
            return "***At celebration North**** \nSteve: Alright, the rest of our party should be joining us soon"
        if self.counter_a == 29:
            return "YK: What? I thought it was just going to be the two of us. Who else is coming?"
        if self.counter_a == 30:
            return "Catalina: STEVE! YK! HI! I'm not late am I? "
        if self.counter_a == 31:
            return "Steve: Nope. Just in time. Ready to watch how Thanos gets his butt kicked?"
        if self.counter_a == 32:
            return "Catalina: Heck yeah. Let's go YK!...wait who is Thanos again?"
        if self.counter_a == 33:
            self.update_love()
            return "Press A to continue" 
        #The first year ends
        if self.counter_a == 34:
            self.update_education()
            return "Press A to continue"
        #Second year starts
        if self.counter_a == 35:
            return "Steve: YK! Duuuude. How was your break?"
        if self.counter_a == 36:
            return "YK: Pretty good thanks. How about yours? Are you excited that you are on your third and final year?"
        if self.counter_a == 37:
            return "Steve: Noooo. I'm gonna miss you so much man. Also, I need to start applying to jobs so that should be fun..."
        if self.counter_a == 38:
            return "Steve: Oh I know. We should go to the library! You can study there and I'll be polishing my resume and applying at jobs online!"
        if self.counter_a == 39:
            return "YK: But the semester just started...There is nothing to study yet. You want me to review the syllabus or something?"
        if self.counter_a == 40:
            return "Catalina: YK! STEVE! HI! How have you guys been??"
        if self.counter_a == 41:
            return "YK: Steve was just telling me we should go to the library"
        if self.counter_a == 42:
            return "Catalina: WHAT?! Are you forreal, Steve? Who are you and what did you do to our, Steve?!"
        if self.counter_a == 43:
            self.update_education()
            self.update_social()
            self.update_love()
            return "Steve:... Let's just go to the library already"
        if self.counter_a == 44:
            return "Press A to continue"
        if self.counter_a == 45:
            return "Steve: Alright, I finally finished applying to as many jobs as possible. Do you know what this means, YK?"
        if self.counter_a == 46:
            return "YK: ...drinks?"
        if self.counter_a == 47:
            return "Steve: Yes! You know me so well, YK. Maybe we should invite Catalina. What do you think?"
        if self.counter_a == 48:
            return "YK:     A) Yeah, sounds good     B) Nah"
        if self.counter_a == 49:
            return "Steven: Alright, I'll give her a call and let her know you want her to come"
        if self.counter_a == 50:
            return "YK: ..."
        if self.counter_a == 51:
            self.update_love()
            self.update_social()
            return "Press A to continue"
        #2nd year mid terms are done. Finals are approaching
        if self.counter_a == 52:
            self.update_education()
            return "Press A to continue"
        if self.counter_a == 53:
            return "Steve: Alright, finals are approaching and so is my graduation..."
        if self.counter_a == 54:
            return "YK: Are you excited?"
        if self.counter_a == 55:
            return "Steve: Not really. Kinda hard to be excited about graduation when I still don't have a job lined up yet"
        if self.counter_a == 56:
            return "YK: Don't worry about it, Steve. I'm sure you'll hear some positive news from an employer soon"
        if self.counter_a == 57:
            return "Steve: Thanks YK..."
        if self.counter_a == 58:
            return "YK: Hey, I know. How about we order some pizza and binge watch The Office?"
        if self.counter_a == 59:
            return "Steve: You wanna do that this close to finals? You sure?"
        if self.counter_a == 60:
            return "YK: Yeah. Not like we will be able to do this anymore after you graduate"
        if self.counter_a == 61:
            return "Steve: Dude..."
        if self.counter_a == 62:
            return "YK: yeah, yeah. I'm awesome. Let's order the pizza before it gets any later"
        if self.counter_a == 63:
            return "Catalina: Did I hear pizza?!"
        if self.counter_a == 64:
            return "Steve: Yeah, YK says he is buying us enough pizza for a Netflix marathon"
        if self.counter_a == 65:
            return "Catalina: Really??? Yay! Seems like I bumped into you guys at the right time!"
        if self.counter_a == 66:
            return "YK: I never said I was buying all of the pizzas..."
        if self.counter_a == 67: 
            return "Steve: No time to waste. I'll order the pizza before they close. YK, what was your debit card number again?"
        if self.counter_a == 68:
            return "YK: ......1212-121212"
        #second year ends
        if self.counter_a == 69:
            self.update_education()
            self.update_love()
            self.update_social()
            return "Press A to continue"
        #third year starts
        if self.counter_a == 70:
            return "Press A to continue"
        
        #First Branch. If love is high enough it will take this branch
        if self.counter_a == 71 and self.get_love() > 65:
            return "Catalina: Hey YK! How was your break? Miss me much?"
        if self.counter_a == 72 and self.get_love() > 65:
            return "YK: It wasn't too exciting but it's a lot better now"
        if self.counter_a == 73 and self.get_love() > 65:
            return "Catalina: Oh yeah?"
        if self.counter_a == 74 and self.get_love() > 65:
            return "YK: Yeah, yeah. Whatever. Hey, do you want to go to the climbing wall?"
        if self.counter_a == 75 and self.get_love() > 65:
            return "Catalina: Thought you would never ask"
        if self.counter_a == 76 and self.get_love() > 65:
            return "Press A to continue"
        if self.counter_a == 77 and self.get_love() > 65:
            return "YK: Man, finally graduating huh. This feels surreal"
        if self.counter_a == 78 and self.get_love() > 65:
            return "Catalina: Yeah, I know what you mean. Can't believe we are actually graduating. I feel like we barely spent any time studying"
        if self.counter_a == 79 and self.get_love() > 65:
            return "YK: Yeah... good thing that the requirements to graduate in this game are basically non-existent."
        if self.counter_a == 80 and self.get_love() > 65:
            return "Press A to continue"
        if self.counter_a == 81 and self.get_love() > 65:
            return "Game Done. Congratulations! Press the QUIT button to exit"
        #Second branch. If love is NOT high enough it will take this branch
        if self.counter_a == 71 and self.get_love() < 65:
            return "YK: My final year at John Calvin University... Time sure does fly pretty fast"
        if self.counter_a == 72 and self.get_love() < 65:
            return "YK: ...I wonder what Steve is up to."
        if self.counter_a == 73 and self.get_love() < 65:
            return "Steve: You called?"
        if self.counter_a == 74 and self.get_love() < 65:
            return "YK: STEVE!?!? What are you doing here?!"
        if self.counter_a == 75 and self.get_love() < 65:
            return "Steve: I was feeling nostalgic so I decided to visit the campus"
        if self.counter_a == 76 and self.get_love() < 65:
            return "YK: Shouldn't you be at work?"
        if self.counter_a == 77 and self.get_love() < 65:
            return "Steve: ...no comment"
        if self.counter_a == 78 and self.get_love() < 65:
            return "Steve: Anyhow, where's Catalina? I thought you two would be hanging out together now that I'm gone"
        if self.counter_a == 79 and self.get_love() < 65:
            return "YK: Not sure, don't care"
        if self.counter_a == 80 and self.get_love() < 65:
            return "Steve: Dang, YK. Pretty cold there."
        if self.counter_a == 81 and self.get_love() < 65:
            return "YK: Whatever. Hey, you wanna go bowl?"
        if self.counter_a == 82 and self.get_love() < 65:
            return "Steve: Thought you would never ask, bud"
        if self.counter_a == 83 and self.get_love() < 65:
            return "Press A"
        if self.counter_a == 84 and self.get_love() < 65:
            return "Game End. Press the QUIT button to exit."
                
    def get_b(self):
        self.counter_b = self.counter_b + 1
        if self.counter_b < 3 and self.counter_a == 13:
            self.counter_a = self.counter_a + 8
            self.update_education()
            return "Steve: bummer... have fun studying \nPress A to continue"
#         if self.counter_b <= 4 and self.counter_a == 18 :
#             self.update_education()
#             return "Steve: I see you are quite diligent on your education. Nice \nPress A to continue"
        if self.counter_a == 19 and self.counter_b < 5:
            self.counter_a = self.counter_a + 2
            return "Catalina: Good, thank you... \nPress A to continue"
        if self.counter_a == 26 and self.counter_b < 6:
            self.counter_a = self.counter_a + 7
            self.update_education()
            return "Steve: Ok... goodluck with your studies \nPress A to continue"
        if self.counter_a == 48 and self.counter_b < 7:
            self.counter_a = self.counter_a + 3
            self.update_social()
            return "Steve: Ok then. Bro-date, let's go! \nPress A to continue"
        else:
            return "If you are reading this message, you pressed the B-Button out of order. You'll need to restart the game"
        
    def change_pic(self):
        if self.counter_a >= 1 and self.counter_a < 3:
            return "images/oa introduction.gif"
        if self.counter_a == 3:
            return "images/intro with all four.gif"
        if self.counter_a == 4:
            return "images/yk introduction.gif"
        if self.counter_a == 5:
            return "images/catalina introduction.gif"
        if self.counter_a == 6:
            return "images/jane doe introduction.gif"
        if self.counter_a == 7:
            return "images/oa introduction.gif"
        if self.counter_a == 8:
            return "images/intro with all four.gif"
        if self.counter_a == 9:
            return "images/orientationDone.gif"
        if self.counter_a > 9 and self.counter_a < 15:
            return "images/ykAndOa.gif"
        if self.counter_a == 15:
            return "images/ykoaparty.gif"
        if self.counter_a > 15 and self.counter_a < 18:
            return "images/ykoacatalinaparty.gif"
        if self.counter_a > 17 and self.counter_a < 21:
            return "images/ykcatalinaparty.gif"
        if self.counter_a == 21:
            return "images/firstYearParty.gif"
        if self.counter_a == 22:
            return "images/firstYearFinalsApproaching.gif"
        if self.counter_a > 22 and self.counter_a < 28:
            return "images/ykAndOa.gif"
        if self.counter_a > 27 and self.counter_a < 30:
            return "images/ykoamovies.gif"
        if self.counter_a == 30:
            return "images/ykoacatalinamovies.gif"
        if self.counter_a > 30 and self.counter_a < 33:
            return "images/ykoacatalinamovies2.gif"
        if self.counter_a == 33:
            return "images/firstyearend.gif"
        if self.counter_a == 34:
            return "images/secondyearstart.gif"
        if self.counter_a > 34 and self.counter_a < 40:
            return "images/ykAndOa.gif"
        if self.counter_a > 39 and self.counter_a < 44:
            return "images/ykoacatalinadorm.gif"
        if self.counter_a == 44:
            return "images/oaapplyjobs.gif"
        if self.counter_a > 44 and self.counter_a < 51:
            return "images/ykAndOa.gif"
        if self.counter_a == 51:
            return "images/drinks.gif"
        if self.counter_a == 52:
            return "images/2ndyearfinals.gif"
        if self.counter_a > 52 and self.counter_a < 63:
            return "images/ykAndOa.gif"
        if self.counter_a > 62 and self.counter_a < 69:
            return "images/ykoacatalinadorm.gif"
        if self.counter_a == 69:
            return "images/2ndyearends.gif"
        if self.counter_a == 70:
            return "images/thirdyearstarts.gif"
        #The first branch if love status is high enough
        if self.get_love() > 65:
            if self.counter_a == 71:
                return "images/ykcatalinalast_year.gif"
            if self.counter_a > 73 and self.counter_a < 76:
                return "images/ykcatalinalast_year2.gif"
            if self.counter_a == 76:
                return "images/76.gif"
            if self.counter_a > 76 and self.counter_a < 80:
                return "images/graduation.gif"
            if self.counter_a == 80:
                return "images/80.gif"
            if self.counter_a == 81:
                return "images/diploma.gif"
        #The second branch if love status is NOT high enough
        if self.get_love() < 65:
            if self.counter_a > 70 and self.counter_a < 73:
                return "images/ykdorm.gif"
            if self.counter_a > 72 and self.counter_a < 78:
                return "images/ykandsteve.gif"
            if self.counter_a > 77 and self.counter_a < 83:
                return "images/ykandsteve2.gif"
            if self.counter_a == 83:
                return "images/finalbranchb.gif"
            if self.counter_a == 84:
                return "images/finalrevoke.gif"
   
        
        