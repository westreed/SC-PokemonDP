from eudplib import *


def WriteVersion(versionCheck):
    chkt = GetChkTokenized()
    #buildTime = GetStringIndex(str(datetime.now()))
    SPRP = bytearray(chkt.getsection("SPRP"))
    a = unProxy(versionCheck)
    versionN = str(a)
    SPRP[0:2] = i2b2(GetStringIndex("{}{}.{}.{}".format("[EUD] 언데드 디펜스 ", versionN[0], versionN[1], versionN[2])))
    chkt.setsection("SPRP", SPRP)