from eudplib import *


def onPluginStart():
    DoActions([  # Basic DatFile Actions
        SetMemory(0x6644F8, Add, -7),# units:Graphics  index:0    from 78 To 71
        SetMemory(0x6644FC, Add, -167772160),# units:Graphics  index:7    from 81 To 71
        SetMemory(0x664500, Add, -3840),# units:Graphics  index:9    from 86 To 71
        SetMemory(0x664500, Add, -131072),# units:Graphics  index:10    from 73 To 71
        SetMemory(0x664504, Add, -3328),# units:Graphics  index:13    from 89 To 76
        SetMemory(0x664520, Add, 0),# units:Graphics  index:41    from 5 To 5
        SetMemory(0x664524, Add, 16128),# units:Graphics  index:45    from 13 To 76
        SetMemory(0x664524, Add, 838860800),# units:Graphics  index:47    from 0 To 50
        SetMemory(0x66115C, Add, -40),# units:Construction Animation  index:43    from 40 To 0
        SetMemory(0x661160, Add, -27),# units:Construction Animation  index:44    from 27 To 0
        SetMemory(0x66116C, Add, -2),# units:Construction Animation  index:47    from 2 To 0
        SetMemory(0x6647F0, Add, -256),# units:Shield Enable  index:65    from 1 To 0
        SetMemory(0x663158, Add, -14),# units:Elevation Level  index:8    from 18 To 4
        SetMemory(0x663158, Add, -3072),# units:Elevation Level  index:9    from 16 To 4
        SetMemory(0x663178, Add, -256),# units:Elevation Level  index:41    from 4 To 3
        SetMemory(0x663178, Add, -234881024),# units:Elevation Level  index:43    from 18 To 4
        SetMemory(0x66317C, Add, -14),# units:Elevation Level  index:44    from 18 To 4
        SetMemory(0x66317C, Add, -3584),# units:Elevation Level  index:45    from 18 To 4
        SetMemory(0x663DD0, Add, -2),# units:Rank/Sublabel  index:0    from 2 To 0
        SetMemory(0x663DD0, Add, -1024),# units:Rank/Sublabel  index:1    from 5 To 1
        SetMemory(0x663DD0, Add, -262144),# units:Rank/Sublabel  index:2    from 6 To 2
        SetMemory(0x663DD4, Add, -16777216),# units:Rank/Sublabel  index:7    from 1 To 0
        SetMemory(0x663DD8, Add, -7),# units:Rank/Sublabel  index:8    from 10 To 3
        SetMemory(0x663DD8, Add, -2816),# units:Rank/Sublabel  index:9    from 11 To 0
        SetMemory(0x663DD8, Add, -786432),# units:Rank/Sublabel  index:10    from 12 To 0
        SetMemory(0x663DE0, Add, -18),# units:Rank/Sublabel  index:16    from 18 To 0
        SetMemory(0x663DE0, Add, -218103808),# units:Rank/Sublabel  index:19    from 17 To 4
        SetMemory(0x663DE4, Add, -12),# units:Rank/Sublabel  index:20    from 17 To 5
        SetMemory(0x663DE4, Add, -2048),# units:Rank/Sublabel  index:21    from 14 To 6
        SetMemory(0x663DF0, Add, -4),# units:Rank/Sublabel  index:32    from 4 To 0
        SetMemory(0x663DF0, Add, -196608),# units:Rank/Sublabel  index:34    from 3 To 0
        SetMemory(0x663DF8, Add, -1024),# units:Rank/Sublabel  index:41    from 4 To 0
        SetMemory(0x663DF8, Add, -50331648),# units:Rank/Sublabel  index:43    from 10 To 7
        SetMemory(0x663DFC, Add, -3),# units:Rank/Sublabel  index:44    from 11 To 8
        SetMemory(0x663E10, Add, -768),# units:Rank/Sublabel  index:65    from 3 To 0
        SetMemory(0x663E34, Add, -22),# units:Rank/Sublabel  index:100    from 22 To 0
        SetMemory(0x662EAC, Add, 768),# units:Comp AI Idle  index:13    from 20 To 23
        SetMemory(0x662EC0, Add, -11337728),# units:Comp AI Idle  index:34    from 175 To 2
        SetMemory(0x662ECC, Add, 5376),# units:Comp AI Idle  index:45    from 2 To 23
        SetMemory(0x662ECC, Add, 1376256),# units:Comp AI Idle  index:46    from 2 To 23
        SetMemory(0x662ED4, Add, 21),# units:Comp AI Idle  index:52    from 2 To 23
        SetMemory(0x662F04, Add, 0),# units:Comp AI Idle  index:100    from 2 To 2
        SetMemory(0x662274, Add, 768),# units:Human AI Idle  index:13    from 20 To 23
        SetMemory(0x662288, Add, -11337728),# units:Human AI Idle  index:34    from 175 To 2
        SetMemory(0x662294, Add, 5376),# units:Human AI Idle  index:45    from 2 To 23
        SetMemory(0x662294, Add, 0),# units:Human AI Idle  index:46    from 2 To 2
        SetMemory(0x6622CC, Add, 0),# units:Human AI Idle  index:100    from 2 To 2
        SetMemory(0x6648A4, Add, 768),# units:Return to Idle  index:13    from 20 To 23
        SetMemory(0x6648B8, Add, -11337728),# units:Return to Idle  index:34    from 175 To 2
        SetMemory(0x6648C4, Add, 5376),# units:Return to Idle  index:45    from 2 To 23
        SetMemory(0x6648FC, Add, 0),# units:Return to Idle  index:100    from 2 To 2
        SetMemory(0x663320, Add, -8),# units:Attack Unit  index:0    from 10 To 2
        SetMemory(0x663324, Add, -134217728),# units:Attack Unit  index:7    from 10 To 2
        SetMemory(0x663328, Add, -2048),# units:Attack Unit  index:9    from 10 To 2
        SetMemory(0x663328, Add, -524288),# units:Attack Unit  index:10    from 10 To 2
        SetMemory(0x66332C, Add, 768),# units:Attack Unit  index:13    from 20 To 23
        SetMemory(0x663340, Add, -11337728),# units:Attack Unit  index:34    from 175 To 2
        SetMemory(0x663348, Add, -2048),# units:Attack Unit  index:41    from 10 To 2
        SetMemory(0x66334C, Add, -1024),# units:Attack Unit  index:45    from 27 To 23
        SetMemory(0x66334C, Add, -524288),# units:Attack Unit  index:46    from 10 To 2
        SetMemory(0x663354, Add, -8),# units:Attack Unit  index:52    from 10 To 2
        SetMemory(0x663384, Add, -8),# units:Attack Unit  index:100    from 10 To 2
        SetMemory(0x663A5C, Add, -42240),# units:Attack Move  index:13    from 188 To 23
        SetMemory(0x663A70, Add, -11337728),# units:Attack Move  index:34    from 175 To 2
        SetMemory(0x663A7C, Add, 5376),# units:Attack Move  index:45    from 2 To 23
        SetMemory(0x663AB4, Add, 0),# units:Attack Move  index:100    from 2 To 2
        SetMemory(0x6636B8, Add, 130),# units:Ground Weapon  index:0    from 0 To 130
        SetMemory(0x6636B8, Add, -512),# units:Ground Weapon  index:1    from 2 To 0
        SetMemory(0x6636B8, Add, -196608),# units:Ground Weapon  index:2    from 4 To 1
        SetMemory(0x6636BC, Add, 1962934272),# units:Ground Weapon  index:7    from 13 To 130
        SetMemory(0x6636C0, Add, -14),# units:Ground Weapon  index:8    from 16 To 2
        SetMemory(0x6636C0, Add, 6815744),# units:Ground Weapon  index:10    from 26 To 130
        SetMemory(0x6636C4, Add, 31744),# units:Ground Weapon  index:13    from 6 To 130
        SetMemory(0x6636C8, Add, 127),# units:Ground Weapon  index:16    from 3 To 130
        SetMemory(0x6636C8, Add, -33554432),# units:Ground Weapon  index:19    from 5 To 3
        SetMemory(0x6636CC, Add, 3),# units:Ground Weapon  index:20    from 1 To 4
        SetMemory(0x6636CC, Add, -3328),# units:Ground Weapon  index:21    from 18 To 5
        SetMemory(0x6636D8, Add, 105),# units:Ground Weapon  index:32    from 25 To 130
        SetMemory(0x6636DC, Add, 24320),# units:Ground Weapon  index:37    from 35 To 130
        SetMemory(0x6636DC, Add, 6029312),# units:Ground Weapon  index:38    from 38 To 130
        SetMemory(0x6636E0, Add, 22272),# units:Ground Weapon  index:41    from 43 To 130
        SetMemory(0x6636E0, Add, -704643072),# units:Ground Weapon  index:43    from 48 To 6
        SetMemory(0x6636E4, Add, -39),# units:Ground Weapon  index:44    from 46 To 7
        SetMemory(0x6636E8, Add, 4980736),# units:Ground Weapon  index:50    from 54 To 130
        SetMemory(0x6636F8, Add, 16896),# units:Ground Weapon  index:65    from 64 To 130
        SetMemory(0x66371C, Add, 14),# units:Ground Weapon  index:100    from 116 To 130
        SetMemory(0x6616E0, Add, 130),# units:Air Weapon  index:0    from 0 To 130
        SetMemory(0x6616E0, Add, 32768),# units:Air Weapon  index:1    from 2 To 130
        SetMemory(0x6616E8, Add, 115),# units:Air Weapon  index:8    from 15 To 130
        SetMemory(0x6616F0, Add, 127),# units:Air Weapon  index:16    from 3 To 130
        SetMemory(0x6616F4, Add, 129),# units:Air Weapon  index:20    from 1 To 130
        SetMemory(0x6616F4, Add, 28928),# units:Air Weapon  index:21    from 17 To 130
        SetMemory(0x661704, Add, 6029312),# units:Air Weapon  index:38    from 38 To 130
        SetMemory(0x661708, Add, 1375731712),# units:Air Weapon  index:43    from 48 To 130
        SetMemory(0x66170C, Add, 1258291200),# units:Air Weapon  index:47    from 55 To 130
        SetMemory(0x661744, Add, 14),# units:Air Weapon  index:100    from 116 To 130
        SetMemory(0x65FC18, Add, -256),# units:Max Air Hits  index:1    from 1 To 0
        SetMemory(0x65FC20, Add, -1),# units:Max Air Hits  index:8    from 1 To 0
        SetMemory(0x65FC2C, Add, -1),# units:Max Air Hits  index:20    from 1 To 0
        SetMemory(0x65FC2C, Add, -256),# units:Max Air Hits  index:21    from 1 To 0
        SetMemory(0x65FC40, Add, -16777216),# units:Max Air Hits  index:43    from 1 To 0
        SetMemory(0x664080, Add, 536870912),# units:Special Ability Flags  index:0    from 402718720 To 939589632
        SetMemory(0x664084, Add, -2163200),# units:Special Ability Flags  index:1    from 404816384 To 402653184
        SetMemory(0x664088, Add, -1073741824),# units:Special Ability Flags  index:2    from 1476395008 To 402653184
        SetMemory(0x66409C, Add, -536870920),# units:Special Ability Flags  index:7    from 1476460552 To 939589632
        SetMemory(0x6640A0, Add, -1109393924),# units:Special Ability Flags  index:8    from 1512047108 To 402653184
        SetMemory(0x6640A4, Add, -572489988),# units:Special Ability Flags  index:9    from 1512079620 To 939589632
        SetMemory(0x6640A8, Add, 536870848),# units:Special Ability Flags  index:10    from 402718784 To 939589632
        SetMemory(0x6640B4, Add, 134217728),# units:Special Ability Flags  index:13    from 402653184 To 536870912
        SetMemory(0x6640BC, Add, 536870912),# units:Special Ability Flags  index:15    from 402718720 To 939589632
        SetMemory(0x6640C0, Add, 534773184),# units:Special Ability Flags  index:16    from 404816448 To 939589632
        SetMemory(0x6640CC, Add, -1073741888),# units:Special Ability Flags  index:19    from 1476395072 To 402653184
        SetMemory(0x6640D0, Add, -65600),# units:Special Ability Flags  index:20    from 402718784 To 402653184
        SetMemory(0x6640D4, Add, -1109393988),# units:Special Ability Flags  index:21    from 1512047172 To 402653184
        SetMemory(0x664100, Add, 536870912),# units:Special Ability Flags  index:32    from 402718720 To 939589632
        SetMemory(0x664104, Add, -32768),# units:Special Ability Flags  index:33    from 402685956 To 402653188
        SetMemory(0x664108, Add, 534773760),# units:Special Ability Flags  index:34    from 404815872 To 939589632
        SetMemory(0x664114, Add, -402653184),# units:Special Ability Flags  index:37    from 403768448 To 1115264
        SetMemory(0x664118, Add, -402653184),# units:Special Ability Flags  index:38    from 403767424 To 1114240
        SetMemory(0x664124, Add, 535756668),# units:Special Ability Flags  index:41    from 403767432 To 939524100
        SetMemory(0x66412C, Add, -33620100),# units:Special Ability Flags  index:43    from 436273284 To 402653184
        SetMemory(0x664130, Add, -83951748),# units:Special Ability Flags  index:44    from 486604932 To 402653184
        SetMemory(0x664134, Add, 98500476),# units:Special Ability Flags  index:45    from 438370436 To 536870912
        SetMemory(0x664138, Add, -402653184),# units:Special Ability Flags  index:46    from 439419008 To 36765824
        SetMemory(0x66413C, Add, 536804224),# units:Special Ability Flags  index:47    from 402719876 To 939524100
        SetMemory(0x664148, Add, -402653184),# units:Special Ability Flags  index:50    from 403767424 To 1114240
        SetMemory(0x664184, Add, 536870912),# units:Special Ability Flags  index:65    from 402718720 To 939589632
        SetMemory(0x664210, Add, 534773184),# units:Special Ability Flags  index:100    from 404816448 To 939589632
        SetMemory(0x662DB8, Add, -4),# units:Target Acquisition Range  index:0    from 4 To 0
        SetMemory(0x662DBC, Add, -16777216),# units:Target Acquisition Range  index:7    from 1 To 0
        SetMemory(0x662DC0, Add, -196608),# units:Target Acquisition Range  index:10    from 3 To 0
        SetMemory(0x662DC4, Add, -768),# units:Target Acquisition Range  index:13    from 3 To 0
        SetMemory(0x662DDC, Add, -768),# units:Target Acquisition Range  index:37    from 3 To 0
        SetMemory(0x662DDC, Add, -262144),# units:Target Acquisition Range  index:38    from 4 To 0
        SetMemory(0x662DE0, Add, -256),# units:Target Acquisition Range  index:41    from 1 To 0
        SetMemory(0x662DE4, Add, -2048),# units:Target Acquisition Range  index:45    from 8 To 0
        SetMemory(0x662DE4, Add, -50331648),# units:Target Acquisition Range  index:47    from 3 To 0
        SetMemory(0x662DE8, Add, -196608),# units:Target Acquisition Range  index:50    from 3 To 0
        SetMemory(0x663238, Add, 256),# units:Sight Range  index:1    from 9 To 10
        SetMemory(0x663238, Add, 131072),# units:Sight Range  index:2    from 8 To 10
        SetMemory(0x663240, Add, 3),# units:Sight Range  index:8    from 7 To 10
        SetMemory(0x663240, Add, -768),# units:Sight Range  index:9    from 10 To 7
        SetMemory(0x663244, Add, 3072),# units:Sight Range  index:13    from 3 To 15
        SetMemory(0x663248, Add, 33554432),# units:Sight Range  index:19    from 8 To 10
        SetMemory(0x66324C, Add, 3),# units:Sight Range  index:20    from 7 To 10
        SetMemory(0x66324C, Add, 768),# units:Sight Range  index:21    from 7 To 10
        SetMemory(0x663258, Add, 1280),# units:Sight Range  index:33    from 10 To 15
        SetMemory(0x66325C, Add, 2560),# units:Sight Range  index:37    from 5 To 15
        SetMemory(0x66325C, Add, 589824),# units:Sight Range  index:38    from 6 To 15
        SetMemory(0x663260, Add, 50331648),# units:Sight Range  index:43    from 7 To 10
        SetMemory(0x663264, Add, -1),# units:Sight Range  index:44    from 11 To 10
        SetMemory(0x663264, Add, 327680),# units:Sight Range  index:46    from 10 To 15
        SetMemory(0x663264, Add, 167772160),# units:Sight Range  index:47    from 5 To 15
        SetMemory(0x663268, Add, 655360),# units:Sight Range  index:50    from 5 To 15
        SetMemory(0x6635D0, Add, 60),# units:Armor Upgrade  index:0    from 0 To 60
        SetMemory(0x6635D0, Add, 768),# units:Armor Upgrade  index:1    from 0 To 3
        SetMemory(0x6635D0, Add, 131072),# units:Armor Upgrade  index:2    from 1 To 3
        SetMemory(0x6635D4, Add, 1006632960),# units:Armor Upgrade  index:7    from 0 To 60
        SetMemory(0x6635D8, Add, 1),# units:Armor Upgrade  index:8    from 2 To 3
        SetMemory(0x6635D8, Add, 14848),# units:Armor Upgrade  index:9    from 2 To 60
        SetMemory(0x6635D8, Add, 3932160),# units:Armor Upgrade  index:10    from 0 To 60
        SetMemory(0x6635DC, Add, 1006632960),# units:Armor Upgrade  index:15    from 0 To 60
        SetMemory(0x6635E0, Add, 60),# units:Armor Upgrade  index:16    from 0 To 60
        SetMemory(0x6635E0, Add, 33554432),# units:Armor Upgrade  index:19    from 1 To 3
        SetMemory(0x6635E4, Add, 3),# units:Armor Upgrade  index:20    from 0 To 3
        SetMemory(0x6635E4, Add, 256),# units:Armor Upgrade  index:21    from 2 To 3
        SetMemory(0x6635F0, Add, 60),# units:Armor Upgrade  index:32    from 0 To 60
        SetMemory(0x6635F0, Add, 3932160),# units:Armor Upgrade  index:34    from 0 To 60
        SetMemory(0x6635F8, Add, 14592),# units:Armor Upgrade  index:41    from 3 To 60
        SetMemory(0x6635F8, Add, -16777216),# units:Armor Upgrade  index:43    from 4 To 3
        SetMemory(0x6635FC, Add, -1),# units:Armor Upgrade  index:44    from 4 To 3
        SetMemory(0x6635FC, Add, 14336),# units:Armor Upgrade  index:45    from 4 To 60
        SetMemory(0x6635FC, Add, 939524096),# units:Armor Upgrade  index:47    from 4 To 60
        SetMemory(0x663610, Add, 14080),# units:Armor Upgrade  index:65    from 5 To 60
        SetMemory(0x663634, Add, 60),# units:Armor Upgrade  index:100    from 0 To 60
        SetMemory(0x65FED0, Add, -256),# units:Armor  index:9    from 1 To 0
        SetMemory(0x65FED0, Add, -196608),# units:Armor  index:10    from 3 To 0
        SetMemory(0x65FED8, Add, -3),# units:Armor  index:16    from 3 To 0
        SetMemory(0x65FEE8, Add, -1),# units:Armor  index:32    from 1 To 0
        SetMemory(0x65FEE8, Add, -65536),# units:Armor  index:34    from 1 To 0
        SetMemory(0x65FF08, Add, -256),# units:Armor  index:65    from 1 To 0
        SetMemory(0x65FF2C, Add, -3),# units:Armor  index:100    from 3 To 0
        SetMemory(0x662098, Add, 5),# units:Right-click Action  index:0    from 1 To 6
        SetMemory(0x66209C, Add, 16777216),# units:Right-click Action  index:7    from 5 To 6
        SetMemory(0x6620A0, Add, 1024),# units:Right-click Action  index:9    from 2 To 6
        SetMemory(0x6620A0, Add, 327680),# units:Right-click Action  index:10    from 1 To 6
        SetMemory(0x6620A4, Add, 1536),# units:Right-click Action  index:13    from 0 To 6
        SetMemory(0x6620C0, Add, 512),# units:Right-click Action  index:41    from 4 To 6
        SetMemory(0x6620C4, Add, 1024),# units:Right-click Action  index:45    from 2 To 6
        SetMemory(0x6620FC, Add, 0),# units:Right-click Action  index:100    from 1 To 1
        SetMemory(0x661FC0, Add, -275),# units:Ready Sound  index:0    from 275 To 0
        SetMemory(0x661FC0, Add, -14745600),# units:Ready Sound  index:1    from 225 To 0
        SetMemory(0x661FC4, Add, -352),# units:Ready Sound  index:2    from 352 To 0
        SetMemory(0x661FCC, Add, -24117248),# units:Ready Sound  index:7    from 368 To 0
        SetMemory(0x661FD0, Add, -256),# units:Ready Sound  index:8    from 256 To 0
        SetMemory(0x661FD0, Add, -21757952),# units:Ready Sound  index:9    from 332 To 0
        SetMemory(0x661FD4, Add, -295),# units:Ready Sound  index:10    from 295 To 0
        SetMemory(0x661FE8, Add, -16777216),# units:Ready Sound  index:21    from 256 To 0
        SetMemory(0x662010, Add, -54525952),# units:Ready Sound  index:41    from 832 To 0
        SetMemory(0x662014, Add, -61669376),# units:Ready Sound  index:43    from 941 To 0
        SetMemory(0x662018, Add, -857),# units:Ready Sound  index:44    from 857 To 0
        SetMemory(0x662018, Add, -60817408),# units:Ready Sound  index:45    from 928 To 0
        SetMemory(0x66201C, Add, -50790400),# units:Ready Sound  index:47    from 775 To 0
        SetMemory(0x65FFB0, Add, -287),# units:What Sound Start  index:0    from 287 To 0
        SetMemory(0x65FFB0, Add, -15073280),# units:What Sound Start  index:1    from 230 To 0
        SetMemory(0x65FFB4, Add, -360),# units:What Sound Start  index:2    from 360 To 0
        SetMemory(0x65FFBC, Add, -24707072),# units:What Sound Start  index:7    from 377 To 0
        SetMemory(0x65FFC0, Add, -265),# units:What Sound Start  index:8    from 265 To 0
        SetMemory(0x65FFC0, Add, -22282240),# units:What Sound Start  index:9    from 340 To 0
        SetMemory(0x65FFC4, Add, -299),# units:What Sound Start  index:10    from 299 To 0
        SetMemory(0x65FFC8, Add, -983040),# units:What Sound Start  index:13    from 15 To 0
        SetMemory(0x65FFD4, Add, -27721728),# units:What Sound Start  index:19    from 423 To 0
        SetMemory(0x65FFD8, Add, -411),# units:What Sound Start  index:20    from 411 To 0
        SetMemory(0x65FFD8, Add, -17367040),# units:What Sound Start  index:21    from 265 To 0
        SetMemory(0x660000, Add, -54853632),# units:What Sound Start  index:41    from 837 To 0
        SetMemory(0x660004, Add, -62062592),# units:What Sound Start  index:43    from 947 To 0
        SetMemory(0x660008, Add, -858),# units:What Sound Start  index:44    from 858 To 0
        SetMemory(0x660008, Add, -61145088),# units:What Sound Start  index:45    from 933 To 0
        SetMemory(0x66000C, Add, -51183616),# units:What Sound Start  index:47    from 781 To 0
        SetMemory(0x662BF0, Add, -290),# units:What Sound End  index:0    from 290 To 0
        SetMemory(0x662BF0, Add, -15269888),# units:What Sound End  index:1    from 233 To 0
        SetMemory(0x662BF4, Add, -363),# units:What Sound End  index:2    from 363 To 0
        SetMemory(0x662BFC, Add, -24903680),# units:What Sound End  index:7    from 380 To 0
        SetMemory(0x662C00, Add, -268),# units:What Sound End  index:8    from 268 To 0
        SetMemory(0x662C00, Add, -22478848),# units:What Sound End  index:9    from 343 To 0
        SetMemory(0x662C04, Add, -302),# units:What Sound End  index:10    from 302 To 0
        SetMemory(0x662C08, Add, -983040),# units:What Sound End  index:13    from 15 To 0
        SetMemory(0x662C14, Add, -27918336),# units:What Sound End  index:19    from 426 To 0
        SetMemory(0x662C18, Add, -414),# units:What Sound End  index:20    from 414 To 0
        SetMemory(0x662C18, Add, -17563648),# units:What Sound End  index:21    from 268 To 0
        SetMemory(0x662C40, Add, -55115776),# units:What Sound End  index:41    from 841 To 0
        SetMemory(0x662C44, Add, -62259200),# units:What Sound End  index:43    from 950 To 0
        SetMemory(0x662C48, Add, -861),# units:What Sound End  index:44    from 861 To 0
        SetMemory(0x662C48, Add, -61341696),# units:What Sound End  index:45    from 936 To 0
        SetMemory(0x662C4C, Add, -51249152),# units:What Sound End  index:47    from 782 To 0
        SetMemory(0x663B38, Add, -280),# units:Piss Sound Start  index:0    from 280 To 0
        SetMemory(0x663B38, Add, -14811136),# units:Piss Sound Start  index:1    from 226 To 0
        SetMemory(0x663B3C, Add, -356),# units:Piss Sound Start  index:2    from 356 To 0
        SetMemory(0x663B44, Add, -24248320),# units:Piss Sound Start  index:7    from 370 To 0
        SetMemory(0x663B48, Add, -258),# units:Piss Sound Start  index:8    from 258 To 0
        SetMemory(0x663B48, Add, -21823488),# units:Piss Sound Start  index:9    from 333 To 0
        SetMemory(0x663B4C, Add, -303),# units:Piss Sound Start  index:10    from 303 To 0
        SetMemory(0x663B5C, Add, -27459584),# units:Piss Sound Start  index:19    from 419 To 0
        SetMemory(0x663B60, Add, -407),# units:Piss Sound Start  index:20    from 407 To 0
        SetMemory(0x663B60, Add, -16908288),# units:Piss Sound Start  index:21    from 258 To 0
        SetMemory(0x663B88, Add, -54657024),# units:Piss Sound Start  index:41    from 834 To 0
        SetMemory(0x663B8C, Add, -61800448),# units:Piss Sound Start  index:43    from 943 To 0
        SetMemory(0x663B90, Add, -853),# units:Piss Sound Start  index:44    from 853 To 0
        SetMemory(0x663B90, Add, -60882944),# units:Piss Sound Start  index:45    from 929 To 0
        SetMemory(0x663B94, Add, -51052544),# units:Piss Sound Start  index:47    from 779 To 0
        SetMemory(0x661EE8, Add, -286),# units:Piss Sound End  index:0    from 286 To 0
        SetMemory(0x661EE8, Add, -15007744),# units:Piss Sound End  index:1    from 229 To 0
        SetMemory(0x661EEC, Add, -359),# units:Piss Sound End  index:2    from 359 To 0
        SetMemory(0x661EF4, Add, -24641536),# units:Piss Sound End  index:7    from 376 To 0
        SetMemory(0x661EF8, Add, -264),# units:Piss Sound End  index:8    from 264 To 0
        SetMemory(0x661EF8, Add, -22216704),# units:Piss Sound End  index:9    from 339 To 0
        SetMemory(0x661EFC, Add, -309),# units:Piss Sound End  index:10    from 309 To 0
        SetMemory(0x661F0C, Add, -27656192),# units:Piss Sound End  index:19    from 422 To 0
        SetMemory(0x661F10, Add, -410),# units:Piss Sound End  index:20    from 410 To 0
        SetMemory(0x661F10, Add, -17301504),# units:Piss Sound End  index:21    from 264 To 0
        SetMemory(0x661F38, Add, -54788096),# units:Piss Sound End  index:41    from 836 To 0
        SetMemory(0x661F3C, Add, -61997056),# units:Piss Sound End  index:43    from 946 To 0
        SetMemory(0x661F40, Add, -856),# units:Piss Sound End  index:44    from 856 To 0
        SetMemory(0x661F40, Add, -61079552),# units:Piss Sound End  index:45    from 932 To 0
        SetMemory(0x661F44, Add, -51118080),# units:Piss Sound End  index:47    from 780 To 0
        SetMemory(0x663C10, Add, -291),# units:Yes Sound Start  index:0    from 291 To 0
        SetMemory(0x663C10, Add, -15335424),# units:Yes Sound Start  index:1    from 234 To 0
        SetMemory(0x663C14, Add, -364),# units:Yes Sound Start  index:2    from 364 To 0
        SetMemory(0x663C1C, Add, -24969216),# units:Yes Sound Start  index:7    from 381 To 0
        SetMemory(0x663C20, Add, -269),# units:Yes Sound Start  index:8    from 269 To 0
        SetMemory(0x663C20, Add, -22544384),# units:Yes Sound Start  index:9    from 344 To 0
        SetMemory(0x663C24, Add, -310),# units:Yes Sound Start  index:10    from 310 To 0
        SetMemory(0x663C34, Add, -27983872),# units:Yes Sound Start  index:19    from 427 To 0
        SetMemory(0x663C38, Add, -415),# units:Yes Sound Start  index:20    from 415 To 0
        SetMemory(0x663C38, Add, -17629184),# units:Yes Sound Start  index:21    from 269 To 0
        SetMemory(0x663C60, Add, -55181312),# units:Yes Sound Start  index:41    from 842 To 0
        SetMemory(0x663C64, Add, -62324736),# units:Yes Sound Start  index:43    from 951 To 0
        SetMemory(0x663C68, Add, -862),# units:Yes Sound Start  index:44    from 862 To 0
        SetMemory(0x663C68, Add, -61407232),# units:Yes Sound Start  index:45    from 937 To 0
        SetMemory(0x663C6C, Add, -51314688),# units:Yes Sound Start  index:47    from 783 To 0
        SetMemory(0x661440, Add, -294),# units:Yes Sound End  index:0    from 294 To 0
        SetMemory(0x661440, Add, -15532032),# units:Yes Sound End  index:1    from 237 To 0
        SetMemory(0x661444, Add, -367),# units:Yes Sound End  index:2    from 367 To 0
        SetMemory(0x66144C, Add, -25165824),# units:Yes Sound End  index:7    from 384 To 0
        SetMemory(0x661450, Add, -272),# units:Yes Sound End  index:8    from 272 To 0
        SetMemory(0x661450, Add, -22740992),# units:Yes Sound End  index:9    from 347 To 0
        SetMemory(0x661454, Add, -313),# units:Yes Sound End  index:10    from 313 To 0
        SetMemory(0x661464, Add, -28180480),# units:Yes Sound End  index:19    from 430 To 0
        SetMemory(0x661468, Add, -418),# units:Yes Sound End  index:20    from 418 To 0
        SetMemory(0x661468, Add, -17825792),# units:Yes Sound End  index:21    from 272 To 0
        SetMemory(0x661490, Add, -55443456),# units:Yes Sound End  index:41    from 846 To 0
        SetMemory(0x661494, Add, -62521344),# units:Yes Sound End  index:43    from 954 To 0
        SetMemory(0x661498, Add, -865),# units:Yes Sound End  index:44    from 865 To 0
        SetMemory(0x661498, Add, -61603840),# units:Yes Sound End  index:45    from 940 To 0
        SetMemory(0x66149C, Add, -51380224),# units:Yes Sound End  index:47    from 784 To 0
        SetMemory(0x662860, Add, -15),# units:StarEdit Placement Box Width  index:0    from 17 To 2
        SetMemory(0x662864, Add, -3),# units:StarEdit Placement Box Width  index:1    from 15 To 12
        SetMemory(0x662868, Add, -20),# units:StarEdit Placement Box Width  index:2    from 32 To 12
        SetMemory(0x66287C, Add, -21),# units:StarEdit Placement Box Width  index:7    from 23 To 2
        SetMemory(0x662880, Add, -26),# units:StarEdit Placement Box Width  index:8    from 38 To 12
        SetMemory(0x662884, Add, -63),# units:StarEdit Placement Box Width  index:9    from 65 To 2
        SetMemory(0x662888, Add, -21),# units:StarEdit Placement Box Width  index:10    from 23 To 2
        SetMemory(0x662894, Add, -15),# units:StarEdit Placement Box Width  index:13    from 16 To 1
        SetMemory(0x6628AC, Add, -20),# units:StarEdit Placement Box Width  index:19    from 32 To 12
        SetMemory(0x6628B0, Add, -6),# units:StarEdit Placement Box Width  index:20    from 18 To 12
        SetMemory(0x6628B4, Add, -26),# units:StarEdit Placement Box Width  index:21    from 38 To 12
        SetMemory(0x6628E4, Add, -26),# units:StarEdit Placement Box Width  index:33    from 27 To 1
        SetMemory(0x662904, Add, -15),# units:StarEdit Placement Box Width  index:41    from 23 To 8
        SetMemory(0x66290C, Add, -32),# units:StarEdit Placement Box Width  index:43    from 44 To 12
        SetMemory(0x662910, Add, -32),# units:StarEdit Placement Box Width  index:44    from 44 To 12
        SetMemory(0x662914, Add, -47),# units:StarEdit Placement Box Width  index:45    from 48 To 1
        SetMemory(0x66291C, Add, -23),# units:StarEdit Placement Box Width  index:47    from 24 To 1
        SetMemory(0x662964, Add, -22),# units:StarEdit Placement Box Width  index:65    from 23 To 1
        SetMemory(0x662860, Add, -1179648),# units:StarEdit Placement Box Height  index:0    from 20 To 2
        SetMemory(0x662864, Add, -655360),# units:StarEdit Placement Box Height  index:1    from 22 To 12
        SetMemory(0x662868, Add, -1310720),# units:StarEdit Placement Box Height  index:2    from 32 To 12
        SetMemory(0x66287C, Add, -1376256),# units:StarEdit Placement Box Height  index:7    from 23 To 2
        SetMemory(0x662880, Add, -1179648),# units:StarEdit Placement Box Height  index:8    from 30 To 12
        SetMemory(0x662884, Add, -3145728),# units:StarEdit Placement Box Height  index:9    from 50 To 2
        SetMemory(0x662888, Add, -1703936),# units:StarEdit Placement Box Height  index:10    from 28 To 2
        SetMemory(0x662894, Add, -1048576),# units:StarEdit Placement Box Height  index:13    from 16 To 0
        SetMemory(0x6628AC, Add, -1310720),# units:StarEdit Placement Box Height  index:19    from 32 To 12
        SetMemory(0x6628B0, Add, -655360),# units:StarEdit Placement Box Height  index:20    from 22 To 12
        SetMemory(0x6628B4, Add, -1179648),# units:StarEdit Placement Box Height  index:21    from 30 To 12
        SetMemory(0x6628E4, Add, -1966080),# units:StarEdit Placement Box Height  index:33    from 31 To 1
        SetMemory(0x662904, Add, -983040),# units:StarEdit Placement Box Height  index:41    from 23 To 8
        SetMemory(0x66290C, Add, -2097152),# units:StarEdit Placement Box Height  index:43    from 44 To 12
        SetMemory(0x662910, Add, -2097152),# units:StarEdit Placement Box Height  index:44    from 44 To 12
        SetMemory(0x662914, Add, -3145728),# units:StarEdit Placement Box Height  index:45    from 48 To 0
        SetMemory(0x66291C, Add, -1572864),# units:StarEdit Placement Box Height  index:47    from 24 To 0
        SetMemory(0x662964, Add, -1703936),# units:StarEdit Placement Box Height  index:65    from 27 To 1
        SetMemory(0x6617C8, Add, -7),# units:Unit Size Left  index:0    from 8 To 1
        SetMemory(0x6617D0, Add, -1),# units:Unit Size Left  index:1    from 7 To 6
        SetMemory(0x6617D8, Add, -10),# units:Unit Size Left  index:2    from 16 To 6
        SetMemory(0x661800, Add, -10),# units:Unit Size Left  index:7    from 11 To 1
        SetMemory(0x661808, Add, -13),# units:Unit Size Left  index:8    from 19 To 6
        SetMemory(0x661810, Add, -31),# units:Unit Size Left  index:9    from 32 To 1
        SetMemory(0x661818, Add, -10),# units:Unit Size Left  index:10    from 11 To 1
        SetMemory(0x661830, Add, -6),# units:Unit Size Left  index:13    from 7 To 1
        SetMemory(0x661860, Add, -10),# units:Unit Size Left  index:19    from 16 To 6
        SetMemory(0x661868, Add, -2),# units:Unit Size Left  index:20    from 8 To 6
        SetMemory(0x661870, Add, -13),# units:Unit Size Left  index:21    from 19 To 6
        SetMemory(0x6618D0, Add, -12),# units:Unit Size Left  index:33    from 13 To 1
        SetMemory(0x661910, Add, -7),# units:Unit Size Left  index:41    from 11 To 4
        SetMemory(0x661920, Add, -16),# units:Unit Size Left  index:43    from 22 To 6
        SetMemory(0x661928, Add, -16),# units:Unit Size Left  index:44    from 22 To 6
        SetMemory(0x661930, Add, -23),# units:Unit Size Left  index:45    from 24 To 1
        SetMemory(0x661940, Add, -11),# units:Unit Size Left  index:47    from 12 To 1
        SetMemory(0x6619D0, Add, -10),# units:Unit Size Left  index:65    from 11 To 1
        SetMemory(0x6617C8, Add, -524288),# units:Unit Size Up  index:0    from 9 To 1
        SetMemory(0x6617D0, Add, -262144),# units:Unit Size Up  index:1    from 10 To 6
        SetMemory(0x6617D8, Add, -655360),# units:Unit Size Up  index:2    from 16 To 6
        SetMemory(0x661800, Add, -655360),# units:Unit Size Up  index:7    from 11 To 1
        SetMemory(0x661808, Add, -589824),# units:Unit Size Up  index:8    from 15 To 6
        SetMemory(0x661810, Add, -2097152),# units:Unit Size Up  index:9    from 33 To 1
        SetMemory(0x661818, Add, -786432),# units:Unit Size Up  index:10    from 13 To 1
        SetMemory(0x661830, Add, -393216),# units:Unit Size Up  index:13    from 7 To 1
        SetMemory(0x661860, Add, -655360),# units:Unit Size Up  index:19    from 16 To 6
        SetMemory(0x661868, Add, -196608),# units:Unit Size Up  index:20    from 9 To 6
        SetMemory(0x661870, Add, -589824),# units:Unit Size Up  index:21    from 15 To 6
        SetMemory(0x6618D0, Add, -786432),# units:Unit Size Up  index:33    from 13 To 1
        SetMemory(0x661910, Add, -458752),# units:Unit Size Up  index:41    from 11 To 4
        SetMemory(0x661920, Add, -1048576),# units:Unit Size Up  index:43    from 22 To 6
        SetMemory(0x661928, Add, -1048576),# units:Unit Size Up  index:44    from 22 To 6
        SetMemory(0x661930, Add, -1507328),# units:Unit Size Up  index:45    from 24 To 1
        SetMemory(0x661940, Add, -720896),# units:Unit Size Up  index:47    from 12 To 1
        SetMemory(0x6619D0, Add, -262144),# units:Unit Size Up  index:65    from 5 To 1
        SetMemory(0x6617CC, Add, -7),# units:Unit Size Right  index:0    from 8 To 1
        SetMemory(0x6617D4, Add, -1),# units:Unit Size Right  index:1    from 7 To 6
        SetMemory(0x6617DC, Add, -9),# units:Unit Size Right  index:2    from 15 To 6
        SetMemory(0x661804, Add, -10),# units:Unit Size Right  index:7    from 11 To 1
        SetMemory(0x66180C, Add, -12),# units:Unit Size Right  index:8    from 18 To 6
        SetMemory(0x661814, Add, -31),# units:Unit Size Right  index:9    from 32 To 1
        SetMemory(0x66181C, Add, -10),# units:Unit Size Right  index:10    from 11 To 1
        SetMemory(0x661834, Add, -6),# units:Unit Size Right  index:13    from 7 To 1
        SetMemory(0x661864, Add, -9),# units:Unit Size Right  index:19    from 15 To 6
        SetMemory(0x66186C, Add, -2),# units:Unit Size Right  index:20    from 8 To 6
        SetMemory(0x661874, Add, -12),# units:Unit Size Right  index:21    from 18 To 6
        SetMemory(0x6618D4, Add, -12),# units:Unit Size Right  index:33    from 13 To 1
        SetMemory(0x661914, Add, -7),# units:Unit Size Right  index:41    from 11 To 4
        SetMemory(0x661924, Add, -15),# units:Unit Size Right  index:43    from 21 To 6
        SetMemory(0x66192C, Add, -15),# units:Unit Size Right  index:44    from 21 To 6
        SetMemory(0x661934, Add, -22),# units:Unit Size Right  index:45    from 23 To 1
        SetMemory(0x661944, Add, -10),# units:Unit Size Right  index:47    from 11 To 1
        SetMemory(0x6619D4, Add, -10),# units:Unit Size Right  index:65    from 11 To 1
        SetMemory(0x6617CC, Add, -589824),# units:Unit Size Down  index:0    from 10 To 1
        SetMemory(0x6617D4, Add, -327680),# units:Unit Size Down  index:1    from 11 To 6
        SetMemory(0x6617DC, Add, -589824),# units:Unit Size Down  index:2    from 15 To 6
        SetMemory(0x661804, Add, -655360),# units:Unit Size Down  index:7    from 11 To 1
        SetMemory(0x66180C, Add, -524288),# units:Unit Size Down  index:8    from 14 To 6
        SetMemory(0x661814, Add, -983040),# units:Unit Size Down  index:9    from 16 To 1
        SetMemory(0x66181C, Add, -851968),# units:Unit Size Down  index:10    from 14 To 1
        SetMemory(0x661834, Add, -393216),# units:Unit Size Down  index:13    from 7 To 1
        SetMemory(0x661864, Add, -589824),# units:Unit Size Down  index:19    from 15 To 6
        SetMemory(0x66186C, Add, -262144),# units:Unit Size Down  index:20    from 10 To 6
        SetMemory(0x661874, Add, -524288),# units:Unit Size Down  index:21    from 14 To 6
        SetMemory(0x6618D4, Add, -1048576),# units:Unit Size Down  index:33    from 17 To 1
        SetMemory(0x661914, Add, -458752),# units:Unit Size Down  index:41    from 11 To 4
        SetMemory(0x661924, Add, -983040),# units:Unit Size Down  index:43    from 21 To 6
        SetMemory(0x66192C, Add, -983040),# units:Unit Size Down  index:44    from 21 To 6
        SetMemory(0x661934, Add, -1441792),# units:Unit Size Down  index:45    from 23 To 1
        SetMemory(0x661944, Add, -655360),# units:Unit Size Down  index:47    from 11 To 1
        SetMemory(0x6619D4, Add, -786432),# units:Unit Size Down  index:65    from 13 To 1
        SetMemory(0x662F88, Add, 15),# units:Portrait  index:0    from 0 To 15
        SetMemory(0x662F94, Add, 524288),# units:Portrait  index:7    from 7 To 15
        SetMemory(0x662F98, Add, 393216),# units:Portrait  index:9    from 9 To 15
        SetMemory(0x662F9C, Add, 13),# units:Portrait  index:10    from 2 To 15
        SetMemory(0x663898, Add, -6553600),# units:Mineral Cost  index:9    from 100 To 0
        SetMemory(0x66389C, Add, -100),# units:Mineral Cost  index:10    from 100 To 0
        SetMemory(0x6638D8, Add, -3276800),# units:Mineral Cost  index:41    from 50 To 0
        SetMemory(0x6638E0, Add, -6553600),# units:Mineral Cost  index:45    from 100 To 0
        SetMemory(0x6638E4, Add, -1638400),# units:Mineral Cost  index:47    from 25 To 0
        SetMemory(0x65FD10, Add, -14745600),# units:Vespene Cost  index:9    from 225 To 0
        SetMemory(0x65FD14, Add, -50),# units:Vespene Cost  index:10    from 50 To 0
        SetMemory(0x65FD58, Add, -6553600),# units:Vespene Cost  index:45    from 100 To 0
        SetMemory(0x65FD5C, Add, -4915200),# units:Vespene Cost  index:47    from 75 To 0
        SetMemory(0x6637AC, Add, 30208),# units:Staredit Group Flags  index:13    from 10 To 128
        SetMemory(0x6637C4, Add, 8192),# units:Staredit Group Flags  index:37    from 9 To 41
        SetMemory(0x6637C4, Add, 2097152),# units:Staredit Group Flags  index:38    from 9 To 41
        SetMemory(0x6637C8, Add, 30976),# units:Staredit Group Flags  index:41    from 9 To 130
        SetMemory(0x6637CC, Add, 1),# units:Staredit Group Flags  index:44    from 9 To 10
        SetMemory(0x6637CC, Add, 2097152),# units:Staredit Group Flags  index:46    from 9 To 41
        SetMemory(0x6637D0, Add, 2097152),# units:Staredit Group Flags  index:50    from 9 To 41
        SetMemory(0x6637D4, Add, 32),# units:Staredit Group Flags  index:52    from 9 To 41
        SetMemory(0x6637E0, Add, -512),# units:Staredit Group Flags  index:65    from 12 To 10
        SetMemory(0x663CE8, Add, -2),# units:Supply Required  index:0    from 2 To 0
        SetMemory(0x663CE8, Add, -512),# units:Supply Required  index:1    from 2 To 0
        SetMemory(0x663CE8, Add, -262144),# units:Supply Required  index:2    from 4 To 0
        SetMemory(0x663CEC, Add, -33554432),# units:Supply Required  index:7    from 2 To 0
        SetMemory(0x663CF0, Add, -4),# units:Supply Required  index:8    from 4 To 0
        SetMemory(0x663CF0, Add, -1024),# units:Supply Required  index:9    from 4 To 0
        SetMemory(0x663D10, Add, -512),# units:Supply Required  index:41    from 2 To 0
        SetMemory(0x663D10, Add, -67108864),# units:Supply Required  index:43    from 4 To 0
        SetMemory(0x663D14, Add, -4),# units:Supply Required  index:44    from 4 To 0
        SetMemory(0x663D14, Add, -1024),# units:Supply Required  index:45    from 4 To 0
        SetMemory(0x663D14, Add, -16777216),# units:Supply Required  index:47    from 1 To 0
        SetMemory(0x663D28, Add, -1024),# units:Supply Required  index:65    from 4 To 0
        SetMemory(0x664414, Add, 4261412864),# units:Space Required  index:7    from 1 To 255
        SetMemory(0x664418, Add, 16646144),# units:Space Required  index:10    from 1 To 255
        SetMemory(0x664438, Add, 65024),# units:Space Required  index:41    from 1 To 255
        SetMemory(0x663408, Add, -50),# units:Build Score  index:0    from 50 To 0
        SetMemory(0x663414, Add, -3276800),# units:Build Score  index:7    from 50 To 0
        SetMemory(0x663418, Add, -40960000),# units:Build Score  index:9    from 625 To 0
        SetMemory(0x663458, Add, -3276800),# units:Build Score  index:41    from 50 To 0
        SetMemory(0x66345C, Add, -19660800),# units:Build Score  index:43    from 300 To 0
        SetMemory(0x663460, Add, -550),# units:Build Score  index:44    from 550 To 0
        SetMemory(0x663460, Add, -26214400),# units:Build Score  index:45    from 400 To 0
        SetMemory(0x663464, Add, -6553600),# units:Build Score  index:47    from 100 To 0
        SetMemory(0x663EB8, Add, -100),# units:Destroy Score  index:0    from 100 To 0
        SetMemory(0x663EC4, Add, -6553600),# units:Destroy Score  index:7    from 100 To 0
        SetMemory(0x663EC8, Add, -81920000),# units:Destroy Score  index:9    from 1250 To 0
        SetMemory(0x663ECC, Add, -400),# units:Destroy Score  index:10    from 400 To 0
        SetMemory(0x663ED0, Add, -1638400),# units:Destroy Score  index:13    from 25 To 0
        SetMemory(0x663EE0, Add, -199),# units:Destroy Score  index:20    from 200 To 1
        SetMemory(0x663EE0, Add, -104792064),# units:Destroy Score  index:21    from 1600 To 1
        SetMemory(0x663F08, Add, -6553600),# units:Destroy Score  index:41    from 100 To 0
        SetMemory(0x663F0C, Add, -39256064),# units:Destroy Score  index:43    from 600 To 1
        SetMemory(0x663F10, Add, -1099),# units:Destroy Score  index:44    from 1100 To 1
        SetMemory(0x663F10, Add, -52428800),# units:Destroy Score  index:45    from 800 To 0
        SetMemory(0x663F14, Add, -13107200),# units:Destroy Score  index:47    from 200 To 0
        SetMemory(0x661558, Add, 131072),# units:Staredit Availability Flags  index:33    from 0 To 2
        SetMemory(0x657998, Add, -1),# weapons:Target Flags  index:0    from 3 To 2
        SetMemory(0x657998, Add, -65536),# weapons:Target Flags  index:1    from 3 To 2
        SetMemory(0x65799C, Add, -1),# weapons:Target Flags  index:2    from 3 To 2
        SetMemory(0x65799C, Add, -65536),# weapons:Target Flags  index:3    from 3 To 2
        SetMemory(0x6579A4, Add, -16),# weapons:Target Flags  index:6    from 18 To 2
        SetMemory(0x6571D0, Add, 53),# weapons:Damage Upgrade  index:0    from 7 To 60
        SetMemory(0x6571D0, Add, 13568),# weapons:Damage Upgrade  index:1    from 7 To 60
        SetMemory(0x6571D0, Add, 3473408),# weapons:Damage Upgrade  index:2    from 7 To 60
        SetMemory(0x6571D0, Add, 889192448),# weapons:Damage Upgrade  index:3    from 7 To 60
        SetMemory(0x6571D4, Add, 52),# weapons:Damage Upgrade  index:4    from 8 To 60
        SetMemory(0x6571D4, Add, 13312),# weapons:Damage Upgrade  index:5    from 8 To 60
        SetMemory(0x6571D4, Add, 872415232),# weapons:Damage Upgrade  index:7    from 8 To 60
        SetMemory(0x657258, Add, -2),# weapons:Weapon Type  index:0    from 3 To 1
        SetMemory(0x657258, Add, -512),# weapons:Weapon Type  index:1    from 3 To 1
        SetMemory(0x657258, Add, -65536),# weapons:Weapon Type  index:2    from 2 To 1
        SetMemory(0x657258, Add, -16777216),# weapons:Weapon Type  index:3    from 2 To 1
        SetMemory(0x65725C, Add, -1),# weapons:Weapon Type  index:4    from 2 To 1
        SetMemory(0x65725C, Add, -256),# weapons:Weapon Type  index:5    from 2 To 1
        SetMemory(0x65725C, Add, -33554432),# weapons:Weapon Type  index:7    from 3 To 1
        SetMemory(0x6566F8, Add, 0),# weapons:Explosion Type  index:0    from 1 To 1
        SetMemory(0x656990, Add, 16),# weapons:Attack Angle  index:0    from 16 To 32
        SetMemory(0x656990, Add, 4096),# weapons:Attack Angle  index:1    from 16 To 32
        SetMemory(0x656990, Add, 1048576),# weapons:Attack Angle  index:2    from 16 To 32
        SetMemory(0x656990, Add, 268435456),# weapons:Attack Angle  index:3    from 16 To 32
        SetMemory(0x656994, Add, -32),# weapons:Attack Angle  index:4    from 64 To 32
        SetMemory(0x656994, Add, -8192),# weapons:Attack Angle  index:5    from 64 To 32
        SetMemory(0x656994, Add, -6291456),# weapons:Attack Angle  index:6    from 128 To 32
        SetMemory(0x656994, Add, 268435456),# weapons:Attack Angle  index:7    from 16 To 32
        SetMemory(0x6C9C80, Add, 37552128),# flingy:Acceleration  index:5    from 67 To 640
        SetMemory(0x6C9944, Add, -12226),# flingy:Halt Distance  index:5    from 12227 To 1
        SetMemory(0x6C9E24, Add, 10240),# flingy:Turn Radius  index:5    from 40 To 80
        SetMemory(0x66A028, Add, 262144),# images:Draw Function  index:514    from 9 To 13
        SetMemory(0x66EC48, Add, 155),# images:Iscript ID  index:0    from 0 To 155
        SetMemory(0x66FB8C, Add, -141),# images:Iscript ID  index:977    from 391 To 250
    ])

