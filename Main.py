from WishMe import *
import time

if __name__ == "__main__":
    begin = time.time();
    Wish = WishMe();
    Wish.greeting();

    time.sleep(1); # calculates runtime
    end = time.time();
    print(f"Total runtime of the program is {end - begin}");