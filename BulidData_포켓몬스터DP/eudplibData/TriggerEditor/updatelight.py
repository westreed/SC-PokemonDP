from eudplib import *


def UpdateLight(setlight_deaths, setdelay_deaths=None):
    setlight = EncodeUnit(setlight_deaths)  # 밝기 목표 설정용 데스값

    localcp = f_getuserplayerid()
    # CurrentPlayer를 LocalUser로 설정.
    VProc(localcp, localcp.QueueAssignTo(EPD(0x6509B0)))

    BRIGHTNESS = 0x657A9C  # 밝기 오프셋
    IsLightGoal = Memory(BRIGHTNESS, Exactly, 0)  # 현재 밝기가 목표와 같은지 보는 조건
    IsLightMoreThanGoal = Memory(BRIGHTNESS, AtLeast, 0)  # 현재 밝기가 목표 밝기보다 큰지 보는 조건

    IsGoalUnchanged = Deaths(CurrentPlayer, Exactly, 0, setlight)  # 목표 밝기가 그대로인지 보는 조건
    if EUDIfNot()(IsGoalUnchanged):
        # 목표 밝기가 변했으면 목표를 다시 읽어온다.
        light_goal = f_maskread_epd(12 * setlight + localcp, 31)
        # 새 목표 밝기에 맞게 트리거 업데이트.
        VProc(light_goal, light_goal.SetDest(EPD(IsGoalUnchanged) + 2))
        # (목표 밝기) 를 IsLightGoal의 비교할 값 칸에 대입
        VProc(light_goal, light_goal.SetDest(EPD(IsLightGoal) + 2))
        VProc(
            light_goal,
            [
                light_goal.AddNumber(1),
                # (목표+1) 을 IsLightMoreThanGoal의 비교할 값 칸에 대입
                light_goal.SetDest(EPD(IsLightMoreThanGoal) + 2),
            ],
        )
    EUDEndIf()

    delay = EUDLightVariable()
    SetDelay = delay.SetNumber(0)
    if setdelay_deaths is not None:
        setdelay = EncodeUnit(setdelay_deaths)  # 딜레이 설정용 데스값
        IsDelayUnchanged = Deaths(CurrentPlayer, Exactly, 0, setdelay)
        if EUDIfNot()(IsDelayUnchanged):
            new_delay = f_dwread_epd(12 * setdelay + localcp)
            VProc(new_delay, new_delay.SetDest(EPD(IsDelayUnchanged) + 2))
            # SetDelay의 대입할 값 칸에 새 딜레이 값 대입.
            VProc(new_delay, new_delay.SetDest(EPD(SetDelay) + 5))
        EUDEndIf()

    if EUDIfNot()(IsLightGoal):
        # 딜레이가 남아있으면 딜레이-1 하고 패스
        if EUDIf()(delay >= 1):
            delay -= 1
        if EUDElse()():
            DoActions(SetDelay)
            # 현재 밝기가 목표가 아니면, 목표보다 큰지 비교.
            if EUDIf()(IsLightMoreThanGoal):
                # 목표 밝기보다 크니까 밝기를 1 내린다.
                DoActions(SetMemory(BRIGHTNESS, Subtract, 1))
            if EUDElse()():
                # 목표 밝기보다 작으니까 밝기를 1 올린다.
                DoActions(SetMemory(BRIGHTNESS, Add, 1))
            EUDEndIf()
        EUDEndIf()
    EUDEndIf()
    f_setcurpl2cpcache()
