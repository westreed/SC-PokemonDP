﻿from eudplib import *
import TriggerEditor.SCArchive as sca


VChatIndex = EUDArray(8)
VMouseDown_L = EUDArray(8)

def Reg():
    print('... TERegVar ...')
    EUDRegisterObjectToNamespace("VMouseDown_L", VMouseDown_L)
    EUDRegisterObjectToNamespace("VChatIndex", VChatIndex)
    sca.Init()
EUDOnStart(Reg)
