import os
import time
import sys
# Set color
G = '\033[1;32m' # Green

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.002)
delay_print
delay_print (""+G+"  
 __    __   ______   __    __  ______  _______  
/  \  /  | /      \ /  |  /  |/      |/       \ 
$$  \ $$ |/$$$$$$  |$$ |  $$ |$$$$$$/ $$$$$$$  |
$$$  \$$ |$$ |__$$ |$$ |__$$ |  $$ |  $$ |  $$ |
$$$$  $$ |$$    $$ |$$    $$ |  $$ |  $$ |  $$ |
$$ $$ $$ |$$$$$$$$ |$$$$$$$$ |  $$ |  $$ |  $$ |
$$ |$$$$ |$$ |  $$ |$$ |  $$ | _$$ |_ $$ |__$$ |
$$ | $$$ |$$ |  $$ |$$ |  $$ |/ $$   |$$    $$/ 
$$/   $$/ $$/   $$/ $$/   $$/ $$$$$$/ $$$$$$$/  
                                                
                                                
                                                
""\n")
delay_print (""+G+" <═══════════════Created By 'MD.NAHIDIL ISLAM'═══════════════>""\n")
