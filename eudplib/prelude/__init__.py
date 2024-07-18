#!/usr/bin/python
# Copyright 2023 by Armoha.
# All rights reserved.
# This file is part of EUD python library (eudplib),
# and is released under "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

# ruff: noqa: I001
# fmt: off
from ..core import (
    f_div,
    EUDVariable, EUDCreateVariables, SetVariables,
    VProc,
    Db,
    RawTrigger, PreserveTrigger,
    UnitProperty, Disabled,
    # EUDFunc
    EUDFunc, EUDTypedFunc, EUDFuncPtr, EUDTypedFuncPtr,
    EUDMethod, EUDTypedMethod, EUDReturn,
    # EUDStruct
    EUDStruct, EUDVArray, selftype,
    # ConstType
    Iscript,
    Portrait, Icon,
    StatText,
    TrgAIScript, TrgAllyStatus, TrgComparison, TrgCount,
    TrgLocation, TrgModifier, TrgOrder, TrgProperty,
    TrgPropState, TrgResource, TrgScore, TrgString, TrgSwitch,
    TrgSwitchAction, TrgSwitchState,
    # Condition
    Always, Never,
    Accumulate, Bring,
    Command, CommandLeast, CommandLeastAt, CommandMost, CommandMostAt,
    CountdownTimer, ElapsedTime,
    Deaths, DeathsX, Kills,
    Memory, MemoryEPD, MemoryX, MemoryXEPD,
    HighestScore, MostKills, MostResources,
    LowestScore, LeastKills, LeastResources,
    Opponents,
    Score, Switch,
    # Action
    SetCurrentPlayer,
    CenterView, CreateUnit, CreateUnitWithProperties, Comment,
    Defeat, DisplayText, Draw,
    GiveUnits,
    KillUnit, KillUnitAt,
    LeaderBoardComputerPlayers,
    LeaderBoardControl, LeaderBoardGoalControl,
    LeaderBoardControlAt, LeaderBoardGoalControlAt,
    LeaderBoardGreed, LeaderBoardResources, LeaderBoardGoalResources,
    LeaderBoardKills, LeaderBoardGoalKills,
    LeaderBoardScore, LeaderBoardGoalScore,
    MinimapPing,
    ModifyUnitEnergy, ModifyUnitHangarCount, ModifyUnitHitPoints,
    ModifyUnitResourceAmount, ModifyUnitShields,
    MoveLocation, MoveUnit,
    Order,
    MuteUnitSpeech, PauseGame, PauseTimer,
    UnMuteUnitSpeech, UnpauseGame, UnpauseTimer,
    PlayWAV,
    RemoveUnit, RemoveUnitAt,
    RunAIScript, RunAIScriptAt,
    SetAllianceStatus, SetCountdownTimer,
    SetDeaths, SetDeathsX, SetKills,
    SetDoodadState, SetInvincibility,
    SetMemory, SetMemoryEPD, SetMemoryX, SetMemoryXEPD,
    SetMissionObjectives, SetNextScenario,
    SetResources, SetScore, SetSwitch,
    TalkingPortrait, Transmission,
    Victory,
    Wait,
    # TrgResource
    Ore, Gas, OreAndGas,
    # TrgAllyStatus
    Ally, Enemy, AlliedVictory,
    # TrgOrder
    Attack, Move, Patrol,
    # TrgScore
    Units, Buildings, UnitsAndBuildings,
    Razings, KillsAndRazings, Total, Custom,
    # TrgComparison
    AtLeast, AtMost, Exactly,
    # TrgModifier
    Add, Subtract, SetTo,
    # TrgPropState
    Enable, Disable, Toggle,
    # TrgSwitchState
    Set, Cleared,
    # TrgSwitchAction
    Clear, Random,
    # TrgCount
    All,
)
from ..utils import EPD
from ..ctrlstru import (
    DoActions, EUDTernary, EUDLoopRange,
    EUDWhile, EUDWhileNot, EUDEndWhile,
    EUDBreak, EUDContinue, EUDSetContinuePoint,
    EUDContinueIf, EUDContinueIfNot,
    EUDSCAnd, EUDSCOr,
    EUDIf, EUDIfNot, EUDEndIf,
    EUDElseIf, EUDElseIfNot, EUDElse,
    EUDSwitch, EPDSwitch, EUDEndSwitch,
    EUDSwitchCase, EUDSwitchDefault,
)
from ..memio import (
    f_getcurpl, f_setcurpl,
    f_dwread_epd, f_dwepdread_epd, f_epdread_epd,
    f_dwwrite_epd, f_dwadd_epd, f_dwsubtract_epd,
    f_wread_epd, f_wwrite_epd,
    f_bread_epd, f_bwrite_epd,
    f_maskread_epd, f_posread_epd,
    f_dwread, f_dwwrite,
    f_wread, f_wwrite,
    f_bread, f_bwrite,
)
from ..collections import (
    EUDArray, EUDDeque, EUDQueue, EUDStack,
    PVariable, UnitGroup
)
from ..offsetmap.cunit import CUnit
from ..offsetmap.scdata import (
    Flingy,
    Image,
    Sprite,
    Tech,
    TrgUnit,
    UnitOrder,
    Upgrade,
    Weapon,
    TrgPlayer,
    P1, P2, P3, P4, P5, P6, P7, P8, P9, P10, P11, P12,
    Force1, Force2, Force3, Force4, AllPlayers, CurrentPlayer,
    Allies, Foes, NeutralPlayers, NonAlliedVictoryPlayers,
)
from ..string import (
    IsPName, SetPNamef,
    StringBuffer,
    f_println, f_printAt,
    f_printAll, f_printAllAt,
    f_simpleprint,
    f_eprintf, f_settblf,
)

__all__ = [
    "f_div",
    "EUDVariable", "EUDCreateVariables", "SetVariables",
    "VProc",
    "Db",
    "RawTrigger", "PreserveTrigger",
    "UnitProperty", "Disabled",
    # EUDFunc
    "EUDFunc", "EUDTypedFunc", "EUDFuncPtr", "EUDTypedFuncPtr",
    "EUDMethod", "EUDTypedMethod", "EUDReturn",
    # EUDStruct
    "EUDStruct", "EUDVArray", "selftype",
    # ConstType
    "Weapon", "Flingy", "Sprite", "Image", "Iscript",
    "Portrait", "Icon", "Upgrade", "Tech",
    "UnitOrder", "StatText",
    "TrgAIScript", "TrgAllyStatus", "TrgComparison", "TrgCount",
    "TrgLocation", "TrgModifier", "TrgOrder", "TrgPlayer", "TrgProperty",
    "TrgPropState", "TrgResource", "TrgScore", "TrgString", "TrgSwitch",
    "TrgSwitchAction", "TrgSwitchState", "TrgUnit",
    # TrgPlayer
    "P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10", "P11", "P12",
    "Force1", "Force2", "Force3", "Force4", "AllPlayers", "CurrentPlayer",
    "Allies", "Foes", "NeutralPlayers", "NonAlliedVictoryPlayers",
    # Condition
    "Always", "Never",
    "Accumulate", "Bring",
    "Command", "CommandLeast", "CommandLeastAt", "CommandMost", "CommandMostAt",
    "CountdownTimer", "ElapsedTime",
    "Deaths", "DeathsX", "Kills",
    "Memory", "MemoryEPD", "MemoryX", "MemoryXEPD",
    "HighestScore", "MostKills", "MostResources",
    "LowestScore", "LeastKills", "LeastResources",
    "Opponents",
    "Score", "Switch",
    # Action
    "SetCurrentPlayer",
    "CenterView", "CreateUnit", "CreateUnitWithProperties", "Comment",
    "Defeat", "DisplayText", "Draw",
    "GiveUnits",
    "KillUnit", "KillUnitAt",
    "LeaderBoardComputerPlayers",
    "LeaderBoardControl", "LeaderBoardGoalControl",
    "LeaderBoardControlAt", "LeaderBoardGoalControlAt",
    "LeaderBoardGreed", "LeaderBoardResources", "LeaderBoardGoalResources",
    "LeaderBoardKills", "LeaderBoardGoalKills",
    "LeaderBoardScore", "LeaderBoardGoalScore",
    "MinimapPing",
    "ModifyUnitEnergy", "ModifyUnitHangarCount", "ModifyUnitHitPoints",
    "ModifyUnitResourceAmount", "ModifyUnitShields",
    "MoveLocation", "MoveUnit",
    "Order",
    "MuteUnitSpeech", "PauseGame", "PauseTimer",
    "UnMuteUnitSpeech", "UnpauseGame", "UnpauseTimer",
    "PlayWAV",
    "RemoveUnit", "RemoveUnitAt",
    "RunAIScript", "RunAIScriptAt",
    "SetAllianceStatus", "SetCountdownTimer",
    "SetDeaths", "SetDeathsX", "SetKills",
    "SetDoodadState", "SetInvincibility",
    "SetMemory", "SetMemoryEPD", "SetMemoryX", "SetMemoryXEPD",
    "SetMissionObjectives", "SetNextScenario",
    "SetResources", "SetScore", "SetSwitch",
    "TalkingPortrait", "Transmission",
    "Victory",
    "Wait",
    # TrgResource
    "Ore", "Gas", "OreAndGas",
    # TrgAllyStatus
    "Ally", "Enemy", "AlliedVictory",
    # TrgOrder
    "Attack", "Move", "Patrol",
    # TrgScore
    "Units", "Buildings", "UnitsAndBuildings",
    "Razings", "KillsAndRazings", "Total", "Custom",
    # TrgComparison
    "AtLeast", "AtMost", "Exactly",
    # TrgModifier
    "Add", "Subtract", "SetTo",
    # TrgPropState
    "Enable", "Disable", "Toggle",
    # TrgSwitchState
    "Set", "Cleared",
    # TrgSwitchAction
    "Clear", "Random",
    # TrgCount
    "All",
    # utils
    "EPD",
    # control structures
    "DoActions", "EUDTernary", "EUDLoopRange",
    "EUDWhile", "EUDWhileNot", "EUDEndWhile",
    "EUDBreak", "EUDContinue", "EUDSetContinuePoint",
    "EUDContinueIf", "EUDContinueIfNot",
    "EUDSCAnd", "EUDSCOr",
    "EUDIf", "EUDIfNot", "EUDEndIf",
    "EUDElseIf", "EUDElseIfNot", "EUDElse",
    "EUDSwitch", "EPDSwitch", "EUDEndSwitch",
    "EUDSwitchCase", "EUDSwitchDefault",
    # memio
    "f_getcurpl", "f_setcurpl",
    "f_dwread_epd", "f_dwepdread_epd", "f_epdread_epd",
    "f_dwwrite_epd", "f_dwadd_epd", "f_dwsubtract_epd",
    "f_wread_epd", "f_wwrite_epd",
    "f_bread_epd", "f_bwrite_epd",
    "f_maskread_epd", "f_posread_epd",
    "f_dwread", "f_dwwrite",
    "f_wread", "f_wwrite",
    "f_bread", "f_bwrite",
    # collections
    "EUDArray", "EUDDeque", "EUDQueue", "EUDStack",
    "PVariable", "UnitGroup",
    # string
    "IsPName", "SetPNamef",
    "StringBuffer",
    "f_println", "f_printAt",
    "f_printAll", "f_printAllAt",
    "f_simpleprint",
    "f_eprintf", "f_settblf",
    # offsetmap
    "CUnit",
]
