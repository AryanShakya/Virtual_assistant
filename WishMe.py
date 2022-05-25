import datetime
from Credentials import UserInfo


class WishMe(UserInfo):
   def greeting(self):
        hour = int(datetime.datetime.now().hour);
        Name = UserInfo.Name;
        if hour >= 0:
            if hour < 12:
                print(f"Good Morning! {Name}");

            elif 12 <= hour < 18:
                print(f"Good Afternoon! {Name}");

            else:
                print(f"Good Evening! {Name}");
        
        print(f"Welcome, {Name} How can i help you?")
    
   def Weather(self):
        print(f"Weather not avail")
