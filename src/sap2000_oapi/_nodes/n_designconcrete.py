"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_DesignConcrete:
    """Wrapper para SapModel.DesignConcrete."""

    def __init__(self, raw):
        self._raw = raw

    def DeleteResults(self):
        """This function deletes all concrete frame design results. The function returns zero if the
        results are successfully deleted; otherwise it returns a nonzero value.
        """
        _r = self._raw.DeleteResults()
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.DeleteResults falhou (ret={_r})".format(_r=_r))
        return None

    def GetCode(self):
        """This function retrieves the concrete design code. The function returns zero if the code is
        successfully retrieved; otherwise it returns a nonzero value.
    
        CodeName (output): This is one of the following concrete design code names. AASHTO
            LRFD 2014 AASHTO LRFD 2012 AASHTO Concrete 07 ACI 318-14 ACI 318-11 ACI
            318-08/IBC2009 AS 3600-09 BS8110 97 Chinese 2010 CSA A23.3-14 CSA A23.3-04
            Eurocode 2-2004 Hong Kong CP 2013 Indian IS 456-2000 Italian NTC 2008 KBC 2009
            Mexican RCDF 2004 NZS 3101:2006 Singapore CP 65:99 SP 63.13330.2012 TS 500-2000
        """
        _r = self._raw.GetCode("")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.GetCode falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetComboAutoGenerate(self, AutoGenerate: bool):
        """This function retrieves the value of the automatically generated code-based design load
        combinations option for concrete frame design. The function returns zero if the
        options are successfully set; otherwise it returns a nonzero value.
    
        AutoGenerate (input): If this item is True, the option to automatically generate
            code-based design load combinations for concrete frame design is turned on. If
            it is False, the option is turned off.
        """
        _r = self._raw.GetComboAutoGenerate(AutoGenerate)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.GetComboAutoGenerate falhou (ret={_r})".format(_r=_r))
        return None

    def GetComboStrength(self):
        """This function retrieves the names of all load combinations selected as design combinations
        for concrete strength design. The function returns zero if the names are
        successfully retrieved; otherwise it returns a nonzero value.
    
        NumberItems (output): The number of load combinations selected as design
            combinations for concrete strength design.
        MyName (output): This is an array that includes the name of each response
            combination selected as a design combination for concrete strength design.
        """
        _r = self._raw.GetComboStrength(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.GetComboStrength falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDesignSection(self, Name: str):
        """This function retrieves the design section for a specified concrete frame object. The
        function returns zero if the section is successfully retrieved; otherwise it returns
        a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        PropName (output): The name of the design section for the specified frame object.
        """
        _r = self._raw.GetDesignSection(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.GetDesignSection falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetResultsAvailable(self):
        """The function returns True if the concrete frame design results are available, otherwise
        False.
        """
        _r = self._raw.GetResultsAvailable()
        return _r

    def GetSummaryResultsBeam(self, Name: str, ItemType: int = 0):
        """This function retrieves summary results for concrete design. The function returns zero if
        the results are successfully retrieved; otherwise it returns a nonzero value. Note
        that torsional design is only included for some codes.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The number of frame objects for which results are obtained.
        FrameName (output): This is an array that includes each frame object name for which
            results are obtained.
        Location (output): This is an array that includes the distance from the I-end of the
            frame object to the location where the results are reported. [L]
        TopCombo (output): This is an array that includes the name of the design combination
            for which the controlling top longitudinal rebar area for flexure occurs. A
            combination name followed by (Sp) indicates that the design loads were obtained
            by applying special, code-specific multipliers to all or part of the specified
            design load combination, or that the design was based on the capacity of other
            objects (or other design locations for the same object).
        TopArea (output): This is an array that includes the total top longitudinal rebar
            area required for the flexure at the specified location. It does not include the
            area of steel required for torsion. [L 2 ]
        BotCombo (output): This is an array that includes the name of the design combination
            for which the controlling bottom longitudinal rebar area for flexure occurs. A
            combination name followed by (Sp) indicates that the design loads were obtained
            by applying special, code-specific, multipliers to all or part of the specified
            design load combination, or that the design was based on the capacity of other
            objects (or other design locations for the same object).
        BotArea (output): This is an array that includes the total bottom longitudinal rebar
            area required for the flexure at the specified location. It does not include the
            area of steel required for torsion. [L 2 ]
        VmajorCombo (output): This is an array that includes the name of the design
            combination for which the controlling shear occurs. A combination name followed
            by (Sp) indicates that the design loads were obtained by applying special, code-
            specific, multipliers to all or part of the specified design load combination,
            or that the design was based on the capacity of other objects (or other design
            locations for the same object).
        VmajorArea (output): This is an array that includes the required area of transverse
            shear reinforcing per unit length along the frame object for shear at the
            specified location. [L 2 /L]
        TLCombo (output): This is an array that includes the name of the design combination
            for which the controlling longitudinal rebar area for torsion occurs. A
            combination name followed by (Sp) indicates that the design loads were obtained
            by applying special, code-specific, multipliers to all or part of the specified
            design load combination, or that the design was based on the capacity of other
            objects (or other design locations for the same object).
        TLArea (output): This is an array that includes the total longitudinal rebar area
            required for torsion. [L 2 ]
        TTCombo (output): This is an array that includes the name of the design combination
            for which the controlling transverse reinforcing for torsion occurs. A
            combination name followed by (Sp) indicates that the design loads were obtained
            by applying special, code-specific, multipliers to all or part of the specified
            design load combination, or that the design was based on the capacity of other
            objects (or other design locations for the same object).
        TTArea (output): This is an array that includes the required area of transverse
            torsional shear reinforcing per unit length along the frame object for torsion
            at the specified location. [L 2 /L]
        ErrorSummary (output): This is an array that includes the design error messages for
            the frame object, if any.
        WarningSummary (output): This is an array that includes the design warning messages
            for the frame object, if any.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the design
            results are retrieved for the frame object specified by the Name item. If this
            item is Group, the design results are retrieved for all frame objects in the
            group specified by the Name item. If this item is SelectedObjects, the design
            results are retrieved for all selected frame objects, and the Name item is
            ignored.
        """
        _r = self._raw.GetSummaryResultsBeam(Name, 0, [], [], [], [], [], [], [], [], [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.GetSummaryResultsBeam falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSummaryResultsColumn(self, Name: str, ItemType: int = 0):
        """This function retrieves summary results for concrete design. The function returns zero if
        the results are successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The number of frame objects for which results are obtained.
        FrameName (output): This is an array that includes each frame object name for which
            results are obtained.
        MyOption (output): This is an array that includes 1 or 2, indicating the design
            option for each frame object. 1 = Check 2 = Design
        Location (output): This is an array that includes the distance from the I-end of the
            frame object to the location where the results are reported. [L]
        PMMCombo (output): This is an array that includes the name of the design combination
            for which the controlling PMM ratio or rebar area occurs. A combination name
            followed by (Sp) indicates that the design loads were obtained by applying
            special, code-specific multipliers to all or part of the specified design load
            combination, or that the design was based on the capacity of other objects (or
            other design locations for the same object).
        PMMArea (output): This is an array that includes the total longitudinal rebar area
            required for the axial force plus biaxial moment (PMM) design at the specified
            location. [L 2 ] This item applies only when MyOption = 2 (design).
        PMMRatio (output): This is an array that includes the axial force plus biaxial
            moment (PMM) stress ratio at the specified location. This item applies only when
            MyOption = 1 (check).
        VmajorCombo (output): This is an array that includes the name of the design
            combination for which the controlling major shear occurs.
        AVmajor (output): This is an array that includes the required area of transverse
            shear reinforcing per unit length along the frame object for major shear at the
            specified location. [L 2 /L]
        VminorCombo (output): This is an array that includes the name of the design
            combination for which the controlling minor shear occurs.
        AVminor (output): This is an array that includes the required area of transverse
            shear reinforcing per unit length along the frame object for minor shear at the
            specified location. [L 2 /L]
        ErrorSummary (output): This is an array that includes the design error messages for
            the frame object, if any.
        WarningSummary (output): This is an array that includes the design warning messages
            for the frame object, if any.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the design
            results are retrieved for the frame object specified by the Name item. If this
            item is Group, the design results are retrieved for all frame objects in the
            group specified by the Name item. If this item is SelectedObjects, the design
            results are retrieved for all selected frame objects, and the Name item is
            ignored.
        """
        _r = self._raw.GetSummaryResultsColumn(Name, 0, [], [], [], [], [], [], [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.GetSummaryResultsColumn falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSummaryResultsJoint(self, Name: str, ItemType: int = 0):
        """This function retrieves summary results for concrete design. The function returns zero if
        the results are successfully retrieved; otherwise it returns a nonzero value. Note
        that joint design is only included for some codes.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The number of frame objects for which results are obtained.
        FrameName (output): This is an array that includes each frame object name for which
            results are obtained.
        LCJSRatioMajor (output): This is an array that includes the name of the design
            combination for which the controlling joint shear ratio associated with the
            column major axis occurs. A combination name followed by (Sp) indicates that the
            design loads were obtained by applying special, code-specific multipliers to all
            or part of the specified design load combination, or that the design was based
            on the capacity of other objects (or other design locations for the same
            object).
        JSRatioMajor (output): This is an array that includes the joint shear ratio
            associated with the column major axis. This is the joint shear divided by the
            joint shear capacity.
        LCJSRatioMinor (output): This is an array that includes the name of the design
            combination for which the controlling joint shear ratio associated with the
            column minor axis occurs. A combination name followed by (Sp) indicates that the
            design loads were obtained by applying special, code-specific multipliers to all
            or part of the specified design load combination, or that the design was based
            on the capacity of other objects (or other design locations for the same
            object).
        JSRatioMinor (output): This is an array that includes the joint shear ratio
            associated with the column minor axis. This is the joint shear divided by the
            joint shear capacity.
        LCBCCRatioMajor (output): This is an array that includes the name of the design
            combination for which the controlling beam/column capacity ratio associated with
            the column major axis occurs. A combination name followed by (Sp) indicates that
            the design loads were obtained by applying special, code-specific multipliers to
            all or part of the specified design load combination, or that the design was
            based on the capacity of other objects (or other design locations for the same
            object).
        BCCRatioMajor (output): This is an array that includes the beam/column capacity
            ratio associated with the column major axis. This is the sum of the column
            capacities divided by the sum of the beam capacities at the top of the specified
            column.
        LCBCCRatioMinor (output): This is an array that includes the name of the design
            combination for which the controlling beam/column capacity ratio associated with
            the column minor axis occurs. A combination name followed by (Sp) indicates that
            the design loads were obtained by applying special, code-specific multipliers to
            all or part of the specified design load combination, or that the design was
            based on the capacity of other objects (or other design locations for the same
            object).
        BCCRatioMinor (output): This is an array that includes the beam/column capacity
            ratio associated with the column minor axis. This is the sum of the column
            capacities divided by the sum of the beam capacities at the top of the specified
            column.
        ErrorSummary (output): This is an array that includes the design error messages for
            the frame object, if any.
        WarningSummary (output): This is an array that includes the design warning messages
            for the frame object, if any.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the design
            results are retrieved for the frame object specified by the Name item. If this
            item is Group, the design results are retrieved for all frame objects in the
            group specified by the Name item. If this item is SelectedObjects, the design
            results are retrieved for all selected frame objects, and the Name item is
            ignored.
        """
        _r = self._raw.GetSummaryResultsJoint(Name, 0, [], [], [], [], [], [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.GetSummaryResultsJoint falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def ResetOverwrites(self):
        """This function resets all concrete frame design overwrites to default values. The function
        returns zero if the overwrites are successfully reset; otherwise it returns a
        nonzero value. The function will fail if no concrete frame objects are present.
        """
        _r = self._raw.ResetOverwrites()
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.ResetOverwrites falhou (ret={_r})".format(_r=_r))
        return None

    def SetCode(self, CodeName: str):
        """This function sets the concrete design code. The function returns zero if the code is
        successfully set; otherwise it returns a nonzero value.
    
        CodeName (input): This is one of the following concrete design code names. AASHTO
            LRFD 2014 AASHTO LRFD 2012 AASHTO Concrete 07 ACI 318-14 ACI 318-11 ACI
            318-08/IBC2009 AS 3600-09 BS8110 97 Chinese 2010 CSA A23.3-14 CSA A23.3-04
            Eurocode 2-2004 Hong Kong CP 2013 Indian IS 456-2000 Italian NTC 2008 KBC 2009
            Mexican RCDF 2004 NZS 3101:2006 Singapore CP 65:99 SP 63.13330.2012 TS 500-2000
        """
        _r = self._raw.SetCode(CodeName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.SetCode falhou (ret={_r})".format(_r=_r))
        return None

    def SetComboAutoGenerate(self, AutoGenerate: bool):
        """This function turns on or off the option to automatically generate code-based design load
        combinations for concrete frame design. The function returns zero if the options are
        successfully set; otherwise it returns a nonzero value.
    
        AutoGenerate (input): If this item is True, the option to automatically generate
            code-based design load combinations for concrete frame design is turned on. If
            it is False, the option is turned off.
        """
        _r = self._raw.SetComboAutoGenerate(AutoGenerate)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.SetComboAutoGenerate falhou (ret={_r})".format(_r=_r))
        return None

    def SetComboStrength(self, Name: str, Selected: bool):
        """This function selects or deselects a load combination for concrete strength design. The
        function returns zero if the selection status is successfully set; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing load combination.
        Selected (input): If this item is True, the specified load combination is selected
            as a design combination for concrete strength design. If it is False, the
            combination is not selected for concrete strength design.
        """
        _r = self._raw.SetComboStrength(Name, Selected)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.SetComboStrength falhou (ret={_r})".format(_r=_r))
        return None

    def SetDesignSection(self, Name: str, PropName: str, LastAnalysis: bool, ItemType: int = 0):
        """This function modifies the design section for all specified frame objects that have a
        concrete frame design procedure. The function returns zero if the design section is
        successfully modified; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        PropName (input): The name of an existing frame section property to be used as the
            design section for the specified frame objects. This item applies only when
            LastAnalysis = False.
        LastAnalysis (input): If this item is True, the design section for the specified
            frame objects is reset to the last analysis section for the frame object. If it
            is False, the design section is set to that specified by PropName.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, the assignment is made to all selected
            frame objects, and the Name item is ignored.
        """
        _r = self._raw.SetDesignSection(Name, PropName, LastAnalysis, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.SetDesignSection falhou (ret={_r})".format(_r=_r))
        return None

    def StartDesign(self):
        """This function starts the concrete frame design. The function returns zero if the concrete
        frame design is successfully started; otherwise it returns a nonzero value. The
        function will fail if no concrete frame objects are present. It also will fail if
        analysis results are not available.
        """
        _r = self._raw.StartDesign()
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.StartDesign falhou (ret={_r})".format(_r=_r))
        return None

    def VerifyPassed(self):
        """This function retrieves the names of the frame objects that did not pass the design check or
        have not yet been checked, if any. The function returns zero if the names are
        successfully retrieved; otherwise it returns a nonzero value.
    
        NumberItems (output): The number of concrete frame objects that did not pass the
            design check or have not yet been checked.
        n1 (output): The number of concrete frame objects that did not pass the design
            check.
        n2 (output): The number of concrete frame objects that have not yet been checked.
        MyName (output): This is an array that includes the name of each frame object that
            did not pass the design check or has not yet been checked.
        """
        _r = self._raw.VerifyPassed(0, 0, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.VerifyPassed falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def VerifySections(self):
        """This function retrieves the names of the frame objects that have different analysis and
        design sections, if any. The function returns zero if the names are successfully
        retrieved; otherwise it returns a nonzero value.
    
        NumberItems (output): The number of frame objects that have different analysis and
            design sections.
        MyName (output): This is an array that includes the name of each frame object that
            has different analysis and design sections.
        """
        _r = self._raw.VerifySections(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.VerifySections falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    @cached_property
    def AASHTO_Concrete_07(self):
        return N_DesignConcrete_AASHTO_Concrete_07(self._raw.AASHTO_Concrete_07)

    @cached_property
    def AASHTO_LRFD_2012(self):
        return N_DesignConcrete_AASHTO_LRFD_2012(self._raw.AASHTO_LRFD_2012)

    @cached_property
    def AASHTO_LRFD_2014(self):
        return N_DesignConcrete_AASHTO_LRFD_2014(self._raw.AASHTO_LRFD_2014)

    @cached_property
    def ACI318_05_IBC2003(self):
        return N_DesignConcrete_ACI318_05_IBC2003(self._raw.ACI318_05_IBC2003)

    @cached_property
    def ACI318_08_IBC2009(self):
        return N_DesignConcrete_ACI318_08_IBC2009(self._raw.ACI318_08_IBC2009)

    @cached_property
    def ACI_318_02(self):
        return N_DesignConcrete_ACI_318_02(self._raw.ACI_318_02)

    @cached_property
    def ACI_318_99(self):
        return N_DesignConcrete_ACI_318_99(self._raw.ACI_318_99)

    @cached_property
    def AS_3600_01(self):
        return N_DesignConcrete_AS_3600_01(self._raw.AS_3600_01)

    @cached_property
    def AS_3600_09(self):
        return N_DesignConcrete_AS_3600_09(self._raw.AS_3600_09)

    @cached_property
    def BS8110_89(self):
        return N_DesignConcrete_BS8110_89(self._raw.BS8110_89)

    @cached_property
    def BS8110_97(self):
        return N_DesignConcrete_BS8110_97(self._raw.BS8110_97)

    @cached_property
    def CSA_A23_3_04(self):
        return N_DesignConcrete_CSA_A23_3_04(self._raw.CSA_A23_3_04)

    @cached_property
    def CSA_A23_3_94(self):
        return N_DesignConcrete_CSA_A23_3_94(self._raw.CSA_A23_3_94)

    @cached_property
    def Chinese_2010(self):
        return N_DesignConcrete_Chinese_2010(self._raw.Chinese_2010)

    @cached_property
    def EUROCODE_2_1992(self):
        return N_DesignConcrete_EUROCODE_2_1992(self._raw.EUROCODE_2_1992)

    @cached_property
    def Eurocode_2_2004(self):
        return N_DesignConcrete_Eurocode_2_2004(self._raw.Eurocode_2_2004)

    @cached_property
    def Hong_Kong_CP_2004(self):
        return N_DesignConcrete_Hong_Kong_CP_2004(self._raw.Hong_Kong_CP_2004)

    @cached_property
    def Hong_Kong_CP_2013(self):
        return N_DesignConcrete_Hong_Kong_CP_2013(self._raw.Hong_Kong_CP_2013)

    @cached_property
    def Indian_IS_456_2000(self):
        return N_DesignConcrete_Indian_IS_456_2000(self._raw.Indian_IS_456_2000)

    @cached_property
    def Indian_IS_456_2003(self):
        return N_DesignConcrete_Indian_IS_456_2003(self._raw.Indian_IS_456_2003)

    @cached_property
    def Italian_DM_14_2_92(self):
        return N_DesignConcrete_Italian_DM_14_2_92(self._raw.Italian_DM_14_2_92)

    @cached_property
    def KCI_1999(self):
        return N_DesignConcrete_KCI_1999(self._raw.KCI_1999)

    @cached_property
    def Mexican_RCDF_2001(self):
        return N_DesignConcrete_Mexican_RCDF_2001(self._raw.Mexican_RCDF_2001)

    @cached_property
    def NZS_3101_95(self):
        return N_DesignConcrete_NZS_3101_95(self._raw.NZS_3101_95)

    @cached_property
    def SP63_13330_2012(self):
        return N_DesignConcrete_SP63_13330_2012(self._raw.SP63_13330_2012)

    @cached_property
    def Singaopre_CP_65_99(self):
        return N_DesignConcrete_Singaopre_CP_65_99(self._raw.Singaopre_CP_65_99)

    @cached_property
    def Singapore_CP_65_99(self):
        return N_DesignConcrete_Singapore_CP_65_99(self._raw.Singapore_CP_65_99)

    @cached_property
    def UBC97(self):
        return N_DesignConcrete_UBC97(self._raw.UBC97)


class N_DesignConcrete_BS8110_97:
    """Wrapper para SapModel.DesignConcrete.BS8110_97."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, Beta Major 6 = Effective length factor, Beta Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway 2 = Non-sway 2 = Live load reduction factor Value >= 0;
            0 means use program determined value. 3 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 4 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 5 = Effective length factor, Beta
            Major Value >= 0; 0 means use program determined value. 6 = Effective length
            factor, Beta Minor Value >= 0; 0 means use program determined value. 7 = Moment
            coefficient, Cm Major Value >= 0; 0 means use program determined value. 8 =
            Moment coefficient, Cm Minor Value >= 0; 0 means use program determined value. 9
            = Non-sway moment factor, Dns Major Value >= 0; 0 means use program determined
            value. 10 = Non-sway moment factor, Dns Minor Value >= 0; 0 means use program
            determined value. 11 = Sway moment factor, Ds Major Value >= 0; 0 means use
            program determined value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means
            use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.BS8110_97.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 9, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Gamma steel 5 = Gamma
            concrete 6 = Gamma concrete shear 7 = Pattern live load factor 8 = Utilization
            factor limit 9 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and desvisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Gamma steel Value > 0 5 = Gamma concrete Value > 0 6 = Gamma
            concrete shear Value > 0 7 = Pattern live load factor Value >= 0 8 = Utilization
            factor limit Value > 0 9 = Multi-response case design 1 = Envelopes 2 = Step-by-
            step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.BS8110_97.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, Beta Major 6 = Effective length factor, Beta Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway 2 = Non-sway 2 = Live load reduction factor Value >= 0;
            0 means use program determined value. 3 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 4 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 5 = Effective length factor, Beta
            Major Value >= 0; 0 means use program determined value. 6 = Effective length
            factor, Beta Minor Value >= 0; 0 means use program determined value. 7 = Moment
            coefficient, Cm Major Value >= 0; 0 means use program determined value. 8 =
            Moment coefficient, Cm Minor Value >= 0; 0 means use program determined value. 9
            = Non-sway moment factor, Dns Major Value >= 0; 0 means use program determined
            value. 10 = Non-sway moment factor, Dns Minor Value >= 0; 0 means use program
            determined value. 11 = Sway moment factor, Ds Major Value >= 0; 0 means use
            program determined value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means
            use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.BS8110_97.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 9, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Gamma steel 5 = Gamma
            concrete 6 = Gamma concrete shear 7 = Pattern live load factor 8 = Utilization
            factor limit 9 = Multi-response case design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Gamma steel Value > 0 5 = Gamma concrete Value > 0 6 = Gamma
            concrete shear Value > 0 7 = Pattern live load factor Value >= 0 8 = Utilization
            factor limit Value > 0 9 = Multi-response case design 1 = Envelopes 2 = Step-by-
            step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.BS8110_97.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_ACI_318_02:
    """Wrapper para SapModel.DesignConcrete.ACI_318_02."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway special 2 = Sway intermediate 3 = Sway ordinary 4 =
            Non-sway 2 = Live load reduction factor Value >= 0; 0 means use program
            determined value. 3 = Unbraced length ratio, Major Value >= 0; 0 means use
            program determined value. 4 = Unbraced length ratio, Minor Value >= 0; 0 means
            use program determined value. 5 = Effective length factor, K Major Value >= 0; 0
            means use program determined value. 6 = Effective length factor, K Minor Value
            >= 0; 0 means use program determined value. 7 = Moment coefficient, Cm Major
            Value >= 0; 0 means use program determined value. 8 = Moment coefficient, Cm
            Minor Value >= 0; 0 means use program determined value. 9 = Non-sway moment
            factor, Dns Major Value >= 0; 0 means use program determined value. 10 = Non-
            sway moment factor, Dns Minor Value >= 0; 0 means use program determined value.
            11 = Sway moment factor, Ds Major Value >= 0; 0 means use program determined
            value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means use program
            determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.ACI_318_02.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 13, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Seismic design category
            5 = Phi tension controlled 6 = Phi compression controlled tied 7 = Phi
            compression controlled spiral 8 = Phi shear and/or torsion 9 = Phi shear seismic
            10 = Phi joint shear 11 = Pattern live load factor 12 = Utilization factor limit
            13 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Seismic design category 1 = A 2 = B 3 = C 4 = D 5 = E 6 = F 5 =
            Phi tension controlled Value > 0 6 = Phi compression controlled tied Value > 0 7
            = Phi compression controlled spiral Value > 0 8 = Phi shear and/or torsion Value
            > 0 9 = Phi shear seismic Value > 0 10 = Phi joint shear Value > 0 11 = Pattern
            live load factor Value >= 0 12 = Utilization factor limit Value > 0 13 = Multi-
            response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes
            -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.ACI_318_02.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway special 2 = Sway intermediate 3 = Sway ordinary 4 =
            Non-sway 2 = Live load reduction factor Value >= 0; 0 means use program
            determined value. 3 = Unbraced length ratio, Major Value >= 0; 0 means use
            program determined value. 4 = Unbraced length ratio, Minor Value >= 0; 0 means
            use program determined value. 5 = Effective length factor, K Major Value >= 0; 0
            means use program determined value. 6 = Effective length factor, K Minor Value
            >= 0; 0 means use program determined value. 7 = Moment coefficient, Cm Major
            Value >= 0; 0 means use program determined value. 8 = Moment coefficient, Cm
            Minor Value >= 0; 0 means use program determined value. 9 = Non-sway moment
            factor, Dns Major Value >= 0; 0 means use program determined value. 10 = Non-
            sway moment factor, Dns Minor Value >= 0; 0 means use program determined value.
            11 = Sway moment factor, Ds Major Value >= 0; 0 means use program determined
            value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means use program
            determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.ACI_318_02.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 13, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Seismic design category
            5 = Phi tension controlled 6 = Phi compression controlled tied 7 = Phi
            compression controlled spiral 8 = Phi shear and/or torsion 9 = Phi shear seismic
            10 = Phi joint shear 11 = Pattern live load factor 12 = Utilization factor limit
            13 = Multi-response case design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Seismic design category 1 = A 2 = B 3 = C 4 = D 5 = E 6 = F 5 =
            Phi tension controlled Value > 0 6 = Phi compression controlled tied Value > 0 7
            = Phi compression controlled spiral Value > 0 8 = Phi shear and/or torsion Value
            > 0 9 = Phi shear seismic Value > 0 10 = Phi joint shear Value > 0 11 = Pattern
            live load factor Value >= 0 12 = Utilization factor limit Value > 0 13 = Multi-
            response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes
            -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.ACI_318_02.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_BS8110_89:
    """Wrapper para SapModel.DesignConcrete.BS8110_89."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, Beta Major 6 = Effective length factor, Beta Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway 2 = Non-sway 2 = Live load reduction factor Value >= 0;
            0 means use program determined value. 3 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 4 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 5 = Effective length factor, Beta
            Major Value >= 0; 0 means use program determined value. 6 = Effective length
            factor, Beta Minor Value >= 0; 0 means use program determined value. 7 = Moment
            coefficient, Cm Major Value >= 0; 0 means use program determined value. 8 =
            Moment coefficient, Cm Minor Value >= 0; 0 means use program determined value. 9
            = Non-sway moment factor, Dns Major Value >= 0; 0 means use program determined
            value. 10 = Non-sway moment factor, Dns Minor Value >= 0; 0 means use program
            determined value. 11 = Sway moment factor, Ds Major Value >= 0; 0 means use
            program determined value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means
            use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.BS8110_89.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 6, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Pattern live load
            factor 5 = Utilization factor limit 6 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Pattern live load factor Value >= 0 5 = Utilization factor limit
            Value > 0 6 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last
            step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.BS8110_89.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, Beta Major 6 = Effective length factor, Beta Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway 2 = Non-sway 2 = Live load reduction factor Value >= 0;
            0 means use program determined value. 3 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 4 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 5 = Effective length factor, Beta
            Major Value >= 0; 0 means use program determined value. 6 = Effective length
            factor, Beta Minor Value >= 0; 0 means use program determined value. 7 = Moment
            coefficient, Cm Major Value >= 0; 0 means use program determined value. 8 =
            Moment coefficient, Cm Minor Value >= 0; 0 means use program determined value. 9
            = Non-sway moment factor, Dns Major Value >= 0; 0 means use program determined
            value. 10 = Non-sway moment factor, Dns Minor Value >= 0; 0 means use program
            determined value. 11 = Sway moment factor, Ds Major Value >= 0; 0 means use
            program determined value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means
            use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.BS8110_89.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 6, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Pattern live load
            factor 5 = Utilization factor limit 6 = Multi-response case design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Pattern live load factor Value >= 0 5 = Utilization factor limit
            Value > 0 6 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last
            step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.BS8110_89.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_Indian_IS_456_2003:
    """Wrapper para SapModel.DesignConcrete.Indian_IS_456_2003."""

    def __init__(self, raw):
        self._raw = raw

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 8, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Gamma steel 5 = Gamma
            concrete 6 = Pattern live load factor 7 = Utilization factor limit 8 = Multi-
            response case design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Gamma steel Value > 0 5 = Gamma concrete Value > 0 6 = Pattern
            live load factor Value >= 0 7 = Utilization factor limit Value > 0 8 = Multi-
            response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes
            -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Indian_IS_456_2003.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 8, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Gamma steel 5 = Gamma
            concrete 6 = Pattern live load factor 7 = Utilization factor limit 8 = Multi-
            response case design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Gamma steel Value > 0 5 = Gamma concrete Value > 0 6 = Pattern
            live load factor Value >= 0 7 = Utilization factor limit Value > 0 8 = Multi-
            response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes
            -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Indian_IS_456_2003.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_Indian_IS_456_2000:
    """Wrapper para SapModel.DesignConcrete.Indian_IS_456_2000."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 16, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor 13 = Top rebar area of a beam
            at the left end (I-end) 14 = Bottom rebar area of a beam at the left end (I-end)
            15 = Top rebar area of a beam at the right end (J-end) 16 = Bottom rebar area of
            a beam at the right end (J-end)
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Ductile 2 = Ordinary 3 = Non-sway 2 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 3 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 4 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 5 =
            Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 6 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 7 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 8 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 9 = Non-sway moment factor, Dns Major Value >= 0;
            0 means use program determined value. 10 = Non-sway moment factor, Dns Minor
            Value >= 0; 0 means use program determined value. 11 = Sway moment factor, Ds
            Major Value >= 0; 0 means use program determined value. 12 = Sway moment factor,
            Ds Minor Value >= 0; 0 means use program determined value. 13 = Top rebar area
            of a beam at the left end (I-end) Value >= 0; 0 means use program determined
            value. 14 = Bottom rebar area of a beam at the left end (I-end) Value >= 0; 0
            means use program determined value. 15 = Top rebar area of a beam at the right
            end (J-end) Value >= 0; 0 means use program determined value. 16 = Bottom rebar
            area of a beam at the right end (J-end) Value >= 0; 0 means use program
            determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Indian_IS_456_2000.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor 13 = Top rebar area of a beam
            at the left end (I-end) 14 = Bottom rebar area of a beam at the left end (I-end)
            15 = Top rebar area of a beam at the right end (J-end) 16 = Bottom rebar area of
            a beam at the right end (J-end)
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Ductile 2 = Ordinary 3 = Non-sway 2 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 3 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 4 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 5 =
            Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 6 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 7 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 8 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 9 = Non-sway moment factor, Dns Major Value >= 0;
            0 means use program determined value. 10 = Non-sway moment factor, Dns Minor
            Value >= 0; 0 means use program determined value. 11 = Sway moment factor, Ds
            Major Value >= 0; 0 means use program determined value. 12 = Sway moment factor,
            Ds Minor Value >= 0; 0 means use program determined value. 13 = Top rebar area
            of a beam at the left end (I-end) Value >= 0; 0 means use program determined
            value. 14 = Bottom rebar area of a beam at the left end (I-end) Value >= 0; 0
            means use program determined value. 15 = Top rebar area of a beam at the right
            end (J-end) Value >= 0; 0 means use program determined value. 16 = Bottom rebar
            area of a beam at the right end (J-end) Value >= 0; 0 means use program
            determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is
            Group,the assignment is made to all frame objects in the group specified by the
            Name item. If this item is SelectedObjects, assignment is made to all selected
            frame objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Indian_IS_456_2000.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_EUROCODE_2_1992:
    """Wrapper para SapModel.DesignConcrete.EUROCODE_2_1992."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, Beta Major 6 = Effective length factor, Beta Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway 2 = Non-sway 2 = Live load reduction factor Value >= 0;
            0 means use program determined value. 3 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 4 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 5 = Effective length factor, Beta
            Major Value >= 0; 0 means use program determined value. 6 = Effective length
            factor, Beta Minor Value >= 0; 0 means use program determined value. 7 = Moment
            coefficient, Cm Major Value >= 0; 0 means use program determined value. 8 =
            Moment coefficient, Cm Minor Value >= 0; 0 means use program determined value. 9
            = Non-sway moment factor, Dns Major Value >= 0; 0 means use program determined
            value. 10 = Non-sway moment factor, Dns Minor Value >= 0; 0 means use program
            determined value. 11 = Sway moment factor, Ds Major Value >= 0; 0 means use
            program determined value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means
            use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.EUROCODE_2_1992.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 9, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Nu 5 = Gamma steel 6 =
            Gamma concrete 7 = Pattern live load factor 8 = Utilization factor limit 9 =
            Multi-response case design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Nu Value > 0 5 = Gamma steel Value > 0 6 = Gamma concrete Value
            > 0 7 = Pattern live load factor Value >= 0 8 = Utilization factor limit Value >
            0 9 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4
            = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.EUROCODE_2_1992.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, Beta Major 6 = Effective length factor, Beta Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway 2 = Non-sway 2 = Live load reduction factor Value >= 0;
            0 means use program determined value. 3 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 4 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 5 = Effective length factor, Beta
            Major Value >= 0; 0 means use program determined value. 6 = Effective length
            factor, Beta Minor Value >= 0; 0 means use program determined value. 7 = Moment
            coefficient, Cm Major Value >= 0; 0 means use program determined value. 8 =
            Moment coefficient, Cm Minor Value >= 0; 0 means use program determined value. 9
            = Non-sway moment factor, Dns Major Value >= 0; 0 means use program determined
            value. 10 = Non-sway moment factor, Dns Minor Value >= 0; 0 means use program
            determined value. 11 = Sway moment factor, Ds Major Value >= 0; 0 means use
            program determined value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means
            use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.EUROCODE_2_1992.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 9, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Nu 5 = Gamma steel 6 =
            Gamma concrete 7 = Pattern live load factor 8 = Utilization factor limit 9 =
            Multi-response case design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Nu Value > 0 5 = Gamma steel Value > 0 6 = Gamma concrete Value
            > 0 7 = Pattern live load factor Value >= 0 8 = Utilization factor limit Value >
            0 9 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4
            = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.EUROCODE_2_1992.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_Chinese_2010:
    """Wrapper para SapModel.DesignConcrete.Chinese_2010."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 18, inclusive, indicating the
            overwrite item considered. 1 = Seismic design grade 2 = Dual system SMF 3 = MMF
            4 = SMF 5 = AFMF 6 = Column location 7 = Transfer beam of column 8 = Corner
            column seismic modification 9 = Beam gravity neg moment red factor 10 = Unbraced
            length ratio, Major 11 = Unbraced length ratio, Minor 12 = Effective length
            factor, K Major 13 = Effective length factor, K Minor 14 = Torsion modification
            factor 15 = Torsion design factor, Zeta 16 = Concrete cover for closed stirrup
            17 = Effective length factor for gravity, K Major 18 = Effective length factor
            for gravity, K Minor
        Value (output): The value of the considered overwrite item. 1 = Seismic design grade
            0 = As specified in preferences 1 = Seismic Super I 2 = Seismic Class I 3 =
            Seismic Class II 4 = Seismic Class III 5 = Seismic Class IV 6 = NonSeismic 2 =
            Dual system SMF Value >= 0; 0 means use program determined value. 3 = MMF Value
            >= 0; 0 means use program determined value. 4 = SMF Value >= 0; 0 means use
            program determined value. 5 = AFMF Value >= 0; 0 means use program determined
            value. 6 = Column Location 1 = Center Column 2 = Side Column 3 = Corner Column 4
            = End Column 5 = Individual Column 7 = Transfer beam or column 0 = Program
            Determined 1 = No 2 = Yes 8 = Corner column seismic modification 0 = Program
            Determined 1 = No 2 = Yes 9 = Beam gravity neg moment red factor Value >= 0; 0
            means use program determined value. 10 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 11 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 12 = Effective length factor, K
            Major Value >= 0; 0 means use program determined value. 13 = Effective length
            factor, K Major Value >= 0; 0 means use program determined value. 14 = Torsion
            modification factor Value >= 0; 0 means use program determined value. 15 =
            Torsion design factor, Zeta Value >= 0; 0 means use program determined value. 16
            = Concrete cover for closed stirrup Value >= 0; 0 means use program determined
            value. 17 = Effective length factor for gravity, K Major Value >= 0; 0 means use
            program default value. 18 = Effective length factor for gravity, K Minor Value
            >= 0; 0 means use program default value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Chinese_2010.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Importance factor gamma 0 4 = Column design procedure 5 =
            Seismic design grade 6 = Pattern live load factor 7 = Utilization factor limit 8
            = Multi-response case design 9 = Structural system 10 = Is tall building? 11 =
            Seismic field type
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Importance factor gamma 0 Value > 0 4 = Column
            design procedure 1 = Appendix F 2 = Simplified 5 = Seismic design grade 1 =
            Super I 2 = Grade I 3 = Grade II 4 = Grade III 5 = Grade IV 6 = Nonseismic 6 =
            Pattern live load factor Value >= 0 7 = Utilization factor limit Value > 0 8 =
            Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 =
            Envelopes -- All 5 = Step-by-step -- All 9 = Structural system 1 = Frame only 2
            = Shearwall only 3 = Frame-shearwall 4 = Braced frame only 5 = Frame-braced
            frame 10 = Is tall building? 0 = No 1 = Yes 11 = Seismic field type 1 = I 2 = II
            3 = III 4 = IV
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Chinese_2010.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 18, inclusive, indicating the
            overwrite item considered. 1 = Seismic design grade 2 = Dual system SMF 3 = MMF
            4 = SMF 5 = AFMF 6 = Column location 7 = Transfer beam of column 8 = Corner
            column seismic modification 9 = Beam gravity neg moment red factor 10 = Unbraced
            length ratio, Major 11 = Unbraced length ratio, Minor 12 = Effective length
            factor, K Major 13 = Effective length factor, K Minor 14 = Torsion modification
            factor 15 = Torsion design factor, Zeta 16 = Concrete cover for closed stirrup
            17 = Effective length factor for gravity, K Major 18 = Effective length factor
            for gravity, K Minor
        Value (input): The value of the considered overwrite item. 1 = Seismic design grade
            0 = As specified in preferences 1 = Seismic Super I 2 = Seismic Class I 3 =
            Seismic Class II 4 = Seismic Class III 5 = Seismic Class IV 6 = NonSeismic 2 =
            Dual system SMF Value >= 0; 0 means use program determined value. 3 = MMF Value
            >= 0; 0 means use program determined value. 4 = SMF Value >= 0; 0 means use
            program determined value. 5 = AFMF Value >= 0; 0 means use program determined
            value. 6 = Column Location 1 = Center Column 2 = Side Column 3 = Corner Column 4
            = End Column 5 = Individual Column 7 = Transfer beam or column 0 = Program
            Determined 1 = No 2 = Yes 8 = Corner column seismic modification 0 = Program
            Determined 1 = No 2 = Yes 9 = Beam gravity neg moment red factor Value >= 0; 0
            means use program determined value. 10 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 11 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 12 = Effective length factor, K
            Major Value >= 0; 0 means use program determined value. 13 = Effective length
            factor, K Major Value >= 0; 0 means use program determined value. 14 = Torsion
            modification factor Value >= 0; 0 means use program determined value. 15 =
            Torsion design factor, Zeta Value >= 0; 0 means use program determined value. 16
            = Concrete cover for closed stirrup Value >= 0; 0 means use program determined
            value. 17 = Effective length factor for gravity, K Major Value >= 0; 0 means use
            program default value. 18 = Effective length factor for gravity, K Minor Value
            >= 0; 0 means use program default value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Chinese_2010.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Importance factor gamma 0 4 = Column design procedure 5 =
            Seismic design grade 6 = Pattern live load factor 7 = Utilization factor limit 8
            = Multi-response case design 9 = Structural system 10 = Is tall building? 11 =
            Seismic field type
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Importance factor gamma 0 Value > 0 4 = Column
            design procedure 1 = Appendix F 2 = Simplified 5 = Seismic design grade 1 =
            Super I 2 = Grade I 3 = Grade II 4 = Grade III 5 = Grade IV 6 = Nonseismic 6 =
            Pattern live load factor Value >= 0 7 = Utilization factor limit Value > 0 8 =
            Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 =
            Envelopes -- All 5 = Step-by-step -- All 9 = Structural system 1 = Frame only 2
            = Shearwall only 3 = Frame-shearwall 4 = Braced frame only 5 = Frame-braced
            frame 10 = Is tall building? 0 = No 1 = Yes 11 = Seismic field type 1 = I 2 = II
            3 = III 4 = IV
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Chinese_2010.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_ACI318_05_IBC2003:
    """Wrapper para SapModel.DesignConcrete.ACI318_05_IBC2003."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Nonsway moment
            factor, Dns Major 10 = Nonsway moment factor, Dns Minor 11 = Sway moment factor,
            Ds Major 12 = Sway moment factor, Ds Minor
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway special 2 = Sway Intermediate 3 = Sway Ordinary 4 =
            Nonsway 2 = Live load reduction factor Value >= 0; 0 means use program
            determined value. 3 = Unbraced length ratio, Major Value >= 0; 0 means use
            program determined value. 4 = Unbraced length ratio, Minor Value >= 0; 0 means
            use program determined value. 5 = Effective length factor, K Major Value >= 0; 0
            means use program determined value. 6 = Effective length factor, K Minor Value
            >= 0; 0 means use program determined value. 7 = Moment coefficient, Cm Major
            Value >= 0; 0 means use program determined value. 8 = Moment coefficient, Cm
            Minor Value >= 0; 0 means use program determined value. 9 = Nonsway moment
            factor, Dns Major Value >= 0; 0 means use program determined value. 10 = Nonsway
            moment factor, Dns Minor Value >= 0; 0 means use program determined value. 11 =
            Sway moment factor, Ds Major Value >= 0; 0 means use program determined value.
            12 = Sway moment factor, Ds Minor Value >= 0; 0 means use program determined
            value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.ACI318_05_IBC2003.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 13, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Seismic design category
            5 = Phi tension controlled 6 = Phi compression controlled tied 7 = Phi
            compression controlled spiral 8 = Phi shear and/or torsion 9 = Phi shear seismic
            10 = Phi joint shear 11 = Pattern live load factor 12 = Utilization factor limit
            13 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and divisible by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Seismic design category 1 = A 2 = B 3 = C 4 = D 5 = E 6 = F 5 =
            Phi tension controlled Value > 0 6 = Phi compression controlled tied Value > 0 7
            = Phi compression controlled spiral Value > 0 8 = Phi shear and/or torsion Value
            > 0 9 = Phi shear seismic Value > 0 10 = Phi joint shear Value > 0 11 = Pattern
            live load factor Value >= 0 12 = Utilization factor limit Value > 0 13 = Multi-
            response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes
            -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.ACI318_05_IBC2003.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway special 2 = Sway Intermediate 3 = Sway Ordinary 4 =
            Non-sway 2 = Live load reduction factor Value >= 0; 0 means use program
            determined value. 3 = Unbraced length ratio, Major Value >= 0; 0 means use
            program determined value. 4 = Unbraced length ratio, Minor Value >= 0; 0 means
            use program determined value. 5 = Effective length factor, K Major Value >= 0; 0
            means use program determined value. 6 = Effective length factor, K Minor Value
            >= 0; 0 means use program determined value. 7 = Moment coefficient, Cm Major
            Value >= 0; 0 means use program determined value. 8 = Moment coefficient, Cm
            Minor Value >= 0; 0 means use program determined value. 9 = Non-sway moment
            factor, Dns Major Value >= 0; 0 means use program determined value. 10 = Non-
            sway moment factor, Dns Minor Value >= 0; 0 means use program determined value.
            11 = Sway moment factor, Ds Major Value >= 0; 0 means use program determined
            value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means use program
            determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects= 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.ACI318_05_IBC2003.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 13, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Seismic design category
            5 = Phi tension controlled 6 = Phi compression controlled tied 7 = Phi
            compression controlled spiral 8 = Phi shear and/or torsion 9 = Phi shear seismic
            10 = Phi joint shear 11 = Pattern live load factor 12 = Utilization factor limit
            13 = Multi-response case design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and divisible by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Seismic design category 1 = A 2 = B 3 = C 4 = D 5 = E 6 = F 5 =
            Phi tension controlled Value > 0 6 = Phi compression controlled tied Value > 0 7
            = Phi compression controlled spiral Value > 0 8 = Phi shear and/or torsion Value
            > 0 9 = Phi shear seismic Value > 0 10 = Phi joint shear Value > 0 11 = Pattern
            live load factor Value >= 0 12 = Utilization factor limit Value > 0 13 = Multi-
            response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes
            -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.ACI318_05_IBC2003.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_Italian_DM_14_2_92:
    """Wrapper para SapModel.DesignConcrete.Italian_DM_14_2_92."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Amplification
            Coefficient, Omega Major 8 = Amplification Coefficient, Omega Minor 9 = Moment
            coefficient, c Major 10 = Moment coefficient, c Minor 11 = Moment coefficient,
            c_sway Major 12 = Moment coefficient, c_sway Minor
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway 2 = Braced 2 = Live load reduction factor Value >= 0; 0
            means use program determined value. 3 = Unbraced length ratio, Major Value >= 0;
            0 means use program determined value. 4 = Unbraced length ratio, Minor Value >=
            0; 0 means use program determined value. 5 = Effective length factor, K Major
            Value >= 0; 0 means use program determined value. 6 = Effective length factor, K
            Minor Value >= 0; 0 means use program determined value. 7 = Amplification
            coefficient, Omega Major Value >= 0; 0 means use program determined value. 8 =
            Amplification coefficient, Omega Minor Value >= 0; 0 means use program
            determined value. 9 = Moment coefficient, c Major Value >= 0; 0 means use
            program determined value. 10 = Moment coefficient, c Minor Value >= 0; 0 means
            use program determined value. 11 = Moment coefficient, c_sway Major Value >= 0;
            0 means use program determined value. 12 = Moment coefficient, c_sway Minor
            Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Italian_DM_14_2_92.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 5, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Pattern live load factor 4 = Utilization factor limit 5 =
            Multi-response case design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Pattern live load factor Value >= 0 4 =
            Utilization factor limit Value > 0 5 = Multi-response case design 1 = Envelopes
            2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Italian_DM_14_2_92.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Amplification
            Coefficient, Omega Major 8 = Amplification Coefficient, Omega Minor 9 = Moment
            coefficient, c Major 10 = Moment coefficient, c Minor 11 = Moment coefficient,
            c_sway Major 12 = Moment coefficient, c_sway Minor
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway 2 = Braced 2 = Live load reduction factor Value >= 0; 0
            means use program determined value. 3 = Unbraced length ratio, Major Value >= 0;
            0 means use program determined value. 4 = Unbraced length ratio, Minor Value >=
            0; 0 means use program determined value. 5 = Effective length factor, K Major
            Value >= 0; 0 means use program determined value. 6 = Effective length factor, K
            Minor Value >= 0; 0 means use program determined value. 7 = Amplification
            coefficient, Omega Major Value >= 0; 0 means use program determined value. 8 =
            Amplification coefficient, Omega Minor Value >= 0; 0 means use program
            determined value. 9 = Moment coefficient, c Major Value >= 0; 0 means use
            program determined value. 10 = Moment coefficient, c Minor Value >= 0; 0 means
            use program determined value. 11 = Moment coefficient, c_sway Major Value >= 0;
            0 means use program determined value. 12 = Moment coefficient, c_sway Minor
            Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Italian_DM_14_2_92.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 5, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Pattern live load factor 4 = Utilization factor limit 5 =
            Multi-response case design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Pattern live load factor Value >= 0 4 =
            Utilization factor limit Value > 0 5 = Multi-response case design 1 = Envelopes
            2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Italian_DM_14_2_92.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_ACI318_08_IBC2009:
    """Wrapper para SapModel.DesignConcrete.ACI318_08_IBC2009."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, False)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.ACI318_08_IBC2009.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.ACI318_08_IBC2009.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.ACI318_08_IBC2009.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.ACI318_08_IBC2009.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_Singapore_CP_65_99:
    """Wrapper para SapModel.DesignConcrete.Singapore_CP_65_99."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, Beta Major 6 = Effective length factor, Beta Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway 2 = Non-sway 2 = Live load reduction factor Value >= 0;
            0 means use program determined value. 3 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 4 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 5 = Effective length factor, Beta
            Major Value >= 0; 0 means use program determined value. 6 = Effective length
            factor, Beta Minor Value >= 0; 0 means use program determined value. 7 = Moment
            coefficient, Cm Major Value >= 0; 0 means use program determined value. 8 =
            Moment coefficient, Cm Minor Value >= 0; 0 means use program determined value. 9
            = Non-sway moment factor, Dns Major Value >= 0; 0 means use program determined
            value. 10 = Non-sway moment factor, Dns Minor Value >= 0; 0 means use program
            determined value. 11 = Sway moment factor, Ds Major Value >= 0; 0 means use
            program determined value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means
            use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Singapore_CP_65_99.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 9, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Gamma steel 5 = Gamma
            concrete 6 = Gamma concrete shear 7 = Pattern live load factor 8 = Utilization
            factor limit 9 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Gamma steel Value > 0 5 = Gamma concrete Value > 0 6 = Gamma
            concrete shear Value > 0 7 = Pattern live load factor Value >= 0 8 = Utilization
            factor limit Value > 0 9 = Multi-response case design 1 = Envelopes 2 = Step-by-
            step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Singapore_CP_65_99.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 9, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Gamma steel 5 = Gamma
            concrete 6 = Gamma concrete shear 7 = Pattern live load factor 8 = Utilization
            factor limit 9 = Multi-response case design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Gamma steel Value > 0 5 = Gamma concrete Value > 0 6 = Gamma
            concrete shear Value > 0 7 = Pattern live load factor Value >= 0 8 = Utilization
            factor limit Value > 0 9 = Multi-response case design 1 = Envelopes 2 = Step-by-
            step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Singapore_CP_65_99.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_AASHTO_Concrete_07:
    """Wrapper para SapModel.DesignConcrete.AASHTO_Concrete_07."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            overwrite item considered. 1 = Live load reduction factor 2 = Unbraced length
            ratio, Major 3 = Unbraced length ratio, Minor 4 = Effective length factor, K
            Major 5 = Effective length factor, K Minor 6 = Moment coefficient, Cm Major 7 =
            Moment coefficient, Cm Minor 8 = Nonsway moment factor, Db Major 9 = Nonsway
            moment factor, Db Minor 10 = Sway moment factor, Ds Major 11 = Sway moment
            factor, Ds Minor
        Value (output): The value of the considered overwrite item. 1 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 2 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 3 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 4 =
            Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 5 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 6 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 7 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 8 = Nonsway moment factor, Db Major Value >= 0; 0
            means use program determined value. 9 = Nonsway moment factor, Db Minor Value >=
            0; 0 means use program determined value. 10 = Sway moment factor, Ds Major Value
            >= 0; 0 means use program determined value. 11 = Sway moment factor, Ds Minor
            Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AASHTO_Concrete_07.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 7, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Seismic Zone 5 =
            Pattern live load factor 6 = Utilization factor limit 7 = Multi-response case
            design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and divisible by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Seismic Zone 0 = Zone 0 1 = Zone 1 2 = Zone 2 3 = Zone 3 4 =
            Zone 4 5 = Pattern live load factor Value >= 0 6 = Utilization factor limit
            Value > 0 7 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last
            step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AASHTO_Concrete_07.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            overwrite item considered. 1 = Live load reduction factor 2 = Unbraced length
            ratio, Major 3 = Unbraced length ratio, Minor 4 = Effective length factor, K
            Major 5 = Effective length factor, K Minor 6 = Moment coefficient, Cm Major 7 =
            Moment coefficient, Cm Minor 8 = Nonsway moment factor, Db Major 9 = Nonsway
            moment factor, Db Minor 10 = Sway moment factor, Ds Major 11 = Sway moment
            factor, Ds Minor
        Value (input): The value of the considered overwrite item. 1 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 2 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 3 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 4 =
            Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 5 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 6 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 7 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 8 = Nonsway moment factor, Db Major Value >= 0; 0
            means use program determined value. 9 = Nonsway moment factor, Db Minor Value >=
            0; 0 means use program determined value. 10 = Sway moment factor, Ds Major Value
            >= 0; 0 means use program determined value. 11 = Sway moment factor, Ds Minor
            Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, the assignment is made to all selected
            frame objects and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AASHTO_Concrete_07.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 7, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Seismic Zone 5 =
            Pattern live load factor 6 = Utilization factor limit 7 = Multi-response case
            design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and divisible by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Seismic Zone 0 = Zone 0 1 = Zone 1 2 = Zone 2 3 = Zone 3 4 =
            Zone 4 5 = Pattern live load factor Value >= 0 6 = Utilization factor limit
            Value > 0 7 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last
            step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AASHTO_Concrete_07.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_Hong_Kong_CP_2004:
    """Wrapper para SapModel.DesignConcrete.Hong_Kong_CP_2004."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, Beta Major 6 = Effective length factor, Beta Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway 2 = Non-sway 2 = Live load reduction factor Value >= 0;
            0 means use program determined value. 3 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 4 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 5 = Effective length factor, Beta
            Major Value >= 0; 0 means use program determined value. 6 = Effective length
            factor, Beta Minor Value >= 0; 0 means use program determined value. 7 = Moment
            coefficient, Cm Major Value >= 0; 0 means use program determined value. 8 =
            Moment coefficient, Cm Minor Value >= 0; 0 means use program determined value. 9
            = Non-sway moment factor, Dns Major Value >= 0; 0 means use program determined
            value. 10 = Non-sway moment factor, Dns Minor Value >= 0; 0 means use program
            determined value. 11 = Sway moment factor, Ds Major Value >= 0; 0 means use
            program determined value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means
            use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Hong_Kong_CP_2004.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 9, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Gamma steel 5 = Gamma
            concrete 6 = Gamma concrete shear 7 = Pattern live load factor 8 = Utilization
            factor limit 9 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Gamma steel Value > 0 5 = Gamma concrete Value > 0 6 = Gamma
            concrete shear Value > 0 7 = Pattern live load factor Value >= 0 8 = Utilization
            factor limit Value > 0 9 = Multi-response case design 1 = Envelopes 2 = Step-by-
            step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Hong_Kong_CP_2004.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, Beta Major 6 = Effective length factor, Beta Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway 2 = Non-sway 2 = Live load reduction factor Value >= 0;
            0 means use program determined value. 3 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 4 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 5 = Effective length factor, Beta
            Major Value >= 0; 0 means use program determined value. 6 = Effective length
            factor, Beta Minor Value >= 0; 0 means use program determined value. 7 = Moment
            coefficient, Cm Major Value >= 0; 0 means use program determined value. 8 =
            Moment coefficient, Cm Minor Value >= 0; 0 means use program determined value. 9
            = Non-sway moment factor, Dns Major Value >= 0; 0 means use program determined
            value. 10 = Non-sway moment factor, Dns Minor Value >= 0; 0 means use program
            determined value. 11 = Sway moment factor, Ds Major Value >= 0; 0 means use
            program determined value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means
            use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Hong_Kong_CP_2004.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 9, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Gamma steel 5 = Gamma
            concrete 6 = Gamma concrete shear 7 = Pattern live load factor 8 = Utilization
            factor limit 9 = Multi-response case design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Gamma steel Value > 0 5 = Gamma concrete Value > 0 6 = Gamma
            concrete shear Value > 0 7 = Pattern live load factor Value >= 0 8 = Utilization
            factor limit Value > 0 9 = Multi-response case design 1 = Envelopes 2 = Step-by-
            step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Hong_Kong_CP_2004.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_NZS_3101_95:
    """Wrapper para SapModel.DesignConcrete.NZS_3101_95."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Db Major 10 = Non-sway moment factor, Db Minor 11 = Sway moment factor,
            Ds Major 12 = Sway moment factor, Ds Minor
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Ductile 2 = Limited 3 = Elastic 4 = Ordinary 2 = Live load
            reduction factor Value >= 0; 0 means use program determined value. 3 = Unbraced
            length ratio, Major Value >= 0; 0 means use program determined value. 4 =
            Unbraced length ratio, Minor Value >= 0; 0 means use program determined value. 5
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 6 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 7 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 8 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 9 = Non-sway moment factor, Db Major Value >= 0; 0
            means use program determined value. 10 = Non-sway moment factor, Db Minor Value
            >= 0; 0 means use program determined value. 11 = Sway moment factor, Ds Major
            Value >= 0; 0 means use program determined value. 12 = Sway moment factor, Ds
            Minor Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.NZS_3101_95.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 14, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Phi bending 5 = Phi
            tension 6 = Phi compression 7 = Phi shear 8 = Omega 9 = Phi 0 10 = Rm 11 = Rv 12
            = Pattern live load factor 13 = Utilization factor limit 14 = Multi-response
            case design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Phi bending Value > 0 5 = Phi tension Value > 0 6 = Phi
            compression Value > 0 7 = Phi shear Value > 0 8 = Omega Value > 0 9 = Phi 0
            Value > 0 10 = Rm Value > 0 11 = Rv Value > 0 12 = Pattern live load factor
            Value >= 0 13 = Utilization factor limit Value > 0 14 = Multi-response case
            design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 =
            Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.NZS_3101_95.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Db Major 10 = Non-sway moment factor, Db Minor 11 = Sway moment factor,
            Ds Major 12 = Sway moment factor, Ds Minor
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Ductile 2 = Limited 3 = Elastic 4 = Ordinary 2 = Live load
            reduction factor Value >= 0; 0 means use program determined value. 3 = Unbraced
            length ratio, Major Value >= 0; 0 means use program determined value. 4 =
            Unbraced length ratio, Minor Value >= 0; 0 means use program determined value. 5
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 6 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 7 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 8 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 9 = Non-sway moment factor, Db Major Value >= 0; 0
            means use program determined value. 10 = Non-sway moment factor, Db Minor Value
            >= 0; 0 means use program determined value. 11 = Sway moment factor, Ds Major
            Value >= 0; 0 means use program determined value. 12 = Sway moment factor, Ds
            Minor Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.NZS_3101_95.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 14, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Phi bending 5 = Phi
            tension 6 = Phi compression 7 = Phi shear 8 = Omega 9 = Phi 0 10 = Rm 11 = Rv 12
            = Pattern live load factor 13 = Utilization factor limit 14 = Multi-response
            case design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Phi bending Value > 0 5 = Phi tension Value > 0 6 = Phi
            compression Value > 0 7 = Phi shear Value > 0 8 = Omega Value > 0 9 = Phi 0
            Value > 0 10 = Rm Value > 0 11 = Rv Value > 0 12 = Pattern live load factor
            Value >= 0 13 = Utilization factor limit Value > 0 14 = Multi-response case
            design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 =
            Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.NZS_3101_95.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_CSA_A23_3_04:
    """Wrapper para SapModel.DesignConcrete.CSA_A23_3_04."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Db Major 10 = Non-sway moment factor, Db Minor 11 = Sway moment factor,
            Ds Major 12 = Sway moment factor, Ds Minor 13 = Force modification factor, Rd 14
            = Force modification factor, Ro 15 = Maximum aggregate size
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Ductile 2 = Moderate 3 = Conventional 2 = Live load
            reduction factor Value >= 0; 0 means use program determined value. 3 = Unbraced
            length ratio, Major Value >= 0; 0 means use program determined value. 4 =
            Unbraced length ratio, Minor Value >= 0; 0 means use program determined value. 5
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 6 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 7 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 8 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 9 = Non-sway moment factor, Db Major Value >= 0; 0
            means use program determined value. 10 = Non-sway moment factor, Db Minor Value
            >= 0; 0 means use program determined value. 11 = Sway moment factor, Ds Major
            Value >= 0; 0 means use program determined value. 12 = Sway moment factor, Ds
            Minor Value >= 0; 0 means use program determined value. 13 = Force modification
            factor, Rd Value >= 0; 0 means use program determined value. 14 = Force
            modification factor, Ro Value >= 0; 0 means use program determined value. 15 =
            Maximum aggregate size Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.CSA_A23_3_04.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 8, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Phi steel 5 = Phi
            concrete 6 = Pattern live load factor 7 = Utilization factor limit 8 = Multi-
            response case design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Phi steel Value > 0 5 = Phi concrete Value > 0 6 = Pattern live
            load factor Value >= 0 7 = Utilization factor limit Value > 0 8 = Multi-response
            case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5
            = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.CSA_A23_3_04.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Db Major 10 = Non-sway moment factor, Db Minor 11 = Sway moment factor,
            Ds Major 12 = Sway moment factor, Ds Minor 13 = Force modification factor, Rd 14
            = Force modification factor, Ro 15 = Maximum aggregate size
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Ductile 2 = Moderate 3 = Conventional 2 = Live load
            reduction factor Value >= 0; 0 means use program determined value. 3 = Unbraced
            length ratio, Major Value >= 0; 0 means use program determined value. 4 =
            Unbraced length ratio, Minor Value >= 0; 0 means use program determined value. 5
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 6 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 7 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 8 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 9 = Non-sway moment factor, Db Major Value >= 0; 0
            means use program determined value. 10 = Non-sway moment factor, Db Minor Value
            >= 0; 0 means use program determined value. 11 = Sway moment factor, Ds Major
            Value >= 0; 0 means use program determined value. 12 = Sway moment factor, Ds
            Minor Value >= 0; 0 means use program determined value. 13 = Force modification
            factor, Rd Value >= 0; 0 means use program determined value. 14 = Force
            modification factor, Ro Value >= 0; 0 means use program determined value. 15 =
            Maximum aggregate size Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.CSA_A23_3_04.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 8, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Phi steel 5 = Phi
            concrete 6 = Pattern live load factor 7 = Utilization factor limit 8 = Multi-
            response case design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Phi steel Value > 0 5 = Phi concrete Value > 0 6 = Pattern live
            load factor Value >= 0 7 = Utilization factor limit Value > 0 8 = Multi-response
            case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5
            = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.CSA_A23_3_04.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_AS_3600_09:
    """Wrapper para SapModel.DesignConcrete.AS_3600_09."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, km Major 8 = Moment coefficient, km Minor 9 = Nonsway moment
            factor, Db Major 10 = Nonsway moment factor, Db Minor 11 = Sway moment factor,
            Ds Major 12 = Sway moment factor, Ds Minor
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 = As
            specified in preferences 1 = Sway special 2 = Sway intermediate 3 = Sway
            ordinary 4 = Nonsway 2 = Live load reduction factor Value >= 0; 0 means use
            program determined value. 3 = Unbraced length ratio, Major Value >= 0; 0 means
            use program determined value. 4 = Unbraced length ratio, Minor Value >= 0; 0
            means use program determined value. 5 = Effective length factor, K Major Value
            >= 0; 0 means use program determined value. 6 = Effective length factor, K Minor
            Value >= 0; 0 means use program determined value. 7 = Moment coefficient, km
            Major Value >= 0; 0 means use program determined value. 8 = Moment coefficient,
            km Minor Value >= 0; 0 means use program determined value. 9 = Nonsway moment
            factor, Db Major Value >= 0; 0 means use program determined value. 10 = Nonsway
            moment factor, Db Minor Value >= 0; 0 means use program determined value. 11 =
            Sway moment factor, Ds Major Value >= 0; 0 means use program determined value.
            12 = Sway moment factor, Ds Minor Value >= 0; 0 means use program determined
            value.
        ProgDet (input): If this item is True then the specified value is program
            determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AS_3600_09.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved, otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Phi tension controlled
            5 = Phi compression controlled 6 = Phi shear and/or torsion 7 = Phi shear
            seismic 8 = Phi joint shear 9 = Pattern live load factor 10 = Utilization factor
            limit 11 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and divisible by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Phi tension controlled Value > 0 5 = Phi compression controlled
            Value > 0 6 = Phi shear and/or torsion Value > 0 7 = Phi shear seismic Value > 0
            8 = Phi joint shear Value > 0 9 = Pattern live load factor Value >= 0 10 =
            Utilization factor limit Value > 0 11 = Multi-response case design 1 = Envelopes
            2 = Step-by step 3= Last step 4 = Envelopes - All 5 = Step-by step - All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AS_3600_09.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, km Major 8 = Moment coefficient, km Minor 9 = Nonsway moment
            factor, Db Major 10 = Nonsway moment factor, Db Minor 11 = Sway moment factor,
            Ds Major 12 = Sway moment factor, Ds Minor
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 = As
            specified in preferences 1 = Sway special 2 = Sway intermediate 3 = Sway
            ordinary 4 = Nonsway 2 = Live load reduction factor Value >= 0; 0 means use
            program determined value. 3 = Unbraced length ratio, Major Value >= 0; 0 means
            use program determined value. 4 = Unbraced length ratio, Minor Value >= 0; 0
            means use program determined value. 5 = Effective length factor, K Major Value
            >= 0; 0 means use program determined value. 6 = Effective length factor, K Minor
            Value >= 0; 0 means use program determined value. 7 = Moment coefficient, km
            Major Value >= 0; 0 means use program determined value. 8 = Moment coefficient,
            km Minor Value >= 0; 0 means use program determined value. 9 = Nonsway moment
            factor, Db Major Value >= 0; 0 means use program determined value. 10 = Nonsway
            moment factor, Db Minor Value >= 0; 0 means use program determined value. 11 =
            Sway moment factor, Ds Major Value >= 0; 0 means use program determined value.
            12 = Sway moment factor, Ds Minor Value >= 0; 0 means use program determined
            value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AS_3600_09.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise, it returns a nonzero value.
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AS_3600_09.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_Singaopre_CP_65_99:
    """Wrapper para SapModel.DesignConcrete.Singaopre_CP_65_99."""

    def __init__(self, raw):
        self._raw = raw

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, Beta Major 6 = Effective length factor, Beta Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway 2 = Non-sway 2 = Live load reduction factor Value >= 0;
            0 means use program determined value. 3 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 4 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 5 = Effective length factor, Beta
            Major Value >= 0; 0 means use program determined value. 6 = Effective length
            factor, Beta Minor Value >= 0; 0 means use program determined value. 7 = Moment
            coefficient, Cm Major Value >= 0; 0 means use program determined value. 8 =
            Moment coefficient, Cm Minor Value >= 0; 0 means use program determined value. 9
            = Non-sway moment factor, Dns Major Value >= 0; 0 means use program determined
            value. 10 = Non-sway moment factor, Dns Minor Value >= 0; 0 means use program
            determined value. 11 = Sway moment factor, Ds Major Value >= 0; 0 means use
            program determined value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means
            use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Singaopre_CP_65_99.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_AASHTO_LRFD_2014:
    """Wrapper para SapModel.DesignConcrete.AASHTO_LRFD_2014."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            overwrite item considered. 1 = Live load reduction factor 2 = Unbraced length
            ratio, Major 3 = Unbraced length ratio, Minor 4 = Effective length factor, K
            Major 5 = Effective length factor, K Minor 6 = Moment coefficient, Cm Major 7 =
            Moment coefficient, Cm Minor 8 = Nonsway moment factor, Db Major 9 = Nonsway
            moment factor, Db Minor 10 = Sway moment factor, Ds Major 11 = Sway moment
            factor, Ds Minor
        Value (output): The value of the considered overwrite item. 1 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 2 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 3 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 4 =
            Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 5 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 6 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 7 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 8 = Nonsway moment factor, Db Major Value >= 0; 0
            means use program determined value. 9 = Nonsway moment factor, Db Minor Value >=
            0; 0 means use program determined value. 10 = Sway moment factor, Ds Major Value
            >= 0; 0 means use program determined value. 11 = Sway moment factor, Ds Minor
            Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AASHTO_LRFD_2014.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 7, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Seismic Zone 5 =
            Pattern live load factor 6 = Utilization factor limit 7 = Multi-response case
            design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and divisible by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Seismic Zone 0 = Zone 0 1 = Zone 1 2 = Zone 2 3 = Zone 3 4 =
            Zone 4 5 = Pattern live load factor Value >= 0 6 = Utilization factor limit
            Value > 0 7 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last
            step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AASHTO_LRFD_2014.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            overwrite item considered. 1 = Live load reduction factor 2 = Unbraced length
            ratio, Major 3 = Unbraced length ratio, Minor 4 = Effective length factor, K
            Major 5 = Effective length factor, K Minor 6 = Moment coefficient, Cm Major 7 =
            Moment coefficient, Cm Minor 8 = Nonsway moment factor, Db Major 9 = Nonsway
            moment factor, Db Minor 10 = Sway moment factor, Ds Major 11 = Sway moment
            factor, Ds Minor
        Value (input): The value of the considered overwrite item. 1 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 2 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 3 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 4 =
            Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 5 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 6 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 7 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 8 = Nonsway moment factor, Db Major Value >= 0; 0
            means use program determined value. 9 = Nonsway moment factor, Db Minor Value >=
            0; 0 means use program determined value. 10 = Sway moment factor, Ds Major Value
            >= 0; 0 means use program determined value. 11 = Sway moment factor, Ds Minor
            Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, the assignment is made to all selected
            frame objects and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AASHTO_LRFD_2014.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 7, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Seismic Zone 5 =
            Pattern live load factor 6 = Utilization factor limit 7 = Multi-response case
            design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and divisible by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Seismic Zone 0 = Zone 0 1 = Zone 1 2 = Zone 2 3 = Zone 3 4 =
            Zone 4 5 = Pattern live load factor Value >= 0 6 = Utilization factor limit
            Value > 0 7 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last
            step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AASHTO_LRFD_2014.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_KCI_1999:
    """Wrapper para SapModel.DesignConcrete.KCI_1999."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway special 2 = Sway intermediate 3 = Sway ordinary 4 =
            Non-sway 2 = Live load reduction factor Value >= 0; 0 means use program
            determined value. 3 = Unbraced length ratio, Major Value >= 0; 0 means use
            program determined value. 4 = Unbraced length ratio, Minor Value >= 0; 0 means
            use program determined value. 5 = Effective length factor, K Major Value >= 0; 0
            means use program determined value. 6 = Effective length factor, K Minor Value
            >= 0; 0 means use program determined value. 7 = Moment coefficient, Cm Major
            Value >= 0; 0 means use program determined value. 8 = Moment coefficient, Cm
            Minor Value >= 0; 0 means use program determined value. 9 = Non-sway moment
            factor, Dns Major Value >= 0; 0 means use program determined value. 10 = Non-
            sway moment factor, Dns Minor Value >= 0; 0 means use program determined value.
            11 = Sway moment factor, Ds Major Value >= 0; 0 means use program determined
            value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means use program
            determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.KCI_1999.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 10, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Phi bending tension 5 =
            Phi compression controlled tied 6 = Phi compression controlled spiral 7 = Phi
            shear 8 = Pattern live load factor 9 = Utilization factor limit 10 = Multi-
            response case design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Phi bending tension Value > 0 5 = Phi compression controlled
            tied Value > 0 6 = Phi compression controlled spiral Value > 0 7 = Phi shear
            Value > 0 8 = Pattern live load factor Value >= 0 9 = Utilization factor limit
            Value > 0 10 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 =
            Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.KCI_1999.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway special 2 = Sway intermediate 3 = Sway ordinary 4 =
            Non-sway 2 = Live load reduction factor Value >= 0; 0 means use program
            determined value. 3 = Unbraced length ratio, Major Value >= 0; 0 means use
            program determined value. 4 = Unbraced length ratio, Minor Value >= 0; 0 means
            use program determined value. 5 = Effective length factor, K Major Value >= 0; 0
            means use program determined value. 6 = Effective length factor, K Minor Value
            >= 0; 0 means use program determined value. 7 = Moment coefficient, Cm Major
            Value >= 0; 0 means use program determined value. 8 = Moment coefficient, Cm
            Minor Value >= 0; 0 means use program determined value. 9 = Non-sway moment
            factor, Dns Major Value >= 0; 0 means use program determined value. 10 = Non-
            sway moment factor, Dns Minor Value >= 0; 0 means use program determined value.
            11 = Sway moment factor, Ds Major Value >= 0; 0 means use program determined
            value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means use program
            determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.KCI_1999.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 10, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Phi bending tension 5 =
            Phi compression controlled tied 6 = Phi compression controlled spiral 7 = Phi
            shear 8 = Pattern live load factor 9 = Utilization factor limit 10 = Multi-
            response case design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Phi bending tension Value > 0 5 = Phi compression controlled
            tied Value > 0 6 = Phi compression controlled spiral Value > 0 7 = Phi shear
            Value > 0 8 = Pattern live load factor Value >= 0 9 = Utilization factor limit
            Value > 0 10 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 =
            Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.KCI_1999.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_AS_3600_01:
    """Wrapper para SapModel.DesignConcrete.AS_3600_01."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, km Major 8 = Moment coefficient, km Minor 9 = Nonsway moment
            factor, Db Major 10 = Nonsway moment factor, Db Minor 11 = Sway moment factor,
            Ds Major 12 = Sway moment factor, Ds Minor
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway special 2 = Sway intermediate 3 = Sway ordinary 4 =
            Nonsway 2 = Live load reduction factor Value >= 0; 0 means use program
            determined value. 3 = Unbraced length ratio, Major Value >= 0; 0 means use
            program determined value. 4 = Unbraced length ratio, Minor Value >= 0; 0 means
            use program determined value. 5 = Effective length factor, K Major Value >= 0; 0
            means use program determined value. 6 = Effective length factor, K Minor Value
            >= 0; 0 means use program determined value. 7 = Moment coefficient, km Major
            Value >= 0; 0 means use program determined value. 8 = Moment coefficient, km
            Minor Value >= 0; 0 means use program determined value. 9 = Nonsway moment
            factor, Db Major Value >= 0; 0 means use program determined value. 10 = Nonsway
            moment factor, Db Minor Value >= 0; 0 means use program determined value. 11 =
            Sway moment factor, Ds Major Value >= 0; 0 means use program determined value.
            12 = Sway moment factor, Ds Minor Value >= 0; 0 means use program determined
            value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AS_3600_01.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Phi tension controlled
            5 = Phi compression controlled 6 = Phi shear and/or torsion 7 = Phi shear
            seismic 8 = Phi joint shear 9 = Pattern live load factor 10 = Utilization factor
            limit 11 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and divisible by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Phi tension controlled Value > 0 5 = Phi compression controlled
            Value > 0 6 = Phi shear and/or torsion Value > 0 7 = Phi shear seismic Value > 0
            8 = Phi joint shear Value > 0 9 = Pattern live load factor Value >= 0 10 =
            Utilization factor limit Value > 0 11 = Multi-response case design 1 = Envelopes
            2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AS_3600_01.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise, it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, km Major 8 = Moment coefficient, km Minor 9 = Nonsway moment
            factor, Db Major 10 = Nonsway moment factor, Db Minor 11 = Sway moment factor,
            Ds Major 12 = Sway moment factor, Ds Minor
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway special 2 = Sway intermediate 3 = Sway ordinary 4 =
            Nonsway 2 = Live load reduction factor Value >= 0; 0 means use program
            determined value. 3 = Unbraced length ratio, Major Value >= 0; 0 means use
            program determined value. 4 = Unbraced length ratio, Minor Value >= 0; 0 means
            use program determined value. 5 = Effective length factor, K Major Value >= 0; 0
            means use program determined value. 6 = Effective length factor, K Minor Value
            >= 0; 0 means use program determined value. 7 = Moment coefficient, km Major
            Value >= 0; 0 means use program determined value. 8 = Moment coefficient, km
            Minor Value >= 0; 0 means use program determined value. 9 = Nonsway moment
            factor, Db Major Value >= 0; 0 means use program determined value. 10 = Nonsway
            moment factor, Db Minor Value >= 0; 0 means use program determined value. 11 =
            Sway moment factor, Ds Major Value >= 0; 0 means use program determined value.
            12 = Sway moment factor, Ds Minor Value >= 0; 0 means use program determined
            value
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AS_3600_01.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise, it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Phi tension controlled
            5 = Phi compression controlled 6 = Phi shear and/or torsion 7 = Phi shear
            seismic 8 = Phi joint shear 9 = Pattern live load factor 10 = Utilization factor
            limit 11 = Multi-response case design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and divisible by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Phi tension controlled Value > 0 5 = Phi compression controlled
            Value > 0 6 = Phi shear and/or torsion Value > 0 7 = Phi shear seismic Value > 0
            8 = Phi joint shear Value > 0 9 = Pattern live load factor Value >= 0 10 =
            Utilization factor limit Value > 0 11 = Multi-response case design 1 = Envelopes
            2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AS_3600_01.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_UBC97:
    """Wrapper para SapModel.DesignConcrete.UBC97."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway special 2 = Sway Intermediate 3 = Sway Ordinary 4 =
            Non-sway 2 = Live load reduction factor Value >= 0; 0 means use program
            determined value. 3 = Unbraced length ratio, Major Value >= 0; 0 means use
            program determined value. 4 = Unbraced length ratio, Minor Value >= 0; 0 means
            use program determined value. 5 = Effective length factor, K Major Value >= 0; 0
            means use program determined value. 6 = Effective length factor, K Minor Value
            >= 0; 0 means use program determined value. 7 = Moment coefficient, Cm Major
            Value >= 0; 0 means use program determined value. 8 = Moment coefficient, Cm
            Minor Value >= 0; 0 means use program determined value. 9 = Non-sway moment
            factor, Dns Major Value >= 0; 0 means use program determined value. 10 = Non-
            sway moment factor, Dns Minor Value >= 0; 0 means use program determined value.
            11 = Sway moment factor, Ds Major Value >= 0; 0 means use program determined
            value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means use program
            determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.UBC97.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 10, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Phi bending tension 5 =
            Phi compression controlled tied 6 = Phi compression controlled spiral 7 = Phi
            shear 8 = Pattern live load factor 9 = Utilization factor limit 10 = Multi-
            response case design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Phi bending tension Value > 0 5 = Phi compression controlled
            tied Value > 0 6 = Phi compression controlled spiral Value > 0 7 = Phi shear
            Value > 0 8 = Pattern live load factor Value >= 0 9 = Utilization factor limit
            Value > 0 10 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 =
            Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.UBC97.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway special 2 = Sway Intermediate 3 = Sway Ordinary 4 =
            Non-sway 2 = Live load reduction factor Value >= 0; 0 means use program
            determined value. 3 = Unbraced length ratio, Major Value >= 0; 0 means use
            program determined value. 4 = Unbraced length ratio, Minor Value >= 0; 0 means
            use program determined value. 5 = Effective length factor, K Major Value >= 0; 0
            means use program determined value. 6 = Effective length factor, K Minor Value
            >= 0; 0 means use program determined value. 7 = Moment coefficient, Cm Major
            Value >= 0; 0 means use program determined value. 8 = Moment coefficient, Cm
            Minor Value >= 0; 0 means use program determined value. 9 = Non-sway moment
            factor, Dns Major Value >= 0; 0 means use program determined value. 10 = Non-
            sway moment factor, Dns Minor Value >= 0; 0 means use program determined value.
            11 = Sway moment factor, Ds Major Value >= 0; 0 means use program determined
            value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means use program
            determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.UBC97.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 10, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Phi bending tension 5 =
            Phi compression controlled tied 6 = Phi compression controlled spiral 7 = Phi
            shear 8 = Pattern live load factor 9 = Utilization factor limit 10 = Multi-
            response case design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Phi bending tension Value > 0 5 = Phi compression controlled
            tied Value > 0 6 = Phi compression controlled spiral Value > 0 7 = Phi shear
            Value > 0 8 = Pattern live load factor Value >= 0 9 = Utilization factor limit
            Value > 0 10 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 =
            Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.UBC97.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_Hong_Kong_CP_2013:
    """Wrapper para SapModel.DesignConcrete.Hong_Kong_CP_2013."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, Beta Major 6 = Effective length factor, Beta Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway 2 = Non-sway 2 = Live load reduction factor Value >= 0;
            0 means use program determined value. 3 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 4 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 5 = Effective length factor, Beta
            Major Value >= 0; 0 means use program determined value. 6 = Effective length
            factor, Beta Minor Value >= 0; 0 means use program determined value. 7 = Moment
            coefficient, Cm Major Value >= 0; 0 means use program determined value. 8 =
            Moment coefficient, Cm Minor Value >= 0; 0 means use program determined value. 9
            = Non-sway moment factor, Dns Major Value >= 0; 0 means use program determined
            value. 10 = Non-sway moment factor, Dns Minor Value >= 0; 0 means use program
            determined value. 11 = Sway moment factor, Ds Major Value >= 0; 0 means use
            program determined value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means
            use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Hong_Kong_CP_2013.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, Beta Major 6 = Effective length factor, Beta Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway 2 = Non-sway 2 = Live load reduction factor Value >= 0;
            0 means use program determined value. 3 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 4 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 5 = Effective length factor, Beta
            Major Value >= 0; 0 means use program determined value. 6 = Effective length
            factor, Beta Minor Value >= 0; 0 means use program determined value. 7 = Moment
            coefficient, Cm Major Value >= 0; 0 means use program determined value. 8 =
            Moment coefficient, Cm Minor Value >= 0; 0 means use program determined value. 9
            = Non-sway moment factor, Dns Major Value >= 0; 0 means use program determined
            value. 10 = Non-sway moment factor, Dns Minor Value >= 0; 0 means use program
            determined value. 11 = Sway moment factor, Ds Major Value >= 0; 0 means use
            program determined value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means
            use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Hong_Kong_CP_2013.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 9, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Gamma steel 5 = Gamma
            concrete 6 = Gamma concrete shear 7 = Pattern live load factor 8 = Utilization
            factor limit 9 = Multi-response case design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Gamma steel Value > 0 5 = Gamma concrete Value > 0 6 = Gamma
            concrete shear Value > 0 7 = Pattern live load factor Value >= 0 8 = Utilization
            factor limit Value > 0 9 = Multi-response case design 1 = Envelopes 2 = Step-by-
            step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Hong_Kong_CP_2013.SetPreference falhou (ret={_r})".format(_r=_r))
        return None

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 9, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Gamma steel 5 = Gamma
            concrete 6 = Gamma concrete shear 7 = Pattern live load factor 8 = Utilization
            factor limit 9 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Gamma steel Value > 0 5 = Gamma concrete Value > 0 6 = Gamma
            concrete shear Value > 0 7 = Pattern live load factor Value >= 0 8 = Utilization
            factor limit Value > 0 9 = Multi-response case design 1 = Envelopes 2 = Step-by-
            step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Hong_Kong_CP_2013.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]


class N_DesignConcrete_Mexican_RCDF_2001:
    """Wrapper para SapModel.DesignConcrete.Mexican_RCDF_2001."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, k Major 6 = Effective length factor, k Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Fab Major 10 = Non-sway moment factor, Fab Minor 11 = Sway moment
            factor, Fas Major 12 = Sway moment factor, Fas Minor
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway special 2 = Sway ordinary 3 = Non-sway 2 = Live load
            reduction factor Value >= 0; 0 means use program determined value. 3 = Unbraced
            length ratio, Major Value >= 0; 0 means use program determined value. 4 =
            Unbraced length ratio, Minor Value >= 0; 0 means use program determined value. 5
            = Effective length factor, k Major Value >= 0; 0 means use program determined
            value. 6 = Effective length factor, k Minor Value >= 0; 0 means use program
            determined value. 7 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 8 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 9 = Non-sway moment factor, Fab Major Value >= 0;
            0 means use program determined value. 10 = Non-sway moment factor, Fab Minor
            Value >= 0; 0 means use program determined value. 11 = Sway moment factor, Fas
            Major Value >= 0; 0 means use program determined value. 12 = Sway moment factor,
            Fas Minor Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Mexican_RCDF_2001.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Phi bending 5 = Phi
            tension 6 = Phi compression controlled tied 7 = Phi compression controlled
            spiral 8 = Phi shear 9 = Pattern live load factor 10 = Utilization factor limit
            11 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Phi bending Value > 0 5 = Phi tension Value > 0 6 = Phi
            compression controlled tied Value > 0 7 = Phi compression controlled spiral
            Value > 0 8 = Phi shear Value > 0 9 = Pattern live load factor Value >= 0 10 =
            Utilization factor limit Value > 0 11 = Multi-response case design 1 = Envelopes
            2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Mexican_RCDF_2001.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, k Major 6 = Effective length factor, k Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Fab Major 10 = Non-sway moment factor, Fab Minor 11 = Sway moment
            factor, Fas Major 12 = Sway moment factor, Fas Minor
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway special 2 = Sway ordinary 3 = Non-sway 2 = Live load
            reduction factor Value >= 0; 0 means use program determined value. 3 = Unbraced
            length ratio, Major Value >= 0; 0 means use program determined value. 4 =
            Unbraced length ratio, Minor Value >= 0; 0 means use program determined value. 5
            = Effective length factor, k Major Value >= 0; 0 means use program determined
            value. 6 = Effective length factor, k Minor Value >= 0; 0 means use program
            determined value. 7 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 8 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 9 = Non-sway moment factor, Fab Major Value >= 0;
            0 means use program determined value. 10 = Non-sway moment factor, Fab Minor
            Value >= 0; 0 means use program determined value. 11 = Sway moment factor, Fas
            Major Value >= 0; 0 means use program determined value. 12 = Sway moment factor,
            Fas Minor Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Mexican_RCDF_2001.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Phi bending 5 = Phi
            tension 6 = Phi compression controlled tied 7 = Phi compression controlled
            spiral 8 = Phi shear 9 = Pattern live load factor 10 = Utilization factor limit
            11 = Multi-response case design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Phi bending Value > 0 5 = Phi tension Value > 0 6 = Phi
            compression controlled tied Value > 0 7 = Phi compression controlled spiral
            Value > 0 8 = Phi shear Value > 0 9 = Pattern live load factor Value >= 0 10 =
            Utilization factor limit Value > 0 11 = Multi-response case design 1 = Envelopes
            2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Mexican_RCDF_2001.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_Eurocode_2_2004:
    """Wrapper para SapModel.DesignConcrete.Eurocode_2_2004."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, Beta Major 6 = Effective length factor, Beta Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Nonsway moment
            factor, Dns Major 10 = Nonsway moment factor, Dns Minor 11 = Sway moment factor,
            Ds Major 12 = Sway moment factor, Ds Minor
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway 2 = Nonsway 2 = Live load reduction factor Value >= 0;
            0 means use program determined value. 3 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 4 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 5 = Effective length factor, Beta
            Major Value >= 0; 0 means use program determined value. 6 = Effective length
            factor, Beta Minor Value >= 0; 0 means use program determined value. 7 = Moment
            coefficient, Cm Major Value >= 0; 0 means use program determined value. 8 =
            Moment coefficient, Cm Minor Value >= 0; 0 means use program determined value. 9
            = Nonsway moment factor, Dns Major Value >= 0; 0 means use program determined
            value. 10 = Nonsway moment factor, Dns Minor Value >= 0; 0 means use program
            determined value. 11 = Sway moment factor, Ds Major Value >= 0; 0 means use
            program determined value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means
            use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Eurocode_2_2004.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 16, inclusive, indicating the
            preference item considered. 1 = Country 2 = Combos equation 3 = Second order
            method 4 = Number of interaction curves 5 = Number of interaction points 6 =
            Consider minimum eccentricity 7 = Theta0 8 = Gamma steel 9 = Gamma concrete 10 =
            AlphaCC 11 = AlphaCT 12 = AlphaLCC 13 = AlphaLCT 14 = Pattern live load factor
            15 = Utilization factor limit 16 = Multi-response case design 17 = Reliability
            Class
        Value (output): The value of the considered preference item. 1 = Country 1 = CEN
            Default 2 = United Kingdom 3 = Slovenia 5 = Norway 6 = Singapore 7 = Sweden 8 =
            Finland 9 = Denmark 10 = Portugal 11 = Germany 2 = Combos equation 1 = Eq. 6.10
            2 = Max of Eqs. 6.10a and 6.10b 3 = Second order method 1 = Nominal stiffness 2
            = Nominal curvature 3 = None 4 = Number of interaction curves Value >= 4 and
            divisible by 4 5 = Number of interaction points Value >= 5 and odd 6 = Consider
            minimum eccentricity 0 = No Any other value = Yes 7 = Theta0 Value > 0 8 = Gamma
            steel Value > 0 9 = Gamma concrete Value > 0 10 = AlphaCC Value > 0 11 = AlphaCT
            Value > 0 12 = AlphaLCC Value > 0 13 = AlphaLCT Value > 0 14 = Pattern live load
            factor Value >= 0 15 = Utilization factor limit Value > 0 16 = Multi-response
            case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5
            = Step-by-step -- All 17 = Reliability Class 1 = Class 1 2 = Class 2 3 = Class 3
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Eurocode_2_2004.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, Beta Major 6 = Effective length factor, Beta Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Nonsway moment
            factor, Dns Major 10 = Nonsway moment factor, Dns Minor 11 = Sway moment factor,
            Ds Major 12 = Sway moment factor, Ds Minor
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway 2 = Nonsway 2 = Live load reduction factor Value >= 0;
            0 means use program determined value. 3 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 4 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 5 = Effective length factor, Beta
            Major Value >= 0; 0 means use program determined value. 6 = Effective length
            factor, Beta Minor Value >= 0; 0 means use program determined value. 7 = Moment
            coefficient, Cm Major Value >= 0; 0 means use program determined value. 8 =
            Moment coefficient, Cm Minor Value >= 0; 0 means use program determined value. 9
            = Nonsway moment factor, Dns Major Value >= 0; 0 means use program determined
            value. 10 = Nonsway moment factor, Dns Minor Value >= 0; 0 means use program
            determined value. 11 = Sway moment factor, Ds Major Value >= 0; 0 means use
            program determined value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means
            use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Eurocode_2_2004.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise, it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 16, inclusive, indicating the
            preference item considered. 1 = Country 2 = Combos equation 3 = Second order
            method 4 = Number of interaction curves 5 = Number of interaction points 6 =
            Consider minimum eccentricity 7 = Theta0 8 = Gamma steel 9 = Gamma concrete 10 =
            AlphaCC 11 = AlphaCT 12 = AlphaLCC 13 = AlphaLCT 14 = Pattern live load factor
            15 = Utilization factor limit 16 = Multi-response case design 17 = Reliability
            Class
        Value (input): The value of the considered preference item. 1 = Country 1 = CEN
            Default 2 = United Kingdom 3 = Slovenia 5 = Norway 6 = Singapore 7 = Sweden 8 =
            Finland 9 = Denmark 10 = Portugal 11 = Germany 2 = Combos equation 1 = Eq. 6.10
            2 = Max of Eqs. 6.10a and 6.10b 3 = Second order method 1 = Nominal stiffness 2
            = Nominal curvature 3 = None 4 = Number of interaction curves Value >= 4 and
            divisible by 4 5 = Number of interaction points Value >= 5 and odd 6 = Consider
            minimum eccentricity 0 = No Any other value = Yes 7 = Theta0 Value > 0 8 = Gamma
            steel Value > 0 9 = Gamma concrete Value > 0 10 = AlphaCC Value > 0 11 = AlphaCT
            Value > 0 12 = AlphaLCC Value > 0 13 = AlphaLCT Value > 0 14 = Pattern live load
            factor Value >= 0 15 = Utilization factor limit Value > 0 16 = Multi-response
            case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5
            = Step-by-step -- All 17 = Reliability Class 1 = Class 1 2 = Class 2 3 = Class 3
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.Eurocode_2_2004.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_SP63_13330_2012:
    """Wrapper para SapModel.DesignConcrete.SP63_13330_2012."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 14, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            amplification factor, Eta Major 8 = Moment amplification factor, Eta Minor 9 =
            Gammab3 for column 10 = Gammab3 for beam 11 = Consider torsion? 12 =
            (qsw,1*Z1)/(Rs*As,1) 13 = Corner rebar fraction top 14 = Corner rebar fraction
            bottom
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Determined 1 = Sway 2 = Nonsway 2 = Live load reduction factor Value
            >=0; 0 means use program determined value. 3 = Unbraced length ratio, Major
            Value >=0; 0 means use program determined value. 4 = Unbraced length ratio,
            Minor Value >=0; 0 means use program determined value. 5 = Effective length
            factor, K Major Value >=0; 0 means use program determined value. 6 = Effective
            length factor, K Minor Value >=0; 0 means use program determined value. 7 =
            Moment amplification factor, Eta Major Value >=0; 0 means use program determined
            value. 8 = Moment amplification factor, Eta Minor Value >=0; 0 means use program
            determined value. 9 = Gammab3 for column Value >=0; 0 means use program
            determined value. 10 = Gammab3 for beam Value >=0; 0 means use program
            determined value. 11 = Consider torsion? 0 = Program Determined 1 = No 2 = Yes
            12 = (qsw,1*Z1)/(Rs*As,1) 0.5 <= Value <= 1.5; 0 means use program determined
            value. 13 = Corner rebar fraction top 0 < Value <= 1; 0 means use program
            determined value. 14 = Corner rebar fraction bottom 0 < Value <= 1; 0 means use
            program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.SP63_13330_2012.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 23, inclusive, indicating the
            preference item considered. 1 = Multi-response case design 2 = Number of
            interaction curves 3 = Number of interaction points 4 = Consider minimum
            eccentricity? 5 = Consider torsion? 6 = (qsw,1*Z1)/(Rs*As,1) 7 = Corner rebar
            fraction top 8 = Corner rebar fraction bottom 9 = Relative humidity 10 =
            Moisture content 11 = Gamma_b 12 = Gamma_bt 13 = Gamma_b1 short term 14 =
            Gamma_b1 long term 15 = Gamma_b2 16 = Gamma_b3 beams 17 = Gamma_b3 columns 18 =
            Gamma_b4 19 = Gamma_b5 20 = Gamma_S 21 = Gamma_S1 22 = Pattern live load factor
            23 = Utilization factor limit
        Value (output): The value of the considered preference item. 1 = Multi-response case
            design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 =
            Step-by-step -- All 2 = Number of interaction curves Value >= 4 and divisible by
            4 3 = Number of interaction points Value >= 5 and odd 4 = Consider minimum
            eccentricity? 0 = No Any other value = Yes 5 = Consider torsion? 0 = No Any
            other value = Yes 6 = (qsw,1*Z1)/(Rs*As,1) 0.5 <= Value <= 1.5 7 = Corner rebar
            fraction top 0 < Value <= 1 8 = Corner rebar fraction bottom 0 < Value <= 1 9 =
            Relative humidity 0 <= Value <= 100 10 = Moisture content 0 <= Value <= 1 11 =
            Gamma_b Value > 0 12 = Gamma_bt Value > 0 13 = Gamma_b1 short term Value > 0 14
            = Gamma_b1 long term Value > 0 15 = Gamma_b2 Value > 0 16 = Gamma_b3 beams Value
            > 0 17 = Gamma_b3 columns Value > 0 18 = Gamma_b4 Value > 0 19 = Gamma_b5 Value
            > 0 20 = Gamma_S Value > 0 21 = Gamma_S1 Value > 0 22 = Pattern live load factor
            Value >= 0 23 = Utilization factor limit Value > 0
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.SP63_13330_2012.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 14, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            amplification factor, Eta Major 8 = Moment amplification factor, Eta Minor 9 =
            Gammab3 for column 10 = Gammab3 for beam 11 = Consider torsion? 12 =
            (qsw,1*Z1)/(Rs*As,1) 13 = Corner rebar fraction top 14 = Corner rebar fraction
            bottom
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Determined 1 = Sway 2 = Nonsway 2 = Live load reduction factor Value
            >=0; 0 means use program determined value. 3 = Unbraced length ratio, Major
            Value >=0; 0 means use program determined value. 4 = Unbraced length ratio,
            Minor Value >=0; 0 means use program determined value. 5 = Effective length
            factor, K Major Value >=0; 0 means use program determined value. 6 = Effective
            length factor, K Minor Value >=0; 0 means use program determined value. 7 =
            Moment amplification factor, Eta Major Value >=0; 0 means use program determined
            value. 8 = Moment amplification factor, Eta Minor Value >=0; 0 means use program
            determined value. 9 = Gammab3 for column Value >=0; 0 means use program
            determined value. 10 = Gammab3 for beam Value >=0; 0 means use program
            determined value. 11 = Consider torsion? 0 = Program Determined 1 = No 2 = Yes
            12 = (qsw,1*Z1)/(Rs*As,1) 0.5 <= Value <= 1.5; 0 means use program determined
            value. 13 = Corner rebar fraction top 0 < Value <= 1; 0 means use program
            determined value. 14 = Corner rebar fraction bottom 0 < Value <= 1; 0 means use
            program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.SP63_13330_2012.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 23, inclusive, indicating the
            preference item considered. 1 = Multi-response case design 2 = Number of
            interaction curves 3 = Number of interaction points 4 = Consider minimum
            eccentricity? 5 = Consider torsion? 6 = (qsw,1*Z1)/(Rs*As,1) 7 = Corner rebar
            fraction top 8 = Corner rebar fraction bottom 9 = Relative humidity 10 =
            Moisture content 11 = Gamma_b 12 = Gamma_bt 13 = Gamma_b1 short term 14 =
            Gamma_b1 long term 15 = Gamma_b2 16 = Gamma_b3 beams 17 = Gamma_b3 columns 18 =
            Gamma_b4 19 = Gamma_b5 20 = Gamma_S 21 = Gamma_S1 22 = Pattern live load factor
            23 = Utilization factor limit
        Value (input): The value of the considered preference item. 1 = Multi-response case
            design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 =
            Step-by-step -- All 2 = Number of interaction curves Value >= 4 and divisible by
            4 3 = Number of interaction points Value >= 5 and odd 4 = Consider minimum
            eccentricity? 0 = No Any other value = Yes 5 = Consider torsion? 0 = No Any
            other value = Yes 6 = (qsw,1*Z1)/(Rs*As,1) 0.5 <= Value <= 1.5 7 = Corner rebar
            fraction top 0 < Value <= 1 8 = Corner rebar fraction bottom 0 < Value <= 1 9 =
            Relative humidity 0 <= Value <= 100 10 = Moisture content 0 <= Value <= 1 11 =
            Gamma_b Value > 0 12 = Gamma_bt Value > 0 13 = Gamma_b1 short term Value > 0 14
            = Gamma_b1 long term Value > 0 15 = Gamma_b2 Value > 0 16 = Gamma_b3 beams Value
            > 0 17 = Gamma_b3 columns Value > 0 18 = Gamma_b4 Value > 0 19 = Gamma_b5 Value
            > 0 20 = Gamma_S Value > 0 21 = Gamma_S1 Value > 0 22 = Pattern live load factor
            Value >= 0 23 = Utilization factor limit Value > 0
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.SP63_13330_2012.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_AASHTO_LRFD_2012:
    """Wrapper para SapModel.DesignConcrete.AASHTO_LRFD_2012."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            overwrite item considered. 1 = Live load reduction factor 2 = Unbraced length
            ratio, Major 3 = Unbraced length ratio, Minor 4 = Effective length factor, K
            Major 5 = Effective length factor, K Minor 6 = Moment coefficient, Cm Major 7 =
            Moment coefficient, Cm Minor 8 = Nonsway moment factor, Db Major 9 = Nonsway
            moment factor, Db Minor 10 = Sway moment factor, Ds Major 11 = Sway moment
            factor, Ds Minor
        Value (output): The value of the considered overwrite item. 1 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 2 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 3 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 4 =
            Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 5 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 6 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 7 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 8 = Nonsway moment factor, Db Major Value >= 0; 0
            means use program determined value. 9 = Nonsway moment factor, Db Minor Value >=
            0; 0 means use program determined value. 10 = Sway moment factor, Ds Major Value
            >= 0; 0 means use program determined value. 11 = Sway moment factor, Ds Minor
            Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AASHTO_LRFD_2012.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 7, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Seismic Zone 5 =
            Pattern live load factor 6 = Utilization factor limit 7 = Multi-response case
            design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and divisible by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Seismic Zone 0 = Zone 0 1 = Zone 1 2 = Zone 2 3 = Zone 3 4 =
            Zone 4 5 = Pattern live load factor Value >= 0 6 = Utilization factor limit
            Value > 0 7 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last
            step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AASHTO_LRFD_2012.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            overwrite item considered. 1 = Live load reduction factor 2 = Unbraced length
            ratio, Major 3 = Unbraced length ratio, Minor 4 = Effective length factor, K
            Major 5 = Effective length factor, K Minor 6 = Moment coefficient, Cm Major 7 =
            Moment coefficient, Cm Minor 8 = Nonsway moment factor, Db Major 9 = Nonsway
            moment factor, Db Minor 10 = Sway moment factor, Ds Major 11 = Sway moment
            factor, Ds Minor
        Value (input): The value of the considered overwrite item. 1 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 2 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 3 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 4 =
            Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 5 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 6 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 7 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 8 = Nonsway moment factor, Db Major Value >= 0; 0
            means use program determined value. 9 = Nonsway moment factor, Db Minor Value >=
            0; 0 means use program determined value. 10 = Sway moment factor, Ds Major Value
            >= 0; 0 means use program determined value. 11 = Sway moment factor, Ds Minor
            Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, the assignment is made to all selected
            frame objects and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AASHTO_LRFD_2012.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 7, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Seismic Zone 5 =
            Pattern live load factor 6 = Utilization factor limit 7 = Multi-response case
            design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and divisible by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Seismic Zone 0 = Zone 0 1 = Zone 1 2 = Zone 2 3 = Zone 3 4 =
            Zone 4 5 = Pattern live load factor Value >= 0 6 = Utilization factor limit
            Value > 0 7 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last
            step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.AASHTO_LRFD_2012.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_ACI_318_99:
    """Wrapper para SapModel.DesignConcrete.ACI_318_99."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = No-nsway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway special 2 = Sway intermediate 3 = Sway ordinary 4 =
            Non-sway 2 = Live load reduction factor Value >= 0; 0 means use program
            determined value. 3 = Unbraced length ratio, Major Value >= 0; 0 means use
            program determined value. 4 = Unbraced length ratio, Minor Value >= 0; 0 means
            use program determined value. 5 = Effective length factor, K Major Value >= 0; 0
            means use program determined value. 6 = Effective length factor, K Minor Value
            >= 0; 0 means use program determined value. 7 = Moment coefficient, Cm Major
            Value >= 0; 0 means use program determined value. 8 = Moment coefficient, Cm
            Minor Value >= 0; 0 means use program determined value. 9 = Non-sway moment
            factor, Dns Major Value >= 0; 0 means use program determined value. 10 = Non-
            sway moment factor, Dns Minor Value >= 0; 0 means use program determined value.
            11 = Sway moment factor, Ds Major Value >= 0; 0 means use program determined
            value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means use program
            determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.ACI_318_99.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 10, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Phi bending torsion 5 =
            Phi compression controlled tied 6 = Phi compression controlled spiral 7 = Phi
            shear 8 = Pattern live load factor 9 = Utilization factor limit 10 = Multi-
            response case design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Phi bending torsion Value > 0 5 = Phi compression controlled
            tied Value > 0 6 = Phi compression controlled spiral Value > 0 7 = Phi shear
            Value > 0 8 = Pattern live load factor Value >= 0 9 = Utilization factor limit
            Value > 0 10 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 =
            Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.ACI_318_99.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Dns Major 10 = Non-sway moment factor, Dns Minor 11 = Sway moment
            factor, Ds Major 12 = Sway moment factor, Ds Minor
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway special 2 = Sway intermediate 3 = Sway ordinary 4 =
            Non-sway 2 = Live load reduction factor Value >= 0; 0 means use program
            determined value. 3 = Unbraced length ratio, Major Value >= 0; 0 means use
            program determined value. 4 = Unbraced length ratio, Minor Value >= 0; 0 means
            use program determined value. 5 = Effective length factor, K Major Value >= 0; 0
            means use program determined value. 6 = Effective length factor, K Minor Value
            >= 0; 0 means use program determined value. 7 = Moment coefficient, Cm Major
            Value >= 0; 0 means use program determined value. 8 = Moment coefficient, Cm
            Minor Value >= 0; 0 means use program determined value. 9 = Non-sway moment
            factor, Dns Major Value >= 0; 0 means use program determined value. 10 = Non-
            sway moment factor, Dns Minor Value >= 0; 0 means use program determined value.
            11 = Sway moment factor, Ds Major Value >= 0; 0 means use program determined
            value. 12 = Sway moment factor, Ds Minor Value >= 0; 0 means use program
            determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.ACI_318_99.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 10, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Phi bending torsion 5 =
            Phi compression controlled tied 6 = Phi compression controlled spiral 7 = Phi
            shear 8 = Pattern live load factor 9 = Utilization factor limit 10 = Multi-
            response case design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Phi bending torsion Value > 0 5 = Phi compression controlled
            tied Value > 0 6 = Phi compression controlled spiral Value > 0 7 = Phi shear
            Value > 0 8 = Pattern live load factor Value >= 0 9 = Utilization factor limit
            Value > 0 10 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 =
            Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.ACI_318_99.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignConcrete_CSA_A23_3_94:
    """Wrapper para SapModel.DesignConcrete.CSA_A23_3_94."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a concrete design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a concrete frame design procedure.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, Db Major 10 = Non-sway moment factor, Db Minor 11 = Sway moment factor,
            Ds Major 12 = Sway moment factor, Ds Minor
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Ductile 2 = Nominal 3 = Ordinary 2 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 3 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 4 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 5 =
            Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 6 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 7 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 8 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 9 = Non-sway moment factor, Db Major Value >= 0; 0
            means use program determined value. 10 = Non-sway moment factor, Db Minor Value
            >= 0; 0 means use program determined value. 11 = Sway moment factor, Ds Major
            Value >= 0; 0 means use program determined value. 12 = Sway moment factor, Ds
            Minor Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.CSA_A23_3_94.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a concrete design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 8, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Phi steel 5 = Phi
            concrete 6 = Pattern live load factor 7 = Utilization factor limit 8 = Multi-
            response case design
        Value (output): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Phi steel Value > 0 5 = Phi concrete Value > 0 6 = Pattern live
            load factor Value >= 0 7 = Utilization factor limit Value > 0 8 = Multi-response
            case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5
            = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.CSA_A23_3_94.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a concrete design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor 5 = Effective
            length factor, K Major 6 = Effective length factor, K Minor 7 = Moment
            coefficient, Cm Major 8 = Moment coefficient, Cm Minor 9 = Non-sway moment
            factor, DbMajor 10 = Non-sway moment factor, DbMinor 11 = Sway moment factor, Ds
            Major 12 = Sway moment factor, Ds Minor
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Ductile 2 = Nominal 3 = Ordinary 2 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 3 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 4 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 5 =
            Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 6 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 7 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 8 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 9 = Non-sway moment factor, Db Major Value >= 0; 0
            means use program determined value. 10 = Non-sway moment factor, Db Minor Value
            >= 0; 0 means use program determined value. 11 = Sway moment factor, Ds Major
            Value >= 0; 0 means use program determined value. 12 = Sway moment factor, Ds
            Minor Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.CSA_A23_3_94.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a concrete design preference item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 8, inclusive, indicating the
            preference item considered. 1 = Number of interaction curves 2 = Number of
            interaction points 3 = Consider minimum eccentricity 4 = Phi steel 5 = Phi
            concrete 6 = Pattern live load factor 7 = Utilization factor limit 8 = Multi-
            response case design
        Value (input): The value of the considered preference item. 1 = Number of
            interaction curves Value >= 4 and devisable by 4 2 = Number of interaction
            points Value >= 5 and odd 3 = Consider minimum eccentricity 0 = No Any other
            value = Yes 4 = Phi steel Value > 0 5 = Phi concrete Value > 0 6 = Pattern live
            load factor Value >= 0 7 = Utilization factor limit Value > 0 8 = Multi-response
            case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5
            = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignConcrete.CSA_A23_3_94.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


