import datetime
class Post():
    def __init__(self, nickname, like, text, comments):
        self.nickname = nickname
        self.like = like
        self.text = text
        self.comments = comments
        self.time()
        self.censor()

    def time(self):
        return (datetime.datetime.now())
    
    def censor(self):
       forbidden_words = ['suck', 'stupid','pimp','dumb','homo','slut',
                          'damn','ass','rape','poop','cock','lol','crap',
                          'sex','nazi','neo-nazi','fuck','bitch','pussy',
                          'penis','vagina','whore','shit','nigger','nigga',
                          'cocksucker','assrape','motherfucker','wanker',
                          'cunt','faggot','fags','asshole', 'piss', 'cum']
       newText = ""
       for i in self.text.split():
           if (i in forbidden_words) == 0:
               newText += str(i) + " "
       self.text = newText
       return (self.text)

    def commentsList(self):
        list = []
        list.append(self.comments)
        print(list)

    def giveLike(self):
        self.like += 1
        return self.like
        

c1 = Post("ibdsf", 3, "dshio fuck shit sdkl", "dbjeds")

print(c1.censor())


