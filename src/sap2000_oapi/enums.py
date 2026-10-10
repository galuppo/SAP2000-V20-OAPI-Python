"""Enumerações eXxx extraídas da documentação da OAPI (SAP2000 v20)."""

from __future__ import annotations

from enum import IntEnum


class e2DFrameType(IntEnum):
    PortalFrame = 0
    ConcentricBraced = 1
    EccentricBraced = 2


class e3DFrameType(IntEnum):
    OpenFrame = 0
    PerimeterFrame = 1
    BeamSlab = 2
    FlatPlate = 3


class eCNameType(IntEnum):
    LoadCase = 0
    LoadCombo = 1


class eConstraintAxis(IntEnum):
    X = 1
    Y = 2
    Z = 3
    AutoAxis = 4


class eConstraintType(IntEnum):
    CONSTRAINT_BODY = 1
    CONSTRAINT_DIAPHRAGM = 2
    CONSTRAINT_PLATE = 3
    CONSTRAINT_ROD = 4
    CONSTRAINT_BEAM = 5
    CONSTRAINT_EQUAL = 6
    CONSTRAINT_LOCAL = 7
    CONSTRAINT_WELD = 8
    CONSTRAINT_LINE = 13


class eFramePropType(IntEnum):
    SECTION_I = 1
    SECTION_CHANNEL = 2
    SECTION_T = 3
    SECTION_ANGLE = 4
    SECTION_DBLANGLE = 5
    SECTION_BOX = 6
    SECTION_PIPE = 7
    SECTION_RECTANGULAR = 8
    SECTION_CIRCLE = 9
    SECTION_GENERAL = 10
    SECTION_DBCHANNEL = 11
    SECTION_AUTO = 12
    SECTION_SD = 13
    SECTION_VARIABLE = 14
    SECTION_JOIST = 15
    SECTION_BRIDGE = 16
    SECTION_COLD_C = 17
    SECTION_COLD_2C = 18
    SECTION_COLD_Z = 19
    SECTION_COLD_L = 20


class eItemType(IntEnum):
    Object = 0
    Group = 1
    SelectedObjects = 2
    Selection = 2


class eItemTypeElm(IntEnum):
    ObjectElm = 0
    Element = 1
    GroupElm = 2
    SelectionElm = 3
    GroupElmc = 2


class eLinkPropType(IntEnum):
    NLPROP_LINEAR = 1
    NLPROP_DAMPER = 2
    NLPROP_GAP = 3
    NLPROP_HOOK = 4
    NLPROP_PLASTIC_WEN = 5
    NLPROP_ISOLATOR1 = 6
    NLPROP_ISOLATOR2 = 7
    NLPROP_MULTILINEAR_ELASTIC = 8
    NLPROP_MULTILINEAR_PLASTIC = 9
    NLPROP_ISOLATOR3 = 10


class eLoadCaseType(IntEnum):
    CASE_LINEAR_STATIC = 1
    CASE_NONLINEAR_STATIC = 2
    CASE_MODAL = 3
    CASE_RESPONSE_SPECTRUM = 4
    CASE_LINEAR_HISTORY = 5
    CASE_NONLINEAR_HISTORY = 6
    CASE_LINEAR_DYNAMIC = 7
    CASE_NONLINEAR_DYNAMIC = 8
    CASE_MOVING_LOAD = 9
    CASE_BUCKLING = 10
    CASE_STEADY_STATE = 11
    CASE_POWER_SPECTRAL_DENSITY = 12


class eLoadPatternType(IntEnum):
    LTYPE_DEAD = 1
    LTYPE_SUPERDEAD = 2
    LTYPE_LIVE = 3
    LTYPE_REDUCELIVE = 4
    LTYPE_QUAKE = 5
    LTYPE_WIND = 6
    LTYPE_SNOW = 7
    LTYPE_OTHER = 8
    LTYPE_MOVE = 9
    LTYPE_TEMPERATURE = 10
    LTYPE_ROOFLIVE = 11
    LTYPE_NOTIONAL = 12
    LTYPE_PATTERNLIVE = 13
    LTYPE_WAVE = 14
    LTYPE_BRAKING = 15
    LTYPE_CENTRIFUGAL = 16
    LTYPE_FRICTION = 17
    LTYPE_ICE = 18
    LTYPE_WINDONLIVELOAD = 19
    LTYPE_HORIZONTALEARTHPRESSURE = 20


class eMatType(IntEnum):
    MATERIAL_STEEL = 1
    MATERIAL_CONCRETE = 2
    MATERIAL_NODESIGN = 3
    MATERIAL_ALUMINUM = 4
    MATERIAL_COLDFORMED = 5
    MATERIAL_REBAR = 6
    MATERIAL_TENDON = 7


class eUnits(IntEnum):
    lb_in_F = 1
    lb_ft_F = 2
    kip_in_F = 3
    kip_ft_F = 4
    kN_mm_C = 5
    kN_m_C = 6
    kgf_mm_C = 7
    kgf_m_C = 8
    N_mm_C = 9
    N_m_C = 10
    Ton_mm_C = 11
    Ton_m_C = 12
    kN_cm_C = 13
    kgf_cm_C = 14
    N_cm_C = 15
    Ton_cm_C = 16

class eLoadDistributedDir(IntEnum):
    LOCAL_1 = 1
    LOCAL_2 = 2
    LOCAL_3 = 3
    GLOBAL_X = 4
    GLOBAL_Y = 5
    GLOBAL_Z = 6
    PROJECTED_X = 7
    PROJECTED_Y = 8
    PROJECTED_Z = 9
    GRAVITY = 10
    GRAVITY_PROJECTED = 11

class eLoadDistributedType(IntEnum):
    FORCE = 1
    MOMENT = 2

class eGroupObjectType(IntEnum):
    POINT = 1
    FRAME = 2
    CABLE = 3
    TENDON = 4
    AREA = 5
    SOLID = 6
    LINK = 7

class eFrameResultIndex(IntEnum):
    NUMBER_RESULTS = 0
    OBJ = 1
    OBJ_STATION = 2
    ELM = 3
    ELM_STATION = 4
    LOAD_CASE = 5
    STEP_TYPE = 6
    STEP_NUM = 7
    P = 8
    V2 = 9
    V3 = 10
    T = 11
    M2 = 12
    M3 = 13
    


