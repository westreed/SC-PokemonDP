from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x6644F8, Add, -7),# units:Graphics  index:0    from 78 To 71
        SetMemory(0x6647F0, Add, -256),# units:Shield Enable  index:65    from 1 To 0
        SetMemory(0x663DD0, Add, -2),# units:Rank/Sublabel  index:0    from 2 To 0
        SetMemory(0x663DE0, Add, -18),# units:Rank/Sublabel  index:16    from 18 To 0
        SetMemory(0x663DF0, Add, -4),# units:Rank/Sublabel  index:32    from 4 To 0
        SetMemory(0x663DF0, Add, -196608),# units:Rank/Sublabel  index:34    from 3 To 0
        SetMemory(0x663E10, Add, -768),# units:Rank/Sublabel  index:65    from 3 To 0
        SetMemory(0x663E34, Add, -22),# units:Rank/Sublabel  index:100    from 22 To 0
        SetMemory(0x662EC0, Add, -11337728),# units:Comp AI Idle  index:34    from 175 To 2
        SetMemory(0x662ECC, Add, 1376256),# units:Comp AI Idle  index:46    from 2 To 23
        SetMemory(0x662ED4, Add, 21),# units:Comp AI Idle  index:52    from 2 To 23
        SetMemory(0x662F04, Add, 0),# units:Comp AI Idle  index:100    from 2 To 2
        SetMemory(0x662288, Add, -11337728),# units:Human AI Idle  index:34    from 175 To 2
        SetMemory(0x662294, Add, 0),# units:Human AI Idle  index:46    from 2 To 2
        SetMemory(0x6622CC, Add, 0),# units:Human AI Idle  index:100    from 2 To 2
        SetMemory(0x6648B8, Add, -11337728),# units:Return to Idle  index:34    from 175 To 2
        SetMemory(0x6648FC, Add, 0),# units:Return to Idle  index:100    from 2 To 2
        SetMemory(0x663320, Add, -8),# units:Attack Unit  index:0    from 10 To 2
        SetMemory(0x663340, Add, -11337728),# units:Attack Unit  index:34    from 175 To 2
        SetMemory(0x66334C, Add, -524288),# units:Attack Unit  index:46    from 10 To 2
        SetMemory(0x663354, Add, -8),# units:Attack Unit  index:52    from 10 To 2
        SetMemory(0x663384, Add, -8),# units:Attack Unit  index:100    from 10 To 2
        SetMemory(0x663A70, Add, -11337728),# units:Attack Move  index:34    from 175 To 2
        SetMemory(0x663AB4, Add, 0),# units:Attack Move  index:100    from 2 To 2
        SetMemory(0x6636B8, Add, 130),# units:Ground Weapon  index:0    from 0 To 130
        SetMemory(0x6636C8, Add, 127),# units:Ground Weapon  index:16    from 3 To 130
        SetMemory(0x6636D8, Add, 105),# units:Ground Weapon  index:32    from 25 To 130
        SetMemory(0x6636F8, Add, 16896),# units:Ground Weapon  index:65    from 64 To 130
        SetMemory(0x66371C, Add, 14),# units:Ground Weapon  index:100    from 116 To 130
        SetMemory(0x6616E0, Add, 130),# units:Air Weapon  index:0    from 0 To 130
        SetMemory(0x6616F0, Add, 127),# units:Air Weapon  index:16    from 3 To 130
        SetMemory(0x661744, Add, 14),# units:Air Weapon  index:100    from 116 To 130
        SetMemory(0x664080, Add, 536870912),# units:Special Ability Flags  index:0    from 402718720 To 939589632
        SetMemory(0x6640BC, Add, 536870912),# units:Special Ability Flags  index:15    from 402718720 To 939589632
        SetMemory(0x6640C0, Add, 534773184),# units:Special Ability Flags  index:16    from 404816448 To 939589632
        SetMemory(0x664100, Add, 536870912),# units:Special Ability Flags  index:32    from 402718720 To 939589632
        SetMemory(0x664108, Add, 534773760),# units:Special Ability Flags  index:34    from 404815872 To 939589632
        SetMemory(0x664184, Add, 536870912),# units:Special Ability Flags  index:65    from 402718720 To 939589632
        SetMemory(0x664210, Add, 534773184),# units:Special Ability Flags  index:100    from 404816448 To 939589632
        SetMemory(0x662DB8, Add, -4),# units:Target Acquisition Range  index:0    from 4 To 0
        SetMemory(0x6635D0, Add, 60),# units:Armor Upgrade  index:0    from 0 To 60
        SetMemory(0x6635DC, Add, 1006632960),# units:Armor Upgrade  index:15    from 0 To 60
        SetMemory(0x6635E0, Add, 60),# units:Armor Upgrade  index:16    from 0 To 60
        SetMemory(0x6635F0, Add, 60),# units:Armor Upgrade  index:32    from 0 To 60
        SetMemory(0x6635F0, Add, 3932160),# units:Armor Upgrade  index:34    from 0 To 60
        SetMemory(0x663610, Add, 14080),# units:Armor Upgrade  index:65    from 5 To 60
        SetMemory(0x663634, Add, 60),# units:Armor Upgrade  index:100    from 0 To 60
        SetMemory(0x65FED8, Add, -3),# units:Armor  index:16    from 3 To 0
        SetMemory(0x65FEE8, Add, -1),# units:Armor  index:32    from 1 To 0
        SetMemory(0x65FEE8, Add, -65536),# units:Armor  index:34    from 1 To 0
        SetMemory(0x65FF08, Add, -256),# units:Armor  index:65    from 1 To 0
        SetMemory(0x65FF2C, Add, -3),# units:Armor  index:100    from 3 To 0
        SetMemory(0x662098, Add, 1),# units:Right-click Action  index:0    from 1 To 2
        SetMemory(0x6620FC, Add, 0),# units:Right-click Action  index:100    from 1 To 1
        SetMemory(0x661FC0, Add, -275),# units:Ready Sound  index:0    from 275 To 0
        SetMemory(0x65FFB0, Add, -287),# units:What Sound Start  index:0    from 287 To 0
        SetMemory(0x662BF0, Add, -290),# units:What Sound End  index:0    from 290 To 0
        SetMemory(0x663B38, Add, -280),# units:Piss Sound Start  index:0    from 280 To 0
        SetMemory(0x661EE8, Add, -286),# units:Piss Sound End  index:0    from 286 To 0
        SetMemory(0x663C10, Add, -291),# units:Yes Sound Start  index:0    from 291 To 0
        SetMemory(0x661440, Add, -294),# units:Yes Sound End  index:0    from 294 To 0
        SetMemory(0x662860, Add, -16),# units:StarEdit Placement Box Width  index:0    from 17 To 1
        SetMemory(0x662964, Add, -22),# units:StarEdit Placement Box Width  index:65    from 23 To 1
        SetMemory(0x662860, Add, -1245184),# units:StarEdit Placement Box Height  index:0    from 20 To 1
        SetMemory(0x662964, Add, -1703936),# units:StarEdit Placement Box Height  index:65    from 27 To 1
        SetMemory(0x6617C8, Add, -7),# units:Unit Size Left  index:0    from 8 To 1
        SetMemory(0x6619D0, Add, -10),# units:Unit Size Left  index:65    from 11 To 1
        SetMemory(0x6617C8, Add, -524288),# units:Unit Size Up  index:0    from 9 To 1
        SetMemory(0x6619D0, Add, -262144),# units:Unit Size Up  index:65    from 5 To 1
        SetMemory(0x6617CC, Add, -7),# units:Unit Size Right  index:0    from 8 To 1
        SetMemory(0x6619D4, Add, -10),# units:Unit Size Right  index:65    from 11 To 1
        SetMemory(0x6617CC, Add, -589824),# units:Unit Size Down  index:0    from 10 To 1
        SetMemory(0x6619D4, Add, -786432),# units:Unit Size Down  index:65    from 13 To 1
        SetMemory(0x662F88, Add, 15),# units:Portrait  index:0    from 0 To 15
        SetMemory(0x6637C4, Add, 8192),# units:Staredit Group Flags  index:37    from 9 To 41
        SetMemory(0x6637C4, Add, 2097152),# units:Staredit Group Flags  index:38    from 9 To 41
        SetMemory(0x6637CC, Add, 2097152),# units:Staredit Group Flags  index:46    from 9 To 41
        SetMemory(0x6637D0, Add, 2097152),# units:Staredit Group Flags  index:50    from 9 To 41
        SetMemory(0x6637D4, Add, 32),# units:Staredit Group Flags  index:52    from 9 To 41
        SetMemory(0x6637E0, Add, -512),# units:Staredit Group Flags  index:65    from 12 To 10
        SetMemory(0x663CE8, Add, -2),# units:Supply Required  index:0    from 2 To 0
        SetMemory(0x663D28, Add, -1024),# units:Supply Required  index:65    from 4 To 0
        SetMemory(0x663408, Add, -50),# units:Build Score  index:0    from 50 To 0
        SetMemory(0x663EB8, Add, -100),# units:Destroy Score  index:0    from 100 To 0
        SetMemory(0x661558, Add, 131072),# units:Staredit Availability Flags  index:33    from 0 To 2
        SetMemory(0x66A028, Add, 262144),# images:Draw Function  index:514    from 9 To 13
    ])

