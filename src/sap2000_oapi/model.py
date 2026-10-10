"""Monta a árvore SapModel completa a partir dos nós gerados."""

from __future__ import annotations

from functools import cached_property

from ._nodes.n__root import RootMethods
from ._nodes.n_analyze import N_Analyze
from ._nodes.n_areaelm import N_AreaElm
from ._nodes.n_areaobj import N_AreaObj
from ._nodes.n_bridgeadvancedsuper import N_BridgeAdvancedSuper, N_BridgeAdvancedSuper_BASConcBox
from ._nodes.n_bridgeobj import N_BridgeObj
from ._nodes.n_cableobj import N_CableObj
from ._nodes.n_constraintdef import N_ConstraintDef
from ._nodes.n_coordsys import N_CoordSys
from ._nodes.n_designaluminum import N_DesignAluminum, N_DesignAluminum_AA_ASD_2000, N_DesignAluminum_AA_LRFD_2000
from ._nodes.n_designcoldformed import N_DesignColdFormed, N_DesignColdFormed_AISI_ASD96, N_DesignColdFormed_AISI_LRFD96
from ._nodes.n_designconcrete import N_DesignConcrete, N_DesignConcrete_AASHTO_Concrete_07, N_DesignConcrete_AASHTO_LRFD_2012, N_DesignConcrete_AASHTO_LRFD_2014, N_DesignConcrete_ACI318_05_IBC2003, N_DesignConcrete_ACI318_08_IBC2009, N_DesignConcrete_ACI_318_02, N_DesignConcrete_ACI_318_99, N_DesignConcrete_AS_3600_01, N_DesignConcrete_AS_3600_09, N_DesignConcrete_BS8110_89, N_DesignConcrete_BS8110_97, N_DesignConcrete_CSA_A23_3_04, N_DesignConcrete_CSA_A23_3_94, N_DesignConcrete_Chinese_2010, N_DesignConcrete_EUROCODE_2_1992, N_DesignConcrete_Eurocode_2_2004, N_DesignConcrete_Hong_Kong_CP_2004, N_DesignConcrete_Hong_Kong_CP_2013, N_DesignConcrete_Indian_IS_456_2000, N_DesignConcrete_Indian_IS_456_2003, N_DesignConcrete_Italian_DM_14_2_92, N_DesignConcrete_KCI_1999, N_DesignConcrete_Mexican_RCDF_2001, N_DesignConcrete_NZS_3101_95, N_DesignConcrete_SP63_13330_2012, N_DesignConcrete_Singaopre_CP_65_99, N_DesignConcrete_Singapore_CP_65_99, N_DesignConcrete_UBC97
from ._nodes.n_designsteel import N_DesignSteel, N_DesignSteel_AISC360_05_IBC2006, N_DesignSteel_AISC360_10, N_DesignSteel_AISC_ASD01, N_DesignSteel_AISC_ASD89, N_DesignSteel_AISC_LRFD93, N_DesignSteel_AISC_LRFD99, N_DesignSteel_API_RP2A_LRFD97, N_DesignSteel_API_RP2A_WSD2000, N_DesignSteel_API_RP2A_WSD2014, N_DesignSteel_ASCE_10_97, N_DesignSteel_Australian_AS4100_1998, N_DesignSteel_BS5950_2000, N_DesignSteel_BS5950_90, N_DesignSteel_CISC_95, N_DesignSteel_Canadian_S16_01, N_DesignSteel_Canadian_S16_09, N_DesignSteel_Chinese_2010, N_DesignSteel_EUROCODE_3_1993, N_DesignSteel_Eurocode_3_2005, N_DesignSteel_INDIAN_IS_800_1998, N_DesignSteel_ITALIAN_UNI_10011, N_DesignSteel_Indian_IS_800_1998, N_DesignSteel_Indian_IS_800_2007, N_DesignSteel_Italian_NTC_2008, N_DesignSteel_Italian_NTC_2018, N_DesignSteel_Italian_UNI_10011, N_DesignSteel_NewZealand_NZS3404_1997, N_DesignSteel_Norsok_N004, N_DesignSteel_Norsok_N0042013, N_DesignSteel_SP_16_13330_2011, N_DesignSteel_UBC97_ASD, N_DesignSteel_UBC97_LRFD
from ._nodes.n_editarea import N_EditArea
from ._nodes.n_editframe import N_EditFrame
from ._nodes.n_editgeneral import N_EditGeneral
from ._nodes.n_editpoint import N_EditPoint
from ._nodes.n_editsolid import N_EditSolid
from ._nodes.n_externalanalysisresults import N_ExternalAnalysisResults
from ._nodes.n_file import N_File
from ._nodes.n_frameobj import N_FrameObj
from ._nodes.n_func import N_Func, N_Func_FuncPSD, N_Func_FuncRS, N_Func_FuncSS, N_Func_FuncTH
from ._nodes.n_gdispl import N_GDispl
from ._nodes.n_genrefline import N_GenRefLine
from ._nodes.n_group import N_Group
from ._nodes.n_groupdef import N_GroupDef
from ._nodes.n_lineelm import N_LineElm
from ._nodes.n_linkelm import N_LinkElm
from ._nodes.n_linkobj import N_LinkObj
from ._nodes.n_loadcases import N_LoadCases, N_LoadCases_Buckling, N_LoadCases_DirHistLinear, N_LoadCases_DirHistNonlinear, N_LoadCases_ExternalResults, N_LoadCases_HyperStatic, N_LoadCases_ModHistLinear, N_LoadCases_ModHistNonlinear, N_LoadCases_ModalEigen, N_LoadCases_ModalRitz, N_LoadCases_Moving, N_LoadCases_PSD, N_LoadCases_ResponseSpectrum, N_LoadCases_StaticLinear, N_LoadCases_StaticLinearMultistep, N_LoadCases_StaticNonlinear, N_LoadCases_StaticNonlinearStaged, N_LoadCases_Static_Nonlinear, N_LoadCases_Static_NonlinearStaged, N_LoadCases_SteadyState
from ._nodes.n_loadpatterns import N_LoadPatterns, N_LoadPatterns_AutoSeastate, N_LoadPatterns_AutoSeismic, N_LoadPatterns_AutoWind
from ._nodes.n_namedassign import N_NamedAssign, N_NamedAssign_ModifierArea, N_NamedAssign_ModifierCable, N_NamedAssign_ModifierFrame, N_NamedAssign_ReleaseFrame
from ._nodes.n_namedsets import N_NamedSets
from ._nodes.n_options import N_Options
from ._nodes.n_patterndef import N_PatternDef
from ._nodes.n_planeelm import N_PlaneElm
from ._nodes.n_pointelm import N_PointElm
from ._nodes.n_pointobj import N_PointObj
from ._nodes.n_proparea import N_PropArea
from ._nodes.n_propcable import N_PropCable
from ._nodes.n_propframe import N_PropFrame, N_PropFrame_SDShape
from ._nodes.n_proplink import N_PropLink
from ._nodes.n_propmaterial import N_PropMaterial, N_PropMaterial_TimeDep
from ._nodes.n_propsolid import N_PropSolid
from ._nodes.n_proptendon import N_PropTendon
from ._nodes.n_respcombo import N_RespCombo
from ._nodes.n_results import N_Results, N_Results_Setup
from ._nodes.n_sapmdel import N_SapMdel, N_SapMdel_PointObj
from ._nodes.n_sapmoel import N_SapMoel, N_SapMoel_SelectObj
from ._nodes.n_sectcut import N_SectCut
from ._nodes.n_selectobj import N_SelectObj
from ._nodes.n_solidelm import N_SolidElm
from ._nodes.n_solidobj import N_SolidObj
from ._nodes.n_sourcemass import N_SourceMass
from ._nodes.n_tendonobj import N_TendonObj
from ._nodes.n_view import N_View


class SapModelWrapper(RootMethods):
    """Wrapper tipado para SapModel. Espelha a árvore de objetos da OAPI:
    sap.PropMaterial.SetMaterial(...), sap.LoadPatterns.AutoSeismic.GetNBCC95(...), etc.
    """

    def __init__(self, raw):
        self._raw = raw

    @cached_property
    def Analyze(self):
        return N_Analyze(self._raw.Analyze)

    @cached_property
    def AreaElm(self):
        return N_AreaElm(self._raw.AreaElm)

    @cached_property
    def AreaObj(self):
        return N_AreaObj(self._raw.AreaObj)

    @cached_property
    def BridgeAdvancedSuper(self):
        return N_BridgeAdvancedSuper(self._raw.BridgeAdvancedSuper)

    @cached_property
    def BridgeObj(self):
        return N_BridgeObj(self._raw.BridgeObj)

    @cached_property
    def CableObj(self):
        return N_CableObj(self._raw.CableObj)

    @cached_property
    def ConstraintDef(self):
        return N_ConstraintDef(self._raw.ConstraintDef)

    @cached_property
    def CoordSys(self):
        return N_CoordSys(self._raw.CoordSys)

    @cached_property
    def DesignAluminum(self):
        return N_DesignAluminum(self._raw.DesignAluminum)

    @cached_property
    def DesignColdFormed(self):
        return N_DesignColdFormed(self._raw.DesignColdFormed)

    @cached_property
    def DesignConcrete(self):
        return N_DesignConcrete(self._raw.DesignConcrete)

    @cached_property
    def DesignSteel(self):
        return N_DesignSteel(self._raw.DesignSteel)

    @cached_property
    def EditArea(self):
        return N_EditArea(self._raw.EditArea)

    @cached_property
    def EditFrame(self):
        return N_EditFrame(self._raw.EditFrame)

    @cached_property
    def EditGeneral(self):
        return N_EditGeneral(self._raw.EditGeneral)

    @cached_property
    def EditPoint(self):
        return N_EditPoint(self._raw.EditPoint)

    @cached_property
    def EditSolid(self):
        return N_EditSolid(self._raw.EditSolid)

    @cached_property
    def ExternalAnalysisResults(self):
        return N_ExternalAnalysisResults(self._raw.ExternalAnalysisResults)

    @cached_property
    def File(self):
        return N_File(self._raw.File)

    @cached_property
    def FrameObj(self):
        return N_FrameObj(self._raw.FrameObj)

    @cached_property
    def Func(self):
        return N_Func(self._raw.Func)

    @cached_property
    def GDispl(self):
        return N_GDispl(self._raw.GDispl)

    @cached_property
    def GenRefLine(self):
        return N_GenRefLine(self._raw.GenRefLine)

    @cached_property
    def Group(self):
        return N_Group(self._raw.Group)

    @cached_property
    def GroupDef(self):
        return N_GroupDef(self._raw.GroupDef)

    @cached_property
    def LineElm(self):
        return N_LineElm(self._raw.LineElm)

    @cached_property
    def LinkElm(self):
        return N_LinkElm(self._raw.LinkElm)

    @cached_property
    def LinkObj(self):
        return N_LinkObj(self._raw.LinkObj)

    @cached_property
    def LoadCases(self):
        return N_LoadCases(self._raw.LoadCases)

    @cached_property
    def LoadPatterns(self):
        return N_LoadPatterns(self._raw.LoadPatterns)

    @cached_property
    def NamedAssign(self):
        return N_NamedAssign(self._raw.NamedAssign)

    @cached_property
    def NamedSets(self):
        return N_NamedSets(self._raw.NamedSets)

    @cached_property
    def Options(self):
        return N_Options(self._raw.Options)

    @cached_property
    def PatternDef(self):
        return N_PatternDef(self._raw.PatternDef)

    @cached_property
    def PlaneElm(self):
        return N_PlaneElm(self._raw.PlaneElm)

    @cached_property
    def PointElm(self):
        return N_PointElm(self._raw.PointElm)

    @cached_property
    def PointObj(self):
        return N_PointObj(self._raw.PointObj)

    @cached_property
    def PropArea(self):
        return N_PropArea(self._raw.PropArea)

    @cached_property
    def PropCable(self):
        return N_PropCable(self._raw.PropCable)

    @cached_property
    def PropFrame(self):
        return N_PropFrame(self._raw.PropFrame)

    @cached_property
    def PropLink(self):
        return N_PropLink(self._raw.PropLink)

    @cached_property
    def PropMaterial(self):
        return N_PropMaterial(self._raw.PropMaterial)

    @cached_property
    def PropSolid(self):
        return N_PropSolid(self._raw.PropSolid)

    @cached_property
    def PropTendon(self):
        return N_PropTendon(self._raw.PropTendon)

    @cached_property
    def RespCombo(self):
        return N_RespCombo(self._raw.RespCombo)

    @cached_property
    def Results(self):
        return N_Results(self._raw.Results)

    @cached_property
    def SapMdel(self):
        return N_SapMdel(self._raw.SapMdel)

    @cached_property
    def SapMoel(self):
        return N_SapMoel(self._raw.SapMoel)

    @cached_property
    def SectCut(self):
        return N_SectCut(self._raw.SectCut)

    @cached_property
    def SelectObj(self):
        return N_SelectObj(self._raw.SelectObj)

    @cached_property
    def SolidElm(self):
        return N_SolidElm(self._raw.SolidElm)

    @cached_property
    def SolidObj(self):
        return N_SolidObj(self._raw.SolidObj)

    @cached_property
    def SourceMass(self):
        return N_SourceMass(self._raw.SourceMass)

    @cached_property
    def TendonObj(self):
        return N_TendonObj(self._raw.TendonObj)

    @cached_property
    def View(self):
        return N_View(self._raw.View)

