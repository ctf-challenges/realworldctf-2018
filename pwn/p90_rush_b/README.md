## How this challenge works

> Contact: zh-explorer in IRC
Email: hsadkhk@gmail.com

You send me an email with subject `RealWorldCTF2018-CSGO` to hsadkhk@gmail.com.
It should contain a csgo map named as `realwordctf.bsp`

Your email should at least contain the following text, in the precise format shown
below:

 - Name: <your team name>
 - Token: <your team token from platform>
 - Contact: <some way to contact you, preferably IRC or email>

I will install the latest version CS:GO server in an Ubuntu 16.04 LTS i386 server.
Moreover, I will use this server to load your CS:GO map for three times. 
The only goal that you should achieve is spawning a calc(system("/usr/bin/gnome-calculator")) on my computer.

## Full description

Here is *precisely* what I will do when I receive your *map* file. (possibly replacing steps 1&2 after the first time)

1. Download and import the challenge VMware image
2. Take a VM snapshot
3. Launch SteamCMD and run `login anonymous` and `app_update 740` commands to update the server to the latest version
4. Upload the `realwordctf.bsp` to `/home/realworld/csgo-ds/csgo/maps`
5. Change working directory to `/home/realworld/csgo-ds`
6. Launch the CS:GO server with command `./srcds_run -game csgo -console -usercon +game_type 0 +game_mode 0 +mapgroup mg_active +map de_dust2`
7. Wait until the server is fully booted
8. Load the map by typing `map realwordctf.bsp`
9. AFK one minute
10. Restore VM snapshot and try again 

If the calc is spawned, I will reward you with the flag by email.

I will keep trying for a total of 3 times before I give up.

I will not accept more than 3 emails per team. If you really need more, you
will need to explain to me in detail why you messed up your first 3 tries and
convince me that you deserve a 4th chance.

## PS
1. The envrionment provided is a CS:GO server installed in Ubuntu16.04 LTS (realworld:realworld123). The installation steps are followed by Valve official tutorial [3]. Feel free to use it directly if you don't want to download it or deploy the server by yourself.
2. To be fair, I will do a live broadcasting to check your `evil` maps on Twitch[2]
3. I will reply to you within 6 hours.

## Reference
1. https://www.ubuntu.com/desktop
2. https://www.twitch.tv/zh_explorer
3. https://developer.valvesoftware.com/wiki/Counter-Strike:_Global_Offensive_Dedicated_Servers