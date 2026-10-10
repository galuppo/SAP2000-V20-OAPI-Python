"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_DesignSteel:
    """Wrapper para SapModel.DesignSteel."""

    def __init__(self, raw):
        self._raw = raw

    def DeleteResults(self):
        """This function deletes all steel frame design results. The function returns zero if the
        results are successfully deleted; otherwise it returns a nonzero value.
        """
        _r = self._raw.DeleteResults()
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.DeleteResults falhou (ret={_r})".format(_r=_r))
        return None

    def GetCode(self):
        """This function retrieves the steel design code. The function returns zero if the code is
        successfully retrieved; otherwise it returns a nonzero value.
    
        CodeName (output): This is one of the following steel design code names. AASHTO LRFD
            2007 AISC-ASD89 AISC 360-10 AISC360-05/IBC2006 AISC-LRFD93 API RP2A-LRFD 97 API
            RP2A-WSD2000 API RP2A-WSD2014 AS 4100-1998 ASCE 10-97 BS5950 2000 Chinese 2010
            CSA S16-14 CSA-S16-09 EUROCODE 3-2005 Indian IS 800-2007 Italian NTC 2008
            Italian UNI 10011 KBC 2009 Norsok N-004 2013 NZS 3404-1997 SP 16.13330.2011
        """
        _r = self._raw.GetCode("")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.GetCode falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetComboAutoGenerate(self, AutoGenerate: bool):
        """This function retrieves the value of the automatically generated code-based design load
        combinations option for steel frame design. The function returns zero if the options
        are successfully set; otherwise it returns a nonzero value.
    
        AutoGenerate (input): If this item is True, the option to automatically generate
            code-based design load combinations for steel frame design is turned on. If it
            is False, the option is turned off.
        """
        _r = self._raw.GetComboAutoGenerate(AutoGenerate)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.GetComboAutoGenerate falhou (ret={_r})".format(_r=_r))
        return None

    def GetComboDeflection(self):
        """This function retrieves the names of all load combinations selected as design combinations
        for steel deflection design. The function returns zero if the names are successfully
        retrieved; otherwise it returns a nonzero value.
    
        NumberItems (output): The number of load combinations selected as design
            combinations for steel deflection design.
        MyName (output): This is an array that includes the name of each response
            combination selected as a design combination for steel deflection design.
        """
        _r = self._raw.GetComboDeflection(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.GetComboDeflection falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetComboStrength(self):
        """This function retrieves the names of all load combinations selected as design combinations
        for steel strength design. The function returns zero if the names are successfully
        retrieved; otherwise it returns a nonzero value.
    
        NumberItems (output): The number of load combinations selected as design
            combinations for steel strength design.
        MyName (output): This is an array that includes the name of each response
            combination selected as a design combination for steel strength design.
        """
        _r = self._raw.GetComboStrength(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.GetComboStrength falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDesignSection(self, Name: str):
        """This function retrieves the design section for a specified steel frame object. The function
        returns zero if the section is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        PropName (output): The name of the design section for the specified frame object.
        """
        _r = self._raw.GetDesignSection(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.GetDesignSection falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetDetailResultsText(self, Name: str, ItemType: int, Table: int, Field: str):
        """This function retrieves the design results from steel design output database tables. Note
        that the summary table of all design codes is not included in this function. The
        function returns zero if the results are successfully retrieved; otherwise it
        returns a nonzero value.
        """
        _r = self._raw.GetDetailResultsText(Name, ItemType, Table, Field, 0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.GetDetailResultsText falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDetailResultsValue(self, Name: str, ItemType: int, Table: int, Field: str):
        """This function retrieves the design results from steel design output database tables. Note
        that the summary table of all design codes is not included in this function. The
        function returns zero if the results are successfully retrieved; otherwise it
        returns a nonzero value.
        """
        _r = self._raw.GetDetailResultsValue(Name, ItemType, Table, Field, 0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.GetDetailResultsValue falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetGroup(self):
        """This function retrieves the names of all groups selected for steel design. The function
        returns zero if the names are successfully retrieved; otherwise it returns a nonzero
        value.
    
        NumberItems (output): The number of groups selected for steel design.
        MyName (output): This is an array that includes the name of each group selected for
            steel design.
        """
        _r = self._raw.GetGroup(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.GetGroup falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetResultsAvailable(self):
        """The function returns True if the steel frame design results are available, otherwise False.
        """
        _r = self._raw.GetResultsAvailable()
        return _r

    def GetSummaryResults(self, Name: str, ItemType: int = 0):
        """This function retrieves summary results for steel design. The function returns zero if the
        results are successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The number of frame objects for which results are obtained.
        FrameName (output): This is an array that includes each frame object name for which
            results are obtained.
        Ratio (output): This is an array that includes the controlling stress or capacity
            ratio for each frame object.
        RatioType (output): This is an array that includes 1, 2, 3, 4, 5 or 6, indicating
            the controlling stress or capacity ratio type for each frame object. 1 = PMM 2 =
            Major shear 3 = Minor shear 4 = Major beam-column capacity ratio 5 = Minor beam-
            column capacity ratio 6 = Other
        Location (output): This is an array that includes the distance from the I-end of the
            frame object to the location where the controlling stress or capacity ratio
            occurs. [L]
        ComboName (output): This is an array that includes the name of the design
            combination for which the controlling stress or capacity ratio occurs.
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
        _r = self._raw.GetSummaryResults(Name, 0, [], [], [], [], [], [], [], ItemType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.GetSummaryResults falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTargetDispl(self, Active: bool):
        """This function retrieves lateral displacement targets for steel design. The function returns
        zero if the targets are successfully retrieved; otherwise it returns a nonzero
        value.
    
        NumberItems (output): The number of lateral displacement targets specified.
        LoadCase (output): This is an array that includes the name of the static linear load
            case associated with each lateral displacement target.
        Point (output): This is an array that includes the name of the point object
            associated to which the lateral displacement target applies.
        Displ (output): This is an array that includes the lateral displacement target. [L]
        Active (input): If this item is True, all specified lateral displacement targets are
            active. If it is False, they are inactive.
        """
        _r = self._raw.GetTargetDispl(0, [], [], [], Active)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.GetTargetDispl falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTargetPeriod(self, Active: bool):
        """This function retrieves time period targets for steel design. The function returns zero if
        the targets are successfully retrieved; otherwise it returns a nonzero value.
    
        NumberItems (output): The number of lateral displacement targets specified.
        ModalCase (output): The name of the modal load case for which the target periods
            apply.
        Mode (output): This is an array that includes the mode number associated with each
            target period.
        Period (output): This is an array that includes the target periods. [s]
        Active (input): If this item is True, all specified target periods are active. If it
            is False, they are inactive.
        """
        _r = self._raw.GetTargetPeriod(0, "", [], [], Active)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.GetTargetPeriod falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def ResetOverwrites(self):
        """This function resets all steel frame design overwrites to default values. The function
        returns zero if the overwrites are successfully reset; otherwise it returns a
        nonzero value. The function will fail if no steel frame objects are present.
        """
        _r = self._raw.ResetOverwrites()
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.ResetOverwrites falhou (ret={_r})".format(_r=_r))
        return None

    def SetAutoSelectNull(self, Name: str, ItemType: int = 0):
        """This function removes the auto select section assignments from all specified frame objects
        that have a steel frame design procedure. The function returns zero if the auto
        select section assignments are successfully removed; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetAutoSelectNull(Name, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.SetAutoSelectNull falhou (ret={_r})".format(_r=_r))
        return None

    def SetCode(self, CodeName: str):
        """This function sets the steel design code. The function returns zero if the code is
        successfully set; otherwise it returns a nonzero value.
    
        CodeName (input): This is one of the following steel design code names. AASHTO LRFD
            2007 AISC-ASD89 AISC 360-10 AISC360-05/IBC2006 AISC-LRFD93 API RP2A-LRFD 97 API
            RP2A-WSD2000 API RP2A-WSD2014 AS 4100-1998 ASCE 10-97 BS5950 2000 Chinese 2010
            CSA S16-14 CSA-S16-09 E UROCODE 3-2005 Indian IS 800-2007 Italian NTC 2008
            Italian UNI 10011 KBC 2009 Norsok N-004 2013 NZS 3404-1997 SP 16.13330.2011
        """
        _r = self._raw.SetCode(CodeName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.SetCode falhou (ret={_r})".format(_r=_r))
        return None

    def SetComboAutoGenerate(self, AutoGenerate: bool):
        """This function turns on or off the option to automatically generate code-based design load
        combinations for steel frame design. The function returns zero if the options are
        successfully set; otherwise it returns a nonzero value.
    
        AutoGenerate (input): If this item is True, the option to automatically generate
            code-based design load combinations for steel frame design is turned on. If it
            is False, the option is turned off.
        """
        _r = self._raw.SetComboAutoGenerate(AutoGenerate)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.SetComboAutoGenerate falhou (ret={_r})".format(_r=_r))
        return None

    def SetComboDeflection(self, Name: str, Selected: bool):
        """This function selects or deselects a load combination for steel deflection design. The
        function returns zero if the selection status is successfully set; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing load combination.
        Selected (input): If this item is True, the specified load combination is selected
            as a design combination for steel deflection design. If it is False, the
            combination is not selected for steel deflection design.
        """
        _r = self._raw.SetComboDeflection(Name, Selected)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.SetComboDeflection falhou (ret={_r})".format(_r=_r))
        return None

    def SetComboStrength(self, Name: str, Selected: bool):
        """This function selects or deselects a load combination for steel strength design. The
        function returns zero if the selection status is successfully set; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing load combination.
        Selected (input): If this item is True, the specified load combination is selected
            as a design combination for steel strength design. If it is False, the
            combination is not selected for steel strength design.
        """
        _r = self._raw.SetComboStrength(Name, Selected)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.SetComboStrength falhou (ret={_r})".format(_r=_r))
        return None

    def SetDesignSection(self, Name: str, PropName: str, LastAnalysis: bool, ItemType: int = 0):
        """This function modifies the design section for all specified frame objects that have a steel
        frame design procedure. The function returns zero if the design section is
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
            raise Sap2000ApiError("SapModel.DesignSteel.SetDesignSection falhou (ret={_r})".format(_r=_r))
        return None

    def SetGroup(self, Name: str, Selected: bool):
        """This function selects or deselects a group for steel design. The function returns zero if
        the selection status is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing group.
        Selected (input): If this item is True, the specified group is selected as a design
            group for steel design. If it is False, the group is not selected for steel
            design.
        """
        _r = self._raw.SetGroup(Name, Selected)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.SetGroup falhou (ret={_r})".format(_r=_r))
        return None

    def SetTargetDispl(self, NumberItems: int, LoadCase: list[str], Point: list[str], Displ: list[float], Active: bool = True):
        """This function sets lateral displacement targets for steel design. The function returns zero
        if the targets are successfully set; otherwise it returns a nonzero value.
    
        NumberItems (input): The number of lateral displacement targets specified.
        LoadCase (input): This is an array that includes the name of the static linear load
            case associated with each lateral displacement target.
        Point (input): This is an array that includes the name of the point object
            associated to which the lateral displacement target applies.
        Displ (input): This is an array that includes the lateral displacement target. [L]
        Active (input): If this item is True, all specified lateral displacement targets are
            active. If it is False, they are inactive.
        """
        _r = self._raw.SetTargetDispl(NumberItems, LoadCase, Point, Displ, Active)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.SetTargetDispl falhou (ret={_r})".format(_r=_r))
        return None

    def SetTargetPeriod(self, NumberItems: int, ModalCase: str, Mode: list[int], Period: list[float], Active: bool = True):
        """This function sets time period targets for steel design. The function returns zero if the
        targets are successfully set; otherwise it returns a nonzero value.
    
        NumberItems (input): The number of lateral displacement targets specified.
        ModalCase (input): The name of the modal load case for which the target periods
            apply.
        Mode (input): This is an array that includes the mode number associated with each
            target period.
        Period (input): This is an array that includes the target periods. [s]
        Active (input): If this item is True, all specified target periods are active. If it
            is False, they are inactive.
        """
        _r = self._raw.SetTargetPeriod(NumberItems, ModalCase, Mode, Period, Active)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.SetTargetPeriod falhou (ret={_r})".format(_r=_r))
        return None

    def StartDesign(self):
        """This function starts the steel frame design. The function returns zero if the steel frame
        design is successfully started; otherwise it returns a nonzero value. The function
        will fail if no steel frame objects are present. It will also fail if analysis
        results are not available.
        """
        _r = self._raw.StartDesign()
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.StartDesign falhou (ret={_r})".format(_r=_r))
        return None

    def VerifyPassed(self):
        """This function retrieves the names of the frame objects that did not pass the design check or
        have not yet been checked, if any. The function returns zero if the names are
        successfully retrieved; otherwise it returns a nonzero value.
    
        NumberItems (output): The number of steel frame objects that did not pass the design
            check or have not yet been checked.
        n1 (output): The number of steel frame objects that did not pass the design check.
        n2 (output): The number of steel frame objects that have not yet been checked.
        MyName (output): This is an array that includes the name of each frame object that
            did not pass the design check or has not yet been checked.
        """
        _r = self._raw.VerifyPassed(0, 0, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.VerifyPassed falhou (ret={_ret})".format(_ret=_ret))
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
            raise Sap2000ApiError("SapModel.DesignSteel.VerifySections falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    @cached_property
    def AISC360_05_IBC2006(self):
        return N_DesignSteel_AISC360_05_IBC2006(self._raw.AISC360_05_IBC2006)

    @cached_property
    def AISC360_10(self):
        return N_DesignSteel_AISC360_10(self._raw.AISC360_10)

    @cached_property
    def AISC_ASD01(self):
        return N_DesignSteel_AISC_ASD01(self._raw.AISC_ASD01)

    @cached_property
    def AISC_ASD89(self):
        return N_DesignSteel_AISC_ASD89(self._raw.AISC_ASD89)

    @cached_property
    def AISC_LRFD93(self):
        return N_DesignSteel_AISC_LRFD93(self._raw.AISC_LRFD93)

    @cached_property
    def AISC_LRFD99(self):
        return N_DesignSteel_AISC_LRFD99(self._raw.AISC_LRFD99)

    @cached_property
    def API_RP2A_LRFD97(self):
        return N_DesignSteel_API_RP2A_LRFD97(self._raw.API_RP2A_LRFD97)

    @cached_property
    def API_RP2A_WSD2000(self):
        return N_DesignSteel_API_RP2A_WSD2000(self._raw.API_RP2A_WSD2000)

    @cached_property
    def API_RP2A_WSD2014(self):
        return N_DesignSteel_API_RP2A_WSD2014(self._raw.API_RP2A_WSD2014)

    @cached_property
    def ASCE_10_97(self):
        return N_DesignSteel_ASCE_10_97(self._raw.ASCE_10_97)

    @cached_property
    def Australian_AS4100_1998(self):
        return N_DesignSteel_Australian_AS4100_1998(self._raw.Australian_AS4100_1998)

    @cached_property
    def BS5950_2000(self):
        return N_DesignSteel_BS5950_2000(self._raw.BS5950_2000)

    @cached_property
    def BS5950_90(self):
        return N_DesignSteel_BS5950_90(self._raw.BS5950_90)

    @cached_property
    def CISC_95(self):
        return N_DesignSteel_CISC_95(self._raw.CISC_95)

    @cached_property
    def Canadian_S16_01(self):
        return N_DesignSteel_Canadian_S16_01(self._raw.Canadian_S16_01)

    @cached_property
    def Canadian_S16_09(self):
        return N_DesignSteel_Canadian_S16_09(self._raw.Canadian_S16_09)

    @cached_property
    def Chinese_2010(self):
        return N_DesignSteel_Chinese_2010(self._raw.Chinese_2010)

    @cached_property
    def EUROCODE_3_1993(self):
        return N_DesignSteel_EUROCODE_3_1993(self._raw.EUROCODE_3_1993)

    @cached_property
    def Eurocode_3_2005(self):
        return N_DesignSteel_Eurocode_3_2005(self._raw.Eurocode_3_2005)

    @cached_property
    def INDIAN_IS_800_1998(self):
        return N_DesignSteel_INDIAN_IS_800_1998(self._raw.INDIAN_IS_800_1998)

    @cached_property
    def ITALIAN_UNI_10011(self):
        return N_DesignSteel_ITALIAN_UNI_10011(self._raw.ITALIAN_UNI_10011)

    @cached_property
    def Indian_IS_800_1998(self):
        return N_DesignSteel_Indian_IS_800_1998(self._raw.Indian_IS_800_1998)

    @cached_property
    def Indian_IS_800_2007(self):
        return N_DesignSteel_Indian_IS_800_2007(self._raw.Indian_IS_800_2007)

    @cached_property
    def Italian_NTC_2008(self):
        return N_DesignSteel_Italian_NTC_2008(self._raw.Italian_NTC_2008)

    @cached_property
    def Italian_NTC_2018(self):
        return N_DesignSteel_Italian_NTC_2018(self._raw.Italian_NTC_2018)

    @cached_property
    def Italian_UNI_10011(self):
        return N_DesignSteel_Italian_UNI_10011(self._raw.Italian_UNI_10011)

    @cached_property
    def NewZealand_NZS3404_1997(self):
        return N_DesignSteel_NewZealand_NZS3404_1997(self._raw.NewZealand_NZS3404_1997)

    @cached_property
    def Norsok_N004(self):
        return N_DesignSteel_Norsok_N004(self._raw.Norsok_N004)

    @cached_property
    def Norsok_N0042013(self):
        return N_DesignSteel_Norsok_N0042013(self._raw.Norsok_N0042013)

    @cached_property
    def SP_16_13330_2011(self):
        return N_DesignSteel_SP_16_13330_2011(self._raw.SP_16_13330_2011)

    @cached_property
    def UBC97_ASD(self):
        return N_DesignSteel_UBC97_ASD(self._raw.UBC97_ASD)

    @cached_property
    def UBC97_LRFD(self):
        return N_DesignSteel_UBC97_LRFD(self._raw.UBC97_LRFD)


class N_DesignSteel_Norsok_N004:
    """Wrapper para SapModel.DesignSteel.Norsok_N004."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 36, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, k Major 22 = Moment coefficient,
            k Minor 23 = Bending coefficient, C1 24 = Moment coefficient, kzy 25 = Moment
            coefficient, kyz 26 = Pressure equalized 27 = External pressure 28 = Yield
            stress, Fy 29 = Compressive capacity, Nc.Rd 30 = Tensile capacity, Nt.Rd 31 =
            Major bending capacity, Mc3.Rd 32 = Minor bending capacity, Mc2.Rd 33 = Buckling
            resistance moment, Mb.Rd 34 = Major shear capacity, V2.Rd 35 = Minor shear
            capacity, V3.RD 36 = Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 = As
            specified in preferences 1 = Moment Frame 2 = Braced Frame 2 = Consider
            deflection 0 = Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 =
            Program default 1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value
            Value >= 0; 0 means no check for this item. 5 = SDL + LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 6 = LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 7 = Total load deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 8 = Total camber
            limit, L/Value Value >= 0; 0 means no check for this item. 9 = DL deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 10 = SDL + LL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 11 =
            LL deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 12
            = Total load deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 13 = Total camber limit, absolute Value >= 0; 0 means no check for
            this item. [L] 14 = Specified camber Value >= 0. [L] 15 = Net area to total area
            ratio Value >= 0; 0 means use program default value. 16 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 17 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 18 = Unbraced
            length ratio, Minor Lateral Torsional Buckling Value >= 0; 0 means use program
            determined value. 19 = Effective length factor, K Major Value >= 0; 0 means use
            program determined value. 20 = Effective length factor, K Minor Value >= 0; 0
            means use program determined value. 21 = Moment coefficient, k Major Value >= 0;
            0 means use program determined value. 22 = Moment coefficient, k Minor Value >=
            0; 0 means use program determined value. 23 = Bending coefficient, C1 Value >=
            0; 0 means use program determined value. 24 = Moment coefficient, kzy Value >=
            0; 0 means use program determined value. 25 = Moment coefficient, kyz Value >=
            0; 0 means use program determined value. 26 = Pressure equalized 0 = Program
            Determined 1 = No 2 = Yes 27 = External pressure Any value OK; Positive
            generates hoop compression and negative generates hoop tension. [F/L 2 ] 28 =
            Yield stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 29 =
            Compressive capacity, Nc.Rd Value >= 0; 0 means use program determined value.
            [F] 30 = Tensile capacity, Nt.Rd Value >= 0; 0 means use program determined
            value. [F] 31 = Major bending capacity, Mc3.Rd Value >= 0; 0 means use program
            determined value. [FL] 32 = Minor bending capacity, Mc2.Rd Value >= 0; 0 means
            use program determined value. [FL] 33 = Buckling resistance moment, Mb.Rd Value
            >= 0; 0 means use program determined value. [FL] 34 = Major shear capacity,
            V2.Rd Value >= 0; 0 means use program determined value. [F] 35 = Minor shear
            capacity, V3.RD Value >= 0; 0 means use program determined value. [F] 36 =
            Demand/capacity ratio limit Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Norsok_N004.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 16, inclusive, indicating the
            preference item considered. 1 = Combos equation 2 = K factor method 3 = Pressure
            interaction method 4 = Framing type 5 = GammaM0 6 = GammeM1 7 = GammaM2 8 =
            Consider deflection 9 = DL deflection limit, L/Value 10 = SDL + LL deflection
            limit, L/Value 11 = LL deflection limit, L/Value 12 = Total deflection limit,
            L/Value 13 = Total camber limit, L/Value 14 = Pattern live load factor 15 =
            Demand/capacity ratio limit 16 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Combos equation 1 =
            1 = Eq. 6.10 2 = Max of Eqs. 6.10a and 6.10b 2 = K factor method 1 = Method 1
            (Annex A) 2 = Method 2 (Annex B) 3 = Pressure interaction method 1 = Method A 2
            = Method B 4 = Framing type 1 = Moment Frame 2 = Braced Frame 5 = GammaM0 Value
            > 0 6 = GammeM1 Value > 0 7 = GammeM2 Value > 0 8 = Consider deflection 0 = No
            Any other value = Yes 9 = DL deflection limit, L/Value Value > 0 10 = SDL + LL
            deflection limit, L/Value Value > 0 11 = LL deflection limit, L/Value Value > 0
            12 = Total deflection limit, L/Value Value > 0 13 = Total camber limit, L/Value
            Value > 0 14 = Pattern live load factor Value >= 0 15 = Demand/capacity ratio
            limit Value > 0 16 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3
            = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Norsok_N004.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 36, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, k Major 22 = Moment coefficient,
            k Minor 23 = Bending coefficient, C1 24 = Moment coefficient, kzy 25 = Moment
            coefficient, kyz 26 = Pressure equalized 27 = External pressure 28 = Yield
            stress, Fy 29 = Compressive capacity, Nc.Rd 30 = Tensile capacity, Nt.Rd 31 =
            Major bending capacity, Mc3.Rd 32 = Minor bending capacity, Mc2.Rd 33 = Buckling
            resistance moment, Mb.Rd 34 = Major shear capacity, V2.Rd 35 = Minor shear
            capacity, V3.RD 36 = Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 = As
            specified in preferences 1 = Moment Frame 2 = Braced Frame 2 = Consider
            deflection 0 = Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 =
            Program default 1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value
            Value >= 0; 0 means no check for this item. 5 = SDL + LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 6 = LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 7 = Total load deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 8 = Total camber
            limit, L/Value Value >= 0; 0 means no check for this item. 9 = DL deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 10 = SDL + LL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 11 =
            LL deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 12
            = Total load deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 13 = Total camber limit, absolute Value >= 0; 0 means no check for
            this item. [L] 14 = Specified camber Value >= 0. [L] 15 = Net area to total area
            ratio Value >= 0; 0 means use program default value. 16 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 17 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 18 = Unbraced
            length ratio, Minor Lateral Torsional Buckling Value >= 0; 0 means use program
            determined value. 19 = Effective length factor, K Major Value >= 0; 0 means use
            program determined value. 20 = Effective length factor, K Minor Value >= 0; 0
            means use program determined value. 21 = Moment coefficient, k Major Value >= 0;
            0 means use program determined value. 22 = Moment coefficient, k Minor Value >=
            0; 0 means use program determined value. 23 = Bending coefficient, C1 Value >=
            0; 0 means use program determined value. 24 = Moment coefficient, kzy Value >=
            0; 0 means use program determined value. 25 = Moment coefficient, kyz Value >=
            0; 0 means use program determined value. 26 = Pressure equalized 0 = Program
            Determined 1 = No 2 = Yes 27 = External pressure Any value OK; Positive
            generates hoop compression and negative generates hoop tension. [F/L 2 ] 28 =
            Yield stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 29 =
            Compressive capacity, Nc.Rd Value >= 0; 0 means use program determined value.
            [F] 30 = Tensile capacity, Nt.Rd Value >= 0; 0 means use program determined
            value. [F] 31 = Major bending capacity, Mc3.Rd Value >= 0; 0 means use program
            determined value. [FL] 32 = Minor bending capacity, Mc2.Rd Value >= 0; 0 means
            use program determined value. [FL] 33 = Buckling resistance moment, Mb.Rd Value
            >= 0; 0 means use program determined value. [FL] 34 = Major shear capacity,
            V2.Rd Value >= 0; 0 means use program determined value. [F] 35 = Minor shear
            capacity, V3.RD Value >= 0; 0 means use program determined value. [F] 36 =
            Demand/capacity ratio limit Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Norsok_N004.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 16, inclusive, indicating the
            preference item considered. 1 = Combos equation 2 = K factor method 3 = Pressure
            interaction method 4 = Framing type 5 = GammaM0 6 = GammeM1 7 = GammaM2 8 =
            Consider deflection 9 = DL deflection limit, L/Value 10 = SDL + LL deflection
            limit, L/Value 11 = LL deflection limit, L/Value 12 = Total deflection limit,
            L/Value 13 = Total camber limit, L/Value 14 = Pattern live load factor 15 =
            Demand/capacity ratio limit 16 = Multi-response case design
        Value (input): The value of the considered preference item. 1 = Combos equation 1 =
            1 = Eq. 6.10 2 = Max of Eqs. 6.10a and 6.10b 2 = K factor method 1 = Method 1
            (Annex A) 2 = Method 2 (Annex B) 3 = Pressure interaction method 1 = Method A 2
            = Method B 4 = Framing type 1 = Moment Frame 2 = Braced Frame 5 = GammaM0 Value
            > 0 6 = GammeM1 Value > 0 7 = GammeM2 Value > 0 8 = Consider deflection 0 = No
            Any other value = Yes 9 = DL deflection limit, L/Value Value > 0 10 = SDL + LL
            deflection limit, L/Value Value > 0 11 = LL deflection limit, L/Value Value > 0
            12 = Total deflection limit, L/Value Value > 0 13 = Total camber limit, L/Value
            Value > 0 14 = Pattern live load factor Value >= 0 15 = Demand/capacity ratio
            limit Value > 0 16 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3
            = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Norsok_N004.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_API_RP2A_WSD2000:
    """Wrapper para SapModel.DesignSteel.API_RP2A_WSD2000."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 33, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral TorsionalBuckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, Cm Major 22 = Moment
            coefficient, Cm Minor 23 = Bending coefficient, Cb 24 = Pressure equalized 25 =
            External pressure 26 = Yield stress, Fy 27 = Compressive stress, Fa 28 = Tensile
            stress, Ft 29 = Major bending stress, Fb3 30 = Minor bending stress, Fb2 31 =
            Major shear stress, Fv2 32 = Minor shear stress, Fv3 33 = Demand/capacity ratio
            limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 19
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 22 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 23 = Bending coefficient, Cb Value >= 0; 0 means
            use program determined value. 24 = Pressure equalized 0 = Program Determined 1 =
            No 2 = Yes 25 = External pressure Any value OK; Positive generates hoop
            compression and negative generates hoop tension.. [F/L 2 ] 26 = Yield stress, Fy
            Value >= 0; 0 means use program determined value. [F/L 2 ] 27 = Compressive
            stress, Fa Value >= 0; 0 means use program determined value. [F/L 2 ] 28 =
            Tensile stress, Ft Value >= 0; 0 means use program determined value. [F/L 2 ] 29
            = Major bending stress, Fb3 Value >= 0; 0 means use program determined value.
            [F/L 2 ] 30 = Minor bending stress, Fb2 Value >= 0; 0 means use program
            determined value. [F/L 2 ] 31 = Major shear stress, Fv2 Value >= 0; 0 means use
            program determined value. [F/L 2 ] 32 = Minor shear stress, Fv3 Value >= 0; 0
            means use program determined value. [F/L 2 ] 33 = Demand/capacity ratio limit
            Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.API_RP2A_WSD2000.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Tubular joint punching load
            method 3 = Lateral factor, L/Value 4 = Consider deflection 5 = DL deflection
            limit, L/Value 6 = SDL + LL deflection limit, L/Value 7 = LL deflection limit,
            L/Value 8 = Total deflection limit, L/Value 9 = Total camber limit, L/Value 10 =
            Pattern live load factor 11 = Demand/capacity ratio limit 12 = Multi-response
            case design 13 = Code supplements
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Tubular joint punching load method 1 =
            Punching Shear 2 = Nominal Load 3 = Lateral Factor Value > 0 4 = Consider
            deflection 0 = No Any other value = Yes 5 = DL deflection limit, L/Value Value >
            0 6 = SDL + LL deflection limit, L/Value Value > 0 7 = LL deflection limit,
            L/Value Value > 0 8 = Total deflection limit, L/Value Value > 0 9 = Total camber
            limit, L/Value Value > 0 10 = Pattern live load factor Value >= 0 11 =
            Demand/capacity ratio limit Value > 0 12 = Multi-response case design 1 =
            Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step
            -- All 13 = Code supplements 1 = None 2 = Supplements 2 and 3
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.API_RP2A_WSD2000.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 33, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, Cm Major 22 = Moment
            coefficient, Cm Minor 23 = Bending coefficient, Cb 24 = Pressure equalized 25 =
            External pressure 26 = Yield stress, Fy 27 = Compressive stress, Fa 28 = Tensile
            stress, Ft 29 = Major bending stress, Fb3 30 = Minor bending stress, Fb2 31 =
            Major shear stress, Fv2 32 = Minor shear stress, Fv3 33 = Demand/capacity ratio
            limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 19
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 22 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 23 = Bending coefficient, Cb Value >= 0; 0 means
            use program determined value. 24 = Pressure equalized 0 = Program Determined 1 =
            No 2 = Yes 25 = External pressure Any value OK; Positive generates hoop
            compression and negative generates hoop tension. [F/L 2 ] 26 = Yield stress, Fy
            Value >= 0; 0 means use program determined value. [F/L 2 ] 27 = Compressive
            stress, Fa Value >= 0; 0 means use program determined value. [F/L 2 ] 28 =
            Tensile stress, Ft Value >= 0; 0 means use program determined value. [F/L 2 ] 29
            = Major bending stress, Fb3 Value >= 0; 0 means use program determined value.
            [F/L 2 ] 30 = Minor bending stress, Fb2 Value >= 0; 0 means use program
            determined value. [F/L 2 ] 31 = Major shear stress, Fv2 Value >= 0; 0 means use
            program determined value. [F/L 2 ] 32 = Minor shear stress, Fv3 Value >= 0; 0
            means use program determined value. [F/L 2 ] 33 = Demand/capacity ratio limit
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
            raise Sap2000ApiError("SapModel.DesignSteel.API_RP2A_WSD2000.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Tubular joint punching load
            method 3 = Lateral factor, L/Value 4 = Consider deflection 5 = DL deflection
            limit, L/Value 6 = SDL + LL deflection limit, L/Value 7 = LL deflection limit,
            L/Value 8 = Total deflection limit, L/Value 9 = Total camber limit, L/Value 10 =
            Pattern live load factor 11 = Demand/capacity ratio limit 12 = Multi-response
            case design 13 = Code supplements
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Tubular joint punching load method 1 =
            Punching Shear 2 = Nominal Load 3 = Lateral factor Value > 0 4 = Consider
            deflection 0 = No Any other value = Yes 5 = DL deflection limit, L/Value Value >
            0 6 = SDL + LL deflection limit, L/Value Value > 0 7 = LL deflection limit,
            L/Value Value > 0 8 = Total deflection limit, L/Value Value > 0 9 = Total camber
            limit, L/Value Value >= 0 10 = Pattern live load factor Value >= 0 11 =
            Demand/capacity ratio limit Value > 0 12 = Multi-response case design 1 =
            Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step
            -- All 13 = Code supplements 1 = None 2 = Supplements 2 and 3
        """
        _r = self._raw.SetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.API_RP2A_WSD2000.SetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]


class N_DesignSteel_Indian_IS_800_2007:
    """Wrapper para SapModel.DesignSteel.Indian_IS_800_2007."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 44, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Section class 3 = Column
            buckling curve (z-z) 4 = Column buckling curve (y-y) 5 = Is rolled section 6 =
            Consider deflection 7 = Deflection check type 8 = DL deflection limit, L/Value 9
            = SDL + LL deflection limit, L/Value 10 = LL deflection limit, L/Value 11 =
            Total load deflection limit, L/Value 12 = Total camber limit, L/Value 13 = DL
            deflection limit, absolute 14 = SDL + LL deflection limit, absolute 15 = LL
            deflection limit, absolute 16 = Total load deflection limit, absolute 17 = Total
            camber limit, absolute 18 = Specified camber 19 = Net area to total area ratio
            20 = Live load reduction factor 21 = Unbraced length ratio, Major 22 = Unbraced
            length ratio, Minor 23 = Unbraced length ratio, Lateral Torsional Buckling 24 =
            Effective length factor Braced, K1 Major 25 = Effective length factor Braced, K1
            Minor 26 = Effective length factor Sway, K2 Major 27 = Effective length factor
            Sway, K2 Minor 28 = Effective length factor, K Lateral Torsional Buckling 29 =
            Bending coefficient, C1 30 = Uniform moment factor, Cmz 31 = Uniform moment
            factor, Cmy 32 = Uniform moment factor, CmLT 33 = Moment coefficient, kz 34 =
            Moment coefficient, ky 35 = Moment coefficient, k_LT 36 = Yield stress, Fy 37 =
            Compressive capacity, Pd 38 = Tensile capacity, Td 39 = Major bending capacity,
            Mdz 40 = Minor bending capacity, Mdy 41 = Critical buckling moment, Mcr 42 =
            Major shear capacity, Vdy 43 = Minor shear capacity, Vdz 44 = Demand/capacity
            ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 = As
            specified in preferences 1 = SMF 2 = OMF 3 = SCBF 4 = OCBF 5 = EBF 6 = Secondary
            2 = Section class 1 = Class 1 (Plastic) 2 = Class 2 (Compact) 3 = Class 3
            (Semicompact) 4 = Class 4 (Slender) 3 = Column buckling curve (z-z) 1 = a 2 = b
            3 = c 4 = d 4 = Column buckling curve (y-y) 1 = a 2 = b 3 = c 4 = d 5 = Is
            rolled section Value >= 0; 0 means use program default value 6 = Consider
            deflection 0 = Program Determined 1 = No 2 = Yes 7 = Deflection check type 0 =
            Program default 1 = Ratio 2 = Absolute 3 = Both 8 = DL deflection limit, L/Value
            Value >= 0; 0 means no check for this item. 9 = SDL + LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 10 = LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 11 = Total load deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 12 = Total camber
            limit, L/Value Value >= 0; 0 means no check for this item. 13 = DL deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 14 = SDL + LL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 15 =
            LL deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 16
            = Total load deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 17 = Total camber limit, absolute Value >= 0; 0 means no check for
            this item. [L] 18 = Specified camber Value >= 0. [L] 19 = Net area to total area
            ratio Value >= 0; 0 means use program default value. 20 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 21 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 22 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 23 =
            Unbraced length ratio, Lateral Torsional Buckling Value >= 0; 0 means use
            program determined value. 24 = Effective length factor Braced, K1 Major Value >=
            0; 0 means use program determined value. 25 = Effective length factor Braced, K1
            Minor Value >= 0; 0 means use program determined value. 26 = Effective length
            factor Sway, K2 Major Value >= 0; 0 means use program determined value. 27 =
            Effective length Sway factor, K2 Minor Value >= 0; 0 means use program
            determined value. 28 = Effective length factor, K Lateral Torsional Buckling
            Value >= 0; 0 means use program determined value. 29 = Bending coefficient, C1
            Value >= 0; 0 means use program determined value. 30 = Uniform moment factor,
            Cmz Value >= 0; 0 means use program determined value. 31 = Uniform moment
            factor, Cmy Value >= 0; 0 means use program determined value. 32 = Uniform
            moment factor, CmLT Value >= 0; 0 means use program determined value. 33 =
            Moment coefficient, kz Value >= 0; 0 means use program determined value. 34 =
            Moment coefficient, ky Value >= 0; 0 means use program determined value. 35 =
            Moment coefficient, k_LT Value >= 0; 0 means use program determined value. 36 =
            Yield stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 37 =
            Compressive capacity, Pd Value >= 0; 0 means use program determined value. [F]
            38 = Tensile capacity, Td Value >= 0; 0 means use program determined value. [F]
            39 = Major bending capacity, Mdz Value >= 0; 0 means use program determined
            value. [F-L] 40 = Minor bending capacity, Mdy Value >= 0; 0 means use program
            determined value. [F-L] 41 = Critical buckling moment, Mcr Value >= 0; 0 means
            use program determined value. [F-L] 42 = Major shear capacity, Vdy Value >= 0; 0
            means use program determined value. [F] 43 = Minor shear capacity, Vdz Value >=
            0; 0 means use program determined value. [F] 44 = Demand/capacity ratio limit
            Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True then the specified value is program
            determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Indian_IS_800_2007.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved, otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 18, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Importance factor 3 = Seismic
            Zone 4 = Consider P-delta Done 5 = GammaM0 6 = GammaM1 7 = Ignore sseismic code
            8 = Ignore special seismic load 9 = Is doubler plate plug-welded 10 = Consider
            deflection 11 = DL deflection limit, L/Value 12 = SDL + LL deflection limit,
            L/Value 13 = LL deflection limit, L/Value 14 = Total deflection limit, L/Value
            15 = Total camber limit, L/Value 16 = Pattern live load factor 17 =
            Demand/capacity ratio limit 18 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            SMF 2 = OMF 3 = SCBF 4 = OCBF 5 = EBF 6 = Secondary 2 = Importance factor Value
            > 0 3 = Seismic Zone 1 = Zone I 2 = Zone II 3 = Zone III 4 = Zone IV 5 = Zone V
            4 = Consider P-delta Done 0 = No Any other value = Yes 5 = GammaM0 Value > 0 6 =
            GammaM1 Value > 0 7 = Ignore sseismic code 0 = No Any other value = Yes 8 =
            Ignore special seismic load 0 = No Any other value = Yes 9 = Is doubler plate
            plug-welded 0 = No Any other value = Yes 10 = Consider deflection 0 = No Any
            other value = Yes 11 = DL deflection limit, L/Value Value > 0 12 = SDL + LL
            deflection limit, L/Value Value > 0 13 = LL deflection limit, L/Value Value > 0
            14 = Total deflection limit, L/Value Value > 0 15 = Total camber limit, L/Value
            Value > 0 16 = Pattern live load factor Value >= 0 17 = Demand/capacity ratio
            limit Value > 0 18 = Time history design 1 = Envelopes 2 = Step-by step 3 = Last
            step 4 = Envelopes - All 5 = Step-by step - All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Indian_IS_800_2007.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 44, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Section class 3 = Column
            buckling curve (z-z) 4 = Column buckling curve (y-y) 5 = Is rolled section 6 =
            Consider deflection 7 = Deflection check type 8 = DL deflection limit, L/Value 9
            = SDL + LL deflection limit, L/Value 10 = LL deflection limit, L/Value 11 =
            Total load deflection limit, L/Value 12 = Total camber limit, L/Value 13 = DL
            deflection limit, absolute 14 = SDL + LL deflection limit, absolute 15 = LL
            deflection limit, absolute 16 = Total load deflection limit, absolute 17 = Total
            camber limit, absolute 18 = Specified camber 19 = Net area to total area ratio
            20 = Live load reduction factor 21 = Unbraced length ratio, Major 22 = Unbraced
            length ratio, Minor 23 = Unbraced length ratio, Lateral Torsional Buckling 24 =
            Effective length factor Braced, K1 Major 25 = Effective length factor Braced, K1
            Minor 26 = Effective length factor Sway, K2 Major 27 = Effective length factor
            Sway, K2 Minor 28 = Effective length factor, K Lateral Torsional Buckling 29 =
            Bending coefficient, C1 30 = Uniform moment factor, Cmz 31 = Uniform moment
            factor, Cmy 32 = Uniform moment factor, CmLT 33 = Moment coefficient, kz 34 =
            Moment coefficient, ky 35 = Moment coefficient, k_LT 36 = Yield stress, Fy 37 =
            Compressive capacity, Pd 38 = Tensile capacity, Td 39 = Major bending capacity,
            Mdz 40 = Minor bending capacity, Mdy 41 = Critical buckling moment, Mcr 42 =
            Major shear capacity, Vdy 43 = Minor shear capacity, Vdz 44 = Demand/capacity
            ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 = As
            specified in preferences 1 = SMF 2 = OMF 3 = SCBF 4 = OCBF 5 = EBF 6 = Secondary
            2 = Section class 1 = Class 1 (Plastic) 2 = Class 2 (Compact) 3 = Class 3
            (Semicompact) 4 = Class 4 (Slender) 3 = Column buckling curve (z-z) 1 = a 2 = b
            3 = c 4 = d 4 = Column buckling curve (y-y) 1 = a 2 = b 3 = c 4 = d 5 = Is
            rolled section Value >= 0; 0 means use program default value 6 = Consider
            deflection 0 = Program Determined 1 = No 2 = Yes 7 = Deflection check type 0 =
            Program default 1 = Ratio 2 = Absolute 3 = Both 8 = DL deflection limit, L/Value
            Value >= 0; 0 means no check for this item. 9 = SDL + LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 10 = LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 11 = Total load deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 12 = Total camber
            limit, L/Value Value >= 0; 0 means no check for this item. 13 = DL deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 14 = SDL + LL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 15 =
            LL deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 16
            = Total load deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 17 = Total camber limit, absolute Value >= 0; 0 means no check for
            this item. [L] 18 = Specified camber Value >= 0. [L] 19 = Net area to total area
            ratio Value >= 0; 0 means use program default value. 20 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 21 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 22 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 23 =
            Unbraced length ratio, Lateral Torsional Buckling Value >= 0; 0 means use
            program determined value. 24 = Effective length factor Braced, K1 Major Value >=
            0; 0 means use program determined value. 25 = Effective length factor Braced, K1
            Minor Value >= 0; 0 means use program determined value. 26 = Effective length
            factor Sway, K2 Major Value >= 0; 0 means use program determined value. 27 =
            Effective length Sway factor, K2 Minor Value >= 0; 0 means use program
            determined value. 28 = Effective length factor, K Lateral Torsional Buckling
            Value >= 0; 0 means use program determined value. 29 = Bending coefficient, C1
            Value >= 0; 0 means use program determined value. 30 = Uniform moment factor,
            Cmz Value >= 0; 0 means use program determined value. 31 = Uniform moment
            factor, Cmy Value >= 0; 0 means use program determined value. 32 = Uniform
            moment factor, CmLT Value >= 0; 0 means use program determined value. 33 =
            Moment coefficient, kz Value >= 0; 0 means use program determined value. 34 =
            Moment coefficient, ky Value >= 0; 0 means use program determined value. 35 =
            Moment coefficient, k_LT Value >= 0; 0 means use program determined value. 36 =
            Yield stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 37 =
            Compressive capacity, Pd Value >= 0; 0 means use program determined value. [F]
            38 = Tensile capacity, Td Value >= 0; 0 means use program determined value. [F]
            39 = Major bending capacity, Mdz Value >= 0; 0 means use program determined
            value. [F-L] 40 = Minor bending capacity, Mdy Value >= 0; 0 means use program
            determined value. [F-L] 41 = Critical buckling moment, Mcr Value >= 0; 0 means
            use program determined value. [F-L] 42 = Major shear capacity, Vdy Value >= 0; 0
            means use program determined value. [F] 43 = Minor shear capacity, Vdz Value >=
            0; 0 means use program determined value. [F] 44 = Demand/capacity ratio limit
            Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Indian_IS_800_2007.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set, otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 18, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Importance factor 3 = Seismic
            Zone 4 = Consider P-delta Done 5 = GammaM0 6 = GammaM1 7 = Ignore seismic code 8
            = Ignore special seismic load 9 = Is doubler plate plug-welded 10 = Consider
            deflection 11 = DL deflection limit, L/Value 12 = SDL + LL deflection limit,
            L/Value 13 = LL deflection limit, L/Value 14 = Total deflection limit, L/Value
            15 = Total camber limit, L/Value 16 = Pattern live load factor 17 =
            Demand/capacity ratio limit 18 = Multi-response case design
        Value (input): The value of the considered preference item. The value of the
            considered preference item. 1 = Framing type 1 = SMF 2 = OMF 3 = SCBF 4 = OCBF 5
            = EBF 6 = Secondary 2 = Importance factor Value > 0 3 = Seismic Zone 1 = Zone I
            2 = Zone II 3 = Zone III 4 = Zone IV 5 = Zone V 4 = Consider P-delta Done 0 = No
            Any other value = Yes 5 = GammaM0 Value > 0 6 = GammaM1 Value > 0 7 = Ignore
            sseismic code 0 = No Any other value = Yes 8 = Ignore special seismic load 0 =
            No Any other value = Yes 9 = Is doubler plate plug-welded 0 = No Any other value
            = Yes 10 = Consider deflection 0 = No Any other value = Yes 11 = DL deflection
            limit, L/Value Value > 0 12 = SDL + LL deflection limit, L/Value Value > 0 13 =
            LL deflection limit, L/Value Value > 0 14 = Total deflection limit, L/Value
            Value > 0 15 = Total camber limit, L/Value Value > 0 16 = Pattern live load
            factor Value >= 0 17 = Demand/capacity ratio limit Value > 0 18 = Time history
            design 1 = Envelopes 2 = Step-by step 3 = Last step 4 = Envelopes - All 5 =
            Step-by step - All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Indian_IS_800_2007.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_Chinese_2010:
    """Wrapper para SapModel.DesignSteel.Chinese_2010."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 51, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Element type 3 = Is transfer
            column 4 = Seismic magnification factor 5 = Is rolled section 6 = Is flange edge
            cut by gas 7 = Is both end pinned 8 = Ignore b/t check 9 = Classify beam as
            flexo-compression member 10 = Is beam top loaded 11 = Consider deflection 12 =
            Deflection check type 13 = DL deflection limit, L/Value 14 = SDL + LL deflection
            limit, L/Value 15 = LL deflection limit, L/Value 16 = Total load deflection
            limit, L/Value 17 = Total camber limit, L/Value 18 = DL deflection limit,
            absolute 19 = SDL + LL deflection limit, absolute 20 = LL deflection limit,
            absolute 21 = Total load deflection limit, absolute 22 = Total camber limit,
            absolute 23 = Specified camber 24 = Net area to total area ratio 25 = Live load
            reduction factor 26 = Unbraced length ratio, Major 27 = Unbraced length ratio,
            Minor Lateral Torsional Buckling 28 = Effective length factor, Mue Major 29 =
            Effective length factor, Mue Minor 30 = Moment coefficient, Beta_m Major 31 =
            Moment coefficient, Beta_m Minor 32 = Moment coefficient, Beta_t Major 33 =
            Moment coefficient, Beta_t Minor 34 = Axial stability coefficient, Phi Major 35
            = Axial stability coefficient, Phi Minor 36 = Flexural stability coeff,
            Phi_bMajor 37 = Flexural stability coeff, Phi_bMinor 38 = Plasticity factor,
            Gamma Major 39 = Plasticity factor, Gamma Minor 40 = Section influence
            coefficient, Eta 41 = B/C capacity factor, Eta 42 = Euler moment factor, Delta
            Major 43 = Euler moment factor, Delta Minor 44 = Yield stress, Fy 45 = Allowable
            normal stress, f 46 = Allowable shear stress, fv 47 = Consider fictitious shear
            48 = Demand/capacity ratio limit 49 = Dual system magnification factor 50 = Lo/r
            limit in compression 51 = L/r limit in tension
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 = As
            specified in preferences 1 = Sway Moment Frame, SMF 2 = Concentrically Braced
            Frame, CBF 3 = Eccentrically Braced Frame, EBF 4 = NonSway Moment Frame, NMF 2 =
            Element type 0 = Program Determined 1 = Column 2 = Beam 3 = Brace 4 = Truss 3 =
            Is transfer column 0 = Program Determined 1 = No 2 = Yes 4 = Seismic
            magnification factor Value >= 0; 0 means no check for this item. 5 = Is rolled
            section 0 = Program Determined 1 = No 2 = Yes 6 = Is flange edge cut by gas 0 =
            Program Determined 1 = No 2 = Yes 7 = Is both end pinned 0 = Program Determined
            1 = No 2 = Yes 8 = Ignore b/t check 0 = Program Determined 1 = No 2 = Yes 9 =
            Classify beam as flexo-compression member 0 = Program Determined 1 = No 2 = Yes
            10 = Is beam top loaded 0 = Program Determined 1 = No 2 = Yes 11 = Consider
            deflection 0 = Program Determined 1 = No 2 = Yes 12 = Deflection check type 0 =
            Program default 1 = Ratio 2 = Absolute 3 = Both 13 = DL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 14 = SDL + LL deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 15 = LL deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 16 = Total load
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 17 = Total
            camber limit, L/Value Value >= 0; 0 means no check for this item. 18 = DL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 19 =
            SDL + LL deflection limit, absolute Value >= 0; 0 means no check for this item.
            [L] 20 = LL deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 21 = Total load deflection limit, absolute Value >= 0; 0 means no
            check for this item. [L] 22 = Total camber limit, absolute Value >= 0; 0 means
            no check for this item. [L] 23 = Specified camber Value >= 0. [L] 24 = Net area
            to total area ratio Value >= 0; 0 means use program default value. 25 = Live
            load reduction factor Value >= 0; 0 means use program determined value. 26 =
            Unbraced length ratio, Major Value >= 0; 0 means use program determined value.
            27 = Unbraced length ratio, Minor Lateral Torsional Buckling Value >= 0; 0 means
            use program determined value. 28 = Effective length factor, Mue Major Value >=
            0; 0 means use program determined value. 29 = Effective length factor, Mue Minor
            Value >= 0; 0 means use program determined value. 30 = Moment coefficient,
            Beta_m Major Value >= 0; 0 means use program determined value. 31 = Moment
            coefficient, Beta_m Minor Value >= 0; 0 means use program determined value. 32 =
            Moment coefficient, Beta_t Major Value >= 0; 0 means use program determined
            value. 33 = Moment coefficient, Beta_t Minor Value >= 0; 0 means use program
            determined value. 34 = Axial stability coefficient, Phi Major Value >= 0; 0
            means use program determined value. 35 = Axial stability coefficient, Phi Minor
            Value >= 0; 0 means use program determined value. 36 = Flexural stability
            coefficient, Phi_b Major Value >= 0; 0 means use program determined value. 37 =
            Flexural stability coefficient, Phi_b Minor Value >= 0; 0 means use program
            determined value. 38 = Plasticity factor, Gamma Major Value >= 0; 0 means use
            program determined value. 39 = Plasticity factor, Gamma Minor Value >= 0; 0
            means use program determined value. 40 = Section influence coefficient, Eta
            Value >= 0; 0 means use program determined value. 41 = B/C capacity factor, Eta
            Value >= 0; 0 means use program determined value. 42 = Euler moment factor,
            Delta Major Value >= 0; 0 means use program determined value. 43 = Euler moment
            factor, Delta Minor Value >= 0; 0 means use program determined value. 44 = Yield
            stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 45 =
            Allowable normal stress, f Value >= 0; 0 means use program determined value.
            [F/L 2 ] 46 = Allowable shear stress, fv Value >= 0; 0 means use program
            determined value. [F/L 2 ] 47 = Consider fictitious shear 0 = Program Determined
            1 = No 2 = Yes 48 = Demand/capacity ratio limit Value >= 0; 0 means use program
            determined value. 49 = Dual system magnification factor Value >= 0; 0 means use
            program default value. 50 = Lo/r limit in compression Value >= 0; 0 means use
            program determined value. 51 = L/r limit in tension Value >= 0; 0 means use
            program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Chinese_2010.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 14, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Gamma0 3 = Ignore b/t check 4 =
            Classify beam as flexo compression member 5 = Consider deflection 6 = DL
            deflection limit, L/Value 7 = SDL + LL deflection limit, L/Value 8 = LL
            deflection limit, L/Value 9 = Total load deflection limit, L/Value 10 = Total
            camber limit, L/Value 11 = Pattern live load factor 12 = Demand/capacity ratio
            limit 13 = Multi-response case design 14 = Is tall building? 15 = Seismic Design
            Grade
        Value (output): The value of the considered preference item. 1 = Framing type 0 = As
            specified in preferences 1 = Sway Moment Frame, SMF 2 = Concentrically Braced
            Frame, CBF 3 = Eccentrically Braced Frame, EBF 4 = NonSway Moment Frame, NMF 2 =
            Gamma0 Value > 0 3 = Ignore b/t check 0 = No Any other value = Yes 4 = Classify
            beam as flexo compression member 0 = No Any other value = Yes 5 = Consider
            deflection 0 = No Any other value = Yes 6 = DL deflection limit, L/Value Value >
            0 7 = SDL + LL deflection limit, L/Value Value > 0 8 = LL deflection limit,
            L/Value Value > 0 9 = Total load deflection limit, L/Value Value > 0 10 = Total
            camber limit, L/Value Value > 0 11 = Pattern live load factor Value >= 0 12 =
            Demand/capacity ratio limit Value > 0 13 = Multi-response case design 1 =
            Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step
            -- All 14 = Tall building 0 = No 1 = Yes 15 = Seismic Design Grade 1 = Grade I 2
            = Grade II 3 = Grade III 4 = Grade IV 5 = Non Seismic
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Chinese_2010.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 51, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Element type 3 = Is transfer
            column 4 = Seismic magnification factor 5 = Is rolled section 6 = Is flange edge
            cut by gas 7 = Is both end pinned 8 = Ignore b/t check 9 = Classify beam as
            flexo-compression member 10 = Is beam top loaded 11 = Consider deflection 12 =
            Deflection check type 13 = DL deflection limit, L/Value 14 = SDL + LL deflection
            limit, L/Value 15 = LL deflection limit, L/Value 16 = Total load deflection
            limit, L/Value 17 = Total camber limit, L/Value 18 = DL deflection limit,
            absolute 19 = SDL + LL deflection limit, absolute 20 = LL deflection limit,
            absolute 21 = Total load deflection limit, absolute 22 = Total camber limit,
            absolute 23 = Specified camber 24 = Net area to total area ratio 25 = Live load
            reduction factor 26 = Unbraced length ratio, Major 27 = Unbraced length ratio,
            Minor Lateral TorsionalBuckling 28 = Effective length factor, Mue Major 29 =
            Effective length factor, Mue Minor 30 = Moment coefficient, Beta_m Major 31 =
            Moment coefficient, Beta_m Minor 32 = Moment coefficient, Beta_t Major 33 =
            Moment coefficient, Beta_t Minor 34 = Axial stability coefficient, Phi Major 35
            = Axial stability coefficient, Phi Minor 36 = Flexural stability coeff,
            Phi_bMajor 37 = Flexural stability coeff, Phi_bMinor 38 = Plasticity factor,
            Gamma Major 39 = Plasticity factor, Gamma Minor 40 = Section influence
            coefficient, Eta 41 = B/C capacity factor, Eta 42 = Euler moment factor, Delta
            Major 43 = Euler moment factor, Delta Minor 44 = Yield stress, Fy 45 = Allowable
            normal stress, f 46 = Allowable shear stress, fv 47 = Consider fictitious shear
            48 = Demand/capacity ratio limit 49 = Dual system magnification factor 50 = Lo/r
            limit in compression 51 = L/r limit in tension
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 = As
            specified in preferences 1 = Sway Moment Frame, SMF 2 = Concentrically Braced
            Frame, CBF 3 = Eccentrically Braced Frame, EBF 4 = NonSway Moment Frame, NMF 2 =
            Element type 0 = Program Determined 1 = Column 2 = Beam 3 = Brace 4 = Truss 3 =
            Is transfer column 0 = Program Determined 1 = No 2 = Yes 4 = Seismic
            magnification factor Value >= 0; 0 means no check for this item. 5 = Is rolled
            section 0 = Program Determined 1 = No 2 = Yes 6 = Is flange edge cut by gas 0 =
            Program Determined 1 = No 2 = Yes 7 = Is both end pinned 0 = Program Determined
            1 = No 2 = Yes 8 = Ignore b/t check 0 = Program Determined 1 = No 2 = Yes 9 =
            Classify beam as flexo-compression member 0 = Program Determined 1 = No 2 = Yes
            10 = Is beam top loaded 0 = Program Determined 1 = No 2 = Yes 11 = Consider
            deflection 0 = Program Determined 1 = No 2 = Yes 12 = Deflection check type 0 =
            Program default 1 = Ratio 2 = Absolute 3 = Both 13 = DL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 14 = SDL + LL deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 15 = LL deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 16 = Total load
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 17 = Total
            camber limit, L/Value Value >= 0; 0 means no check for this item. 18 = DL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 19 =
            SDL + LL deflection limit, absolute Value >= 0; 0 means no check for this item.
            [L] 20 = LL deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 21 = Total load deflection limit, absolute Value >= 0; 0 means no
            check for this item. [L] 22 = Total camber limit, absolute Value >= 0; 0 means
            no check for this item. [L] 23 = Specified camber Value >= 0. [L] 24 = Net area
            to total area ratio Value >= 0; 0 means use program default value. 25 = Live
            load reduction factor Value >= 0; 0 means use program determined value. 26 =
            Unbraced length ratio, Major Value >= 0; 0 means use program determined value.
            27 = Unbraced length ratio, Minor Lateral Torsional Buckling Value >= 0; 0 means
            use program determined value. 28 = Effective length factor, Mue Major Value >=
            0; 0 means use program determined value. 29 = Effective length factor, Mue Minor
            Value >= 0; 0 means use program determined value. 30 = Moment coefficient,
            Beta_m Major Value >= 0; 0 means use program determined value. 31 = Moment
            coefficient, Beta_m Minor Value >= 0; 0 means use program determined value. 32 =
            Moment coefficient, Beta_t Major Value >= 0; 0 means use program determined
            value. 33 = Moment coefficient, Beta_t Minor Value >= 0; 0 means use program
            determined value. 34 = Axial stability coefficient, Phi Major Value >= 0; 0
            means use program determined value. 35 = Axial stability coefficient, Phi Minor
            Value >= 0; 0 means use program determined value. 36 = Flexural stability
            coefficient, Phi_b Major Value >= 0; 0 means use program determined value. 37 =
            Flexural stability coefficient, Phi_b Minor Value >= 0; 0 means use program
            determined value. 38 = Plasticity factor, Gamma Major Value >= 0; 0 means use
            program determined value. 39 = Plasticity factor, Gamma Minor Value >= 0; 0
            means use program determined value. 40 = Section influence coefficient, Eta
            Value >= 0; 0 means use program determined value. 41 = B/C capacity factor, Eta
            Value >= 0; 0 means use program determined value. 42 = Euler moment factor,
            Delta Major Value >= 0; 0 means use program determined value. 43 = Euler moment
            factor, Delta Minor Value >= 0; 0 means use program determined value. 44 = Yield
            stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 45 =
            Allowable normal stress, f Value >= 0; 0 means use program determined value.
            [F/L 2 ] 46 = Allowable shear stress, fv Value >= 0; 0 means use program
            determined value. [F/L 2 ] 47 = Consider fictitious shear 0 = Program Determined
            1 = No 2 = Yes 48 = Demand/capacity ratio limit Value >= 0; 0 means use program
            determined value 49 = Dual system magnification factor Value >= 0; 0 means use
            program default value. 50 = Lo/r limit in compression Value >= 0; 0 means use
            program determined value. 51 = L/r limit in tension Value >= 0; 0 means use
            program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects= 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Chinese_2010.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 14, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Gamma0 3 = Ignore b/t check 4 =
            Classify beam as flexo compression member 5 = Consider deflection 6 = DL
            deflection limit, L/Value 7 = SDL + LL deflection limit, L/Value 8 = LL
            deflection limit, L/Value 9 = Total load deflection limit, L/Value 10 = Total
            camber limit, L/Value 11 = Pattern live load factor 12 = Demand/capacity ratio
            limit 13 = Multi-response case design 14 = Is tall building? 15 = Seismic Design
            Grade
        Value (input): The value of the considered preference item. 1 = Framing type 0 = As
            specified in preferences 1 = Sway Moment Frame, SMF 2 = Concentrically Braced
            Frame, CBF 3 = Eccentrically Braced Frame, EBF 4 = NonSway Moment Frame, NMF 2 =
            Gamma0 Value > 0 3 = Ignore b/t check 0 = No Any other value = Yes 4 = Classify
            beam as flexo compression member 0 = No Any other value = Yes 5 = Consider
            deflection 0 = No Any other value = Yes 6 = DL deflection limit, L/Value Value >
            0 7 = SDL + LL deflection limit, L/Value Value > 0 8 = LL deflection limit,
            L/Value Value > 0 9 = Total load deflection limit, L/Value Value > 0 10 = Total
            camber limit, L/Value Value > 0 11 = Pattern live load factor Value >= 0 12 =
            Demand/capacity ratio limit Value > 0 13 = Multi-response case design 1 =
            Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step
            -- All 14 = Tall building 0 = No 1 = Yes 15 = Seismic Design Grade 1 = Grade I 2
            = Grade II 3 = Grade III 4 = Grade IV 5 = Non Seismic
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Chinese_2010.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_Australian_AS4100_1998:
    """Wrapper para SapModel.DesignSteel.Australian_AS4100_1998."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 46, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Steel type 3 = Consider
            deflection 4 = Deflection check type 5 = DL deflection limit, L/Value 6 = SDL +
            LL deflection limit, L/Value 7 = LL deflection limit, L/Value 8 = Total load
            deflection limit, L/Value 9 = Total camber limit, L/Value 10 = DL deflection
            limit, absolute 11 = SDL + LL deflection limit, absolute 12 = LL deflection
            limit, absolute 13 = Total load deflection limit, absolute 14 = Total camber
            limit, absolute 15 = Specified camber 16 = Net area to total area ratio 17 =
            Live load reduction factor 18 = Unbraced length ratio, Major 19 = Unbraced
            length ratio, Minor 20 = Unbraced length ratio, Lateral Torsional Buckling 21 =
            Effective length factor, Ke Major Braced 22 = Effective length factor, Ke Minor
            Braced 23 = Effective length factor, Ke Major Sway 24 = Effective length factor,
            Ke Minor Sway 25 = Twist restraint factor for LTB (kt) 26 = lateral rotation
            restraint factor (kr) 27 = Load height factor for LTB (kl) 28 = Moment
            coefficient, Cm Major 29 = Moment coefficient, Cm Minor 30 = Moment modification
            factor, Alpha_m 31 = Slender reduction factor, Alpha_s 32 = Nonsway moment
            factor, Db Major 33 = Nonsway moment factor, Db Minor 34 = Sway moment factor,
            Ds Major 35 = Sway moment factor, Ds Minor 36 = Form factor, Kf 37 = Axial
            capacity correction factor, Kt 38 = Yield stress, Fy 39 = Compressive capacity,
            Nc 40 = Tensile capacity, Nt 41 = Major bending capacity, Ms33 42 = Minor
            bending capacity, Ms22 43 = Major bending capacity, Mb33 44 = Major shear
            capacity, Vu2 45 = Minor shear capacity, Vu3 46 = Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 = As
            specified in preferences 1 = Moment frame 2 = Braced frame 2 = Steel type 1 =
            Hot rolled 2 = Hot finished 3 = Cold form 4 = Stress relieved 5 = Lightly welded
            6 = Heavily welded 3 = Consider deflection 0 = No Any other value = Yes 4 =
            Deflection check type 0 = Program default 1 = Ratio 2 = Absolute 3 = Both 5 = DL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 6 = SDL +
            LL deflection limit, L/Value Value >= 0; 0 means no check for this item. 7 = LL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 8 = Total
            load deflection limit, L/Value Value >= 0; 0 means no check for this item. 9 =
            Total camber limit, L/Value Value >= 0; 0 means no check for this item. 10 = DL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 11 =
            SDL + LL deflection limit, absolute Value >= 0; 0 means no check for this item.
            [L] 12 = LL deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 13 = Total load deflection limit, absolute Value >= 0; 0 means no
            check for this item. [L]} 14 = Total camber limit, absolute Value >= 0; 0 means
            no check for this item. [L] 15 = Specified camber Value >= 0. [L} 16 = Net area
            to total area ratio Value >= 0; 0 means use program default value. 17 = Live
            load reduction factor Value >= 0; 0 means use program determined value. 18 =
            Unbraced length ratio, Major Value >= 0; 0 means use program determined value.
            19 = Unbraced length ratio, Minor Value >= 0; 0 means use program determined
            value. 20 = Unbraced length ratio, Lateral Torsional Buckling Value >= 0; 0
            means use program determined value. 21 = Effective length factor, Ke Major
            Braced Value >= 0; 0 means use program determined value. 22 = Effective length
            factor, Ke Minor Braced Value >= 0; 0 means use program determined value. 23 =
            Effective length factor, Ke Major Sway Value >= 0; 0 means use program
            determined value. 24 = Effective length factor, Ke Minor Sway Value >= 0; 0
            means use program determined value. 25 = Twist restraint factor for LTB (kt)
            Value >= 0; 0 means use program determined value. 26 = Lateral rotation
            restraint factor (kr) Value >= 0; 0 means use program determined value. 27 =
            Load height factor for LTB (kl) Value >= 0; 0 means use program determined
            value. 28 = Moment coefficient, Cm Major Value >= 0; 0 means use program
            determined value. 29 = Moment coefficient, Cm Minor Value >= 0; 0 means use
            program determined value. 30 = Moment modification factor, Alpha_m Value >= 0; 0
            means use program determined value. 31 = Slender reduction factor, Alpha_s Value
            >= 0; 0 means use program determined value. 32 = Nonsway moment factor, Db Major
            Value >= 0; 0 means use program determined value. 33 = Nonsway moment factor, Db
            Minor Value >= 0; 0 means use program determined value. 34 = Sway moment factor,
            Bs Major Value >= 0; 0 means use program determined value. 35 = Sway moment
            factor, Bs Minor Value >= 0; 0 means use program determined value. 36 = Form
            factor, Kf Value >= 0; 0 means use program determined value. 37 = Axial capacity
            correction factor, Kt Value >= 0; 0 means use program determined value. 38 =
            Yield stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 39 =
            Compressive capacity, Nc Value >= 0; 0 means use program determined value. [F]
            40 = Tensile capacity, Nt Value >= 0; 0 means use program determined value. [F]
            41 = Major bending capacity, Ms33 Value >= 0; 0 means use program determined
            value. [FL] 42 = Minor bending capacity, Ms22 Value >= 0; 0 means use program
            determined value. [FL] 43 = Minor bending capacity, Mb33 Value >= 0; 0 means use
            program determined value. [FL] 44 = Major shear capacity, Vu2 Value >= 0; 0
            means use program determined value. [F] 45 = Minor shear capacity, Vu3 Value >=
            0; 0 means use program determined value. [F] 46 = Demand/capacity ratio limit
            Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True then the specified value is program
            determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Australian_AS4100_1998.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved, otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 17, inclusive, indicating the
            preference item considered. 1 = Multi-response case design 2 = Framing type 3 =
            Structural analysis method 4 = Steel type 5 = Capacity factor, Phi bending 6 =
            Capacity factor, Phi compression 7 = Capacity factor, Phi tension yielding 8 =
            Capacity factor, Phi tension fracture 9 = Capacity factor, Phi shear 10 =
            Consider deflection 11 = DL deflection limit, L/Value 12 = SDL + LL deflection
            limit, L/Value 13 = LL deflection limit, L/Value 14 = Total load deflection
            limit, L/Value 15 = Total camber limit, L/Value 16 = Pattern live load factor 17
            = Demand/capacity ratio limit
        Value (output): The value of the considered preference item. 1 = Multi-response case
            design 1 = Envelopes 2 = Step-by step 3 = Last step 4 = Envelopes - All 5 =
            Step-by step - All 2 = Framing type 1 = Moment frame 2 = Braced frame 3 =
            Structural analysis method 1 = General 2nd Order 2 = Amplified 1st Order 4 =
            Steel type 1 = Hot rolled 2 = Hot finished 3 = Cold form 4 = Stress relieved 5 =
            Lightly welded 6 = Heavily welded 5 = Capacity factor, Phi bending Value > 0 6 =
            Capacity factor, Phi compression Value > 0 7 = Capacity factor, Phi tension
            yielding Value > 0 8 = Capacity factor, Phi tension fracture Value > 0 9 =
            Capacity factor, Phi shear Value > 0 10 = Consider deflection 0 = No Any other
            value = Yes 11 = DL deflection limit, L/Value Value > 0 12 = SDL + LL deflection
            limit, L/Value Value > 0 13 = LL deflection limit, L/Value Value > 0 14 = Total
            load deflection limit, L/Value Value > 0 15 = Total camber limit, L/Value Value
            > 0 16 = Pattern live load factor Value >= 0 17 = Demand/capacity ratio limit
            Value > 0
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Australian_AS4100_1998.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 46, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Steel type 3 = Consider
            deflection 4 = Deflection check type 5 = DL deflection limit, L/Value 6 = SDL +
            LL deflection limit, L/Value 7 = LL deflection limit, L/Value 8 = Total load
            deflection limit, L/Value 9 = Total camber limit, L/Value 10 = DL deflection
            limit, absolute 11 = SDL + LL deflection limit, absolute 12 = LL deflection
            limit, absolute 13 = Total load deflection limit, absolute 14 = Total camber
            limit, absolute 15 = Specified camber 16 = Net area to total area ratio 17 =
            Live load reduction factor 18 = Unbraced length ratio, Major 19 = Unbraced
            length ratio, Minor 20 = Unbraced length ratio, Lateral Torsional Buckling 21 =
            Effective length factor, Ke Major Braced 22 = Effective length factor, Ke Minor
            Braced 23 = Effective length factor, Ke Major Sway 24 = Effective length factor,
            Ke Minor Sway 25 = Twist restraint factor for LTB (kt) 26 = lateral rotation
            restraint factor (kr) 27 = Load height factor for LTB (kl) 28 = Moment
            coefficient, Cm Major 29 = Moment coefficient, Cm Minor 30 = Moment modification
            factor, Alpha_m 31 = Slender reduction factor, Alpha_s 32 = Nonsway moment
            factor, Db Major 33 = Nonsway moment factor, Db Minor 34 = Sway moment factor,
            Ds Major 35 = Sway moment factor, Ds Minor 36 = Form factor, Kf 37 = Axial
            capacity correction factor, Kt 38 = Yield stress, Fy 39 = Compressive capacity,
            Nc 40 = Tensile capacity, Nt 41 = Major bending capacity, Ms33 42 = Minor
            bending capacity, Ms22 43 = Major bending capacity, Mb33 44 = Major shear
            capacity, Vu2 45 = Minor shear capacity, Vu3 46 = Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 = As
            specified in preferences 1 = Moment frame 2 = Braced frame 2 = Steel type 1 =
            Hot rolled 2 = Hot finished 3 = Cold form 4 = Stress relieved 5 = Lightly welded
            6 = Heavily welded 3 = Consider deflection 0 = No Any other value = Yes 4 =
            Deflection check type 0 = Program default 1 = Ratio 2 = Absolute 3 = Both 5 = DL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 6 = SDL +
            LL deflection limit, L/Value Value >= 0; 0 means no check for this item. 7 = LL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 8 = Total
            load deflection limit, L/Value Value >= 0; 0 means no check for this item. 9 =
            Total camber limit, L/Value Value >= 0; 0 means no check for this item. 10 = DL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 11 =
            SDL + LL deflection limit, absolute Value >= 0; 0 means no check for this item.
            [L] 12 = LL deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 13 = Total load deflection limit, absolute Value >= 0; 0 means no
            check for this item. [L]} 14 = Total camber limit, absolute Value >= 0; 0 means
            no check for this item. [L] 15 = Specified camber Value >= 0. [L} 16 = Net area
            to total area ratio Value >= 0; 0 means use program default value. 17 = Live
            load reduction factor Value >= 0; 0 means use program determined value. 18 =
            Unbraced length ratio, Major Value >= 0; 0 means use program determined value.
            19 = Unbraced length ratio, Minor Value >= 0; 0 means use program determined
            value. 20 = Unbraced length ratio, Lateral Torsional Buckling Value >= 0; 0
            means use program determined value. 21 = Effective length factor, Ke Major
            Braced Value >= 0; 0 means use program determined value. 22 = Effective length
            factor, Ke Minor Braced Value >= 0; 0 means use program determined value. 23 =
            Effective length factor, Ke Major Sway Value >= 0; 0 means use program
            determined value. 24 = Effective length factor, Ke Minor Sway Value >= 0; 0
            means use program determined value. 25 = Twist restraint factor for LTB (kt)
            Value >= 0; 0 means use program determined value. 26 = Lateral rotation
            restraint factor (kr) Value >= 0; 0 means use program determined value. 27 =
            Load height factor for LTB (kl) Value >= 0; 0 means use program determined
            value. 28 = Moment coefficient, Cm Major Value >= 0; 0 means use program
            determined value. 29 = Moment coefficient, Cm Minor Value >= 0; 0 means use
            program determined value. 30 = Moment modification factor, Alpha_m Value >= 0; 0
            means use program determined value. 31 = Slender reduction factor, Alpha_s Value
            >= 0; 0 means use program determined value. 32 = Nonsway moment factor, Db Major
            Value >= 0; 0 means use program determined value. 33 = Nonsway moment factor, Db
            Minor Value >= 0; 0 means use program determined value. 34 = Sway moment factor,
            Bs Major Value >= 0; 0 means use program determined value. 35 = Sway moment
            factor, Bs Minor Value >= 0; 0 means use program determined value. 36 = Form
            factor, Kf Value >= 0; 0 means use program determined value. 37 = Axial capacity
            correction factor, Kt Value >= 0; 0 means use program determined value. 38 =
            Yield stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 39 =
            Compressive capacity, Nc Value >= 0; 0 means use program determined value. [F]
            40 = Tensile capacity, Nt Value >= 0; 0 means use program determined value. [F]
            41 = Major bending capacity, Ms33 Value >= 0; 0 means use program determined
            value. [FL] 42 = Minor bending capacity, Ms22 Value >= 0; 0 means use program
            determined value. [FL] 43 = Minor bending capacity, Mb33 Value >= 0; 0 means use
            program determined value. [FL] 44 = Major shear capacity, Vu2 Value >= 0; 0
            means use program determined value. [F] 45 = Minor shear capacity, Vu3 Value >=
            0; 0 means use program determined value. [F] 46 = Demand/capacity ratio limit
            Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Australian_AS4100_1998.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set, otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 17, inclusive, indicating the
            preference item considered. 1 = Multi-response case design 2 = Framing type 3 =
            Structural analysis method 4 = Steel type 5 = Capacity factor, Phi bending 6 =
            Capacity factor, Phi compression 7 = Capacity factor, Phi tension yielding 8 =
            Capacity factor, Phi tension fracture 9 = Capacity factor, Phi shear 10 =
            Consider deflection 11 = DL deflection limit, L/Value 12 = SDL + LL deflection
            limit, L/Value 13 = LL deflection limit, L/Value 14 = Total load deflection
            limit, L/Value 15 = Total camber limit, L/Value 16 = Pattern live load factor 17
            = Demand/capacity ratio limit
        Value (input): The value of the considered preference item. 1 = Multi-response case
            design 1 = Envelopes 2 = Step-by step 3 = Last step 4 = Envelopes - All 5 =
            Step-by step - All 2 = Framing type 1 = Moment frame 2 = Braced frame 3 =
            Structural analysis method 1 = General 2nd Order 2 = Amplified 1st Order 4 =
            Steel type 1 = Hot rolled 2 = Hot finished 3 = Cold form 4 = Stress relieved 5 =
            Lightly welded 6 = Heavily welded 5 = Capacity factor, Phi bending Value > 0 6 =
            Capacity factor, Phi compression Value > 0 7 = Capacity factor, Phi tension
            yielding Value > 0 8 = Capacity factor, Phi tension fracture Value > 0 9 =
            Capacity factor, Phi shear Value > 0 10 = Consider deflection 0 = No Any other
            value = Yes 11 = DL deflection limit, L/Value Value > 0 12 = SDL + LL deflection
            limit, L/Value Value > 0 13 = LL deflection limit, L/Value Value > 0 14 = Total
            load deflection limit, L/Value Value > 0 15 = Total camber limit, L/Value Value
            > 0 16 = Pattern live load factor Value >= 0 17 = Demand/capacity ratio limit
            Value > 0
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Australian_AS4100_1998.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_SP_16_13330_2011:
    """Wrapper para SapModel.DesignSteel.SP_16_13330_2011."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 37, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Section Class 3 = Service
            Factor, GammaC 4 = Service Factor, GammaU 5 = Factor for L-Shapes , GammaC1 6 =
            Column buckling curve major 7 = Column buckling curve minor 8 = Is rolled
            section? 9 = Is beam top loaded? 10 = Consider Deflection 11 = Deflection check
            type 12 = DL deflection limit, L/Value 13 = SDL+LL deflection limit, L/Value 14
            = LL deflection limit, L/Value 15 = Total deflection limit, L/Value 16 = Total-
            camber limit, L/Value 17 = DL deflection limit, absolute 18 = SDL+LL deflection
            limit, absolute 19 = LL deflection limit, absolute 20 = Total deflection limit,
            absolute 21 = Total-camber deflection limit, absolute 22 = Specified camber 23 =
            Net area to total area ratio 24 = Live load reduction factor 25 = Unbraced
            length ratio, Major 26 = Unbraced length ratio, Minor 27 = Unbraced length
            ratio, LTB 28 = Effective length factor, K1 Major 29 = Effective length factor,
            K1 Minor 30 = Effective length factor, K2 Major 31 = Effective length factor, K2
            Minor 32 = Effective length factor, LTB 33 = Characteristic strength, Ryn 34 =
            Design yield strength, Ry 35 = Design fracture strength, Ru 36 = Design shear
            strength, Rs 37 = Demand/capacity ratio, limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Section Class 0 = Program
            Determined 1 = Class 1 2 = Class 2 3 = Class 3 4 = Class 4 3 = Service Factor,
            GammaC Value >= 0; 0 means use program determined value. 4 = Service Factor,
            GammaU Value >= 0; 0 means use program determined value. 5 = Factor for L-Shapes
            , GammaC1 Value >= 0; 0 means use program determined value. 6 = Column buckling
            curve major 0 = Program Determined 1 = a 2 = b 3 = c 7 = Column buckling curve
            minor 0 = Program Determined 1 = a 2 = b 3 = c 8 = Is rolled section? 0 =
            Program Determined 1 = No 2 = Yes 9 = Is beam top loaded? 0 = Program Determined
            1 = No 2 = Yes 10 = Consider Deflection 0 = Program Determined 1 = No 2 = Yes 11
            = Deflection check type 0 = Program Determined 1 = Ratio 2 = Absolute 3 = Both
            12 = DL deflection limit, L/Value Value >= 0; 0 means no check for this item. 13
            = SDL+LL deflection limit, L/Value Value >= 0; 0 means no check for this item.
            14 = LL deflection limit, L/Value Value >= 0; 0 means no check for this item. 15
            = Total deflection limit, L/Value Value >= 0; 0 means no check for this item. 16
            = Total-camber limit, L/Value Value >= 0; 0 means no check for this item. 17 =
            DL deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 18
            = SDL+LL deflection limit, absolute Value >= 0; 0 means no check for this item.
            [L] 19 = LL deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 20 = Total deflection limit, absolute Value >= 0; 0 means no check for
            this item. [L] 21 = Total-camber deflection limit, absolute Value >= 0; 0 means
            no check for this item. [L] 22 = Specified camber Value >= 0. [L] 23 = Net area
            to total area ratio Value >= 0; 0 means use program default value. 24 = Live
            load reduction factor Value >= 0; 0 means use program determined value. 25 =
            Unbraced length ratio, Major Value >= 0; 0 means use program determined value.
            26 = Unbraced length ratio, Minor Value >= 0; 0 means use program determined
            value. 27 = Unbraced length ratio, LTB Value >= 0; 0 means use program
            determined value. 28 = Effective length factor, K1 Major Value >= 0; 0 means use
            program determined value. 29 = Effective length factor, K1 Minor Value >= 0; 0
            means use program determined value. 30 = Effective length factor, K2 Major Value
            >= 0; 0 means use program determined value. 31 = Effective length factor, K2
            Minor Value >= 0; 0 means use program determined value. 32 = Effective length
            factor, LTB Value >= 0; 0 means use program determined value. 33 =
            Characteristic strength, Ryn Value >= 0; 0 means use program determined value.
            [F/L 2 ] 34 = Design yield strength, Ry Value >= 0; 0 means use program
            determined value. [F/L 2 ] 35 = Design fracture strength, Ru Value >= 0; 0 means
            use program determined value. [F/L 2 ] 36 = Design shear strength, Rs Value >=
            0; 0 means use program determined value. [F/L 2 ] 37 = Demand/capacity ratio,
            limit Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.SP_16_13330_2011.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 15, inclusive, indicating the
            preference item considered. 1 = Multi-response case design 2 = Framing type 3 =
            Section class 4 = GammaM 5 = GammaC 6 = GammaU 7 = GammaC1 8 = Consider
            deflection 9 = DL deflection limit, L/Value 10 = SDL + LL deflection limit,
            L/Value 11 = LL deflection limit, L/Value 12 = Total load deflection limit,
            L/Value 13 = Total camber limit, L/Value 14 = Pattern live load factor 15 =
            Demand/capacity ratio limit
        Value (output): The value of the considered preference item. 1 = Multi-response case
            design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 =
            Step-by-step -- All 2 = Framing type 1 = Moment frame 2 = Braced frame 3 =
            Section class 1 = Class 1 2 = Class 2 3 = Class 3 4 = Class 4 4 = GammaM Value >
            0 5 = GammaC Value > 0 6 = GammaU Value > 0 7 = GammaC1 Value > 0 8 = Consider
            deflection 0 = No Any other value = Yes 9 = DL deflection limit, L/Value Value >
            0 10 = SDL + LL deflection limit, L/Value Value > 0 11 = LL deflection limit,
            L/Value Value > 0 12 = Total deflection limit, L/Value Value > 0 13 = Total
            camber limit, L/Value Value > 0 14 = Pattern live load factor Value >= 0 15 =
            Demand/capacity ratio limit Value > 0
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.SP_16_13330_2011.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise, it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 37, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Section Class 3 = Service
            Factor, GammaC 4 = Service Factor, GammaU 5 = Factor for L-Shapes , GammaC1 6 =
            Column buckling curve major 7 = Column buckling curve minor 8 = Is rolled
            section? 9 = Is beam top loaded? 10 = Consider Deflection 11 = Deflection check
            type 12 = DL deflection limit, L/Value 13 = SDL+LL deflection limit, L/Value 14
            = LL deflection limit, L/Value 15 = Total deflection limit, L/Value 16 = Total-
            camber limit, L/Value 17 = DL deflection limit, absolute 18 = SDL+LL deflection
            limit, absolute 19 = LL deflection limit, absolute 20 = Total deflection limit,
            absolute 21 = Total-camber deflection limit, absolute 22 = Specified camber 23 =
            Net area to total area ratio 24 = Live load reduction factor 25 = Unbraced
            length ratio, Major 26 = Unbraced length ratio, Minor 27 = Unbraced length
            ratio, LTB 28 = Effective length factor, K1 Major 29 = Effective length factor,
            K1 Minor 30 = Effective length factor, K2 Major 31 = Effective length factor, K2
            Minor 32 = Effective length factor, LTB 33 = Characteristic strength, Ryn 34 =
            Design yield strength, Ry 35 = Design fracture strength, Ru 36 = Design shear
            strength, Rs 37 = Demand/capacity ratio, limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Section Class 0 = Program
            Determined 1 = Class 1 2 = Class 2 3 = Class 3 4 = Class 4 3 = Service Factor,
            GammaC Value >= 0; 0 means use program determined value. 4 = Service Factor,
            GammaU Value >= 0; 0 means use program determined value. 5 = Factor for L-Shapes
            , GammaC1 Value >= 0; 0 means use program determined value. 6 = Column buckling
            curve major 0 = Program Determined 1 = a 2 = b 3 = c 7 = Column buckling curve
            minor 0 = Program Determined 1 = a 2 = b 3 = c 8 = Is rolled section? 0 =
            Program Determined 1 = No 2 = Yes 9 = Is beam top loaded? 0 = Program Determined
            1 = No 2 = Yes 10 = Consider Deflection 0 = Program Determined 1 = No 2 = Yes 11
            = Deflection check type 0 = Program Determined 1 = Ratio 2 = Absolute 3 = Both
            12 = DL deflection limit, L/Value Value >= 0; 0 means no check for this item. 13
            = SDL+LL deflection limit, L/Value Value >= 0; 0 means no check for this item.
            14 = LL deflection limit, L/Value Value >= 0; 0 means no check for this item. 15
            = Total deflection limit, L/Value Value >= 0; 0 means no check for this item. 16
            = Total-camber limit, L/Value Value >= 0; 0 means no check for this item. 17 =
            DL deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 18
            = SDL+LL deflection limit, absolute Value >= 0; 0 means no check for this item.
            [L] 19 = LL deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 20 = Total deflection limit, absolute Value >= 0; 0 means no check for
            this item. [L] 21 = Total-camber deflection limit, absolute Value >= 0; 0 means
            no check for this item. [L] 22 = Specified camber Value >= 0. [L] 23 = Net area
            to total area ratio Value >= 0; 0 means use program default value. 24 = Live
            load reduction factor Value >= 0; 0 means use program determined value. 25 =
            Unbraced length ratio, Major Value >= 0; 0 means use program determined value.
            26 = Unbraced length ratio, Minor Value >= 0; 0 means use program determined
            value. 27 = Unbraced length ratio, LTB Value >= 0; 0 means use program
            determined value. 28 = Effective length factor, K1 Major Value >= 0; 0 means use
            program determined value. 29 = Effective length factor, K1 Minor Value >= 0; 0
            means use program determined value. 30 = Effective length factor, K2 Major Value
            >= 0; 0 means use program determined value. 31 = Effective length factor, K2
            Minor Value >= 0; 0 means use program determined value. 32 = Effective length
            factor, LTB Value >= 0; 0 means use program determined value. 33 =
            Characteristic strength, Ryn Value >= 0; 0 means use program determined value.
            [F/L 2 ] 34 = Design yield strength, Ry Value >= 0; 0 means use program
            determined value. [F/L 2 ] 35 = Design fracture strength, Ru Value >= 0; 0 means
            use program determined value. [F/L 2 ] 36 = Design shear strength, Rs Value >=
            0; 0 means use program determined value. [F/L 2 ] 37 = Demand/capacity ratio,
            limit Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.SP_16_13330_2011.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 15, inclusive, indicating the
            preference item considered. 1 = Multi-response case design 2 = Framing type 3 =
            Section class 4 = GammaM 5 = GammaC 6 = GammaU 7 = GammaC1 8 = Consider
            deflection 9 = DL deflection limit, L/Value 10 = SDL + LL deflection limit,
            L/Value 11 = LL deflection limit, L/Value 12 = Total load deflection limit,
            L/Value 13 = Total camber limit, L/Value 14 = Pattern live load factor 15 =
            Demand/capacity ratio limit
        Value (input): The value of the considered preference item. 1 = Multi-response case
            design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 =
            Step-by-step -- All 2 = Framing type 1 = Moment frame 2 = Braced frame 3 =
            Section class 1 = Class 1 2 = Class 2 3 = Class 3 4 = Class 4 4 = GammaM Value >
            0 5 = GammaC Value > 0 6 = GammaU Value > 0 7 = GammaC1 Value > 0 8 = Consider
            deflection 0 = No Any other value = Yes 9 = DL deflection limit, L/Value Value >
            0 10 = SDL + LL deflection limit, L/Value Value > 0 11 = LL deflection limit,
            L/Value Value > 0 12 = Total deflection limit, L/Value Value > 0 13 = Total
            camber limit, L/Value Value > 0 14 = Pattern live load factor Value >= 0 15 =
            Demand/capacity ratio limit Value > 0
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.SP_16_13330_2011.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_ASCE_10_97:
    """Wrapper para SapModel.DesignSteel.ASCE_10_97."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 31, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, Cm Major 22 = Moment
            coefficient, Cm Minor 23 = Bending coefficient, Cb 24 = Yield stress, Fy 25 =
            Compressive capacity, Pac 26 = Tensile capacity, Pat 27 = Major bending
            capacity, Ma3 28 = Minor bending capacity, Ma2 29 = Major shear stress, Fv2 30 =
            Minor shear stress, Fv3 31 = Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Brace Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 19
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 22 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 23 = Bending coefficient, Cb Value >= 0; 0 means
            use program determined value. 24 = Yield stress, Fy Value >= 0; 0 means use
            program determined value. [F/L 2 ] 25 = Compressive capacity, Pac Value >= 0; 0
            means use program determined value. [F] 26 = Tensile capacity, Pat Value >= 0; 0
            means use program determined value. [F] 27 = Major bending capacity, Ma3 Value
            >= 0; 0 means use program determined value. [FL] 28 = Minor bending capacity,
            Ma2 Value >= 0; 0 means use program determined value. [FL] 29 = Major shear
            stress, Fv2 Value >= 0; 0 means use program determined value. [F/L 2 ] 30 =
            Minor shear stress, Fv3 Value >= 0; 0 means use program determined value. [F/L 2
            ] 31 = Demand/capacity ratio limit Value >= 0; 0 means use program determined
            value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.ASCE_10_97.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 10, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Consider deflection 3 = DL
            deflection limit, L/Value 4 = SDL + LL deflection limit, L/Value 5 = LL
            deflection limit, L/Value 6 = Total deflection limit, L/Value 7 = Total camber
            limit, L/Value 8 = Pattern live load factor 9 = Demand/capacity ratio limit 10 =
            Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Consider deflection 0 = No Any other value =
            Yes 3 = DL deflection limit, L/Value Value > 0 4 = SDL + LL deflection limit,
            L/Value Value > 0 5 = LL deflection limit, L/Value Value > 0 6 = Total
            deflection limit, L/Value Value > 0 7 = Total camber limit, L/Value Value > 0 8
            = Pattern live load factor Value >= 0 9 = Demand/capacity ratio limit Value > 0
            10 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 =
            Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.ASCE_10_97.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 31, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, Cm Major 22 = Moment
            coefficient, Cm Minor 23 = Bending coefficient, Cb 24 = Yield stress, Fy 25 =
            Compressive capacity, Pac 26 = Tensile capacity, Pat 27 = Major bending
            capacity, Ma3 28 = Minor bending capacity, Ma2 29 = Major shear stress, Fv2 30 =
            Minor shear stress, Fv3 31 = Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Brace Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 19
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 22 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 23 = Bending coefficient, Cb Value >= 0; 0 means
            use program determined value. 24 = Yield stress, Fy Value >= 0; 0 means use
            program determined value. [F/L 2 ] 25 = Compressive capacity, Pac Value >= 0; 0
            means use program determined value. [F] 26 = Tensile capacity, Pat Value >= 0; 0
            means use program determined value. [F] 27 = Major bending capacity, Ma3 Value
            >= 0; 0 means use program determined value. [FL] 28 = Minor bending capacity,
            Ma2 Value >= 0; 0 means use program determined value. [FL] 29 = Major shear
            stress, Fv2 Value >= 0; 0 means use program determined value. [F/L 2 ] 30 =
            Minor shear stress, Fv3 Value >= 0; 0 means use program determined value. [F/L 2
            ] 31 = Demand/capacity ratio limit Value >= 0; 0 means use program determined
            value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.ASCE_10_97.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 10, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Consider deflection 3 = DL
            deflection limit, L/Value 4 = SDL + LL deflection limit, L/Value 5 = LL
            deflection limit, L/Value 6 = Total deflection limit, L/Value 7 = Total camber
            limit, L/Value 8 = Pattern live load factor 9 = Demand/capacity ratio limit 10 =
            Multi-response case design
        Value (input): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Consider deflection 0 = No Any other value =
            Yes 3 = DL deflection limit, L/Value Value > 0 4 = SDL + LL deflection limit,
            L/Value Value > 0 5 = LL deflection limit, L/Value Value > 0 6 = Total
            deflection limit, L/Value Value > 0 7 = Total camber limit, L/Value Value > 0 8
            = Pattern live load factor Value >= 0 9 = Demand/capacity ratio limit Value > 0
            10 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 =
            Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.ASCE_10_97.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_Canadian_S16_01:
    """Wrapper para SapModel.DesignSteel.Canadian_S16_01."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 39, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor LTB
            19 = Unbraced length ratio, Lateral Torsional Buckling 20 = Effective length
            factor, K Major 21 = Effective length factor, K Minor 22 = Effective length
            factor, K LTB 23 = Moment coefficient, Omega1 Major 24 = Moment coefficient,
            Omega1 Minor 25 = Bending coefficient, Omega2 26 = Nonsway moment factor, U1
            Major 27 = Nonsway moment factor, U1 Minor 28 = Sway moment factor, U2 Major 29
            = Sway moment factor, U2 Minor 30 = Parameter for compressive resistance, n 31 =
            Yield stress, Fy 32 = Expected to specified Fy ratio, Ry 33 = Compressive
            resistance, Cr 34 = Tensile resistance, Tr 35 = Major bending resistance, Mr3 36
            = Minor bending resistance, Mr2 37 = Major shear resistance, Vr2 38 = Minor
            shear resistance, Vr3 39 = Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 = As
            specified in preferences 1 = Type LD MRF 2 = Type MD MRF 3 = Type D MRF 4 = Type
            LD CBF(V) 5 = Type LD CBF(TC) 6 = Type LD CBF(TO) 7 = Type LD CBF(OT) 8 = Type
            MD CBF(V) 9 = Type MD CBF(TC) 10 = Type MD CBF(TO) 11 = Type MD CBF(OT) 12 = EBF
            13 = Cantilever Column 14 = Conventional MF 15 = Conventional BF 2 = Consider
            deflection 0 = No Any other value = Yes 3 = Deflection check type 0 = Program
            default 1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value
            >= 0; 0 means no check for this item. 5 = SDL + LL deflection limit, L/Value
            Value >= 0; 0 means no check for this item. 6 = LL deflection limit, L/Value
            Value >= 0; 0 means no check for this item. 7 = Total load deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 8 = Total camber limit,
            L/Value Value >= 0; 0 means no check for this item. 9 = DL deflection limit,
            absolute Value >= 0; 0 means no check for this item. [L] 10 = SDL + LL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 11 =
            LL deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 12
            = Total load deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L]} 13 = Total camber limit, absolute Value >= 0; 0 means no check for
            this item. [L] 14 = Specified camber Value >= 0. [L} 15 = Net area to total area
            ratio Value >= 0; 0 means use program default value. 16 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 17 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 18 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 19 =
            Unbraced length ratio, Lateral Torsional Buckling Value >= 0; 0 means use
            program determined value. 20 = Effective length factor, K Major Value >= 0; 0
            means use program determined value. 21 = Effective length factor, K Minor Value
            >= 0; 0 means use program determined value. 22 = Effective length factor, K LTB
            Value >= 0; 0 means use program determined value. 23 = Moment coefficient,
            Omega1 Major Value >= 0; 0 means use program determined value. 24 = Moment
            coefficient, Omega1 Minor Value >= 0; 0 means use program determined value. 25 =
            Moment coefficient, Omega2 Value >= 0; 0 means use program determined value. 26
            = Nonsway moment factor, U1 Major Value >= 0; 0 means use program determined
            value. 27 = Nonsway moment factor, U1 Minor Value >= 0; 0 means use program
            determined value. 28 = Sway moment factor, U2 Major Value >= 0; 0 means use
            program determined value. 29 = Sway moment factor, U2 Minor Value >= 0; 0 means
            use program determined value. 30 = Parameter for compressive resistance, n Value
            >= 0; 0 means use program determined value. 31 = Yield stress, Fy Value >= 0; 0
            means use program determined value. [F/L 2 ] 32 = Expected to specified Fy
            ratio, Ry Value >= 0; 0 means use program determined value. [F/L 2 ]= 33 =
            Compressive resistance, Cr Value >= 0; 0 means use program determined value. [F]
            34 = Tensile resistance, Tr Value >= 0; 0 means use program determined value.
            [F] 35 = Major bending resistance, Mr3 Value >= 0; 0 means use program
            determined value. [FL] 36 = Minor bending resistance, Mr2 Value >= 0; 0 means
            use program determined value. [FL] 37 = Major shear resistance, Vr2 Value >= 0;
            0 means use program determined value. [F] 38 = Minor shear resistance, Vr3 Value
            >= 0; 0 means use program determined value. [F] 39 = Demand/capacity ratio limit
            Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Canadian_S16_01.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved, otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 21, inclusive, indicating the
            preference item considered. 1 = Multi-response case design 2 = Framing type 3 =
            Spectral Acceleration Ratio, Ie*Fa*Sa(0.2) 4 = Ductility related modification
            factor, Rd 5 = Overstrength related modification factor, Ro 6 = Capacity factor,
            Phi bending 7 = Capacity factor, Phi compression 8 = Capacity factor, Phi
            tension 9 = Capacity factor, Phi shear 10 = Slender section modification 11 =
            Ignore seismic code 12 = Ignore special seismic load 13 = Doubler plate is plug
            welded 14 = Consider deflection 15 = DL deflection limit, L/Value 16 = SDL + LL
            deflection limit, L/Value 17 = LL deflection limit, L/Value 18 = Total load
            deflection limit, L/Value 19 = Total camber limit, L/Value 20 = Pattern live
            load factor 21 = Demand/capacity ratio limit
        Value (output): The value of the considered preference item. 1 = Multi-response case
            design 1 = Envelopes 2 = Step-by step 3 = Last step 4 = Envelopes - All 5 =
            Step-by step - All 2 = Framing type 1 = Type LD MRF 2 = Type MD MRF 3 = Type D
            MRF 4 = Type LD CBF(V) 5 = Type LD CBF(TC) 6 = Type LD CBF(TO) 7 = Type LD
            CBF(OT) 8 = Type MD CBF(V) 9 = Type MD CBF(TC) 10 = Type MD CBF(TO) 11 = Type MD
            CBF(OT) 12 = EBF 13 = Cantilever Column 14 = Conventional MF 15 = Conventional
            BF 3 = Spectral Acceleration Ratio, Ie*Fa*Sa(0.2) Value > 0 4 = Ductility
            related modification factor, Rd Value > 0 5 = Overstrength related modification
            factor, Ro Value > 0 6 = Capacity factor, Phi bending Value > 0 7 = Capacity
            factor, Phi compression Value > 0 8 = Capacity factor, Phi tension Value > 0 9 =
            Capacity factor, Phi shear Value > 0 10 = Slender section modification 1 =
            Modified geometry 2 = modified Fy 11 = Ignore seismic code 0 = No Any other
            value = Yes 12 = Ignore special seismic load 0 = No Any other value = Yes 13 =
            Doubler plate is plug welded 0 = No Any other value = Yes 14 = Consider
            deflection 0 = No Any other value = Yes 15 = DL deflection limit, L/Value Value
            > 0 16 = SDL + LL deflection limit, L/Value Value > 0 17 = LL deflection limit,
            L/Value Value > 0 18 = Total load deflection limit, L/Value Value > 0 19 = Total
            camber limit, L/Value Value > 0 20 = Pattern live load factor Value >= 0 21 =
            Demand/capacity ratio limit Value > 0
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Canadian_S16_01.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 39, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor LTB
            19 = Unbraced length ratio, Lateral Torsional Buckling 20 = Effective length
            factor, K Major 21 = Effective length factor, K Minor 22 = Effective length
            factor, K LTB 23 = Moment coefficient, Omega1 Major 24 = Moment coefficient,
            Omega1 Minor 25 = Bending coefficient, Omega2 26 = Nonsway moment factor, U1
            Major 27 = Nonsway moment factor, U1 Minor 28 = Sway moment factor, U2 Major 29
            = Sway moment factor, U2 Minor 30 = Parameter for compressive resistance, n 31 =
            Yield stress, Fy 32 = Expected to specified Fy ratio, Ry 33 = Compressive
            resistance, Cr 34 = Tensile resistance, Tr 35 = Major bending resistance, Mr3 36
            = Minor bending resistance, Mr2 37 = Major shear resistance, Vr2 38 = Minor
            shear resistance, Vr3 39 = Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 = As
            specified in preferences 1 = Type LD MRF 2 = Type MD MRF 3 = Type D MRF 4 = Type
            LD CBF(V) 5 = Type LD CBF(TC) 6 = Type LD CBF(TO) 7 = Type LD CBF(OT) 8 = Type
            MD CBF(V) 9 = Type MD CBF(TC) 10 = Type MD CBF(TO) 11 = Type MD CBF(OT) 12 = EBF
            13 = Cantilever Column 14 = Conventional MF 15 = Conventional BF 2 = Consider
            deflection 0 = No Any other value = Yes 3 = Deflection check type 0 = Program
            default 1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value
            >= 0; 0 means no check for this item. 5 = SDL + LL deflection limit, L/Value
            Value >= 0; 0 means no check for this item. 6 = LL deflection limit, L/Value
            Value >= 0; 0 means no check for this item. 7 = Total load deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 8 = Total camber limit,
            L/Value Value >= 0; 0 means no check for this item. 9 = DL deflection limit,
            absolute Value >= 0; 0 means no check for this item. [L] 10 = SDL + LL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 11 =
            LL deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 12
            = Total load deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L]} 13 = Total camber limit, absolute Value >= 0; 0 means no check for
            this item. [L] 14 = Specified camber Value >= 0. [L} 15 = Net area to total area
            ratio Value >= 0; 0 means use program default value. 16 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 17 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 18 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 19 =
            Unbraced length ratio, Lateral Torsional Buckling Value >= 0; 0 means use
            program determined value. 20 = Effective length factor, K Major Value >= 0; 0
            means use program determined value. 21 = Effective length factor, K Minor Value
            >= 0; 0 means use program determined value. 22 = Effective length factor, K LTB
            Value >= 0; 0 means use program determined value. 23 = Moment coefficient,
            Omega1 Major Value >= 0; 0 means use program determined value. 24 = Moment
            coefficient, Omega1 Minor Value >= 0; 0 means use program determined value. 25 =
            Moment coefficient, Omega2 Value >= 0; 0 means use program determined value. 26
            = Nonsway moment factor, U1 Major Value >= 0; 0 means use program determined
            value. 27 = Nonsway moment factor, U1 Minor Value >= 0; 0 means use program
            determined value. 28 = Sway moment factor, U2 Major Value >= 0; 0 means use
            program determined value. 29 = Sway moment factor, U2 Minor Value >= 0; 0 means
            use program determined value. 30 = Parameter for compressive resistance, n Value
            >= 0; 0 means use program determined value. 31 = Yield stress, Fy Value >= 0; 0
            means use program determined value. [F/L 2 ] 32 = Expected to specified Fy
            ratio, Ry Value >= 0; 0 means use program determined value. [F/L 2 ]= 33 =
            Compressive resistance, Cr Value >= 0; 0 means use program determined value. [F]
            34 = Tensile resistance, Tr Value >= 0; 0 means use program determined value.
            [F] 35 = Major bending resistance, Mr3 Value >= 0; 0 means use program
            determined value. [FL] 36 = Minor bending resistance, Mr2 Value >= 0; 0 means
            use program determined value. [FL] 37 = Major shear resistance, Vr2 Value >= 0;
            0 means use program determined value. [F] 38 = Minor shear resistance, Vr3 Value
            >= 0; 0 means use program determined value. [F] 39 = Demand/capacity ratio limit
            Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Canadian_S16_01.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set, otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 21, inclusive, indicating the
            preference item considered. 1 = Multi-response case design 2 = Framing type 3 =
            Spectral Acceleration Ratio, Ie*Fa*Sa(0.2) 4 = Ductility related modification
            factor, Rd 5 = Overstrength related modification factor, Ro 6 = Capacity factor,
            Phi bending 7 = Capacity factor, Phi compression 8 = Capacity factor, Phi
            tension 9 = Capacity factor, Phi shear 10 = Slender section modification 11 =
            Ignore seismic code 12 = Ignore special seismic load 13 = Doubler plate is plug
            welded 14 = Consider deflection 15 = DL deflection limit, L/Value 16 = SDL + LL
            deflection limit, L/Value 17 = LL deflection limit, L/Value 18 = Total load
            deflection limit, L/Value 19 = Total camber limit, L/Value 20 = Pattern live
            load factor 21 = Demand/capacity ratio limit
        Value (input): The value of the considered preference item. 1 = Multi-response case
            design 1 = Envelopes 2 = Step-by step 3 = Last step 4 = Envelopes - All 5 =
            Step-by step - All 2 = Framing type 1 = Type LD MRF 2 = Type MD MRF 3 = Type D
            MRF 4 = Type LD CBF(V) 5 = Type LD CBF(TC) 6 = Type LD CBF(TO) 7 = Type LD
            CBF(OT) 8 = Type MD CBF(V) 9 = Type MD CBF(TC) 10 = Type MD CBF(TO) 11 = Type MD
            CBF(OT) 12 = EBF 13 = Cantilever Column 14 = Conventional MF 15 = Conventional
            BF 3 = Spectral Acceleration Ratio, Ie*Fa*Sa(0.2) Value > 0 4 = Ductility
            related modification factor, Rd Value > 0 5 = Overstrength related modification
            factor, Ro Value > 0 6 = Capacity factor, Phi bending Value > 0 7 = Capacity
            factor, Phi compression Value > 0 8 = Capacity factor, Phi tension Value > 0 9 =
            Capacity factor, Phi shear Value > 0 10 = Slender section modification 1 =
            Modified geometry 2 = modified Fy 11 = Ignore seismic code 0 = No Any other
            value = Yes 12 = Ignore special seismic load 0 = No Any other value = Yes 13 =
            Doubler plate is plug welded 0 = No Any other value = Yes 14 = Consider
            deflection 0 = No Any other value = Yes 15 = DL deflection limit, L/Value Value
            > 0 16 = SDL + LL deflection limit, L/Value Value > 0 17 = LL deflection limit,
            L/Value Value > 0 18 = Total load deflection limit, L/Value Value > 0 19 = Total
            camber limit, L/Value Value > 0 20 = Pattern live load factor Value >= 0 21 =
            Demand/capacity ratio limit Value > 0
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Canadian_S16_01.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_EUROCODE_3_1993:
    """Wrapper para SapModel.DesignSteel.EUROCODE_3_1993."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 36, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, k Major 22 = Moment coefficient,
            k Minor 23 = Bending coefficient, C1 24 = Moment coefficient, k Lateral
            Torsional Buckling 25 = Non-sway moment factor 26 = Sway moment factor, Psi
            Major 27 = Sway moment factor, Psi Minor 28 = Yield stress, Fy 29 = Compressive
            capacity, Nc.Rd 30 = Tensile capacity, Nt.Rd 31 = Major bending capacity, Mc3.Rd
            32 = Minor bending capacity, Mc2.Rd 33 = Buckling resistance moment, Mb.Rd 34 =
            Major shear capacity, V2.Rd 35 = Minor shear capacity, V3.RD 36 =
            Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 19
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Moment coefficient, k Major Value >= 0; 0 means use
            program determined value. 22 = Moment coefficient, k Minor Value >= 0; 0 means
            use program determined value. 23 = Bending coefficient, C1 Value >= 0; 0 means
            use program determined value. 24 = Moment coefficient, k Lateral Torsional
            Buckling Value >= 0; 0 means use program determined value. 25 = Non-sway moment
            factor Value >= 0; 0 means use program determined value. 26 = Sway moment
            factor, Psi Major Value >= 0; 0 means use program determined value. 27 = Sway
            moment factor, Psi Minor Value >= 0; 0 means use program determined value. 28 =
            Yield stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 29 =
            Compressive capacity, Nc.Rd Value >= 0; 0 means use program determined value.
            [F] 30 = Tensile capacity, Nt.Rd Value >= 0; 0 means use program determined
            value. [F] 31 = Major bending capacity, Mc3.Rd Value >= 0; 0 means use program
            determined value. [FL] 32 = Minor bending capacity, Mc2.Rd Value >= 0; 0 means
            use program determined value. [FL] 33 = Buckling resistance moment, Mb.Rd Value
            >= 0; 0 means use program determined value. [FL] 34 = Major shear capacity,
            Vn2.Rd Value >= 0; 0 means use program determined value. [F] 35 = Minor shear
            capacity, Vn3.RD Value >= 0; 0 means use program determined value. [F] 36 =
            Demand/capacity ratio limit Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.EUROCODE_3_1993.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = GammaM0 3 = GammeM1 4 =
            Consider deflection 5 = DL deflection limit, L/Value 6 = SDL + LL deflection
            limit, L/Value 7 = LL deflection limit, L/Value 8 = Total deflection limit,
            L/Value 9 = Total camber limit, L/Value 10 = Pattern live load factor 11 =
            Demand/capacity ratio limit 12 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = GammaM0 Value > 0 3 = GammeM1 Value > 0 4 =
            Consider deflection 0 = No Any other value = Yes 5 = DL deflection limit,
            L/Value Value > 0 6 = SDL + LL deflection limit, L/Value Value > 0 7 = LL
            deflection limit, L/Value Value > 0 8 = Total deflection limit, L/Value Value >
            0 9 = Total camber limit, L/Value Value > 0 10 = Pattern live load factor Value
            >= 0 11 = Demand/capacity ratio limit Value > 0 12 = Multi-response case design
            1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-
            step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.EUROCODE_3_1993.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 36, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, k Major 22 = Moment coefficient,
            k Minor 23 = Bending coefficient, C1 24 = Moment coefficient, k Lateral
            Torsional Buckling 25 = Non-sway moment factor 26 = Sway moment factor, Psi
            Major 27 = Sway moment factor, Psi Minor 28 = Yield stress, Fy 29 = Compressive
            capacity, Nc.Rd 30 = Tensile capacity, Nt.Rd 31 = Major bending capacity, Mc3.Rd
            32 = Minor bending capacity, Mc2.Rd 33 = Buckling resistance moment, Mb.Rd 34 =
            Major shear capacity, V2.Rd 35 = Minor shear capacity, V3.RD 36 =
            Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 19
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Moment coefficient, k Major Value >= 0; 0 means use
            program determined value. 22 = Moment coefficient, k Minor Value >= 0; 0 means
            use program determined value. 23 = Bending coefficient, C1 Value >= 0; 0 means
            use program determined value. 24 = Moment coefficient, k Lateral Torsional
            Buckling Value >= 0; 0 means use program determined value. 25 = Non-sway moment
            factor Value >= 0; 0 means use program determined value. 26 = Sway moment
            factor, Psi Major Value >= 0; 0 means use program determined value. 27 = Sway
            moment factor, Psi Minor Value >= 0; 0 means use program determined value. 28 =
            Yield stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 29 =
            Compressive capacity, Nc.Rd Value >= 0; 0 means use program determined value.
            [F] 30 = Tensile capacity, Nt.Rd Value >= 0; 0 means use program determined
            value. [F] 31 = Major bending capacity, Mc3.Rd Value >= 0; 0 means use program
            determined value. [FL] 32 = Minor bending capacity, Mc2.Rd Value >= 0; 0 means
            use program determined value. [FL] 33 = Buckling resistance moment, Mb.Rd Value
            >= 0; 0 means use program determined value. [FL] 34 = Major shear capacity,
            Vn2.Rd Value >= 0; 0 means use program determined value. [F] 35 = Minor shear
            capacity, Vn3.RD Value >= 0; 0 means use program determined value. [F] 36 =
            Demand/capacity ratio limit Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects= 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.EUROCODE_3_1993.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = GammaM0 3 = GammeM1 4 =
            Consider deflection 5 = DL deflection limit, L/Value 6 = SDL + LL deflection
            limit, L/Value 7 = LL deflection limit, L/Value 8 = Total deflection limit,
            L/Value 9 = Total camber limit, L/Value 10 = Pattern live load factor 11 =
            Demand/capacity ratio limit 12 = Multi-response case design
        Value (input): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = GammaM0 Value > 0 3 = GammeM1 Value > 0 4 =
            Consider deflection 0 = No Any other value = Yes 5 = DL deflection limit,
            L/Value Value > 0 6 = SDL + LL deflection limit, L/Value Value > 0 7 = LL
            deflection limit, L/Value Value > 0 8 = Total deflection limit, L/Value Value >
            0 9 = Total camber limit, L/Value Value > 0 10 = Pattern live load factor Value
            >= 0 11 = Demand/capacity ratio limit Value > 0 12 = Multi-response case design
            1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-
            step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.EUROCODE_3_1993.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_AISC_ASD89:
    """Wrapper para SapModel.DesignSteel.AISC_ASD89."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 31, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, Cm Major 22 = Moment
            coefficient, Cm Minor 23 = Bending coefficient, Cb 24 = Yield stress, Fy 25 =
            Compressive stress, Fa 26 = Tensile stress, Ft 27 = Major bending stress, Fb3 28
            = Minor bending stress, Fb2 29 = Major shear stress, Fv2 30 = Minor shear
            stress, Fv3 31 = Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Brace Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 19
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 22 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 23 = Bending coefficient, Cb Value >= 0; 0 means
            use program determined value. 24 = Yield stress, Fy Value >= 0; 0 means use
            program determined value. [F/L 2 ] 25 = Compressive stress, Fa Value >= 0; 0
            means use program determined value. [F/L 2 ] 26 = Tensile stress, Ft Value >= 0;
            0 means use program determined value. [F/L 2 ] 27 = Major bending stress, Fb3
            Value >= 0; 0 means use program determined value. [F/L 2 ] 28 = Minor bending
            stress, Fb2 Value >= 0; 0 means use program determined value. [F/L 2 ] 29 =
            Major shear stress, Fv2 Value >= 0; 0 means use program determined value. [F/L 2
            ] 30 = Minor shear stress, Fv3 Value >= 0; 0 means use program determined value.
            [F/L 2 ] 31 = Demand/capacity ratio limit Value >= 0; 0 means use program
            determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC_ASD89.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Lateral factor 3 = Consider
            deflection 4 = DL deflection limit, L/Value 5 = SDL + LL deflection limit 6 = LL
            deflection limit, L/Value 7 = Total deflection limit, L/Value 8 = Total camber
            limit, L/Value 9 = Pattern live load factor 10 = Demand/capacity ratio limit 11
            = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Lateral factor Value > 0 3 = Consider
            deflection 0 = No Any other value = Yes 4 = DL deflection limit, L/Value Value >
            0 5 = SDL + LL deflection limit Value > 0 6 = LL deflection limit, L/Value Value
            > 0 7 = Total deflection limit, L/Value Value > 0 8 = Total camber limit,
            L/Value Value > 0 9 = Pattern live load factor Value >= 0 10 = Demand/capacity
            ratio limit Value > 0 11 = Multi-response case design 1 = Envelopes 2 = Step-by-
            step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC_ASD89.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 31, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, Cm Major 22 = Moment
            coefficient, Cm Minor 23 = Bending coefficient, Cb 24 = Yield stress, Fy 25 =
            Compressive stress, Fa 26 = Tensile stress, Ft 27 = Major bending stress, Fb3 28
            = Minor bending stress, Fb2 29 = Major shear stress, Fv2 30 = Minor shear
            stress, Fv3 31 = Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Brace Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral TorsionalBuckling Value >= 0; 0 means use program determined value. 19 =
            Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 22 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 23 = Bending coefficient, Cb Value >= 0; 0 means
            use program determined value. 24 = Yield stress, Fy Value >= 0; 0 means use
            program determined value. [F/L 2 ] 25 = Compressive stress, Fa Value >= 0; 0
            means use program determined value. [F/L 2 ] 26 = Tensile stress, Ft Value >= 0;
            0 means use program determined value. [F/L 2 ] 27 = Major bending stress, Fb3
            Value >= 0; 0 means use program determined value. [F/L 2 ] 28 = Minor bending
            stress, Fb2 Value >= 0; 0 means use program determined value. [F/L 2 ] 29 =
            Major shear stress, Fv2 Value >= 0; 0 means use program determined value. [F/L 2
            ] 30 = Minor shear stress, Fv3 Value >= 0; 0 means use program determined value.
            [F/L 2 ] 31 = Demand/capacity ratio limit Value >= 0; 0 means use program
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
            raise Sap2000ApiError("SapModel.DesignSteel.AISC_ASD89.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Lateral factor 3 = Consider
            deflection 4 = DL deflection limit, L/Value 5 = SDL + LL deflection limit 6 = LL
            deflection limit, L/Value 7 = Total deflection limit, L/Value 8 = Total camber
            limit, L/Value 9 = Pattern live load factor 10 = Demand/capacity ratio limit 11
            = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Lateral factor Value > 0 3 = Consider
            deflection 0 = No Any other value = Yes 4 = DL deflection limit, L/Value Value >
            0 5 = SDL + LL deflection limit Value > 0 6 = LL deflection limit, L/Value Value
            > 0 7 = Total deflection limit, L/Value Value > 0 8 = Total camber limit,
            L/Value Value > 0 9 = Pattern live load factor Value >= 0 10 = Demand/capacity
            ratio limit Value > 0 11 = Multi-response case design 1 = Envelopes 2 = Step-by-
            step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC_ASD89.SetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]


class N_DesignSteel_AISC_ASD01:
    """Wrapper para SapModel.DesignSteel.AISC_ASD01."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 32, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Omega0 3 = Consider deflection 4
            = Deflection check type 5 = DL deflection limit, L/Value 6 = SDL + LL deflection
            limit, L/Value 7 = LL deflection limit, L/Value 8 = Total load deflection limit,
            L/Value 9 = Total camber limit, L/Value 10 = DL deflection limit, absolute 11 =
            SDL + LL deflection limit, absolute 12 = LL deflection limit, absolute 13 =
            Total load deflection limit, absolute 14 = Total camber limit, absolute 15 =
            Specified camber 16 = Net area to total area ratio 17 = Live load reduction
            factor 18 = Unbraced length ratio, Major 19 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 20 = Effective length factor, K Major 21 = Effective
            length factor, K Minor 22 = Moment coefficient, Cm Major 23 = Moment
            coefficient, Cm Minor 24 = Bending coefficient, Cb 25 = Yield stress, Fy 26 =
            Compressive stress, Fa 27 = Tensile stress, Ft 28 = Major bending stress, Fb3 29
            = Minor bending stress, Fb2 30 = Major shear stress, Fv2 31 = Minor shear
            stress, Fv3 32 = Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = OMF 2 = IMF 3 = SMF 4 = OCBF 5 = SCBF 6 = EBF 2 = Omega0
            Value >= 0; 0 means use a program determined value. 3 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 4 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 5 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 6 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 7 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 8 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 9 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 10 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 11 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 12 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 13 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 14 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 15 =
            Specified camber Value >= 0. [L] 16 = Net area to total area ratio Value >= 0; 0
            means use program default value. 17 = Live load reduction factor Value >= 0; 0
            means use program determined value. 18 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 19 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 20
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 21 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 22 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 23 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 24 = Bending coefficient, Cb Value >= 0; 0 means
            use program determined value. 25 = Yield stress, Fy Value >= 0; 0 means use
            program determined value. [F/L 2 ] 26 = Compressive stress, Fa Value >= 0; 0
            means use program determined value. [F/L 2 ] 27 = Tensile stress, Ft Value >= 0;
            0 means use program determined value. [F/L 2 ] 28 = Major bending stress, Fb3
            Value >= 0; 0 means use program determined value. [F/L 2 ] 29 = Minor bending
            stress, Fb2 Value >= 0; 0 means use program determined value. [F/L 2 ] 30 =
            Major shear stress, Fv2 Value >= 0; 0 means use program determined value. [F/L 2
            ] 31 = Minor shear stress, Fv3 Value >= 0; 0 means use program determined value.
            [F/L 2 ] 32 = Demand/capacity ratio limit Value >= 0; 0 means use program
            determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC_ASD01.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 14, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Seismic design capacity 3 =
            Ignore seismic code 4 = Ignore special seismic load 5 = Isdoubler plate plug-
            welded 6 = Consider deflection 7 = DL deflection limit, L/Value 8 = SDL + LL
            deflection limit, L/Value 9 = LL deflection limit, L/Value 10 = Total deflection
            limit, L/Value 11 = Total camber limit, L/Value 12 = Pattern live load factor 13
            = Demand/capacity ratio limit 14 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            OMF 2 = IMF 3 = SMF 4 = OCBF 5 = SCBF 6 = EBF 2 = Seismic design capacity 1 = A
            2 = B 3 = C 4 = D 5 = E 6 = F 3 = Ignore seismic code 0 = No Any other value =
            Yes 4 = Ignore special seismic load 0 = No Any other value = Yes 5 = Isdoubler
            plate plug-welded 0 = No Any other value = Yes 6 = Consider deflection 0 = No
            Any other value = Yes 7 = DL DLdeflection limit, L/Value Value > 0 8 = SDL + LL
            deflection limit, L/Value Value > 0 9 = LL deflection limit, L/Value Value > 0
            10 = Total deflection limit, L/Value Value > 0 11 = Total camber limit, L/Value
            Value > 0 12 = Pattern live load factor Value >= 0 13 = Demand/capacity ratio
            limit Value > 0 14 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3
            = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC_ASD01.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 32, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Omega0 3 = Consider deflection 4
            = Deflection check type 5 = DL deflection limit, L/Value 6 = SDL + LL deflection
            limit, L/Value 7 = LL deflection limit, L/Value 8 = Total load deflection limit,
            L/Value 9 = Total camber limit, L/Value 10 = DL deflection limit, absolute 11 =
            SDL + LL deflection limit, absolute 12 = LL deflection limit, absolute 13 =
            Total load deflection limit, absolute 14 = Total camber limit, absolute 15 =
            Specified camber 16 = Net area to total area ratio 17 = Live load reduction
            factor 18 = Unbraced length ratio, Major 19 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 20 = Effective length factor, K Major 21 = Effective
            length factor, K Minor 22 = Moment coefficient, Cm Major 23 = Moment
            coefficient, Cm Minor 24 = Bending coefficient, Cb 25 = Yield stress, Fy 26 =
            Compressive stress, Fa 27 = Tensile stress, Ft 28 = Major bending stress, Fb3 29
            = Minor bending stress, Fb2 30 = Major shear stress, Fv2 31 = Minor shear
            stress, Fv3 32 = Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = OMF 2 = IMF 3 = SMF 4 = OCBF 5 = SCBF 6 = EBF 2 = Omega0
            Value >= 0; 0 means use a program determined value. 3 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 4 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 5 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 6 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 7 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 8 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 9 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 10 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 11 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 12 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 13 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 14 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 15 =
            Specified camber Value >= 0. [L] 16 = Net area to total area ratio Value >= 0; 0
            means use program default value. 17 = Live load reduction factor Value >= 0; 0
            means use program determined value. 18 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 19 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 20
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 21 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 22 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 23 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 24 = Bending coefficient, Cb Value >= 0; 0 means
            use program determined value. 25 = Yield stress, Fy Value >= 0; 0 means use
            program determined value. [F/L 2 ] 26 = Compressive stress, Fa Value >= 0; 0
            means use program determined value. [F/L 2 ] 27 = Tensile stress, Ft Value >= 0;
            0 means use program determined value. [F/L 2 ] 28 = Major bending stress, Fb3
            Value >= 0; 0 means use program determined value. [F/L 2 ] 29 = Minor bending
            stress, Fb2 Value >= 0; 0 means use program determined value. [F/L 2 ] 30 =
            Major shear stress, Fv2 Value >= 0; 0 means use program determined value. [F/L 2
            ] 31 = Minor shear stress, Fv3 Value >= 0; 0 means use program determined value.
            [F/L 2 ] 32 = Demand/capacity ratio limit Value >= 0; 0 means use program
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
            raise Sap2000ApiError("SapModel.DesignSteel.AISC_ASD01.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 14, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Seismic design capacity 3 =
            Ignore seismic code 4 = Ignore special seismic load 5 = Isdoubler plate plug-
            welded 6 = Consider deflection 7 = DL deflection limit, L/Value 8 = SDL + LL
            deflection limit, L/Value 9 = LL deflection limit, L/Value 10 = Total deflection
            limit, L/Value 11 = Total camber limit, L/Value 12 = Pattern live load factor 13
            = Demand/capacity ratio limit 14 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            OMF 2 = IMF 3 = SMF 4 = OCBF 5 = SCBF 6 = EBF 2 = Seismic design capacity 1 = A
            2 = B 3 = C 4 = D 5 = E 6 = F 3 = Ignore seismic code 0 = No Any other value =
            Yes 4 = Ignore special seismic load 0 = No Any other value = Yes 5 = Is doubler
            plate plug-welded 0 = No Any other value = Yes 6 = Consider deflection 0 = No
            Any other value = Yes 7 = DL DLdeflection limit, L/Value Value > 0 8 = SDL + LL
            deflection limit, L/Value Value > 0 9 = LL deflection limit, L/Value Value > 0
            10 = Total deflection limit, L/Value Value > 0 11 = Total camber limit, L/Value
            Value > 0 12 = Pattern live load factor Value >= 0 13 = Demand/capacity ratio
            limit Value > 0 14 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3
            = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC_ASD01.SetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]


class N_DesignSteel_INDIAN_IS_800_1998:
    """Wrapper para SapModel.DesignSteel.INDIAN_IS_800_1998."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 34, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor 19 =
            Unbraced length ratio, Lateral Torsional Buckling 20 = Effective length factor,
            K Major 21 = Effective length factor, K Minor 22 = Effective length factor, K
            Lateral Torsional Buckling 23 = Moment coefficient, Cm Major 24 = Moment
            coefficient, Cm Minor 25 = Yield stress, Fy 26 = Allowable compressive stress,
            Sigma_ac 27 = Allowable tensile stress, Sigma_at 28 = Allowable major bending
            stress, Sigma_bc33 29 = Allowable minor bending stress, Sigma_bc22 30 = Major
            average shear stress, Tau_va2 31 = Minor average shear stress, Tau_va3 32 =
            Maximum elastic shear stress, Tau_vm 33 = Allowable effective stress, Sigma_e 34
            = Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway Frame 2 = Nonsway Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 19 = Unbraced length ratio, Lateral
            Torsional Buckling Value >= 0; 0 means use program determined value. 20 =
            Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 21 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 22 = Effective length factor, K Lateral Torsional Buckling
            Value >= 0; 0 means use program determined value. 23 = Moment coefficient, Cm
            Major Value >= 0; 0 means use program determined value. 24 = Moment coefficient,
            Cm Minor Value >= 0; 0 means use program determined value. 25 = Yield stress, Fy
            Value >= 0; 0 means use program determined value. [F/L 2 ] 26 = Allowable
            compressive stress, Sigma_ac Value >= 0; 0 means use program determined value.
            [F/L 2 ] 27 = Allowable tensile stress, Sigma_at Value >= 0; 0 means use program
            determined value. [F/L 2 ] 28 = Allowable major bending stress, Sigma_bc33 Value
            >= 0; 0 means use program determined value. [F/L 2 ] 29 = Allowable minor
            bending stress, Sigma_bc22 Value >= 0; 0 means use program determined value.
            [F/L 2 ] 30 = Major average shear stress, Tau_va2 Value >= 0; 0 means use
            program determined value. [F/L 2 ] 31 = Minor average shear stress, Tau_va3
            Value >= 0; 0 means use program determined value. [F/L 2 ] 32 = Maximum elastic
            shear stress, Tau_vm Value >= 0; 0 means use program determined value. [F/L 2 ]
            33 = Allowable effective stress, Sigma_e Value >= 0; 0 means use program
            determined value. [F/L 2 ] 34 = Demand/capacity ratio limit Value >= 0; 0 means
            use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.INDIAN_IS_800_1998.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 34, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor 19 =
            Unbraced length ratio, Lateral Torsional Buckling 20 = Effective length factor,
            K Major 21 = Effective length factor, K Minor 22 = Effective length factor, K
            Lateral Torsional Buckling 23 = Moment coefficient, Cm Major 24 = Moment
            coefficient, Cm Minor 25 = Yield stress, Fy 26 = Allowable compressive stress,
            Sigma_ac 27 = Allowable tensile stress, Sigma_at 28 = Allowable major bending
            stress, Sigma_bc33 29 = Allowable minor bending stress, Sigma_bc22 30 = Major
            average shear stress, Tau_va2 31 = Minor average shear stress, Tau_va3 32 =
            Maximum elastic shear stress, Tau_vm 33 = Allowable effective stress, Sigma_e 34
            = Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway Frame 2 = Nonsway Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 19 = Unbraced length ratio, Lateral
            Torsional Buckling Value >= 0; 0 means use program determined value. 20 =
            Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 21 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 22 = Effective length factor, K Lateral Torsional Buckling
            Value >= 0; 0 means use program determined value. 23 = Moment coefficient, Cm
            Major Value >= 0; 0 means use program determined value. 24 = Moment coefficient,
            Cm Minor Value >= 0; 0 means use program determined value. 25 = Yield stress, Fy
            Value >= 0; 0 means use program determined value. [F/L 2 ] 26 = Allowable
            compressive stress, Sigma_ac Value >= 0; 0 means use program determined value.
            [F/L 2 ] 27 = Allowable tensile stress, Sigma_at Value >= 0; 0 means use program
            determined value. [F/L 2 ] 28 = Allowable major bending stress, Sigma_bc33 Value
            >= 0; 0 means use program determined value. [F/L 2 ] 29 = Allowable minor
            bending stress, Sigma_bc22 Value >= 0; 0 means use program determined value.
            [F/L 2 ] 30 = Major average shear stress, Tau_va2 Value >= 0; 0 means use
            program determined value. [F/L 2 ] 31 = Minor average shear stress, Tau_va3
            Value >= 0; 0 means use program determined value. [F/L 2 ] 32 = Maximum elastic
            shear stress, Tau_vm Value >= 0; 0 means use program determined value. [F/L 2 ]
            33 = Allowable effective stress, Sigma_e Value >= 0; 0 means use program
            determined value. [F/L 2 ] 34 = Demand/capacity ratio limit Value >= 0; 0 means
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
            raise Sap2000ApiError("SapModel.DesignSteel.INDIAN_IS_800_1998.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_ITALIAN_UNI_10011:
    """Wrapper para SapModel.DesignSteel.ITALIAN_UNI_10011."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 26, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Axial load amplification(Omega)
            3 = Consider deflection 4 = Deflection check type 5 = DL deflection limit,
            L/Value 6 = SDL + LL deflection limit, L/Value 7 = LL deflection limit, L/Value
            8 = Total load deflection limit, L/Value 9 = Total camber limit, L/Value 10 = DL
            deflection limit, absolute 11 = SDL + LL deflection limit, absolute 12 = LL
            deflection limit, absolute 13 = Total load deflection limit, absolute 14 = Total
            camber limit, absolute 15 = Specified camber 16 = Net area to total area ratio
            17 = Live load reduction factor 18 = Unbraced length ratio, Major 19 = Unbraced
            length ratio, Minor Lateral Torsional Buckling 20 = Effective length factor,
            Beta Major 21 = Effective length factor, Beta Minor 22 = Moment coefficient,
            Meq/Mmax Major 23 = Moment coefficient, Meq/Mmax Minor 24 = LTB moment
            coefficient (Omega1) 25 = Yield stress, Fy 26 = Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway Frame 2 = NonSway Frame 2 = Axial load
            amplification(Omega) Value >= 0; 0 means use a program determined value. 3 =
            Consider deflection 0 = Program Determined 1 = No 2 = Yes 4 = Deflection check
            type 0 = Program default 1 = Ratio 2 = Absolute 3 = Both 5 = DL deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 6 = SDL + LL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 7 = LL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 8 = Total
            load deflection limit, L/Value Value >= 0; 0 means no check for this item. 9 =
            Total camber limit, L/Value Value >= 0; 0 means no check for this item. 10 = DL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 11 =
            SDL + LL deflection limit, absolute Value >= 0; 0 means no check for this item.
            [L] 12 = LL deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 13 = Total load deflection limit, absolute Value >= 0; 0 means no
            check for this item. [L] 14 = Total camber limit, absolute Value >= 0; 0 means
            no check for this item. [L] 15 = Specified camber Value >= 0. [L] 16 = Net area
            to total area ratio Value >= 0; 0 means use program default value. 17 = Live
            load reduction factor Value >= 0; 0 means use program determined value. 18 =
            Unbraced length ratio, Major Value >= 0; 0 means use program determined value.
            19 = Unbraced length ratio, Minor Lateral Torsional Buckling Value >= 0; 0 means
            use program determined value. 20 = Effective length factor, Beta Major Value >=
            0; 0 means use program determined value. 21 = Effective length factor, Beta
            Minor Value >= 0; 0 means use program determined value. 22 = Moment coefficient,
            Meq/Mmax Major Value >= 0; 0 means use program determined value. 23 = Moment
            coefficient, Meq/Mmax Minor Value >= 0; 0 means use program determined value. 24
            = LTB moment coefficient (Omega1) Value >= 0; 0 means use program determined
            value. 25 = Yield stress, Fy Value >= 0; 0 means use program determined value.
            [F/L 2 ] 26 = Demand/capacity ratio limit Value >= 0; 0 means use program
            determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.ITALIAN_UNI_10011.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 26, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Axial load amplification(Omega)
            3 = Consider deflection 4 = Deflection check type 5 = DL deflection limit,
            L/Value 6 = SDL + LL deflection limit, L/Value 7 = LL deflection limit, L/Value
            8 = Total load deflection limit, L/Value 9 = Total camber limit, L/Value 10 = DL
            deflection limit, absolute 11 = SDL + LL deflection limit, absolute 12 = LL
            deflection limit, absolute 13 = Total load deflection limit, absolute 14 = Total
            camber limit, absolute 15 = Specified camber 16 = Net area to total area ratio
            17 = Live load reduction factor 18 = Unbraced length ratio, Major 19 = Unbraced
            length ratio, Minor Lateral TorsionalBuckling 20 = Effective length factor, Beta
            Major 21 = Effective length factor, Beta Minor 22 = Moment coefficient, Meq/Mmax
            Major 23 = Moment coefficient, Meq/Mmax Minor 24 = LTB moment coefficient
            (Omega1) 25 = Yield stress, Fy 26 = Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Sway Frame 2 = NonSway Frame 2 = Axial load
            amplification(Omega) Value >= 0; 0 means use a program determined value. 3 =
            Consider deflection 0 = Program Determined 1 = No 2 = Yes 4 = Deflection check
            type 0 = Program default 1 = Ratio 2 = Absolute 3 = Both 5 = DL deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 6 = SDL + LL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 7 = LL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 8 = Total
            load deflection limit, L/Value Value >= 0; 0 means no check for this item. 9 =
            Total camber limit, L/Value Value >= 0; 0 means no check for this item. 10 = DL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 11 =
            SDL + LL deflection limit, absolute Value >= 0; 0 means no check for this item.
            [L] 12 = LL deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 13 = Total load deflection limit, absolute Value >= 0; 0 means no
            check for this item. [L] 14 = Total camber limit, absolute Value >= 0; 0 means
            no check for this item. [L] 15 = Specified camber Value >= 0. [L] 16 = Net area
            to total area ratio Value >= 0; 0 means use program default value. 17 = Live
            load reduction factor Value >= 0; 0 means use program determined value. 18 =
            Unbraced length ratio, Major Value >= 0; 0 means use program determined value.
            19 = Unbraced length ratio, Minor Lateral TorsionalBuckling Value >= 0; 0 means
            use program determined value. 20 = Effective length factor, Beta Major Value >=
            0; 0 means use program determined value. 21 = Effective length factor, Beta
            Minor Value >= 0; 0 means use program determined value. 22 = Moment coefficient,
            Meq/Mmax Major Value >= 0; 0 means use program determined value. 23 = Moment
            coefficient, Meq/Mmax Minor Value >= 0; 0 means use program determined value. 24
            = LTB moment coefficient (Omega1) Value >= 0; 0 means use program determined
            value. 25 = Yield stress, Fy Value >= 0; 0 means use program determined value.
            [F/L 2 ] 26 = Demand/capacity ratio limit Value >= 0; 0 means use program
            determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjectst, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.ITALIAN_UNI_10011.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_BS5950_2000:
    """Wrapper para SapModel.DesignSteel.BS5950_2000."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 32, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Uniform moment factor, m Major 22 = Uniform moment
            factor, m Minor 23 = Eqv. uniform moment factor, mLT 24 = Yield stress, Fy 25 =
            Compressive capacity, Pc 26 = Tensile capacity, Pt 27 = Major bending capacity,
            Mc3 28 = Minor bending capacity, Mc2 29 = Buckling resistance moment, Mb 30 =
            Major shear capacity, Pv2 31 = Minor shear capacity, Pv3 32 = Demand/capacity
            ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 19
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Uniform moment factor, m Major Value >= 0; 0 means use
            program determined value. 22 = Uniform moment factor, m Minor Value >= 0; 0
            means use program determined value. 23 = Eqv. Uniform moment factor, mLT Value
            >= 0; 0 means use program determined value. 24 = Yield stress, Fy Value >= 0; 0
            means use program determined value. [F/L 2 ] 25 = Compressive capacity, Pc Value
            >= 0; 0 means use program determined value. [F] 26 = Tensile capacity, Pt Value
            >= 0; 0 means use program determined value. [F] 27 = Major bending capacity, Mc3
            Value >= 0; 0 means use program determined value. [FL] 28 = Minor bending
            capacity, Mc2 Value >= 0; 0 means use program determined value. [FL] 29 =
            Buckling resistance moment, Mb Value >= 0; 0 means use program determined value.
            [FL] 30 = Major shear capacity, Pv2 Value >= 0; 0 means use program determined
            value. [F] 31 = Minor shear capacity, Pv3 Value >= 0; 0 means use program
            determined value. [F] 32 = Demand/capacity ratio limit Value >= 0; 0 means use
            program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.BS5950_2000.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 10, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Consider deflection 3 = DL
            deflection limit, L/Value 4 = SDL + LL deflection limit, L/Value 5 = LL
            deflection limit, L/Value 6 = Total deflection limit, L/Value 7 = Total camber
            limit, L/Value 8 = Pattern live load factor 9 = Demand/capacity ratio limit 10 =
            Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Consider deflection 0 = No Any other value =
            Yes 3 = DL deflection limit, L/Value Value > 0 4 = SDL + LL deflection limit,
            L/Value Value > 0 5 = LL deflection limit, L/Value Value > 0 6 = Total
            deflection limit, L/Value Value > 0 7 = Total camber limit, L/Value Value > 0 8
            = Pattern live load factor Value >= 0 9 = Demand/capacity ratio limit Value > 0
            10 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 =
            Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.BS5950_2000.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 32, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Uniform moment factor, m Major 22 = Uniform moment
            factor, m Minor 23 = Eqv. uniform moment factor, mLT 24 = Yield stress, Fy 25 =
            Compressive capacity, Pc 26 = Tensile capacity, Pt 27 = Major bending capacity,
            Mc3 28 = Minor bending capacity, Mc2 29 = Buckling resistance moment, Mb 30 =
            Major shear capacity, Pv2 31 = Minor shear capacity, Pv3 32 = Demand/capacity
            ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 19
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Uniform moment factor, m Major Value >= 0; 0 means use
            program determined value. 22 = Uniform moment factor, m Minor Value >= 0; 0
            means use program determined value. 23 = Eqv. Uniform moment factor, mLT Value
            >= 0; 0 means use program determined value. 24 = Yield stress, Fy Value >= 0; 0
            means use program determined value. [F/L 2 ] 25 = Compressive capacity, Pc Value
            >= 0; 0 means use program determined value. [F] 26 = Tensile capacity, Pt Value
            >= 0; 0 means use program determined value. [F] 27 = Major bending capacity, Mc3
            Value >= 0; 0 means use program determined value. [FL] 28 = Minor bending
            capacity, Mc2 Value >= 0; 0 means use program determined value. [FL] 29 =
            Buckling resistance moment, Mb Value >= 0; 0 means use program determined value.
            [FL] 30 = Major shear capacity, Pv2 Value >= 0; 0 means use program determined
            value. [F] 31 = Minor shear capacity, Pv3 Value >= 0; 0 means use program
            determined value. [F] 32 = Demand/capacity ratio limit Value >= 0; 0 means use
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
            raise Sap2000ApiError("SapModel.DesignSteel.BS5950_2000.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 10, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Consider deflection 3 = DL
            deflection limit, L/Value 4 = SDL + LL deflection limit, L/Value 5 = LL
            deflection limit, L/Value 6 = Total deflection limit, L/Value 7 = Total camber
            limit, L/Value 8 = Pattern live load factor 9 = Demand/capacity ratio limit 10 =
            Multi-response case design
        Value (input): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Consider deflection 0 = No Any other value =
            Yes 3 = DL deflection limit, L/Value Value > 0 4 = SDL + LL deflection limit,
            L/Value Value > 0 5 = LL deflection limit, L/Value Value > 0 6 = Total
            deflection limit, L/Value Value > 0 7 = Total camber limit, L/Value Value > 0 8
            = Pattern live load factor Value >= 0 9 = Demand/capacity ratio limit Value > 0
            10 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 =
            Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.BS5950_2000.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_AISC360_05_IBC2006:
    """Wrapper para SapModel.DesignSteel.AISC360_05_IBC2006."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 43, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Omega0 3 = Consider deflection 4
            = Deflection check type 5 = DL deflection limit, L/Value 6 = SDL + LL deflection
            limit, L/Value 7 = LL deflection limit, L/Value 8 = Total load deflection limit,
            L/Value 9 = Total camber limit, L/Value 10 = DL deflection limit, absolute 11 =
            SDL + LL deflection limit, absolute 12 = LL deflection limit, absolute 13 =
            Total load deflection limit, absolute 14 = Total camber limit, absolute 15 =
            Specified camber 16 = Net area to total area ratio 17 = Live load reduction
            factor 18 = Unbraced length ratio, Major 19 = Unbraced length ratio, Minor 20 =
            Unbraced length ratio, Lateral Torsional Buckling 21 = Effective length factor,
            K1 Major 22 = Effective length factor, K1 Minor 23 = Effective length factor, K2
            Major 24 = Effective length factor, K2 Minor 25 = Effective length factor, K
            Lateral Torsional Buckling 26 = Moment coefficient, Cm Major 27 = Moment
            coefficient, Cm Minor 28 = Bending coefficient, Cb 29 = Nonsway moment factor,
            B1 Major 30 = Nonsway moment factor, B1 Minor 31 = Sway moment factor, B2 Major
            32 = Sway moment factor, B2 Minor 33 = Reduce HSS thickness 34 = HSS welding
            type 35 = Yield stress, Fy 36 = Expected to specified Fy ratio, Ry 37 =
            Compressive capacity, Pnc 38 = Tensile capacity, Pnt 39 = Major bending
            capacity, Mn3 40 = Minor bending capacity, Mn2 41 = Major shear capacity, Vn2 42
            = Minor shear capacity, Vn3 43 = Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = SMF 2 = IMF 3 = OMF 4 = SCBF 5 = OCBF 6 = OCBFI 7 = EBF 2 =
            Omega0 Value >= 0; 0 means use a program determined value. 3 = Consider
            deflection 0 = Program default 1 = No 2 = Yes 4 = Deflection check type 0 =
            Program default 1 = Ratio 2 = Absolute 3 = Both 5 = DL deflection limit, L/Value
            Value >= 0; 0 means no check for this item. 6 = SDL + LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 7 = LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 8 = Total load deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 9 = Total camber
            limit, L/Value Value >= 0; 0 means no check for this item. 10 = DL deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 11 = SDL + LL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 12 =
            LL deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 13
            = Total load deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L]} 14 = Total camber limit, absolute Value >= 0; 0 means no check for
            this item. [L] 15 = Specified camber Value >= 0. [L} 16 = Net area to total area
            ratio Value >= 0; 0 means use program default value. 17 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 18 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 19 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 20 =
            Unbraced length ratio, Lateral Torsional Buckling Value >= 0; 0 means use
            program determined value. 21 = Effective length factor, K1 Major Value >= 0; 0
            means use program determined value. 22 = Effective length factor, K1 Minor Value
            >= 0; 0 means use program determined value. 23 = Effective length factor, K2
            Major Value >= 0; 0 means use program determined value. 24 = Effective length
            factor, K2 Minor Value >= 0; 0 means use program determined value. 25 =
            Effective length factor, K Lateral Torsional Buckling Value >= 0; 0 means use
            program determined value. 26 = Moment coefficient, Cm Major Value >= 0; 0 means
            use program determined value. 27 = Moment coefficient, Cm Minor Value >= 0; 0
            means use program determined value. 28 = Bending coefficient, Cb Value >= 0; 0
            means use program determined value. 29 = Nonsway moment factor, B1 Major Value
            >= 0; 0 means use program determined value. 30 = Nonsway moment factor, B1 Minor
            Value >= 0; 0 means use program determined value. 31 = Sway moment factor, B2
            Major Value >= 0; 0 means use program determined value. 32 = Sway moment factor,
            B2 Minor Value >= 0; 0 means use program determined value. 33 = Reduce HSS
            thickness 0 = Program default 1 = No 2 = Yes 34 = HSS welding type 0 = Program
            default 1 = ERW 2 = SAW 35 = Yield stress, Fy Value >= 0; 0 means use program
            determined value. [F/L 2 ] 36 = Expected to specified Fy ratio, Ry Value >= 0; 0
            means use program determined value. 37 = Compressive capacity, Pnc Value >= 0; 0
            means use program determined value. [F] 38 = Tensile capacity, Pnt Value >= 0; 0
            means use program determined value. [F] 39 = Major bending capacity, Mn3 Value
            >= 0; 0 means use program determined value. [FL] 40 = Minor bending capacity,
            Mn2 Value >= 0; 0 means use program determined value. [FL] 41 = Major shear
            capacity, Vn2 Value >= 0; 0 means use program determined value. [F] 42 = Minor
            shear capacity, Vn3 Value >= 0; 0 means use program determined value. [F] 43 =
            Demand/capacity ratio limit Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC360_05_IBC2006.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 26, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Seismic design category 3 =
            Design provision 4 = Analysis method (Obsolete, replaced by 27, 28, and 29) 5 =
            Notional load coefficient 6 = Phi bending 7 = Phi compression 8 = Phi tension
            yielding 9 = Phi tension fracture 10 = Phi shear 11 = Phi shear sort webbed
            rolled I 12 = Phi torsion 13 = Ignore seismic code 14 = Ignore special seismic
            load 15 = Doubler plate is plug welded 16 = HSS welding type 17 = Reduce HSS
            thickness 18 = Consider deflection 19 = DL deflection limit, L/Value 20 = SDL +
            LL deflection limit, L/Value 21 = LL deflection limit, L/Value 22 = Total load
            deflection limit, L/Value 23 = Total camber limit, L/Value 24 = Pattern live
            load factor 25 = Demand/capacity ratio limit 26 = Multi-response case design 27
            = Analysis Method 28 = Second Order Method 29 = Stiffness Reduction Method 30 =
            Importance Factor 31 = Design Systems Rho 32 = Design Systems Sds 33 = Design
            Systems R 34 = Design Systems Omega0 35 = Design Systems Cd
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            SMF 2 = IMF 3 = OMF 4 = SCBF 5 = OCBF 6 = OCBFI 7 = EBF 2 = Seismic design
            category 1 = A 2 = B 3 = C 4 = D 5 = E 6 = F 3 = Design provision 1 = LRFD 2 =
            ASD 4 = Analysis method (Obsolete, replaced by 27, 28, and 29) 1 = Gen 2nd Order
            Elastic 2 = 2nd Order By Amp 1st Order 3 = Limited 1st Order Elastic 4 = DAM Gen
            2nd Order Taub Variable 5 = DAM Gen 2nd Order Taub Fixed 6 = DAM Amp 1st Order
            Taub Variable 7 = DAM Amp 1st Order Taub Fixed 5 = Notional load coefficient
            Value > 0 6 = Phi bending Value > 0 7 = Phi compression Value > 0 8 = Phi
            tension yielding Value > 0 9 = Phi tension fracture Value > 0 10 = Phi shear
            Value > 0 11 = Phi shear sort webbed rolled I Value > 0 12 = Phi torsion Value >
            0 13 = Ignore seismic code 0 = No Any other value = Yes 14 = Ignore special
            seismic load 0 = No Any other value = Yes 15 = Doubler plate is plug welded 0 =
            No Any other value = Yes 16 = HSS welding type 1 = ERW 2 = SAW 17 = Reduce HSS
            thickness 0 = No Any other value = Yes 18 = Consider deflection 0 = No Any other
            value = Yes 19 = DL deflection limit, L/Value Value > 0 20 = SDL + LL deflection
            limit, L/Value Value > 0 21 = LL deflection limit, L/Value Value > 0 22 = Total
            load deflection limit, L/Value Value > 0 23 = Total camber limit, L/Value Value
            > 0 24 = Pattern live load factor Value >= 0 25 = Demand/capacity ratio limit
            Value > 0 26 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 =
            Last step 4 = Envelopes -- All 5 = Step-by-step -- All 27 = Analysis Method 1 =
            Direct Analysis 2 = Effective Length 3 = Limited 1st Order 28 = Second Order
            Method 1 = General 2nd Order 2 = Amplified 1st Order 29 = Stiffness Reduction
            Method 1 = Tau-b variable 2 = Tau-b Fixed 3 = No Modification 30 = Importance
            Factor Value > 0 31 = Design System Rho Value > 0 32 = Design System Sds Value
            >= 0 33 = Design System R Value > 0 34 = Design System Omega0 Value > 0 35 =
            Design System Cd Value > 0
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC360_05_IBC2006.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 43, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Omega0 3 = Consider deflection 4
            = Deflection check type 5 = DL deflection limit, L/Value 6 = SDL + LL deflection
            limit, L/Value 7 = LL deflection limit, L/Value 8 = Total load deflection limit,
            L/Value 9 = Total camber limit, L/Value 10 = DL deflection limit, absolute 11 =
            SDL + LL deflection limit, absolute 12 = LL deflection limit, absolute 13 =
            Total load deflection limit, absolute 14 = Total camber limit, absolute 15 =
            Specified camber 16 = Net area to total area ratio 17 = Live load reduction
            factor 18 = Unbraced length ratio, Major 19 = Unbraced length ratio, Minor 20 =
            Unbraced length ratio, Lateral Torsional Buckling 21 = Effective length factor,
            K1 Major 22 = Effective length factor, K1 Minor 23 = Effective length factor, K2
            Major 24 = Effective length factor, K2 Minor 25 = Effective length factor, K
            Lateral Torsional Buckling 26 = Moment coefficient, Cm Major 27 = Moment
            coefficient, Cm Minor 28 = Bending coefficient, Cb 29 = Nonsway moment factor,
            B1 Major 30 = Nonsway moment factor, B1 Minor 31 = Sway moment factor, B2 Major
            32 = Sway moment factor, B2 Minor 33 = Reduce HSS thickness 34 = HSS welding
            type 35 = Yield stress, Fy 36 = Expected to specified Fy ratio, Ry 37 =
            Compressive capacity, Pnc 38 = Tensile capacity, Pnt 39 = Major bending
            capacity, Mn3 40 = Minor bending capacity, Mn2 41 = Major shear capacity, Vn2 42
            = Minor shear capacity, Vn3 43 = Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = SMF 2 = IMF 3 = OMF 4 = SCBF 5 = OCBF 6 = OCBFI 7 = EBF 2 =
            Omega0 Value >= 0; 0 means use a program determined value. 3 = Consider
            deflection 0 = Program default 1 = No 2 = Yes 4 = Deflection check type 0 =
            Program default 1 = Ratio 2 = Absolute 3 = Both 5 = DL deflection limit, L/Value
            Value >= 0; 0 means no check for this item. 6 = SDL + LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 7 = LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 8 = Total load deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 9 = Total camber
            limit, L/Value Value >= 0; 0 means no check for this item. 10 = DL deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 11 = SDL + LL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 12 =
            LL deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 13
            = Total load deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L]} 14 = Total camber limit, absolute Value >= 0; 0 means no check for
            this item. [L] 15 = Specified camber Value >= 0. [L} 16 = Net area to total area
            ratio Value >= 0; 0 means use program default value. 17 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 18 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 19 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 20 =
            Unbraced length ratio, Lateral Torsional Buckling Value >= 0; 0 means use
            program determined value. 21 = Effective length factor, K1 Major Value >= 0; 0
            means use program determined value. 22 = Effective length factor, K1 Minor Value
            >= 0; 0 means use program determined value. 23 = Effective length factor, K2
            Major Value >= 0; 0 means use program determined value. 24 = Effective length
            factor, K2 Minor Value >= 0; 0 means use program determined value. 25 =
            Effective length factor, K Lateral Torsional Buckling Value >= 0; 0 means use
            program determined value. 26 = Moment coefficient, Cm Major Value >= 0; 0 means
            use program determined value. 27 = Moment coefficient, Cm Minor Value >= 0; 0
            means use program determined value. 28 = Bending coefficient, Cb Value >= 0; 0
            means use program determined value. 29 = Nonsway moment factor, B1 Major Value
            >= 0; 0 means use program determined value. 30 = Nonsway moment factor, B1 Minor
            Value >= 0; 0 means use program determined value. 31 = Sway moment factor, B2
            Major Value >= 0; 0 means use program determined value. 32 = Sway moment factor,
            B2 Minor Value >= 0; 0 means use program determined value. 33 = Reduce HSS
            thickness 0 = Program default 1 = No 2 = Yes 34 = HSS welding type 0 = Program
            default 1 = ERW 2 = SAW 35 = Yield stress, Fy Value >= 0; 0 means use program
            determined value. [F/L 2 ] 36 = Expected to specified Fy ratio, Ry Value >= 0; 0
            means use program determined value. 37 = Compressive capacity, Pnc Value >= 0; 0
            means use program determined value. [F] 38 = Tensile capacity, Pnt Value >= 0; 0
            means use program determined value. [F] 39 = Major bending capacity, Mn3 Value
            >= 0; 0 means use program determined value. [FL] 40 = Minor bending capacity,
            Mn2 Value >= 0; 0 means use program determined value. [FL] 41 = Major shear
            capacity, Vn2 Value >= 0; 0 means use program determined value. [F] 42 = Minor
            shear capacity, Vn3 Value >= 0; 0 means use program determined value. [F] 43 =
            Demand/capacity ratio limit Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC360_05_IBC2006.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 26, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Seismic design category 3 =
            Design provision 4 = Analysis method (Obsolete, replaced by 27, 28, and 29) 5 =
            Notional load coefficient 6 = Phi bending 7 = Phi compression 8 = Phi tension
            yielding 9 = Phi tension fracture 10 = Phi shear 11 = Phi shear sort webbed
            rolled I 12 = Phi torsion 13 = Ignore seismic code 14 = Ignore special seismic
            load 15 = Doubler plate is plug welded 16 = HSS welding type 17 = Reduce HSS
            thickness 18 = Consider deflection 19 = DL deflection limit, L/Value 20 = SDL +
            LL deflection limit, L/Value 21 = LL deflection limit, L/Value 22 = Total load
            deflection limit, L/Value 23 = Total camber limit, L/Value 24 = Pattern live
            load factor 25 = Demand/capacity ratio limit 26 = Multi-response case design 27
            = Analysis Method 28 = Second Order Method 29 = Stiffness Reduction Method 30 =
            Importance Factor 31 = Design Systems Rho 32 = Design Systems Sds 33 = Design
            Systems R 34 = Design Systems Omega0 35 = Design Systems Cd
        Value (input): The value of the considered preference item. 1 = Framing type 1 = SMF
            2 = IMF 3 = OMF 4 = SCBF 5 = OCBF 6 = OCBFI 7 = EBF 2 = Seismic design category
            1 = A 2 = B 3 = C 4 = D 5 = E 6 = F 3 = Design provision 1 = LRFD 2 = ASD 4 =
            Analysis method (Obsolete, replaced by 27, 28, and 29) 1 = Gen 2nd Order Elastic
            2 = 2nd Order By Amp 1st Order 3 = Limited 1st Order Elastic 4 = DAM Gen 2nd
            Order Taub Variable 5 = DAM Gen 2nd Order Taub Fixed 6 = DAM Amp 1st Order Taub
            Variable 7 = DAM Amp 1st Order Taub Fixed 5 = Notional load coefficient Value >
            0 6 = Phi bending Value > 0 7 = Phi compression Value > 0 8 = Phi tension
            yielding Value > 0 9 = Phi tension fracture Value > 0 10 = Phi shear Value > 0
            11 = Phi shear sort webbed rolled I Value > 0 12 = Phi torsion Value > 0 13 =
            Ignore seismic code 0 = No Any other value = Yes 14 = Ignore special seismic
            load 0 = No Any other value = Yes 15 = Doubler plate is plug welded 0 = No Any
            other value = Yes 16 = HSS welding type 1 = ERW 2 = SAW 17 = Reduce HSS
            thickness 0 = No Any other value = Yes 18 = Consider deflection 0 = No Any other
            value = Yes 19 = DL deflection limit, L/Value Value > 0 20 = SDL + LL deflection
            limit, L/Value Value > 0 21 = LL deflection limit, L/Value Value > 0 22 = Total
            load deflection limit, L/Value Value > 0 23 = Total camber limit, L/Value Value
            > 0 24 = Pattern live load factor Value >= 0 25 = Demand/capacity ratio limit
            Value > 0 26 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 =
            Last step 4 = Envelopes -- All 5 = Step-by-step -- All 27 = Analysis Method 1 =
            Direct Analysis 2 = Effective Length 3 = Limited 1st Order 28 = Second Order
            Method 1 = General 2nd Order 2 = Amplified 1st Order 29 = Stiffness Reduction
            Method 1 = Tau-b variable 2 = Tau-b Fixed 3 = No Modification 30 = Importance
            Factor Value > 0 31 = Design System Rho Value > 0 32 = Design System Sds Value
            >= 0 33 = Design System R Value > 0 34 = Design System Omega0 Value > 0 35 =
            Design System Cd Value > 0
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC360_05_IBC2006.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_AISC360_10:
    """Wrapper para SapModel.DesignSteel.AISC360_10."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 43, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Omega0 3 = Consider deflection 4
            = Deflection check type 5 = DL deflection limit, L/Value 6 = SDL + LL deflection
            limit, L/Value 7 = LL deflection limit, L/Value 8 = Total load deflection limit,
            L/Value 9 = Total camber limit, L/Value 10 = DL deflection limit, absolute 11 =
            SDL + LL deflection limit, absolute 12 = LL deflection limit, absolute 13 =
            Total load deflection limit, absolute 14 = Total camber limit, absolute 15 =
            Specified camber 16 = Net area to total area ratio 17 = Live load reduction
            factor 18 = Unbraced length ratio, Major 19 = Unbraced length ratio, Minor 20 =
            Unbraced length ratio, Lateral Torsional Buckling 21 = Effective length factor,
            K1 Major 22 = Effective length factor, K1 Minor 23 = Effective length factor, K2
            Major 24 = Effective length factor, K2 Minor 25 = Effective length factor, K
            Lateral Torsional Buckling 26 = Moment coefficient, Cm Major 27 = Moment
            coefficient, Cm Minor 28 = Bending coefficient, Cb 29 = Nonsway moment factor,
            B1 Major 30 = Nonsway moment factor, B1 Minor 31 = Sway moment factor, B2 Major
            32 = Sway moment factor, B2 Minor 33 = Reduce HSS thickness 34 = HSS welding
            type 35 = Yield stress, Fy 36 = Expected to specified Fy ratio, Ry 37 =
            Compressive capacity, Pnc 38 = Tensile capacity, Pnt 39 = Major bending
            capacity, Mn3 40 = Minor bending capacity, Mn2 41 = Major shear capacity, Vn2 42
            = Minor shear capacity, Vn3 43 = Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = SMF 2 = IMF 3 = OMF 4 = SCBF 5 = OCBF 6 = OCBFI 7 = EBF 2 =
            Omega0 Value >= 0; 0 means use a program determined value. 3 = Consider
            deflection 0 = Program default 1 = No 2 = Yes 4 = Deflection check type 0 =
            Program default 1 = Ratio 2 = Absolute 3 = Both 5 = DL deflection limit, L/Value
            Value >= 0; 0 means no check for this item. 6 = SDL + LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 7 = LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 8 = Total load deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 9 = Total camber
            limit, L/Value Value >= 0; 0 means no check for this item. 10 = DL deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 11 = SDL + LL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 12 =
            LL deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 13
            = Total load deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L]} 14 = Total camber limit, absolute Value >= 0; 0 means no check for
            this item. [L] 15 = Specified camber Value >= 0. [L} 16 = Net area to total area
            ratio Value >= 0; 0 means use program default value. 17 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 18 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 19 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 20 =
            Unbraced length ratio, Lateral Torsional Buckling Value >= 0; 0 means use
            program determined value. 21 = Effective length factor, K1 Major Value >= 0; 0
            means use program determined value. 22 = Effective length factor, K1 Minor Value
            >= 0; 0 means use program determined value. 23 = Effective length factor, K2
            Major Value >= 0; 0 means use program determined value. 24 = Effective length
            factor, K2 Minor Value >= 0; 0 means use program determined value. 25 =
            Effective length factor, K Lateral Torsional Buckling Value >= 0; 0 means use
            program determined value. 26 = Moment coefficient, Cm Major Value >= 0; 0 means
            use program determined value. 27 = Moment coefficient, Cm Minor Value >= 0; 0
            means use program determined value. 28 = Bending coefficient, Cb Value >= 0; 0
            means use program determined value. 29 = Nonsway moment factor, B1 Major Value
            >= 0; 0 means use program determined value. 30 = Nonsway moment factor, B1 Minor
            Value >= 0; 0 means use program determined value. 31 = Sway moment factor, B2
            Major Value >= 0; 0 means use program determined value. 32 = Sway moment factor,
            B2 Minor Value >= 0; 0 means use program determined value. 33 = Reduce HSS
            thickness 0 = Program default 1 = No 2 = Yes 34 = HSS welding type 0 = Program
            default 1 = ERW 2 = SAW 35 = Yield stress, Fy Value >= 0; 0 means use program
            determined value. [F/L 2 ] 36 = Expected to specified Fy ratio, Ry Value >= 0; 0
            means use program determined value. 37 = Compressive capacity, Pnc Value >= 0; 0
            means use program determined value. [F] 38 = Tensile capacity, Pnt Value >= 0; 0
            means use program determined value. [F] 39 = Major bending capacity, Mn3 Value
            >= 0; 0 means use program determined value. [FL] 40 = Minor bending capacity,
            Mn2 Value >= 0; 0 means use program determined value. [FL] 41 = Major shear
            capacity, Vn2 Value >= 0; 0 means use program determined value. [F] 42 = Minor
            shear capacity, Vn3 Value >= 0; 0 means use program determined value. [F] 43 =
            Demand/capacity ratio limit Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC360_10.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 26, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Seismic design category 3 =
            Design provision 4 = Analysis method (Obsolete, replaced by 27, 28, and 29) 5 =
            Notional load coefficient 6 = Phi bending 7 = Phi compression 8 = Phi tension
            yielding 9 = Phi tension fracture 10 = Phi shear 11 = Phi shear sort webbed
            rolled I 12 = Phi torsion 13 = Ignore seismic code 14 = Ignore special seismic
            load 15 = Doubler plate is plug welded 16 = HSS welding type 17 = Reduce HSS
            thickness 18 = Consider deflection 19 = DL deflection limit, L/Value 20 = SDL +
            LL deflection limit, L/Value 21 = LL deflection limit, L/Value 22 = Total load
            deflection limit, L/Value 23 = Total camber limit, L/Value 24 = Pattern live
            load factor 25 = Demand/capacity ratio limit 26 = Multi-response case design 27
            = Analysis Method 28 = Second Order Method 29 = Stiffness Reduction Method 30 =
            Importance Factor 31 = Design Systems Rho 32 = Design Systems Sds 33 = Design
            Systems R 34 = Design Systems Omega0 35 = Design Systems Cd
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            SMF 2 = IMF 3 = OMF 4 = SCBF 5 = OCBF 6 = OCBFI 7 = EBF 2 = Seismic design
            category 1 = A 2 = B 3 = C 4 = D 5 = E 6 = F 3 = Design provision 1 = LRFD 2 =
            ASD 4 = Analysis method (Obsolete, replaced by 27, 28, and 29) 1 = Gen 2nd Order
            Elastic 2 = 2nd Order By Amp 1st Order 3 = Limited 1st Order Elastic 4 = DAM Gen
            2nd Order Taub Variable 5 = DAM Gen 2nd Order Taub Fixed 6 = DAM Amp 1st Order
            Taub Variable 7 = DAM Amp 1st Order Taub Fixed 5 = Notional load coefficient
            Value > 0 6 = Phi bending Value > 0 7 = Phi compression Value > 0 8 = Phi
            tension yielding Value > 0 9 = Phi tension fracture Value > 0 10 = Phi shear
            Value > 0 11 = Phi shear sort webbed rolled I Value > 0 12 = Phi torsion Value >
            0 13 = Ignore seismic code 0 = No Any other value = Yes 14 = Ignore special
            seismic load 0 = No Any other value = Yes 15 = Doubler plate is plug welded 0 =
            No Any other value = Yes 16 = HSS welding type 1 = ERW 2 = SAW 17 = Reduce HSS
            thickness 0 = No Any other value = Yes 18 = Consider deflection 0 = No Any other
            value = Yes 19 = DL deflection limit, L/Value Value > 0 20 = SDL + LL deflection
            limit, L/Value Value > 0 21 = LL deflection limit, L/Value Value > 0 22 = Total
            load deflection limit, L/Value Value > 0 23 = Total camber limit, L/Value Value
            > 0 24 = Pattern live load factor Value >= 0 25 = Demand/capacity ratio limit
            Value > 0 26 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 =
            Last step 4 = Envelopes -- All 5 = Step-by-step -- All 27 = Analysis Method 1 =
            Direct Analysis 2 = Effective Length 3 = Limited 1st Order 28 = Second Order
            Method 1 = General 2nd Order 2 = Amplified 1st Order 29 = Stiffness Reduction
            Method 1 = Tau-b variable 2 = Tau-b Fixed 3 = No Modification 30 = Importance
            Factor Value > 0 31 = Design System Rho Value > 0 32 = Design System Sds Value
            >= 0 33 = Design System R Value > 0 34 = Design System Omega0 Value > 0 35 =
            Design System Cd Value > 0
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC360_10.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 43, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Omega0 3 = Consider deflection 4
            = Deflection check type 5 = DL deflection limit, L/Value 6 = SDL + LL deflection
            limit, L/Value 7 = LL deflection limit, L/Value 8 = Total load deflection limit,
            L/Value 9 = Total camber limit, L/Value 10 = DL deflection limit, absolute 11 =
            SDL + LL deflection limit, absolute 12 = LL deflection limit, absolute 13 =
            Total load deflection limit, absolute 14 = Total camber limit, absolute 15 =
            Specified camber 16 = Net area to total area ratio 17 = Live load reduction
            factor 18 = Unbraced length ratio, Major 19 = Unbraced length ratio, Minor 20 =
            Unbraced length ratio, Lateral Torsional Buckling 21 = Effective length factor,
            K1 Major 22 = Effective length factor, K1 Minor 23 = Effective length factor, K2
            Major 24 = Effective length factor, K2 Minor 25 = Effective length factor, K
            Lateral Torsional Buckling 26 = Moment coefficient, Cm Major 27 = Moment
            coefficient, Cm Minor 28 = Bending coefficient, Cb 29 = Nonsway moment factor,
            B1 Major 30 = Nonsway moment factor, B1 Minor 31 = Sway moment factor, B2 Major
            32 = Sway moment factor, B2 Minor 33 = Reduce HSS thickness 34 = HSS welding
            type 35 = Yield stress, Fy 36 = Expected to specified Fy ratio, Ry 37 =
            Compressive capacity, Pnc 38 = Tensile capacity, Pnt 39 = Major bending
            capacity, Mn3 40 = Minor bending capacity, Mn2 41 = Major shear capacity, Vn2 42
            = Minor shear capacity, Vn3 43 = Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = SMF 2 = IMF 3 = OMF 4 = SCBF 5 = OCBF 6 = OCBFI 7 = EBF 2 =
            Omega0 Value >= 0; 0 means use a program determined value. 3 = Consider
            deflection 0 = Program default 1 = No 2 = Yes 4 = Deflection check type 0 =
            Program default 1 = Ratio 2 = Absolute 3 = Both 5 = DL deflection limit, L/Value
            Value >= 0; 0 means no check for this item. 6 = SDL + LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 7 = LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 8 = Total load deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 9 = Total camber
            limit, L/Value Value >= 0; 0 means no check for this item. 10 = DL deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 11 = SDL + LL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 12 =
            LL deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 13
            = Total load deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L]} 14 = Total camber limit, absolute Value >= 0; 0 means no check for
            this item. [L] 15 = Specified camber Value >= 0. [L} 16 = Net area to total area
            ratio Value >= 0; 0 means use program default value. 17 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 18 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 19 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 20 =
            Unbraced length ratio, Lateral Torsional Buckling Value >= 0; 0 means use
            program determined value. 21 = Effective length factor, K1 Major Value >= 0; 0
            means use program determined value. 22 = Effective length factor, K1 Minor Value
            >= 0; 0 means use program determined value. 23 = Effective length factor, K2
            Major Value >= 0; 0 means use program determined value. 24 = Effective length
            factor, K2 Minor Value >= 0; 0 means use program determined value. 25 =
            Effective length factor, K Lateral Torsional Buckling Value >= 0; 0 means use
            program determined value. 26 = Moment coefficient, Cm Major Value >= 0; 0 means
            use program determined value. 27 = Moment coefficient, Cm Minor Value >= 0; 0
            means use program determined value. 28 = Bending coefficient, Cb Value >= 0; 0
            means use program determined value. 29 = Nonsway moment factor, B1 Major Value
            >= 0; 0 means use program determined value. 30 = Nonsway moment factor, B1 Minor
            Value >= 0; 0 means use program determined value. 31 = Sway moment factor, B2
            Major Value >= 0; 0 means use program determined value. 32 = Sway moment factor,
            B2 Minor Value >= 0; 0 means use program determined value. 33 = Reduce HSS
            thickness 0 = Program default 1 = No 2 = Yes 34 = HSS welding type 0 = Program
            default 1 = ERW 2 = SAW 35 = Yield stress, Fy Value >= 0; 0 means use program
            determined value. [F/L 2 ] 36 = Expected to specified Fy ratio, Ry Value >= 0; 0
            means use program determined value. 37 = Compressive capacity, Pnc Value >= 0; 0
            means use program determined value. [F] 38 = Tensile capacity, Pnt Value >= 0; 0
            means use program determined value. [F] 39 = Major bending capacity, Mn3 Value
            >= 0; 0 means use program determined value. [FL] 40 = Minor bending capacity,
            Mn2 Value >= 0; 0 means use program determined value. [FL] 41 = Major shear
            capacity, Vn2 Value >= 0; 0 means use program determined value. [F] 42 = Minor
            shear capacity, Vn3 Value >= 0; 0 means use program determined value. [F] 43 =
            Demand/capacity ratio limit Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC360_10.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 26, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Seismic design category 3 =
            Design provision 4 = Analysis method (Obsolete, replaced by 27, 28, and 29) 5 =
            Notional load coefficient 6 = Phi bending 7 = Phi compression 8 = Phi tension
            yielding 9 = Phi tension fracture 10 = Phi shear 11 = Phi shear sort webbed
            rolled I 12 = Phi torsion 13 = Ignore seismic code 14 = Ignore special seismic
            load 15 = Doubler plate is plug welded 16 = HSS welding type 17 = Reduce HSS
            thickness 18 = Consider deflection 19 = DL deflection limit, L/Value 20 = SDL +
            LL deflection limit, L/Value 21 = LL deflection limit, L/Value 22 = Total load
            deflection limit, L/Value 23 = Total camber limit, L/Value 24 = Pattern live
            load factor 25 = Demand/capacity ratio limit 26 = Multi-response case design 27
            = Analysis Method 28 = Second Order Method 29 = Stiffness Reduction Method 30 =
            Importance Factor 31 = Design Systems Rho 32 = Design Systems Sds 33 = Design
            Systems R 34 = Design Systems Omega0 35 = Design Systems Cd
        Value (input): The value of the considered preference item. 1 = Framing type 1 = SMF
            2 = IMF 3 = OMF 4 = SCBF 5 = OCBF 6 = OCBFI 7 = EBF 2 = Seismic design category
            1 = A 2 = B 3 = C 4 = D 5 = E 6 = F 3 = Design provision 1 = LRFD 2 = ASD 4 =
            Analysis method (Obsolete, replaced by 27, 28, and 29) 1 = Gen 2nd Order Elastic
            2 = 2nd Order By Amp 1st Order 3 = Limited 1st Order Elastic 4 = DAM Gen 2nd
            Order Taub Variable 5 = DAM Gen 2nd Order Taub Fixed 6 = DAM Amp 1st Order Taub
            Variable 7 = DAM Amp 1st Order Taub Fixed 5 = Notional load coefficient Value >
            0 6 = Phi bending Value > 0 7 = Phi compression Value > 0 8 = Phi tension
            yielding Value > 0 9 = Phi tension fracture Value > 0 10 = Phi shear Value > 0
            11 = Phi shear sort webbed rolled I Value > 0 12 = Phi torsion Value > 0 13 =
            Ignore seismic code 0 = No Any other value = Yes 14 = Ignore special seismic
            load 0 = No Any other value = Yes 15 = Doubler plate is plug welded 0 = No Any
            other value = Yes 16 = HSS welding type 1 = ERW 2 = SAW 17 = Reduce HSS
            thickness 0 = No Any other value = Yes 18 = Consider deflection 0 = No Any other
            value = Yes 19 = DL deflection limit, L/Value Value > 0 20 = SDL + LL deflection
            limit, L/Value Value > 0 21 = LL deflection limit, L/Value Value > 0 22 = Total
            load deflection limit, L/Value Value > 0 23 = Total camber limit, L/Value Value
            > 0 24 = Pattern live load factor Value >= 0 25 = Demand/capacity ratio limit
            Value > 0 26 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 =
            Last step 4 = Envelopes -- All 5 = Step-by-step -- All 27 = Analysis Method 1 =
            Direct Analysis 2 = Effective Length 3 = Limited 1st Order 28 = Second Order
            Method 1 = General 2nd Order 2 = Amplified 1st Order 29 = Stiffness Reduction
            Method 1 = Tau-b variable 2 = Tau-b Fixed 3 = No Modification 30 = Importance
            Factor Value > 0 31 = Design System Rho Value > 0 32 = Design System Sds Value
            >= 0 33 = Design System R Value > 0 34 = Design System Omega0 Value > 0 35 =
            Design System Cd Value > 0
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC360_10.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_BS5950_90:
    """Wrapper para SapModel.DesignSteel.BS5950_90."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 32, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Uniform moment factor, m Major 22 = Uniform moment
            factor, m Minor 23 = Slenderness correction factor, n 24 = Yield stress, Fy 25 =
            Compressive capacity, Pc 26 = Tensile capacity, Pt 27 = Major bending capacity,
            Mc3 28 = Minor bending capacity, Mc2 29 = Buckling resistance moment, Mb 30 =
            Major shear capacity, Pv2 31 = Minor shear capacity, Pv3 32 = Demand/capacity
            ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 19
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Uniform moment factor, m Major Value >= 0; 0 means use
            program determined value. 22 = Uniform moment factor, m Minor Value >= 0; 0
            means use program determined value. 23 = Slenderness correction factor, n Value
            >= 0; 0 means use program determined value. 24 = Yield stress, Fy Value >= 0; 0
            means use program determined value. [F/L 2 ] 25 = Compressive capacity, Pc Value
            >= 0; 0 means use program determined value. [F] 26 = Tensile capacity, Pt Value
            >= 0; 0 means use program determined value. [F] 27 = Major bending capacity, Mc3
            Value >= 0; 0 means use program determined value. [FL] 28 = Minor bending
            capacity, Mc2 Value >= 0; 0 means use program determined value. [FL] 29 =
            Buckling resistance moment, Mb Value >= 0; 0 means use program determined value.
            [FL] 30 = Major shear capacity, Pv2 Value >= 0; 0 means use program determined
            value. [F] 31 = Minor shear capacity, Pv3 Value >= 0; 0 means use program
            determined value. [F] 32 = Demand/capacity ratio limit Value >= 0; 0 means use
            program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.BS5950_90.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 10, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Consider deflection 3 = DL
            deflection limit, L/Value 4 = SDL + LL deflection limit, L/Value 5 = LL
            deflection limit, L/Value 6 = Total deflection limit, L/Value 7 = Total camber
            limit, L/Value 8 = Pattern live load factor 9 = Demand/capacity ratio limit 10 =
            Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Consider deflection 0 = No Any other value =
            Yes 3 = DL deflection limit, L/Value Value > 0 4 = SDL + LL deflection limit,
            L/Value Value > 0 5 = LL deflection limit, L/Value Value > 0 6 = Total
            deflection limit, L/Value Value > 0 7 = Total camber limit, L/Value Value > 0 8
            = Pattern live load factor Value >= 0 9 = Demand/capacity ratio limit Value > 0
            10 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 =
            Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.BS5950_90.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 32, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Uniform moment factor, m Major 22 = Uniform moment
            factor, m Minor 23 = Slenderness correction factor, n 24 = Yield stress, Fy 25 =
            Compressive capacity, Pc 26 = Tensile capacity, Pt 27 = Major bending capacity,
            Mc3 28 = Minor bending capacity, Mc2 29 = Buckling resistance moment, Mb 30 =
            Major shear capacity, Pv2 31 = Minor shear capacity, Pv3 32 = Demand/capacity
            ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 19
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Uniform moment factor, m Major Value >= 0; 0 means use
            program determined value. 22 = Uniform moment factor, m Minor Value >= 0; 0
            means use program determined value. 23 = Slenderness correction factor, n Value
            >= 0; 0 means use program determined value. 24 = Yield stress, Fy Value >= 0; 0
            means use program determined value. [F/L 2 ] 25 = Compressive capacity, Pc Value
            >= 0; 0 means use program determined value. [F] 26 = Tensile capacity, Pt Value
            >= 0; 0 means use program determined value. [F] 27 = Major bending capacity, Mc3
            Value >= 0; 0 means use program determined value. [FL] 28 = Minor bending
            capacity, Mc2 Value >= 0; 0 means use program determined value. [FL] 29 =
            Buckling resistance moment, Mb Value >= 0; 0 means use program determined value.
            [FL] 30 = Major shear capacity, Pv2 Value >= 0; 0 means use program determined
            value. [F] 31 = Minor shear capacity, Pv3 Value >= 0; 0 means use program
            determined value. [F] 32 = Demand/capacity ratio limit Value >= 0; 0 means use
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
            raise Sap2000ApiError("SapModel.DesignSteel.BS5950_90.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 10, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Consider deflection 3 = DL
            deflection limit, L/Value 4 = SDL + LL deflection limit, L/Value 5 = LL
            deflection limit, L/Value 6 = Total deflection limit, L/Value 7 = Total camber
            limit, L/Value 8 = Pattern live load factor 9 = Demand/capacity ratio limit 10 =
            Multi-response case design
        Value (input): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Consider deflection 0 = No Any other value =
            Yes 3 = DL deflection limit, L/Value Value > 0 4 = SDL + LL deflection limit,
            L/Value Value > 0 5 = LL deflection limit, L/Value Value > 0 6 = Total
            deflection limit, L/Value Value > 0 7 = Total camber limit, L/Value Value > 0 8
            = Pattern live load factor Value >= 0 9 = Demand/capacity ratio limit Value > 0
            10 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 =
            Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.BS5950_90.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_Italian_NTC_2008:
    """Wrapper para SapModel.DesignSteel.Italian_NTC_2008."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 48, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor 19 =
            Effective length factor sway, K2 Major 20 = Effective length factor sway, K2
            Minor 21 = Moment coefficient, kyy Major 22 = Moment coefficient, kzz Minor 23 =
            Bending coefficient, C1 24 = Moment coefficient, kzy 25 = Moment coefficient,
            kyz 26 = Yield stress, Fy 27 = Compressive capacity, Nc.Rd 28 = Tensile
            capacity, Nt.Rd 29 = Major bending capacity, Mc3.Rd 30 = Minor bending capacity,
            Mc2.Rd 31 = Buckling resistance moment, Mb.Rd 32 = Major shear capacity, V2.Rd
            33 = Minor shear capacity, V3.Rd 34 = Demand/capacity ratio limit 35 = Section
            class 36 = Column buckling curve, y-y 37 = Column buckling curve, z-z 38 =
            Buckling curve for LTB 39 = System overstrength factor, Omega 40 = Is rolled
            section 41 = Unbraced length ratio, LTB 42 = Effective length factor braced, K1
            Major 43 = Effective length factor braced, K1 Minor 44 = Effective length
            factor, K LTB 45 = Material overstrength factor, GammaRd 46 = Warping constant,
            Iw 47 = Elastic torsional buckling force, Ncr T 48 = Elastic torsional-flexural
            buckling force, Ncr TF
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = DCH-MRF 2 = DCL-MRF 3 = DCH-CBF 4 = DCL-CBF 5 = DCH-EBF 6 =
            DCL-EBF 7 = InvPendulum 8 = NonDissipative 2 = Consider deflection 0 = Program
            Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default 1 =
            Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0 means
            no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 19 = Effective length factor sway,
            K2 Major Value >= 0; 0 means use program determined value. 20 = Effective length
            factor sway, K2 Minor Value >= 0; 0 means use program determined value. 21 =
            Moment coefficient, kyy Major Value >= 0; 0 means use program determined value.
            22 = Moment coefficient, kzz Minor Value >= 0; 0 means use program determined
            value. 23 = Bending coefficient, C1 Value >= 0; 0 means use program determined
            value. 24 = Moment coefficient, kzy Value >= 0; 0 means use program determined
            value. 25 = Moment coefficient, kyz Value >= 0; 0 means use program determined
            value. 26 = Yield stress, Fy Value >= 0; 0 means use program determined value.
            [F/L 2 ] 27 = Compressive capacity, Nc.Rd Value >= 0; 0 means use program
            determined value. [F] 28 = Tensile capacity, Nt.Rd Value >= 0; 0 means use
            program determined value. [F] 29 = Major bending capacity, Mc3.Rd Value >= 0; 0
            means use program determined value. [FL] 30 = Minor bending capacity, Mc2.Rd
            Value >= 0; 0 means use program determined value. [FL] 31 = Buckling resistance
            moment, Mb.Rd Value >= 0; 0 means use program determined value. [FL] 32 = Major
            shear capacity, V2.Rd Value >= 0; 0 means use program determined value. [F] 33 =
            Minor shear capacity, V3.Rd Value >= 0; 0 means use program determined value.
            [F] 34 = Demand/capacity ratio limit Value >= 0; 0 means use program determined
            value. 35 = Section class 0 = Program default 1 = Class 1 2 = Class 2 3 = Class
            3 4 = Class 4 36 = Column buckling curve, y-y 0 = Program default 1 = a0 2 = a 3
            = b 4 = c 5 = d 37 = Column buckling curve, z-z 0 = Program default 1 = a0 2 = a
            3 = b 4 = c 5 = d 38 = Buckling curve for LTB 0 = Program default 1 = a0 2 = a 3
            = b 4 = c 5 = d 39 = System overstrength factor, Omega Value >= 0; 0 means use
            program determined value. 40 = Is rolled section 0 = Program Determined 1 = No 2
            = Yes 41 = Unbraced length ratio, LTB Value >= 0; 0 means use program determined
            value. 42 = Effective length factor braced, K1 Major Value >= 0; 0 means use
            program determined value. 43 = Effective length factor braced, K1 Minor Value >=
            0; 0 means use program determined value. 44 = Effective length factor, K LTB
            Value >= 0; 0 means use program determined value. 45 = Material overstrength
            factor, GammaRd Value >= 0; 0 means use program determined value. 46 = Warping
            constant, Iw Value >= 0; 0 means use program determined value. [L 6 ] 47 =
            Elastic torsional buckling force, Ncr T Value >= 0; 0 means use program
            determined value. [F] 48 = Elastic torsional-flexural buckling force, Ncr TF
            Value >= 0; 0 means use program determined value. [F]
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Italian_NTC_2008.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Item (input): This is an integer between 3 and 23, inclusive, indicating the
            preference item considered. 3 = Method Used for Buckling in P-M-M 4 = Framing
            type 5 = GammaM0 6 = GammeM1 7 = GammaM2 8 = Consider deflection 9 = DL
            deflection limit, L/Value 10 = SDL + LL deflection limit, L/Value 11 = LL
            deflection limit, L/Value 12 = Total deflection limit, L/Value 13 = Total camber
            limit, L/Value 14 = Pattern live load factor 15 = Demand/capacity ratio limit 16
            = Multi-Response Case Design 17 = Behavior Factor, q 0 18 = System Overstrength
            Factor, W 19 = Consider P-Delta 20 = Consider Torsion 21 = Ignore Seismic Code
            22 = Ignore Special Seismic Load 23 = Is Doubler Plate Plug-Welded
        Value (output): The value of the considered preference item. 3 = K factor method 1 =
            Method A 2 = Method B (default) 3 = Both 4 = Framing type 1 = DCH-MRF (Default)
            2 = DCL-MRF 3 = DCH-CBF 4 = DCL-CBF 5 = DCH-EBF 6 = DCL-EBF 7 = InvPendulum 8 =
            NonDissipative 5 = GammaM0 Default = 1.05, Value > 0 6 = GammaM1 Default = 1.05,
            Value > 0 7 = GammaM2 Default = 1.25, Value > 0 8 = Consider deflection Default
            = No = 1, Yes = 2 9 = DL deflection limit, L/Value Default = 120, Value > 0 10 =
            SDL + LL deflection limit, L/Value Default = 120, Value > 0 11 = LL deflection
            limit, L/Value Default = 360, Value > 0 12 = Total deflection limit, L/Value
            Default = 240, Value > 0 13 = Total camber limit, L/Value Default = 240, Value >
            0 14 = Pattern live load factor Default = 0, Value >= 0 15 = Demand/capacity
            ratio limit Default = 0.95, Value > 0 16 = Multi-response case design 1 =
            Envelopes (Default) 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 =
            Step-by-step -- All 17 = Behavior Factor, q 0 Default = 4, Value > 0 18 = System
            Overstrength Factor, W Default = 1.0, Value > 0 19 = Consider P-Delta Default =
            No = 1, Yes = 2 20 = Consider Torsion Default = No = 1, Yes = 2 21 = Ignore
            Seismic Code Default = No = 1, Yes = 2 22 = Ignore Special Seismic Load Default
            = No = 1, Yes = 2 23 = Is Doubler Plate Plug-Welded No = 1, Default = Yes = 2
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Italian_NTC_2008.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise, it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 48, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor 19 =
            Effective length factor, K2 Major 20 = Effective length factor, K2 Minor 21 =
            Moment coefficient, kyy Major 22 = Moment coefficient, kzz Minor 23 = Bending
            coefficient, C1 24 = Moment coefficient, kzy 25 = Moment coefficient, kyz 26 =
            Yield stress, Fy 27 = Compressive capacity, Nc.Rd 28 = Tensile capacity, Nt.Rd
            29 = Major bending capacity, Mc3.Rd 30 = Minor bending capacity, Mc2.Rd 31 =
            Buckling resistance moment, Mb.Rd 32 = Major shear capacity, V2.Rd 33 = Minor
            shear capacity, V3.RD 34 = Demand/capacity ratio limit 35 = Section class 36 =
            Column buckling curve, y-y 37 = Column buckling curve, z-z 38 = Buckling curve
            for LTB 39 = System overstrength factor, Omega 40 = Is rolled section 41 =
            Unbraced length ratio, LTB 42 = Effective length factor braced, K1 Major 43 =
            Effective length factor braced, K1 Minor 44 = Effective length factor, K LTB 45
            = Material overstrength factor, GammaRd 46 = Warping constant, Iw 47 = Elastic
            torsional buckling force, Ncr T 48 = Elastic torsional-flexural buckling force,
            Ncr TF
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = DCH-MRF 2 = DCL-MRF 3 = DCH-CBF 4 = DCL-CBF 5 = DCH-EBF 6 =
            DCL-EBF 7 = InvPendulum 8 = NonDissipative 2 = Consider deflection 0 = Program
            Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default 1 =
            Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0 means
            no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 19 = Effective length factor sway,
            K2 Major Value >= 0; 0 means use program determined value. 20 = Effective length
            factor sway, K2 Minor Value >= 0; 0 means use program determined value. 21 =
            Moment coefficient, kyy Major Value >= 0; 0 means use program determined value.
            22 = Moment coefficient, kzz Minor Value >= 0; 0 means use program determined
            value. 23 = Bending coefficient, C1 Value >= 0; 0 means use program determined
            value. 24 = Moment coefficient, kzy Value >= 0; 0 means use program determined
            value. 25 = Moment coefficient, kyz Value >= 0; 0 means use program determined
            value. 26 = Yield stress, Fy Value >= 0; 0 means use program determined value.
            [F/L 2 ] 27 = Compressive capacity, Nc.Rd Value >= 0; 0 means use program
            determined value. [F] 28 = Tensile capacity, Nt.Rd Value >= 0; 0 means use
            program determined value. [F] 29 = Major bending capacity, Mc3.Rd Value >= 0; 0
            means use program determined value. [FL] 30 = Minor bending capacity, Mc2.Rd
            Value >= 0; 0 means use program determined value. [FL] 31 = Buckling resistance
            moment, Mb.Rd Value >= 0; 0 means use program determined value. [FL] 32 = Major
            shear capacity, V2.Rd Value >= 0; 0 means use program determined value. [F] 33 =
            Minor shear capacity, V3.Rd Value >= 0; 0 means use program determined value.
            [F] 34 = Demand/capacity ratio limit Value >= 0; 0 means use program determined
            value. 35 = Section class 0 = Program default 1 = Class 1 2 = Class 2 3 = Class
            3 4 = Class 4 36 = Column buckling curve, y-y 0 = Program default 1 = a0 2 = a 3
            = b 4 = c 5 = d 37 = Column buckling curve, z-z 0 = Program default 1 = a0 2 = a
            3 = b 4 = c 5 = d 38 = Buckling curve for LTB 0 = Program default 1 = a0 2 = a 3
            = b 4 = c 5 = d 39 = System overstrength factor, Omega Value >= 0; 0 means use
            program determined value. 40 = Is rolled section 0 = Program Determined 1 = No 2
            = Yes 41 = Unbraced length ratio, LTB Value >= 0; 0 means use program determined
            value. 42 = Effective length factor braced, K1 Major Value >= 0; 0 means use
            program determined value. 43 = Effective length factor braced, K1 Minor Value >=
            0; 0 means use program determined value. 44 = Effective length factor, K LTB
            Value >= 0; 0 means use program determined value. 45 = Material overstrength
            factor, GammaRd Value >= 0; 0 means use program determined value. 46 = Warping
            constant, Iw Value >= 0; 0 means use program determined value. [L 6 ] 47 =
            Elastic torsional buckling force, Ncr T Value >= 0; 0 means use program
            determined value. [F] 48 = Elastic torsional-flexural buckling force, Ncr TF
            Value >= 0; 0 means use program determined value. [F]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Italian_NTC_2008.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise, it returns a nonzero value.
    
        Item (input): This is an integer between 3 and 23, inclusive, indicating the
            preference item considered. 3 = Method Used for Buckling in P-M-M 4 = Framing
            type 5 = GammaM0 6 = GammeM1 7 = GammaM2 8 = Consider deflection 9 = DL
            deflection limit, L/Value 10 = SDL + LL deflection limit, L/Value 11 = LL
            deflection limit, L/Value 12 = Total deflection limit, L/Value 13 = Total camber
            limit, L/Value 14 = Pattern live load factor 15 = Demand/capacity ratio limit 16
            = Multi-Response Case Design 17 = Behavior Factor, q 0 18 = System Overstrength
            Factor, W 19 = Consider P-Delta 20 = Consider Torsion 21 = Ignore Seismic Code
            22 = Ignore Special Seismic Load 23 = Is Doubler Plate Plug-Welded
        Value (input): The value of the considered preference item. 3 = K factor method 1 =
            Method A 2 = Method B (default) 3 = Both 4 = Framing type 1 = DCH-MRF (Default)
            2 = DCL-MRF 3 = DCH-CBF 4 = DCL-CBF 5 = DCH-EBF 6 = DCL-EBF 7 = InvPendulum 8 =
            NonDissipative 5 = GammaM0 Default = 1.05, Value > 0 6 = GammaM1 Default = 1.05,
            Value > 0 7 = GammaM2 Default = 1.25, Value > 0 8 = Consider deflection Default
            = No = 1, Yes = 2 9 = DL deflection limit, L/Value Default = 120, Value > 0 10 =
            SDL + LL deflection limit, L/Value Default = 120, Value > 0 11 = LL deflection
            limit, L/Value Default = 360, Value > 0 12 = Total deflection limit, L/Value
            Default = 240, Value > 0 13 = Total camber limit, L/Value Default = 240, Value >
            0 14 = Pattern live load factor Default = 0, Value >= 0 15 = Demand/capacity
            ratio limit Default = 0.95, Value > 0 16 = Multi-response case design 1 =
            Envelopes (Default) 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 =
            Step-by-step -- All 17 = Behavior Factor, q 0 Default = 4, Value > 0 18 = System
            Overstrength Factor, W Default = 1.0, Value > 0 19 = Consider P-Delta Default =
            No = 1, Yes = 2 20 = Consider Torsion Default = No = 1, Yes = 2 21 = Ignore
            Seismic Code Default = No = 1, Yes = 2 22 = Ignore Special Seismic Load Default
            = No = 1, Yes = 2 23 = Is Doubler Plate Plug-Welded No = 1, Default = Yes = 2
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Italian_NTC_2008.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_Eurocode_3_2005:
    """Wrapper para SapModel.DesignSteel.Eurocode_3_2005."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 48, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor 19 =
            Effective length factor sway, K2 Major 20 = Effective length factor sway, K2
            Minor 21 = Moment coefficient, kyy Major 22 = Moment coefficient, kzz Minor 23 =
            Bending coefficient, C1 24 = Moment coefficient, kzy 25 = Moment coefficient,
            kyz 26 = Yield stress, Fy 27 = Compressive capacity, Nc.Rd 28 = Tensile
            capacity, Nt.Rd 29 = Major bending capacity, Mc3.Rd 30 = Minor bending capacity,
            Mc2.Rd 31 = Buckling resistance moment, Mb.Rd 32 = Major shear capacity, V2.Rd
            33 = Minor shear capacity, V3.Rd 34 = Demand/capacity ratio limit 35 = Section
            class 36 = Column buckling curve, y-y 37 = Column buckling curve, z-z 38 =
            Buckling curve for LTB 39 = System overstrength factor, Omega 40 = Is rolled
            section 41 = Unbraced length ratio, LTB 42 = Effective length factor braced, K1
            Major 43 = Effective length factor braced, K1 Minor 44 = Effective length
            factor, K LTB 45 = Material overstrength factor, GammaOV 46 = Warping constant,
            Iw 47 = Elastic torsional buckling force, Ncr T 48 = Elastic torsional-flexural
            buckling force, Ncr TF
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 19 = Effective length factor sway,
            K2 Major Value >= 0; 0 means use program determined value. 20 = Effective length
            factor sway, K2 Minor Value >= 0; 0 means use program determined value. 21 =
            Moment coefficient, kyy Major Value >= 0; 0 means use program determined value.
            22 = Moment coefficient, kzz Minor Value >= 0; 0 means use program determined
            value. 23 = Bending coefficient, C1 Value >= 0; 0 means use program determined
            value. 24 = Moment coefficient, kzy Value >= 0; 0 means use program determined
            value. 25 = Moment coefficient, kyz Value >= 0; 0 means use program determined
            value. 26 = Yield stress, Fy Value >= 0; 0 means use program determined value.
            [F/L 2 ] 27 = Compressive capacity, Nc.Rd Value >= 0; 0 means use program
            determined value. [F] 28 = Tensile capacity, Nt.Rd Value >= 0; 0 means use
            program determined value. [F] 29 = Major bending capacity, Mc3.Rd Value >= 0; 0
            means use program determined value. [FL] 30 = Minor bending capacity, Mc2.Rd
            Value >= 0; 0 means use program determined value. [FL] 31 = Buckling resistance
            moment, Mb.Rd Value >= 0; 0 means use program determined value. [FL] 32 = Major
            shear capacity, V2.Rd Value >= 0; 0 means use program determined value. [F] 33 =
            Minor shear capacity, V3.Rd Value >= 0; 0 means use program determined value.
            [F] 34 = Demand/capacity ratio limit Value >= 0; 0 means use program determined
            value. 35 = Section class 0 = Program default 1 = Class 1 2 = Class 2 3 = Class
            3 4 = Class 4 36 = Column buckling curve, y-y 0 = Program default 1 = a0 2 = a 3
            = b 4 = c 5 = d 37 = Column buckling curve, z-z 0 = Program default 1 = a0 2 = a
            3 = b 4 = c 5 = d 38 = Buckling curve for LTB 0 = Program default 1 = a0 2 = a 3
            = b 4 = c 5 = d 39 = System overstrength factor, Omega Value >= 0; 0 means use
            program determined value. 40 = Is rolled section 0 = Program Determined 1 = No 2
            = Yes 41 = Unbraced length ratio, LTB Value >= 0; 0 means use program determined
            value. 42 = Effective length factor braced, K1 Major Value >= 0; 0 means use
            program determined value. 43 = Effective length factor braced, K1 Minor Value >=
            0; 0 means use program determined value. 44 = Effective length factor, K LTB
            Value >= 0; 0 means use program determined value. 45 = Material overstrength
            factor, GammaOV Value >= 0; 0 means use program determined value. 46 = Warping
            constant, Iw Value >= 0; 0 means use program determined value. [L 6 ] 47 =
            Elastic torsional buckling force, Ncr T Value >= 0; 0 means use program
            determined value. [F] 48 = Elastic torsional-flexural buckling force, Ncr TF
            Value >= 0; 0 means use program determined value. [F]
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Eurocode_3_2005.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 16, inclusive, indicating the
            preference item considered. 1 = Country 2 = Combos equation 3 = K factor method
            4 = Framing type 5 = GammaM0 6 = GammaM1 7 = GammaM2 8 = Consider deflection 9 =
            DL deflection limit, L/Value 10 = SDL + LL deflection limit, L/Value 11 = LL
            deflection limit, L/Value 12 = Total deflection limit, L/Value 13 = Total camber
            limit, L/Value 14 = Pattern live load factor 15 = Demand/capacity ratio limit 16
            = Multi-response case design 17 = Reliability Class
        Value (output): The value of the considered preference item. 1 = Country 1 = CEN
            Default 2 = United Kingdom 3 = Slovenia 4 = Bulgaria 5 = Norway 7 = Sweden 8 =
            Finland 9 = Denmark 10 = Portugal 11 = Germany 2 = Combos equation 1 = 1 = Eq.
            6.10 2 = Max of Eqs. 6.10a and 6.10b 3 = K factor method 1 = Method 1 (Annex A)
            2 = Method 2 (Annex B) 4 = Framing type 1 = Moment Frame 2 = Braced Frame 5 =
            GammaM0 Value > 0 6 = GammaM1 Value > 0 7 = GammaM2 Value > 0 8 = Consider
            deflection 0 = No Any other value = Yes 9 = DL deflection limit, L/Value Value >
            0 10 = SDL + LL deflection limit, L/Value Value > 0 11 = LL deflection limit,
            L/Value Value > 0 12 = Total deflection limit, L/Value Value > 0 13 = Total
            camber limit, L/Value Value > 0 14 = Pattern live load factor Value >= 0 15 =
            Demand/capacity ratio limit Value > 0 16 = Multi-response case design 1 =
            Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step
            -- All 17 = Reliability Class 1 = Class 1 2 = Class 2 3 = Class 3
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Eurocode_3_2005.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise, it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 48, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor 19 =
            Effective length factor, K2 Major 20 = Effective length factor, K2 Minor 21 =
            Moment coefficient, kyy Major 22 = Moment coefficient, kzz Minor 23 = Bending
            coefficient, C1 24 = Moment coefficient, kzy 25 = Moment coefficient, kyz 26 =
            Yield stress, Fy 27 = Compressive capacity, Nc.Rd 28 = Tensile capacity, Nt.Rd
            29 = Major bending capacity, Mc3.Rd 30 = Minor bending capacity, Mc2.Rd 31 =
            Buckling resistance moment, Mb.Rd 32 = Major shear capacity, V2.Rd 33 = Minor
            shear capacity, V3.RD 34 = Demand/capacity ratio limit 35 = Section class 36 =
            Column buckling curve, y-y 37 = Column buckling curve, z-z 38 = Buckling curve
            for LTB 39 = System overstrength factor, Omega 40 = Is rolled section 41 =
            Unbraced length ratio, LTB 42 = Effective length factor braced, K1 Major 43 =
            Effective length factor braced, K1 Minor 44 = Effective length factor, K LTB 45
            = Material overstrength factor, GammaOV 46 = Warping constant, Iw 47 = Elastic
            torsional buckling force, Ncr T 48 = Elastic torsional-flexural buckling force,
            Ncr TF
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor Value
            >= 0; 0 means use program determined value. 19 = Effective length factor sway,
            K2 Major Value >= 0; 0 means use program determined value. 20 = Effective length
            factor sway, K2 Minor Value >= 0; 0 means use program determined value. 21 =
            Moment coefficient, kyy Major Value >= 0; 0 means use program determined value.
            22 = Moment coefficient, kzz Minor Value >= 0; 0 means use program determined
            value. 23 = Bending coefficient, C1 Value >= 0; 0 means use program determined
            value. 24 = Moment coefficient, kzy Value >= 0; 0 means use program determined
            value. 25 = Moment coefficient, kyz Value >= 0; 0 means use program determined
            value. 26 = Yield stress, Fy Value >= 0; 0 means use program determined value.
            [F/L 2 ] 27 = Compressive capacity, Nc.Rd Value >= 0; 0 means use program
            determined value. [F] 28 = Tensile capacity, Nt.Rd Value >= 0; 0 means use
            program determined value. [F] 29 = Major bending capacity, Mc3.Rd Value >= 0; 0
            means use program determined value. [FL] 30 = Minor bending capacity, Mc2.Rd
            Value >= 0; 0 means use program determined value. [FL] 31 = Buckling resistance
            moment, Mb.Rd Value >= 0; 0 means use program determined value. [FL] 32 = Major
            shear capacity, V2.Rd Value >= 0; 0 means use program determined value. [F] 33 =
            Minor shear capacity, V3.Rd Value >= 0; 0 means use program determined value.
            [F] 34 = Demand/capacity ratio limit Value >= 0; 0 means use program determined
            value. 35 = Section class 0 = Program default 1 = Class 1 2 = Class 2 3 = Class
            3 4 = Class 4 36 = Column buckling curve, y-y 0 = Program default 1 = a0 2 = a 3
            = b 4 = c 5 = d 37 = Column buckling curve, z-z 0 = Program default 1 = a0 2 = a
            3 = b 4 = c 5 = d 38 = Buckling curve for LTB 0 = Program default 1 = a0 2 = a 3
            = b 4 = c 5 = d 39 = System overstrength factor, Omega Value >= 0; 0 means use
            program determined value. 40 = Is rolled section 0 = Program Determined 1 = No 2
            = Yes 41 = Unbraced length ratio, LTB Value >= 0; 0 means use program determined
            value. 42 = Effective length factor braced, K1 Major Value >= 0; 0 means use
            program determined value. 43 = Effective length factor braced, K1 Minor Value >=
            0; 0 means use program determined value. 44 = Effective length factor, K LTB
            Value >= 0; 0 means use program determined value. 45 = Material overstrength
            factor, GammaOV Value >= 0; 0 means use program determined value. 46 = Warping
            constant, Iw Value >= 0; 0 means use program determined value. [L 6 ] 47 =
            Elastic torsional buckling force, Ncr T Value >= 0; 0 means use program
            determined value. [F] 48 = Elastic torsional-flexural buckling force, Ncr TF
            Value >= 0; 0 means use program determined value. [F]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Eurocode_3_2005.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise, it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 16, inclusive, indicating the
            preference item considered. 1 = Country 2 = Combos equation 3 = K factor method
            4 = Framing type 5 = GammaM0 6 = GammeM1 7 = GammaM2 8 = Consider deflection 9 =
            DL deflection limit, L/Value 10 = SDL + LL deflection limit, L/Value 11 = LL
            deflection limit, L/Value 12 = Total deflection limit, L/Value 13 = Total camber
            limit, L/Value 14 = Pattern live load factor 15 = Demand/capacity ratio limit 16
            = Multi-response case design 17 = Reliability Class
        Value (input): The value of the considered preference item. 1 = Country 1 = CEN
            Default 2 = United Kingdom 3 = Slovenia 4 = Bulgaria 5 = Norway 7 = Sweden 8 =
            Finland 9 = Denmark 10 = Portugal 11 = Germany 2 = Combos equation 1 = 1 = Eq.
            6.10 2 = Max of Eqs. 6.10a and 6.10b 3 = K factor method 1 = Method 1 (Annex A)
            2 = Method 2 (Annex B) 4 = Framing type 1 = Moment Frame 2 = Braced Frame 5 =
            GammaM0 Value > 0 6 = GammeM1 Value > 0 7 = GammeM2 Value > 0 8 = Consider
            deflection 0 = No Any other value = Yes 9 = DL deflection limit, L/Value Value >
            0 10 = SDL + LL deflection limit, L/Value Value > 0 11 = LL deflection limit,
            L/Value Value > 0 12 = Total deflection limit, L/Value Value > 0 13 = Total
            camber limit, L/Value Value > 0 14 = Pattern live load factor Value >= 0 15 =
            Demand/capacity ratio limit Value > 0 16 = Multi-response case design 1 =
            Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step
            -- All 17 = Reliability Class 1 = Class 1 2 = Class 2 3 = Class 3
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Eurocode_3_2005.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_Norsok_N0042013:
    """Wrapper para SapModel.DesignSteel.Norsok_N0042013."""

    def __init__(self, raw):
        self._raw = raw

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 16, inclusive, indicating the
            preference item considered. 1 = Combos equation 2 = K factor method 3 = Pressure
            interaction method 4 = Framing type 5 = GammaM0 6 = GammeM1 7 = GammaM2 8 =
            Consider deflection 9 = DL deflection limit, L/Value 10 = SDL + LL deflection
            limit, L/Value 11 = LL deflection limit, L/Value 12 = Total deflection limit,
            L/Value 13 = Total camber limit, L/Value 14 = Pattern live load factor 15 =
            Demand/capacity ratio limit 16 = Multi-response case design
        Value (input): The value of the considered preference item. 1 = Combos equation 1 =
            1 = Eq. 6.10 2 = Max of Eqs. 6.10a and 6.10b 2 = K factor method 1 = Method 1
            (Annex A) 2 = Method 2 (Annex B) 3 = Pressure interaction method 1 = Method A 2
            = Method B 4 = Framing type 1 = Moment Frame 2 = Braced Frame 5 = GammaM0 Value
            > 0 6 = GammeM1 Value > 0 7 = GammeM2 Value > 0 8 = Consider deflection 0 = No
            Any other value = Yes 9 = DL deflection limit, L/Value Value > 0 10 = SDL + LL
            deflection limit, L/Value Value > 0 11 = LL deflection limit, L/Value Value > 0
            12 = Total deflection limit, L/Value Value > 0 13 = Total camber limit, L/Value
            Value > 0 14 = Pattern live load factor Value >= 0 15 = Demand/capacity ratio
            limit Value > 0 16 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3
            = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Norsok_N0042013.SetPreference falhou (ret={_r})".format(_r=_r))
        return None

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 36, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, k Major 22 = Moment coefficient,
            k Minor 23 = Bending coefficient, C1 24 = Moment coefficient, kzy 25 = Moment
            coefficient, kyz 26 = Pressure equalized 27 = External pressure 28 = Yield
            stress, Fy 29 = Compressive capacity, Nc.Rd 30 = Tensile capacity, Nt.Rd 31 =
            Major bending capacity, Mc3.Rd 32 = Minor bending capacity, Mc2.Rd 33 = Buckling
            resistance moment, Mb.Rd 34 = Major shear capacity, V2.Rd 35 = Minor shear
            capacity, V3.RD 36 = Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 = As
            specified in preferences 1 = Moment Frame 2 = Braced Frame 2 = Consider
            deflection 0 = Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 =
            Program default 1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value
            Value >= 0; 0 means no check for this item. 5 = SDL + LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 6 = LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 7 = Total load deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 8 = Total camber
            limit, L/Value Value >= 0; 0 means no check for this item. 9 = DL deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 10 = SDL + LL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 11 =
            LL deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 12
            = Total load deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 13 = Total camber limit, absolute Value >= 0; 0 means no check for
            this item. [L] 14 = Specified camber Value >= 0. [L] 15 = Net area to total area
            ratio Value >= 0; 0 means use program default value. 16 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 17 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 18 = Unbraced
            length ratio, Minor Lateral Torsional Buckling Value >= 0; 0 means use program
            determined value. 19 = Effective length factor, K Major Value >= 0; 0 means use
            program determined value. 20 = Effective length factor, K Minor Value >= 0; 0
            means use program determined value. 21 = Moment coefficient, k Major Value >= 0;
            0 means use program determined value. 22 = Moment coefficient, k Minor Value >=
            0; 0 means use program determined value. 23 = Bending coefficient, C1 Value >=
            0; 0 means use program determined value. 24 = Moment coefficient, kzy Value >=
            0; 0 means use program determined value. 25 = Moment coefficient, kyz Value >=
            0; 0 means use program determined value. 26 = Pressure equalized 0 = Program
            Determined 1 = No 2 = Yes 27 = External pressure Any value OK; Positive
            generates hoop compression and negative generates hoop tension. [F/L 2 ] 28 =
            Yield stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 29 =
            Compressive capacity, Nc.Rd Value >= 0; 0 means use program determined value.
            [F] 30 = Tensile capacity, Nt.Rd Value >= 0; 0 means use program determined
            value. [F] 31 = Major bending capacity, Mc3.Rd Value >= 0; 0 means use program
            determined value. [FL] 32 = Minor bending capacity, Mc2.Rd Value >= 0; 0 means
            use program determined value. [FL] 33 = Buckling resistance moment, Mb.Rd Value
            >= 0; 0 means use program determined value. [FL] 34 = Major shear capacity,
            V2.Rd Value >= 0; 0 means use program determined value. [F] 35 = Minor shear
            capacity, V3.RD Value >= 0; 0 means use program determined value. [F] 36 =
            Demand/capacity ratio limit Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Norsok_N0042013.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 16, inclusive, indicating the
            preference item considered. 1 = Combos equation 2 = K factor method 3 = Pressure
            interaction method 4 = Framing type 5 = GammaM0 6 = GammeM1 7 = GammaM2 8 =
            Consider deflection 9 = DL deflection limit, L/Value 10 = SDL + LL deflection
            limit, L/Value 11 = LL deflection limit, L/Value 12 = Total deflection limit,
            L/Value 13 = Total camber limit, L/Value 14 = Pattern live load factor 15 =
            Demand/capacity ratio limit 16 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Combos equation 1 =
            1 = Eq. 6.10 2 = Max of Eqs. 6.10a and 6.10b 2 = K factor method 1 = Method 1
            (Annex A) 2 = Method 2 (Annex B) 3 = Pressure interaction method 1 = Method A 2
            = Method B 4 = Framing type 1 = Moment Frame 2 = Braced Frame 5 = GammaM0 Value
            > 0 6 = GammeM1 Value > 0 7 = GammeM2 Value > 0 8 = Consider deflection 0 = No
            Any other value = Yes 9 = DL deflection limit, L/Value Value > 0 10 = SDL + LL
            deflection limit, L/Value Value > 0 11 = LL deflection limit, L/Value Value > 0
            12 = Total deflection limit, L/Value Value > 0 13 = Total camber limit, L/Value
            Value > 0 14 = Pattern live load factor Value >= 0 15 = Demand/capacity ratio
            limit Value > 0 16 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3
            = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Norsok_N0042013.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 36, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, k Major 22 = Moment coefficient,
            k Minor 23 = Bending coefficient, C1 24 = Moment coefficient, kzy 25 = Moment
            coefficient, kyz 26 = Pressure equalized 27 = External pressure 28 = Yield
            stress, Fy 29 = Compressive capacity, Nc.Rd 30 = Tensile capacity, Nt.Rd 31 =
            Major bending capacity, Mc3.Rd 32 = Minor bending capacity, Mc2.Rd 33 = Buckling
            resistance moment, Mb.Rd 34 = Major shear capacity, V2.Rd 35 = Minor shear
            capacity, V3.RD 36 = Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 = As
            specified in preferences 1 = Moment Frame 2 = Braced Frame 2 = Consider
            deflection 0 = Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 =
            Program default 1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value
            Value >= 0; 0 means no check for this item. 5 = SDL + LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 6 = LL deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 7 = Total load deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 8 = Total camber
            limit, L/Value Value >= 0; 0 means no check for this item. 9 = DL deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 10 = SDL + LL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 11 =
            LL deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 12
            = Total load deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 13 = Total camber limit, absolute Value >= 0; 0 means no check for
            this item. [L] 14 = Specified camber Value >= 0. [L] 15 = Net area to total area
            ratio Value >= 0; 0 means use program default value. 16 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 17 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 18 = Unbraced
            length ratio, Minor Lateral Torsional Buckling Value >= 0; 0 means use program
            determined value. 19 = Effective length factor, K Major Value >= 0; 0 means use
            program determined value. 20 = Effective length factor, K Minor Value >= 0; 0
            means use program determined value. 21 = Moment coefficient, k Major Value >= 0;
            0 means use program determined value. 22 = Moment coefficient, k Minor Value >=
            0; 0 means use program determined value. 23 = Bending coefficient, C1 Value >=
            0; 0 means use program determined value. 24 = Moment coefficient, kzy Value >=
            0; 0 means use program determined value. 25 = Moment coefficient, kyz Value >=
            0; 0 means use program determined value. 26 = Pressure equalized 0 = Program
            Determined 1 = No 2 = Yes 27 = External pressure Any value OK; Positive
            generates hoop compression and negative generates hoop tension. [F/L 2 ] 28 =
            Yield stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 29 =
            Compressive capacity, Nc.Rd Value >= 0; 0 means use program determined value.
            [F] 30 = Tensile capacity, Nt.Rd Value >= 0; 0 means use program determined
            value. [F] 31 = Major bending capacity, Mc3.Rd Value >= 0; 0 means use program
            determined value. [FL] 32 = Minor bending capacity, Mc2.Rd Value >= 0; 0 means
            use program determined value. [FL] 33 = Buckling resistance moment, Mb.Rd Value
            >= 0; 0 means use program determined value. [FL] 34 = Major shear capacity,
            V2.Rd Value >= 0; 0 means use program determined value. [F] 35 = Minor shear
            capacity, V3.RD Value >= 0; 0 means use program determined value. [F] 36 =
            Demand/capacity ratio limit Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Norsok_N0042013.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_API_RP2A_LRFD97:
    """Wrapper para SapModel.DesignSteel.API_RP2A_LRFD97."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 37, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, Cm Major 22 = Moment
            coefficient, Cm Minor 23 = Bending coefficient, Cb 24 = Non-sway moment factor,
            B1 Major 25 = Non-sway moment factor, B1 Minor 26 = Sway moment factor, B2 Major
            27 = Sway moment factor, B2 Minor 28 = Pressure equalized 29 = External pressure
            30 = Yield stress, Fy 31 = Compressive capacity, phi*Pnc 32 = Tensile capacity,
            phi*Pnt 33 = Major bending capacity, phi*Mn3 34 = Minor bending capacity,
            phi*Mn2 35 = Major shear capacity, phi*Vn2 36 = Minor shear capacity, phi*Vn3 37
            = Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 19
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 22 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 23 = Bending coefficient, Cb Value >= 0; 0 means
            use program determined value. 24 = Non-sway moment factor, B1 Major Value >= 0;
            0 means use program determined value. 25 = Non-sway moment factor, B1 Minor
            Value >= 0; 0 means use program determined value. 26 = Sway moment factor, B2
            Major Value >= 0; 0 means use program determined value. 27 = Sway moment factor,
            B2 Minor Value >= 0; 0 means use program determined value. 28 = Pressure
            equalized 0 = Program Determined 1 = No 2 = Yes 29 = External pressure. [F/L 2 ]
            Any value OK; Positive generates hoop compression and negative generates hoop
            tension. [F/L 2 ] 30 = Yield stress, Fy Value >= 0; 0 means use program
            determined value. [F/L 2 ] 31 = Compressive capacity, phi*Pnc Value >= 0; 0
            means use program determined value. [F] 32 = Tensile capacity, phi*Pnt Value >=
            0; 0 means use program determined value. [F] 33 = Major bending capacity,
            phi*Mn3 Value >= 0; 0 means use program determined value. [FL] 34 = Minor
            bending capacity, phi*Mn2 Value >= 0; 0 means use program determined value. [FL]
            35 = Major shear capacity, phi*Vn2 Value >= 0; 0 means use program determined
            value. [F] 36 = Minor shear capacity, phi*Vn3 Value >= 0; 0 means use program
            determined value. [F] 37 = Demand/capacity ratio limit Value >= 0; 0 means use
            program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.API_RP2A_LRFD97.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Tubular joint punching load
            method 3 = Consider deflection 4 = DL deflection limit, L/Value 5 = SDL + LL
            deflection limit, L/Value 6 = LL deflection limit, L/Value 7 = Total deflection
            limit, L/Value 8 = Total camber limit, L/Value 9 = Pattern live load factor 10 =
            Demand/capacity ratio limit 11 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Tubular joint punching load method 1 =
            Punching Shear 2 = Nominal Load 3 = Consider deflection 0 = No Any other value =
            Yes 4 = DL deflection limit, L/Value Value > 0 5 = SDL + LL deflection limit,
            L/Value Value > 0 6 = LL deflection limit, L/Value Value > 0 7 = Total
            deflection limit, L/Value Value > 0 8 = Total camber limit, L/Value Value > 0 9
            = Pattern live load factor Value >= 0 10 = Demand/capacity ratio limit Value > 0
            11 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 =
            Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.API_RP2A_LRFD97.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemTypeitem.
        Item (input): This is an integer between 1 and 37, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, Cm Major 22 = Moment
            coefficient, Cm Minor 23 = Bending coefficient, Cb 24 = Non-sway moment factor,
            B1 Major 25 = Non-sway moment factor, B1 Minor 26 = Sway moment factor, B2 Major
            27 = Sway moment factor, B2 Minor 28 = Pressure equalized 29 = External pressure
            30 = Yield stress, Fy 31 = Compressive capacity, phi*Pnc 32 = Tensile capacity,
            phi*Pnt 33 = Major bending capacity, phi*Mn3 34 = Minor bending capacity,
            phi*Mn2 35 = Major shear capacity, phi*Vn2 36 = Minor shear capacity, phi*Vn3 37
            = Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 19
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 22 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 23 = Bending coefficient, Cb Value >= 0; 0 means
            use program determined value. 24 = Non-sway moment factor, B1 Major Value >= 0;
            0 means use program determined value. 25 = Non-sway moment factor, B1 Minor
            Value >= 0; 0 means use program determined value. 26 = Sway moment factor, B2
            Major Value >= 0; 0 means use program determined value. 27 = Sway moment factor,
            B2 Minor Value >= 0; 0 means use program determined value. 28 = Pressure
            equalized 0 = Program Determined 1 = No 2 = Yes 29 = External pressure Any value
            OK; Positive generates hoop compression and negative generates hoop tension.
            [F/L 2 ] 30 = Yield stress, Fy Value >= 0; 0 means use program determined value.
            [F/L 2 ] 31 = Compressive capacity, phi*Pnc Value >= 0; 0 means use program
            determined value. [F] 32 = Tensile capacity, phi*Pnt Value >= 0; 0 means use
            program determined value. [F] 33 = Major bending capacity, phi*Mn3 Value >= 0; 0
            means use program determined value. [FL] 34 = Minor bending capacity, phi*Mn2
            Value >= 0; 0 means use program determined value. [FL] 35 = Major shear
            capacity, phi*Vn2 Value >= 0; 0 means use program determined value. [F] 36 =
            Minor shear capacity, phi*Vn3 Value >= 0; 0 means use program determined value.
            [F] 37 = Demand/capacity ratio limit Value >= 0; 0 means use program determined
            value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.API_RP2A_LRFD97.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Tubular joint punching load
            method 3 = Consider deflection 4 = DL deflection limit, L/Value 5 = SDL + LL
            deflection limit, L/Value 6 = LL deflection limit, L/Value 7 = Total deflection
            limit, L/Value 8 = Total camber limit, L/Value 9 = Pattern live load factor 10 =
            Demand/capacity ratio limit 11 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Tubular joint punching load method 1 =
            Punching Shear 2 = Nominal Load 3 = Consider deflection 0 = No Any other value =
            Yes 4 = DL deflection limit, L/Value Value > 0 5 = SDL + LL deflection limit,
            L/Value Value > 0 6 = LL deflection limit, L/Value Value > 0 7 = Total
            deflection limit, L/Value Value > 0 8 = Total camber limit, L/Value Value > 0 9
            = Pattern live load factor Value >= 0 10 = Demand/capacity ratio limit Value > 0
            11 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 =
            Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.API_RP2A_LRFD97.SetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]


class N_DesignSteel_Canadian_S16_09:
    """Wrapper para SapModel.DesignSteel.Canadian_S16_09."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 39, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor LTB
            19 = Unbraced length ratio, Lateral Torsional Buckling 20 = Effective length
            factor, K Major 21 = Effective length factor, K Minor 22 = Effective length
            factor, K LTB 23 = Moment coefficient, Omega1 Major 24 = Moment coefficient,
            Omega1 Minor 25 = Bending coefficient, Omega2 26 = Nonsway moment factor, U1
            Major 27 = Nonsway moment factor, U1 Minor 28 = Sway moment factor, U2 Major 29
            = Sway moment factor, U2 Minor 30 = Parameter for compressive resistance, n 31 =
            Yield stress, Fy 32 = Expected to specified Fy ratio, Ry 33 = Compressive
            resistance, Cr 34 = Tensile resistance, Tr 35 = Major bending resistance, Mr3 36
            = Minor bending resistance, Mr2 37 = Major shear resistance, Vr2 38 = Minor
            shear resistance, Vr3 39 = Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 = As
            specified in preferences 1 = Type LD MRF 2 = Type MD MRF 3 = Type D MRF 4 = Type
            LD CBF(V) 5 = Type LD CBF(TC) 6 = Type LD CBF(TO) 7 = Type LD CBF(OT) 8 = Type
            MD CBF(V) 9 = Type MD CBF(TC) 10 = Type MD CBF(TO) 11 = Type MD CBF(OT) 12 = EBF
            13 = Cantilever Column 14 = Conventional MF 15 = Conventional BF 2 = Consider
            deflection 0 = No Any other value = Yes 3 = Deflection check type 0 = Program
            default 1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value
            >= 0; 0 means no check for this item. 5 = SDL + LL deflection limit, L/Value
            Value >= 0; 0 means no check for this item. 6 = LL deflection limit, L/Value
            Value >= 0; 0 means no check for this item. 7 = Total load deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 8 = Total camber limit,
            L/Value Value >= 0; 0 means no check for this item. 9 = DL deflection limit,
            absolute Value >= 0; 0 means no check for this item. [L] 10 = SDL + LL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 11 =
            LL deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 12
            = Total load deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L]} 13 = Total camber limit, absolute Value >= 0; 0 means no check for
            this item. [L] 14 = Specified camber Value >= 0. [L} 15 = Net area to total area
            ratio Value >= 0; 0 means use program default value. 16 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 17 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 18 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 19 =
            Unbraced length ratio, Lateral Torsional Buckling Value >= 0; 0 means use
            program determined value. 20 = Effective length factor, K Major Value >= 0; 0
            means use program determined value. 21 = Effective length factor, K Minor Value
            >= 0; 0 means use program determined value. 22 = Effective length factor, K LTB
            Value >= 0; 0 means use program determined value. 23 = Moment coefficient,
            Omega1 Major Value >= 0; 0 means use program determined value. 24 = Moment
            coefficient, Omega1 Minor Value >= 0; 0 means use program determined value. 25 =
            Moment coefficient, Omega2 Value >= 0; 0 means use program determined value. 26
            = Nonsway moment factor, U1 Major Value >= 0; 0 means use program determined
            value. 27 = Nonsway moment factor, U1 Minor Value >= 0; 0 means use program
            determined value. 28 = Sway moment factor, U2 Major Value >= 0; 0 means use
            program determined value. 29 = Sway moment factor, U2 Minor Value >= 0; 0 means
            use program determined value. 30 = Parameter for compressive resistance, n Value
            >= 0; 0 means use program determined value. 31 = Yield stress, Fy Value >= 0; 0
            means use program determined value. [F/L 2 ] 32 = Expected to specified Fy
            ratio, Ry Value >= 0; 0 means use program determined value. [F/L 2 ]= 33 =
            Compressive resistance, Cr Value >= 0; 0 means use program determined value. [F]
            34 = Tensile resistance, Tr Value >= 0; 0 means use program determined value.
            [F] 35 = Major bending resistance, Mr3 Value >= 0; 0 means use program
            determined value. [FL] 36 = Minor bending resistance, Mr2 Value >= 0; 0 means
            use program determined value. [FL] 37 = Major shear resistance, Vr2 Value >= 0;
            0 means use program determined value. [F] 38 = Minor shear resistance, Vr3 Value
            >= 0; 0 means use program determined value. [F] 39 = Demand/capacity ratio limit
            Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Canadian_S16_09.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved, otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 21, inclusive, indicating the
            preference item considered. 1 = Multi-response case design 2 = Framing type 3 =
            Spectral Acceleration Ratio, Ie*Fa*Sa(0.2) 4 = Ductility related modification
            factor, Rd 5 = Overstrength related modification factor, Ro 6 = Capacity factor,
            Phi bending 7 = Capacity factor, Phi compression 8 = Capacity factor, Phi
            tension 9 = Capacity factor, Phi shear 10 = Slender section modification 11 =
            Ignore seismic code 12 = Ignore special seismic load 13 = Doubler plate is plug
            welded 14 = Consider deflection 15 = DL deflection limit, L/Value 16 = SDL + LL
            deflection limit, L/Value 17 = LL deflection limit, L/Value 18 = Total load
            deflection limit, L/Value 19 = Total camber limit, L/Value 20 = Pattern live
            load factor 21 = Demand/capacity ratio limit
        Value (output): The value of the considered preference item. 1 = Multi-response case
            design 1 = Envelopes 2 = Step-by step 3 = Last step 4 = Envelopes - All 5 =
            Step-by step - All 2 = Framing type 1 = Type LD MRF 2 = Type MD MRF 3 = Type D
            MRF 4 = Type LD CBF(V) 5 = Type LD CBF(TC) 6 = Type LD CBF(TO) 7 = Type LD
            CBF(OT) 8 = Type MD CBF(V) 9 = Type MD CBF(TC) 10 = Type MD CBF(TO) 11 = Type MD
            CBF(OT) 12 = EBF 13 = Cantilever Column 14 = Conventional MF 15 = Conventional
            BF 3 = Spectral Acceleration Ratio, Ie*Fa*Sa(0.2) Value > 0 4 = Ductility
            related modification factor, Rd Value > 0 5 = Overstrength related modification
            factor, Ro Value > 0 6 = Capacity factor, Phi bending Value > 0 7 = Capacity
            factor, Phi compression Value > 0 8 = Capacity factor, Phi tension Value > 0 9 =
            Capacity factor, Phi shear Value > 0 10 = Slender section modification 1 =
            Modified geometry 2 = modified Fy 11 = Ignore seismic code 0 = No Any other
            value = Yes 12 = Ignore special seismic load 0 = No Any other value = Yes 13 =
            Doubler plate is plug welded 0 = No Any other value = Yes 14 = Consider
            deflection 0 = No Any other value = Yes 15 = DL deflection limit, L/Value Value
            > 0 16 = SDL + LL deflection limit, L/Value Value > 0 17 = LL deflection limit,
            L/Value Value > 0 18 = Total load deflection limit, L/Value Value > 0 19 = Total
            camber limit, L/Value Value > 0 20 = Pattern live load factor Value >= 0 21 =
            Demand/capacity ratio limit Value > 0
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Canadian_S16_09.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 39, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor LTB
            19 = Unbraced length ratio, Lateral Torsional Buckling 20 = Effective length
            factor, K Major 21 = Effective length factor, K Minor 22 = Effective length
            factor, K LTB 23 = Moment coefficient, Omega1 Major 24 = Moment coefficient,
            Omega1 Minor 25 = Bending coefficient, Omega2 26 = Nonsway moment factor, U1
            Major 27 = Nonsway moment factor, U1 Minor 28 = Sway moment factor, U2 Major 29
            = Sway moment factor, U2 Minor 30 = Parameter for compressive resistance, n 31 =
            Yield stress, Fy 32 = Expected to specified Fy ratio, Ry 33 = Compressive
            resistance, Cr 34 = Tensile resistance, Tr 35 = Major bending resistance, Mr3 36
            = Minor bending resistance, Mr2 37 = Major shear resistance, Vr2 38 = Minor
            shear resistance, Vr3 39 = Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 = As
            specified in preferences 1 = Type LD MRF 2 = Type MD MRF 3 = Type D MRF 4 = Type
            LD CBF(V) 5 = Type LD CBF(TC) 6 = Type LD CBF(TO) 7 = Type LD CBF(OT) 8 = Type
            MD CBF(V) 9 = Type MD CBF(TC) 10 = Type MD CBF(TO) 11 = Type MD CBF(OT) 12 = EBF
            13 = Cantilever Column 14 = Conventional MF 15 = Conventional BF 2 = Consider
            deflection 0 = No Any other value = Yes 3 = Deflection check type 0 = Program
            default 1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value
            >= 0; 0 means no check for this item. 5 = SDL + LL deflection limit, L/Value
            Value >= 0; 0 means no check for this item. 6 = LL deflection limit, L/Value
            Value >= 0; 0 means no check for this item. 7 = Total load deflection limit,
            L/Value Value >= 0; 0 means no check for this item. 8 = Total camber limit,
            L/Value Value >= 0; 0 means no check for this item. 9 = DL deflection limit,
            absolute Value >= 0; 0 means no check for this item. [L] 10 = SDL + LL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 11 =
            LL deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 12
            = Total load deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L]} 13 = Total camber limit, absolute Value >= 0; 0 means no check for
            this item. [L] 14 = Specified camber Value >= 0. [L} 15 = Net area to total area
            ratio Value >= 0; 0 means use program default value. 16 = Live load reduction
            factor Value >= 0; 0 means use program determined value. 17 = Unbraced length
            ratio, Major Value >= 0; 0 means use program determined value. 18 = Unbraced
            length ratio, Minor Value >= 0; 0 means use program determined value. 19 =
            Unbraced length ratio, Lateral Torsional Buckling Value >= 0; 0 means use
            program determined value. 20 = Effective length factor, K Major Value >= 0; 0
            means use program determined value. 21 = Effective length factor, K Minor Value
            >= 0; 0 means use program determined value. 22 = Effective length factor, K LTB
            Value >= 0; 0 means use program determined value. 23 = Moment coefficient,
            Omega1 Major Value >= 0; 0 means use program determined value. 24 = Moment
            coefficient, Omega1 Minor Value >= 0; 0 means use program determined value. 25 =
            Moment coefficient, Omega2 Value >= 0; 0 means use program determined value. 26
            = Nonsway moment factor, U1 Major Value >= 0; 0 means use program determined
            value. 27 = Nonsway moment factor, U1 Minor Value >= 0; 0 means use program
            determined value. 28 = Sway moment factor, U2 Major Value >= 0; 0 means use
            program determined value. 29 = Sway moment factor, U2 Minor Value >= 0; 0 means
            use program determined value. 30 = Parameter for compressive resistance, n Value
            >= 0; 0 means use program determined value. 31 = Yield stress, Fy Value >= 0; 0
            means use program determined value. [F/L 2 ] 32 = Expected to specified Fy
            ratio, Ry Value >= 0; 0 means use program determined value. [F/L 2 ]= 33 =
            Compressive resistance, Cr Value >= 0; 0 means use program determined value. [F]
            34 = Tensile resistance, Tr Value >= 0; 0 means use program determined value.
            [F] 35 = Major bending resistance, Mr3 Value >= 0; 0 means use program
            determined value. [FL] 36 = Minor bending resistance, Mr2 Value >= 0; 0 means
            use program determined value. [FL] 37 = Major shear resistance, Vr2 Value >= 0;
            0 means use program determined value. [F] 38 = Minor shear resistance, Vr3 Value
            >= 0; 0 means use program determined value. [F] 39 = Demand/capacity ratio limit
            Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Canadian_S16_09.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set, otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 21, inclusive, indicating the
            preference item considered. 1 = Multi-response case design 2 = Framing type 3 =
            Spectral Acceleration Ratio, Ie*Fa*Sa(0.2) 4 = Ductility related modification
            factor, Rd 5 = Overstrength related modification factor, Ro 6 = Capacity factor,
            Phi bending 7 = Capacity factor, Phi compression 8 = Capacity factor, Phi
            tension 9 = Capacity factor, Phi shear 10 = Slender section modification 11 =
            Ignore seismic code 12 = Ignore special seismic load 13 = Doubler plate is plug
            welded 14 = Consider deflection 15 = DL deflection limit, L/Value 16 = SDL + LL
            deflection limit, L/Value 17 = LL deflection limit, L/Value 18 = Total load
            deflection limit, L/Value 19 = Total camber limit, L/Value 20 = Pattern live
            load factor 21 = Demand/capacity ratio limit
        Value (input): The value of the considered preference item. 1 = Multi-response case
            design 1 = Envelopes 2 = Step-by step 3 = Last step 4 = Envelopes - All 5 =
            Step-by step - All 2 = Framing type 1 = Type LD MRF 2 = Type MD MRF 3 = Type D
            MRF 4 = Type LD CBF(V) 5 = Type LD CBF(TC) 6 = Type LD CBF(TO) 7 = Type LD
            CBF(OT) 8 = Type MD CBF(V) 9 = Type MD CBF(TC) 10 = Type MD CBF(TO) 11 = Type MD
            CBF(OT) 12 = EBF 13 = Cantilever Column 14 = Conventional MF 15 = Conventional
            BF 3 = Spectral Acceleration Ratio, Ie*Fa*Sa(0.2) Value > 0 4 = Ductility
            related modification factor, Rd Value > 0 5 = Overstrength related modification
            factor, Ro Value > 0 6 = Capacity factor, Phi bending Value > 0 7 = Capacity
            factor, Phi compression Value > 0 8 = Capacity factor, Phi tension Value > 0 9 =
            Capacity factor, Phi shear Value > 0 10 = Slender section modification 1 =
            Modified geometry 2 = modified Fy 11 = Ignore seismic code 0 = No Any other
            value = Yes 12 = Ignore special seismic load 0 = No Any other value = Yes 13 =
            Doubler plate is plug welded 0 = No Any other value = Yes 14 = Consider
            deflection 0 = No Any other value = Yes 15 = DL deflection limit, L/Value Value
            > 0 16 = SDL + LL deflection limit, L/Value Value > 0 17 = LL deflection limit,
            L/Value Value > 0 18 = Total load deflection limit, L/Value Value > 0 19 = Total
            camber limit, L/Value Value > 0 20 = Pattern live load factor Value >= 0 21 =
            Demand/capacity ratio limit Value > 0
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Canadian_S16_09.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_Indian_IS_800_1998:
    """Wrapper para SapModel.DesignSteel.Indian_IS:800_1998."""

    def __init__(self, raw):
        self._raw = raw

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Lateral factor 3 = Consider
            deflection 4 = DL deflection limit, L/Value 5 = SDL + LL deflection limit,
            L/Value 6 = LL deflection limit, L/Value 7 = Total deflection limit, L/Value 8 =
            Total camber limit, L/Value 9 = Pattern live load factor 10 = Demand/capacity
            ratio limit 11 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Sway Frame 2 = Nonsway Frame 2 = Lateral factor Value > 0 3 = Consider
            deflection 0 = No Any other value = Yes 4 = DL deflection limit, L/Value Value >
            0 5 = SDL + LL deflection limit, L/Value Value > 0 6 = LL deflection limit,
            L/Value Value > 0 7 = Total deflection limit, L/Value Value > 0 8 = Total camber
            limit, L/Value Value > 0 9 = Pattern live load factor Value >= 0 10 =
            Demand/capacity ratio limit Value > 0 11 = Multi-response case design 1 =
            Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step
            -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Indian_IS:800_1998.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Lateral factor 3 = Consider
            deflection 4 = DL deflection limit, L/Value 5 = SDL + LL deflection limit,
            L/Value 6 = LL deflection limit, L/Value 7 = Total deflection limit, L/Value 8 =
            Total camber limit, L/Value 9 = Pattern live load factor 10 = Demand/capacity
            ratio limit 11 = Multi-response case design
        Value (input): The value of the considered preference item. 1 = Framing type 1 =
            Sway Frame 2 = Nonsway Frame 2 = Lateral factor Value > 0 3 = Consider
            deflection 0 = No Any other value = Yes 4 = DL deflection limit, L/Value Value >
            0 5 = SDL + LL deflection limit, L/Value Value > 0 6 = LL deflection limit,
            L/Value Value > 0 7 = Total deflection limit, L/Value Value > 0 8 = Total camber
            limit, L/Value Value > 0 9 = Pattern live load factor Value >= 0 10 =
            Demand/capacity ratio limit Value > 0 11 = Multi-response case design 1 =
            Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step
            -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Indian_IS:800_1998.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_UBC97_ASD:
    """Wrapper para SapModel.DesignSteel.UBC97_ASD."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 32, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Omega0 3 = Consider deflection 4
            = Deflection check type 5 = DL deflection limit, L/Value 6 = SDL + LL deflection
            limit, L/Value 7 = LL deflection limit, L/Value 8 = Total load deflection limit,
            L/Value 9 = Total camber limit, L/Value 10 = DL deflection limit, absolute 11 =
            SDL + LL deflection limit, absolute 12 = LL deflection limit, absolute 13 =
            Total load deflection limit, absolute 14 = Total camber limit, absolute 15 =
            Specified camber 16 = Net area to total area ratio 17 = Live load reduction
            factor 18 = Unbraced length ratio, Major 19 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 20 = Effective length factor, K Major 21 = Effective
            length factor, K Minor 22 = Moment coefficient, Cm Major 23 = Moment
            coefficient, Cm Minor 24 = Bending coefficient, Cb 25 = Yield stress, Fy 26 =
            Compressive stress, Fa 27 = Tensile stress, Ft 28 = Major bending stress, Fb3 29
            = Minor bending stress, Fb2 30 = Major shear stress, Fv2 31 = Minor shear
            stress, Fv3 32 = Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Ordinary MRF 2 = Special MRF 3 = Braced Frame 4 = Special
            CBF 5 = EBF 2 = Omega0 Value >= 0; 0 means use a program determined value. 3 =
            Consider deflection 0 = Program Determined 1 = No 2 = Yes 4 = Deflection check
            type 0 = Program default 1 = Ratio 2 = Absolute 3 = Both 5 = DL deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 6 = SDL + LL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 7 = LL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 8 = Total
            load deflection limit, L/Value Value >= 0; 0 means no check for this item. 9 =
            Total camber limit, L/Value Value >= 0; 0 means no check for this item. 10 = DL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 11 =
            SDL + LL deflection limit, absolute Value >= 0; 0 means no check for this item.
            [L] 12 = LL deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 13 = Total load deflection limit, absolute Value >= 0; 0 means no
            check for this item. [L] 14 = Total camber limit, absolute Value >= 0; 0 means
            no check for this item. [L] 15 = Specified camber Value >= 0. [L] 16 = Net area
            to total area ratio Value >= 0; 0 means use program default value. 17 = Live
            load reduction factor Value >= 0; 0 means use program determined value. 18 =
            Unbraced length ratio, Major Value >= 0; 0 means use program determined value.
            19 = Unbraced length ratio, Minor Lateral Torsional Buckling Value >= 0; 0 means
            use program determined value. 20 = Effective length factor, K Major Value >= 0;
            0 means use program determined value. 21 = Effective length factor, K Minor
            Value >= 0; 0 means use program determined value. 22 = Moment coefficient, Cm
            Major Value >= 0; 0 means use program determined value. 23 = Moment coefficient,
            Cm Minor Value >= 0; 0 means use program determined value. 24 = Bending
            coefficient, Cb Value >= 0; 0 means use program determined value. 25 = Yield
            stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 26 =
            Compressive stress, Fa Value >= 0; 0 means use program determined value. [F/L 2
            ] 27 = Tensile stress, Ft Value >= 0; 0 means use program determined value. [F/L
            2 ] 28 = Major bending stress, Fb3 Value >= 0; 0 means use program determined
            value. [F/L 2 ] 29 = Minor bending stress, Fb2 Value >= 0; 0 means use program
            determined value. [F/L 2 ] 30 = Major shear stress, Fv2 Value >= 0; 0 means use
            program determined value. [F/L 2 ] 31 = Minor shear stress, Fv3 Value >= 0; 0
            means use program determined value. [F/L 2 ] 32 = Demand/capacity ratio limit
            Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.UBC97_ASD.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Seismic zone 3 = Lateral factor
            4 = Consider deflection 5 = DL deflection limit, L/Value 6 = SDL + LL deflection
            limit, L/Value 7 = LL deflection limit, L/Value 8 = Total deflection limit,
            L/Value 9 = Total camber limit, L/Value 10 = Pattern live load factor 11 =
            Demand/capacity ratio limit 12 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Ordinary MRF 2 = Special MRF 3 = Braced Frame 4 = Special CBF 5 = EBF 2 =
            Seismic zone 1 = Zone 0 2 = Zone 1 3 = Zone 2 4 = Zone 3 5 = Zone 4 3 = Lateral
            factor Value > 0 4 = Consider deflection 0 = No Any other value = Yes 5 = DL
            deflection limit, L/Value5 Value > 0 6 = SDL + LL deflection limit, L/Value
            Value > 0 7 = LL deflection limit, L/Value Value > 0 8 = Total deflection limit,
            L/Value Value > 0 9 = Total camber limit, L/Value Value > 0 10 = Pattern live
            load factor Value >= 0 11 = Demand/capacity ratio limit Value > 0 12 = Multi-
            response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes
            -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.UBC97_ASD.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemTypeitem.
        Item (input): This is an integer between 1 and 32, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Omega0 3 = Consider deflection 4
            = Deflection check type 5 = DL deflection limit, L/Value 6 = SDL + LL deflection
            limit, L/Value 7 = LL deflection limit, L/Value 8 = Total load deflection limit,
            L/Value 9 = Total camber limit, L/Value 10 = DL deflection limit, absolute 11 =
            SDL + LL deflection limit, absolute 12 = LL deflection limit, absolute 13 =
            Total load deflection limit, absolute 14 = Total camber limit, absolute 15 =
            Specified camber 16 = Net area to total area ratio 17 = Live load reduction
            factor 18 = Unbraced length ratio, Major 19 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 20 = Effective length factor, K Major 21 = Effective
            length factor, K Minor 22 = Moment coefficient, Cm Major 23 = Moment
            coefficient, Cm Minor 24 = Bending coefficient, Cb 25 = Yield stress, Fy 26 =
            Compressive stress, Fa 27 = Tensile stress, Ft 28 = Major bending stress, Fb3 29
            = Minor bending stress, Fb2 30 = Major shear stress, Fv2 31 = Minor shear
            stress, Fv3 32 = Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Ordinary MRF 2 = Special MRF 3 = Braced Frame 4 = Special
            CBF 5 = EBF 2 = Omega0 Value >= 0; 0 means use a program determined value. 3 =
            Consider deflection 0 = Program Determined 1 = No 2 = Yes 4 = Deflection check
            type 0 = Program default 1 = Ratio 2 = Absolute 3 = Both 5 = DL deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 6 = SDL + LL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 7 = LL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 8 = Total
            load deflection limit, L/Value Value >= 0; 0 means no check for this item. 9 =
            Total camber limit, L/Value Value >= 0; 0 means no check for this item. 10 = DL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 11 =
            SDL + LL deflection limit, absolute Value >= 0; 0 means no check for this item.
            [L] 12 = LL deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 13 = Total load deflection limit, absolute Value >= 0; 0 means no
            check for this item. [L] 14 = Total camber limit, absolute Value >= 0; 0 means
            no check for this item. [L] 15 = Specified camber Value >= 0. [L] 16 = Net area
            to total area ratio Value >= 0; 0 means use program default value. 17 = Live
            load reduction factor Value >= 0; 0 means use program determined value. 18 =
            Unbraced length ratio, Major Value >= 0; 0 means use program determined value.
            19 = Unbraced length ratio, Minor Lateral Torsional Buckling Value >= 0; 0 means
            use program determined value. 20 = Effective length factor, K Major Value >= 0;
            0 means use program determined value. 21 = Effective length factor, K Minor
            Value >= 0; 0 means use program determined value. 22 = Moment coefficient, Cm
            Major Value >= 0; 0 means use program determined value. 23 = Moment coefficient,
            Cm Minor Value >= 0; 0 means use program determined value. 24 = Bending
            coefficient, Cb Value >= 0; 0 means use program determined value. 25 = Yield
            stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 26 =
            Compressive stress, Fa Value >= 0; 0 means use program determined value. [F/L 2
            ] 27 = Tensile stress, Ft Value >= 0; 0 means use program determined value. [F/L
            2 ] 28 = Major bending stress, Fb3 Value >= 0; 0 means use program determined
            value. [F/L 2 ] 29 = Minor bending stress, Fb2 Value >= 0; 0 means use program
            determined value. [F/L 2 ] 30 = Major shear stress, Fv2 Value >= 0; 0 means use
            program determined value. [F/L 2 ] 31 = Minor shear stress, Fv3 Value >= 0; 0
            means use program determined value. [F/L 2 ] 32 = Demand/capacity ratio limit
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
            raise Sap2000ApiError("SapModel.DesignSteel.UBC97_ASD.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Seismic zone 3 = Lateral factor
            4 = Consider deflection 5 = DL deflection limit, L/Value 6 = SDL + LL deflection
            limit, L/Value 7 = LL deflection limit, L/Value 8 = Total deflection limit,
            L/Value 9 = Total camber limit, L/Value 10 = Pattern live load factor 11 =
            Demand/capacity ratio limit 12 = Multi-response case design
        Value (input): The value of the considered preference item. 1 = Framing type 1 =
            Ordinary MRF 2 = Special MRF 3 = Braced Frame 4 = Special CBF 5 = EBF 2 =
            Seismic zone 1 = Zone 0 2 = Zone 1 3 = Zone 2 4 = Zone 3 5 = Zone 4 3 = Lateral
            factor Value > 0 4 = Consider deflection 0 = No Any other value = Yes 5 = DL
            limit, L/Value Value > 0 6 = Super DL + LL limit, L/Value Value > 0 7 = Live
            load limit, L/Value Value > 0 8 = Total limit, L/Value Value > 0 9 = Total
            camber limit, L/Value Value > 0 10 = Pattern live load factor Value >= 0 11 =
            Demand/capacity ratio limit Value > 0 12 = Multi-response case design 1 =
            Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step
            -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.UBC97_ASD.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_API_RP2A_WSD2014:
    """Wrapper para SapModel.DesignSteel.API_RP2A_WSD2014."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 33, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral TorsionalBuckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, Cm Major 22 = Moment
            coefficient, Cm Minor 23 = Bending coefficient, Cb 24 = Pressure equalized 25 =
            External pressure 26 = Yield stress, Fy 27 = Compressive stress, Fa 28 = Tensile
            stress, Ft 29 = Major bending stress, Fb3 30 = Minor bending stress, Fb2 31 =
            Major shear stress, Fv2 32 = Minor shear stress, Fv3 33 = Demand/capacity ratio
            limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 19
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 22 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 23 = Bending coefficient, Cb Value >= 0; 0 means
            use program determined value. 24 = Pressure equalized 0 = Program Determined 1 =
            No 2 = Yes 25 = External pressure Any value OK; Positive generates hoop
            compression and negative generates hoop tension.. [F/L 2 ] 26 = Yield stress, Fy
            Value >= 0; 0 means use program determined value. [F/L 2 ] 27 = Compressive
            stress, Fa Value >= 0; 0 means use program determined value. [F/L 2 ] 28 =
            Tensile stress, Ft Value >= 0; 0 means use program determined value. [F/L 2 ] 29
            = Major bending stress, Fb3 Value >= 0; 0 means use program determined value.
            [F/L 2 ] 30 = Minor bending stress, Fb2 Value >= 0; 0 means use program
            determined value. [F/L 2 ] 31 = Major shear stress, Fv2 Value >= 0; 0 means use
            program determined value. [F/L 2 ] 32 = Minor shear stress, Fv3 Value >= 0; 0
            means use program determined value. [F/L 2 ] 33 = Demand/capacity ratio limit
            Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.API_RP2A_WSD2014.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Lateral factor, L/Value 3 =
            Consider deflection 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = Pattern live load factor 10 =
            Demand/capacity ratio limit 11 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Lateral Factor Value > 0 3 = Consider
            deflection 0 = No Any other value = Yes 4 = DL deflection limit, L/Value Value >
            0 5 = SDL + LL deflection limit, L/Value Value > 0 6 = LL deflection limit,
            L/Value Value > 0 7 = Total deflection limit, L/Value Value > 0 8 = Total camber
            limit, L/Value Value > 0 9 = Pattern live load factor Value >= 0 10 =
            Demand/capacity ratio limit Value > 0 11 = Multi-response case design 1 =
            Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step
            -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.API_RP2A_WSD2014.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 33, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, Cm Major 22 = Moment
            coefficient, Cm Minor 23 = Bending coefficient, Cb 24 = Pressure equalized 25 =
            External pressure 26 = Yield stress, Fy 27 = Compressive stress, Fa 28 = Tensile
            stress, Ft 29 = Major bending stress, Fb3 30 = Minor bending stress, Fb2 31 =
            Major shear stress, Fv2 32 = Minor shear stress, Fv3 33 = Demand/capacity ratio
            limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 19
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 22 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 23 = Bending coefficient, Cb Value >= 0; 0 means
            use program determined value. 24 = Pressure equalized 0 = Program Determined 1 =
            No 2 = Yes 25 = External pressure Any value OK; Positive generates hoop
            compression and negative generates hoop tension. [F/L 2 ] 26 = Yield stress, Fy
            Value >= 0; 0 means use program determined value. [F/L 2 ] 27 = Compressive
            stress, Fa Value >= 0; 0 means use program determined value. [F/L 2 ] 28 =
            Tensile stress, Ft Value >= 0; 0 means use program determined value. [F/L 2 ] 29
            = Major bending stress, Fb3 Value >= 0; 0 means use program determined value.
            [F/L 2 ] 30 = Minor bending stress, Fb2 Value >= 0; 0 means use program
            determined value. [F/L 2 ] 31 = Major shear stress, Fv2 Value >= 0; 0 means use
            program determined value. [F/L 2 ] 32 = Minor shear stress, Fv3 Value >= 0; 0
            means use program determined value. [F/L 2 ] 33 = Demand/capacity ratio limit
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
            raise Sap2000ApiError("SapModel.DesignSteel.API_RP2A_WSD2014.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 11, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Lateral factor, L/Value 3 =
            Consider deflection 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = Pattern live load factor 10 =
            Demand/capacity ratio limit 11 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Lateral Factor Value > 0 3 = Consider
            deflection 0 = No Any other value = Yes 4 = DL deflection limit, L/Value Value >
            0 5 = SDL + LL deflection limit, L/Value Value > 0 6 = LL deflection limit,
            L/Value Value > 0 7 = Total deflection limit, L/Value Value > 0 8 = Total camber
            limit, L/Value Value > 0 9 = Pattern live load factor Value >= 0 10 =
            Demand/capacity ratio limit Value > 0 11 = Multi-response case design 1 =
            Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step
            -- All
        """
        _r = self._raw.SetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.API_RP2A_WSD2000.SetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]


class N_DesignSteel_NewZealand_NZS3404_1997:
    """Wrapper para SapModel.DesignSteel.NewZealand_NZS3404_1997."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved, otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 46, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Steel type 3 = Consider
            deflection 4 = Deflection check type 5 = DL deflection limit, L/Value 6 = SDL +
            LL deflection limit, L/Value 7 = LL deflection limit, L/Value 8 = Total load
            deflection limit, L/Value 9 = Total camber limit, L/Value 10 = DL deflection
            limit, absolute 11 = SDL + LL deflection limit, absolute 12 = LL deflection
            limit, absolute 13 = Total load deflection limit, absolute 14 = Total camber
            limit, absolute 15 = Specified camber 16 = Net area to total area ratio 17 =
            Live load reduction factor 18 = Unbraced length ratio, Major 19 = Unbraced
            length ratio, Minor 20 = Unbraced length ratio, Lateral Torsional Buckling 21 =
            Effective length factor, Ke Major Braced 22 = Effective length factor, Ke Minor
            Braced 23 = Effective length factor, Ke Major Sway 24 = Effective length factor,
            Ke Minor Sway 25 = Twist restraint factor for LTB (kt) 26 = lateral rotation
            restraint factor (kr) 27 = Load height factor for LTB (kl) 28 = Moment
            coefficient, Cm Major 29 = Moment coefficient, Cm Minor 30 = Moment modification
            factor, Alpha_m 31 = Slender reduction factor, Alpha_s 32 = Nonsway moment
            factor, Db Major 33 = Nonsway moment factor, Db Minor 34 = Sway moment factor,
            Ds Major 35 = Sway moment factor, Ds Minor 36 = Form factor, Kf 37 = Axial
            capacity correction factor, Kt 38 = Yield stress, Fy 39 = Compressive capacity,
            Nc 40 = Tensile capacity, Nt 41 = Major bending capacity, Ms33 42 = Minor
            bending capacity, Ms22 43 = Major bending capacity, Mb33 44 = Major shear
            capacity, Vu2 45 = Minor shear capacity, Vu3 46 = Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 = As
            specified in preferences 1 = Moment frame 2 = Braced frame 2 = Steel type 1 =
            Hot rolled 2 = Hot finished 3 = Cold form 4 = Stress relieved 5 = Lightly welded
            6 = Heavily welded 3 = Consider deflection 0 = No Any other value = Yes 4 =
            Deflection check type 0 = Program default 1 = Ratio 2 = Absolute 3 = Both 5 = DL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 6 = SDL +
            LL deflection limit, L/Value Value >= 0; 0 means no check for this item. 7 = LL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 8 = Total
            load deflection limit, L/Value Value >= 0; 0 means no check for this item. 9 =
            Total camber limit, L/Value Value >= 0; 0 means no check for this item. 10 = DL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 11 =
            SDL + LL deflection limit, absolute Value >= 0; 0 means no check for this item.
            [L] 12 = LL deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 13 = Total load deflection limit, absolute Value >= 0; 0 means no
            check for this item. [L]} 14 = Total camber limit, absolute Value >= 0; 0 means
            no check for this item. [L] 15 = Specified camber Value >= 0. [L} 16 = Net area
            to total area ratio Value >= 0; 0 means use program default value. 17 = Live
            load reduction factor Value >= 0; 0 means use program determined value. 18 =
            Unbraced length ratio, Major Value >= 0; 0 means use program determined value.
            19 = Unbraced length ratio, Minor Value >= 0; 0 means use program determined
            value. 20 = Unbraced length ratio, Lateral Torsional Buckling Value >= 0; 0
            means use program determined value. 21 = Effective length factor, Ke Major
            Braced Value >= 0; 0 means use program determined value. 22 = Effective length
            factor, Ke Minor Braced Value >= 0; 0 means use program determined value. 23 =
            Effective length factor, Ke Major Sway Value >= 0; 0 means use program
            determined value. 24 = Effective length factor, Ke Minor Sway Value >= 0; 0
            means use program determined value. 25 = Twist restraint factor for LTB (kt)
            Value >= 0; 0 means use program determined value. 26 = Lateral rotation
            restraint factor (kr) Value >= 0; 0 means use program determined value. 27 =
            Load height factor for LTB (kl) Value >= 0; 0 means use program determined
            value. 28 = Moment coefficient, Cm Major Value >= 0; 0 means use program
            determined value. 29 = Moment coefficient, Cm Minor Value >= 0; 0 means use
            program determined value. 30 = Moment modification factor, Alpha_m Value >= 0; 0
            means use program determined value. 31 = Slender reduction factor, Alpha_s Value
            >= 0; 0 means use program determined value. 32 = Nonsway moment factor, Db Major
            Value >= 0; 0 means use program determined value. 33 = Nonsway moment factor, Db
            Minor Value >= 0; 0 means use program determined value. 34 = Sway moment factor,
            Bs Major Value >= 0; 0 means use program determined value. 35 = Sway moment
            factor, Bs Minor Value >= 0; 0 means use program determined value. 36 = Form
            factor, Kf Value >= 0; 0 means use program determined value. 37 = Axial capacity
            correction factor, Kt Value >= 0; 0 means use program determined value. 38 =
            Yield stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 39 =
            Compressive capacity, Nc Value >= 0; 0 means use program determined value. [F]
            40 = Tensile capacity, Nt Value >= 0; 0 means use program determined value. [F]
            41 = Major bending capacity, Ms33 Value >= 0; 0 means use program determined
            value. [FL] 42 = Minor bending capacity, Ms22 Value >= 0; 0 means use program
            determined value. [FL] 43 = Minor bending capacity, Mb33 Value >= 0; 0 means use
            program determined value. [FL] 44 = Major shear capacity, Vu2 Value >= 0; 0
            means use program determined value. [F] 45 = Minor shear capacity, Vu3 Value >=
            0; 0 means use program determined value. [F] 46 = Demand/capacity ratio limit
            Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.NewZealand_NZS3404_1997.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved, otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 17, inclusive, indicating the
            preference item considered. 1 = Multi-response case design 2 = Framing type 3 =
            Structural analysis method 4 = Steel type 5 = Capacity factor, Phi bending 6 =
            Capacity factor, Phi compression 7 = Capacity factor, Phi tension yielding 8 =
            Capacity factor, Phi tension fracture 9 = Capacity factor, Phi shear 10 =
            Consider deflection 11 = DL deflection limit, L/Value 12 = SDL + LL deflection
            limit, L/Value 13 = LL deflection limit, L/Value 14 = Total load deflection
            limit, L/Value 15 = Total camber limit, L/Value 16 = Pattern live load factor 17
            = Demand/capacity ratio limit
        Value (output): The value of the considered preference item. 1 = Multi-response case
            design 1 = Envelopes 2 = Step-by step 3 = Last step 4 = Envelopes - All 5 =
            Step-by step - All 2 = Framing type 1 = Moment frame 2 = Braced frame 3 =
            Structural analysis method 1 = General 2nd Order 2 = Amplified 1st Order 4 =
            Steel type 1 = Hot rolled 2 = Hot finished 3 = Cold form 4 = Stress relieved 5 =
            Lightly welded 6 = Heavily welded 5 = Capacity factor, Phi bending Value > 0 6 =
            Capacity factor, Phi compression Value > 0 7 = Capacity factor, Phi tension
            yielding Value > 0 8 = Capacity factor, Phi tension fracture Value > 0 9 =
            Capacity factor, Phi shear Value > 0 10 = Consider deflection 0 = No Any other
            value = Yes 11 = DL deflection limit, L/Value Value > 0 12 = SDL + LL deflection
            limit, L/Value Value > 0 13 = LL deflection limit, L/Value Value > 0 14 = Total
            load deflection limit, L/Value Value > 0 15 = Total camber limit, L/Value Value
            > 0 16 = Pattern live load factor Value >= 0 17 = Demand/capacity ratio limit
            Value > 0
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.NewZealand_NZS3404_1997.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 46, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Steel type 3 = Consider
            deflection 4 = Deflection check type 5 = DL deflection limit, L/Value 6 = SDL +
            LL deflection limit, L/Value 7 = LL deflection limit, L/Value 8 = Total load
            deflection limit, L/Value 9 = Total camber limit, L/Value 10 = DL deflection
            limit, absolute 11 = SDL + LL deflection limit, absolute 12 = LL deflection
            limit, absolute 13 = Total load deflection limit, absolute 14 = Total camber
            limit, absolute 15 = Specified camber 16 = Net area to total area ratio 17 =
            Live load reduction factor 18 = Unbraced length ratio, Major 19 = Unbraced
            length ratio, Minor 20 = Unbraced length ratio, Lateral Torsional Buckling 21 =
            Effective length factor, Ke Major Braced 22 = Effective length factor, Ke Minor
            Braced 23 = Effective length factor, Ke Major Sway 24 = Effective length factor,
            Ke Minor Sway 25 = Twist restraint factor for LTB (kt) 26 = lateral rotation
            restraint factor (kr) 27 = Load height factor for LTB (kl) 28 = Moment
            coefficient, Cm Major 29 = Moment coefficient, Cm Minor 30 = Moment modification
            factor, Alpha_m 31 = Slender reduction factor, Alpha_s 32 = Nonsway moment
            factor, Db Major 33 = Nonsway moment factor, Db Minor 34 = Sway moment factor,
            Ds Major 35 = Sway moment factor, Ds Minor 36 = Form factor, Kf 37 = Axial
            capacity correction factor, Kt 38 = Yield stress, Fy 39 = Compressive capacity,
            Nc 40 = Tensile capacity, Nt 41 = Major bending capacity, Ms33 42 = Minor
            bending capacity, Ms22 43 = Major bending capacity, Mb33 44 = Major shear
            capacity, Vu2 45 = Minor shear capacity, Vu3 46 = Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 = As
            specified in preferences 1 = Moment frame 2 = Braced frame 2 = Steel type 1 =
            Hot rolled 2 = Hot finished 3 = Cold form 4 = Stress relieved 5 = Lightly welded
            6 = Heavily welded 3 = Consider deflection 0 = No Any other value = Yes 4 =
            Deflection check type 0 = Program default 1 = Ratio 2 = Absolute 3 = Both 5 = DL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 6 = SDL +
            LL deflection limit, L/Value Value >= 0; 0 means no check for this item. 7 = LL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 8 = Total
            load deflection limit, L/Value Value >= 0; 0 means no check for this item. 9 =
            Total camber limit, L/Value Value >= 0; 0 means no check for this item. 10 = DL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 11 =
            SDL + LL deflection limit, absolute Value >= 0; 0 means no check for this item.
            [L] 12 = LL deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 13 = Total load deflection limit, absolute Value >= 0; 0 means no
            check for this item. [L]} 14 = Total camber limit, absolute Value >= 0; 0 means
            no check for this item. [L] 15 = Specified camber Value >= 0. [L} 16 = Net area
            to total area ratio Value >= 0; 0 means use program default value. 17 = Live
            load reduction factor Value >= 0; 0 means use program determined value. 18 =
            Unbraced length ratio, Major Value >= 0; 0 means use program determined value.
            19 = Unbraced length ratio, Minor Value >= 0; 0 means use program determined
            value. 20 = Unbraced length ratio, Lateral Torsional Buckling Value >= 0; 0
            means use program determined value. 21 = Effective length factor, Ke Major
            Braced Value >= 0; 0 means use program determined value. 22 = Effective length
            factor, Ke Minor Braced Value >= 0; 0 means use program determined value. 23 =
            Effective length factor, Ke Major Sway Value >= 0; 0 means use program
            determined value. 24 = Effective length factor, Ke Minor Sway Value >= 0; 0
            means use program determined value. 25 = Twist restraint factor for LTB (kt)
            Value >= 0; 0 means use program determined value. 26 = Lateral rotation
            restraint factor (kr) Value >= 0; 0 means use program determined value. 27 =
            Load height factor for LTB (kl) Value >= 0; 0 means use program determined
            value. 28 = Moment coefficient, Cm Major Value >= 0; 0 means use program
            determined value. 29 = Moment coefficient, Cm Minor Value >= 0; 0 means use
            program determined value. 30 = Moment modification factor, Alpha_m Value >= 0; 0
            means use program determined value. 31 = Slender reduction factor, Alpha_s Value
            >= 0; 0 means use program determined value. 32 = Nonsway moment factor, Db Major
            Value >= 0; 0 means use program determined value. 33 = Nonsway moment factor, Db
            Minor Value >= 0; 0 means use program determined value. 34 = Sway moment factor,
            Bs Major Value >= 0; 0 means use program determined value. 35 = Sway moment
            factor, Bs Minor Value >= 0; 0 means use program determined value. 36 = Form
            factor, Kf Value >= 0; 0 means use program determined value. 37 = Axial capacity
            correction factor, Kt Value >= 0; 0 means use program determined value. 38 =
            Yield stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 39 =
            Compressive capacity, Nc Value >= 0; 0 means use program determined value. [F]
            40 = Tensile capacity, Nt Value >= 0; 0 means use program determined value. [F]
            41 = Major bending capacity, Ms33 Value >= 0; 0 means use program determined
            value. [FL] 42 = Minor bending capacity, Ms22 Value >= 0; 0 means use program
            determined value. [FL] 43 = Minor bending capacity, Mb33 Value >= 0; 0 means use
            program determined value. [FL] 44 = Major shear capacity, Vu2 Value >= 0; 0
            means use program determined value. [F] 45 = Minor shear capacity, Vu3 Value >=
            0; 0 means use program determined value. [F] 46 = Demand/capacity ratio limit
            Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.NewZealand_NZS3404_1997.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set, otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 17, inclusive, indicating the
            preference item considered. 1 = Multi-response case design 2 = Framing type 3 =
            Structural analysis method 4 = Steel type 5 = Capacity factor, Phi bending 6 =
            Capacity factor, Phi compression 7 = Capacity factor, Phi tension yielding 8 =
            Capacity factor, Phi tension fracture 9 = Capacity factor, Phi shear 10 =
            Consider deflection 11 = DL deflection limit, L/Value 12 = SDL + LL deflection
            limit, L/Value 13 = LL deflection limit, L/Value 14 = Total load deflection
            limit, L/Value 15 = Total camber limit, L/Value 16 = Pattern live load factor 17
            = Demand/capacity ratio limit
        Value (input): The value of the considered preference item. 1 = Multi-response case
            design 1 = Envelopes 2 = Step-by step 3 = Last step 4 = Envelopes - All 5 =
            Step-by step - All 2 = Framing type 1 = Moment frame 2 = Braced frame 3 =
            Structural analysis method 1 = General 2nd Order 2 = Amplified 1st Order 4 =
            Steel type 1 = Hot rolled 2 = Hot finished 3 = Cold form 4 = Stress relieved 5 =
            Lightly welded 6 = Heavily welded 5 = Capacity factor, Phi bending Value > 0 6 =
            Capacity factor, Phi compression Value > 0 7 = Capacity factor, Phi tension
            yielding Value > 0 8 = Capacity factor, Phi tension fracture Value > 0 9 =
            Capacity factor, Phi shear Value > 0 10 = Consider deflection 0 = No Any other
            value = Yes 11 = DL deflection limit, L/Value Value > 0 12 = SDL + LL deflection
            limit, L/Value Value > 0 13 = LL deflection limit, L/Value Value > 0 14 = Total
            load deflection limit, L/Value Value > 0 15 = Total camber limit, L/Value Value
            > 0 16 = Pattern live load factor Value >= 0 17 = Demand/capacity ratio limit
            Value > 0
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.NewZealand_NZS3404_1997.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_Italian_UNI_10011:
    """Wrapper para SapModel.DesignSteel.Italian_UNI_10011."""

    def __init__(self, raw):
        self._raw = raw

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 10, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Consider deflection 3 = DL
            deflection limit, L/Value 4 = SDL + LL deflectionlimit, L/Value 5 = LL
            deflection limit, L/Value 6 = Total deflectionlimit, L/Value 7 = Total camber
            limit, L/Value 8 = Pattern live load factor 9 = Demand/capacity ratio limit 10 =
            Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Sway Frame 2 = NonSway Frame 2 = Consider deflection 0 = No Any other value =
            Yes 3 = DL deflection limit, L/Value Value > 0 4 = SDL + LL deflection limit,
            L/Value Value > 0 5 = LL deflection limit, L/Value Value > 0 6 = Total
            deflection limit, L/Value Value > 0 7 = Total camber limit, L/Value Value > 0 8
            = Pattern live load factor Value >= 0 9 = Demand/capacity ratio limit Value > 0
            10 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 =
            Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Italian_UNI_10011.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 10, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Consider deflection 3 = DL
            deflection limit, L/Value 4 = SDL + LL deflectionlimit, L/Value 5 = LL
            deflection limit, L/Value 6 = Total deflectionlimit, L/Value 7 = Total camber
            limit, L/Value 8 = Pattern live load factor 9 = Demand/capacity ratio limit 10 =
            Multi-response case design
        Value (input): The value of the considered preference item. 1 = Framing type 1 =
            Sway Frame 2 = NonSway Frame 2 = Consider deflection 0 = No Any other value =
            Yes 3 = DL deflection limit, L/Value Value > 0 4 = SDL + LL deflection limit,
            L/Value Value > 0 5 = LL deflection limit, L/Value Value > 0 6 = Total
            deflection limit, L/Value Value > 0 7 = Total camber limit, L/Value Value > 0 8
            = Pattern live load factor Value >= 0 9 = Demand/capacity ratio limit Value > 0
            10 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 =
            Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Italian_UNI_10011.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_CISC_95:
    """Wrapper para SapModel.DesignSteel.CISC_95."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 35, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, Omega1 Major 22 = Moment
            coefficient, Omega1 Minor 23 = Bending coefficient, Cb 24 = Non-sway moment
            factor, U1 Major 25 = Non-sway moment factor, U1 Minor 26 = Sway moment factor,
            U2 Major 27 = Sway moment factor, U2 Minor 28 = Yield stress, Fy 29 =
            Compressive capacity, Cr 30 = Tensile capacity, Tr 31 = Major bending capacity,
            Mr3 32 = Minor bending capacity, Mr2 33 = Major shear capacity, Vr2 34 = Minor
            shear capacity, Vr3 35 = Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 19
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Moment coefficient, Omega1 Major Value >= 0; 0 means use
            program determined value. 22 = Moment coefficient, Omega1 Minor Value >= 0; 0
            means use program determined value. 23 = Bending coefficient, Omega2 Value >= 0;
            0 means use program determined value. 24 = Nonsway moment factor, U1 Major Value
            >= 0; 0 means use program determined value. 25 = Nonsway moment factor, U1 Minor
            Value >= 0; 0 means use program determined value. 26 = Sway moment factor, U2
            Major Value >= 0; 0 means use program determined value. 27 = Sway moment factor,
            U2 Minor Value >= 0; 0 means use program determined value. 28 = Yield stress, Fy
            Value >= 0; 0 means use program determined value. [F/L 2 ] 29 = Compressive
            capacity, Cr Value >= 0; 0 means use program determined value. [F] 30 = Tensile
            capacity, Tr Value >= 0; 0 means use program determined value. [F] 31 = Major
            bending capacity, Mr3 Value >= 0; 0 means use program determined value. [FL] 32
            = Minor bending capacity, Mr2 Value >= 0; 0 means use program determined value.
            [FL] 33 = Major shear capacity, Vr2 Value >= 0; 0 means use program determined
            value. [F] 34 = Minor shear capacity, Vr3 Value >= 0; 0 means use program
            determined value. [F] 35 = Demand/capacity ratio limit Value >= 0; 0 means use
            program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.CISC_95.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 14, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Phi bending 3 = Phi compression
            4 = Phi tension 5 = Phi shear 6 = Consider deflection 7 = DL deflection limit,
            L/Value 8 = SDL + LL deflection limit, L/Value 9 = LL deflection limit, L/Value
            10 = Total deflection limit, L/Value 11 = Total camber limit, L/Value 12 =
            Pattern live load factor 13 = Demand/capacity ratio limit 14 = Multi-response
            case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Phi bending Value > 0 3 = Phi compression
            Value > 0 4 = Phi tension Value > 0 5 = Phi shear Value > 0 6 = Consider
            deflection 0 = No Any other value = Yes 7 = DL deflection limit, L/Value Value >
            0 8 = SDL + LL deflection limit, L/Value Value > 0 9 = LL deflection limit,
            L/Value Value > 0 10 = Total load deflection limit, L/Value Value > 0 11 = Total
            camber limit, L/Value Value > 0 12 = Pattern live load factor Value >= 0 13 =
            Demand/capacity ratio limit Value > 0 14 = Multi-response case design 1 =
            Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step
            -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.CISC_95.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 35, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, Omega1 Major 22 = Moment
            coefficient, Omega1 Minor 23 = Bending coefficient, Cb 24 = Non-sway moment
            factor, U1 Major 25 = Non-sway moment factor, U1 Minor 26 = Sway moment factor,
            U2 Major 27 = Sway moment factor, U2 Minor 28 = Yield stress, Fy 29 =
            Compressive capacity, Cr 30 = Tensile capacity, Tr 31 = Major bending capacity,
            Mr3 32 = Minor bending capacity, Mr2 33 = Major shear capacity, Vr2 34 = Minor
            shear capacity, Vr3 35 = Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 19
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Moment coefficient, Omega1 Major Value >= 0; 0 means use
            program determined value. 22 = Moment coefficient, Omega1 Minor Value >= 0; 0
            means use program determined value. 23 = Bending coefficient, Omega2 Value >= 0;
            0 means use program determined value. 24 = Non-sway moment factor, U1 Major
            Value >= 0; 0 means use program determined value. 25 = Non-sway moment factor,
            U1 Minor Value >= 0; 0 means use program determined value. 26 = Sway moment
            factor, U2 Major Value >= 0; 0 means use program determined value. 27 = Sway
            moment factor, U2 Minor Value >= 0; 0 means use program determined value. 28 =
            Yield stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 29 =
            Compressive capacity, Cr Value >= 0; 0 means use program determined value. [F]
            30 = Tensile capacity, Tr Value >= 0; 0 means use program determined value. [F]
            31 = Major bending capacity, Mr3 Value >= 0; 0 means use program determined
            value. [FL] 32 = Minor bending capacity, Mr2 Value >= 0; 0 means use program
            determined value. [FL] 33 = Major shear capacity, Vr2 Value >= 0; 0 means use
            program determined value. [F] 34 = Minor shear capacity, Vr3 Value >= 0; 0 means
            use program determined value. [F] 35 = Demand/capacity ratio limit Value >= 0; 0
            means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.CISC_95.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 14, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Phi bending 3 = Phi compression
            4 = Phi tension 5 = Phi shear 6 = Consider deflection 7 = DL deflection limit,
            L/Value 8 = SDL + LL deflection limit, L/Value 9 = LL deflection limit, L/Value
            10 = Total deflection limit, L/Value 11 = Total camber limit, L/Value 12 =
            Pattern live load factor 13 = Demand/capacity ratio limit 14 = Multi-response
            case design
        Value (input): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Phi bending Value > 0 3 = Phi compression
            Value > 0 4 = Phi tension Value > 0 5 = Phi shear Value > 0 6 = Consider
            deflection 0 = No Any other value = Yes 7 = DL deflection limit, L/Value Value >
            0 8 = SDL + LL deflection limit, L/Value Value > 0 9 = LL deflection limit,
            L/Value Value > 0 10 = Total load deflection limit, L/Value Value > 0 11 = Total
            camber limit, L/Value Value > 0 12 = Pattern live load factor Value >= 0 13 =
            Demand/capacity ratio limit Value > 0 14 = Multi-response case design 1 =
            Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step
            -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.CISC_95.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_AISC_LRFD99:
    """Wrapper para SapModel.DesignSteel.AISC_LRFD99."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 37, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Omega0 3 = Consider deflection 4
            = Deflection check type 5 = DL deflection limit, L/Value 6 = SDL + LL deflection
            limit, L/Value 7 = LL deflection limit, L/Value 8 = Total load deflection limit,
            L/Value 9 = Total camber limit, L/Value 10 = DL deflection limit, absolute 11 =
            SDL + LL deflection limit, absolute 12 = LL deflection limit, absolute 13 =
            Total load deflection limit, absolute 14 = Total camber limit, absolute 15 =
            Specified camber 16 = Net area to total area ratio 17 = Live load reduction
            factor 18 = Unbraced length ratio, Major 19 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 20 = Effective length factor, K Major 21 = Effective
            length factor, K Minor 22 = Moment coefficient, Cm Major 23 = Moment
            coefficient, Cm Minor 24 = Bending coefficient, Cb 25 = Non-sway moment factor,
            B1 Major 26 = Non-sway moment factor, B1 Minor 27 = Sway moment factor, B2 Major
            28 = Sway moment factor, B2 Minor 29 = Yield stress, Fy 30 = Expected to
            specified Fy ratio, Ry 31 = Compressive capacity, phi*Pnc 32 = Tensile capacity,
            phi*Pnt 33 = Major bending capacity, phi*Mn3 34 = Minor bending capacity,
            phi*Mn2 35 = Major shear capacity, phi*Vn2 36 = Minor shear capacity, phi*Vn3 37
            = Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = OMF 2 = IMF 3 = SMF 4 = OCBF 5 = SCBF 6 = EBF 2 = Omega0
            Value >= 0; 0 means use a program determined value. 3 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 4 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 5 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 6 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 7 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 8 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 9 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 10 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 11 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 12 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 13 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 14 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 15 =
            Specified camber Value >= 0. [L] 16 = Net area to total area ratio Value >= 0; 0
            means use program default value. 17 = Live load reduction factor Value >= 0; 0
            means use program determined value. 18 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 19 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 20
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 21 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 22 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 23 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 24 = Bending coefficient, Cb Value >= 0; 0 means
            use program determined value. 25 = Non-sway moment factor, B1 Major Value >= 0;
            0 means use program determined value. 26 = Non-sway moment factor, B1 Minor
            Value >= 0; 0 means use program determined value. 27 = Sway moment factor, B2
            Major Value >= 0; 0 means use program determined value. 28 = Sway moment factor,
            B2 Minor Value >= 0; 0 means use program determined value. 29 = Yield stress, Fy
            Value >= 0; 0 means use program determined value. [F/L 2 ] 30 = Expected to
            specified Fy ratio, Ry Value >= 0; 0 means use program determined value. 31 =
            Compressive capacity, phi*Pnc Value >= 0; 0 means use program determined value.
            [F] 32 = Tensile capacity, phi*Pnt Value >= 0; 0 means use program determined
            value. [F] 33 = Major bending capacity, phi*Mn3 Value >= 0; 0 means use program
            determined value. [FL] 34 = Minor bending capacity, phi*Mn2 Value >= 0; 0 means
            use program determined value. [FL] 35 = Major shear capacity, phi*Vn2 Value >=
            0; 0 means use program determined value. [F] 36 = Minor shear capacity, phi*Vn3
            Value >= 0; 0 means use program determined value. [F] 37 = Demand/capacity ratio
            limit Value >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC_LRFD99.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 21, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Seismic design capacity 3 = Phi
            bending 4 = Phi compression 5 = Phi tension - yielding 6 = Phi tension -
            fracture 7 = Phi shear 8 = Phi shear - torsion 9 = Phi compression, angle 10 =
            Ignore seismic code 11 = Ignore special seismic code 12 = Is doubler plate plug-
            welded 13 = Consider deflection 14 = DL deflection limit, L/Value 15 = SDL + LL
            deflection limit, L/Value 16 = LL deflection limit, L/Value 17 = Total
            deflection limit, L/Value 18 = Total camber limit, L/Value 19 = Pattern live
            load factor 20 = Demand capacity ratio limit 21 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            OMF 2 = IMF 3 = SMF 4 = OCBF 5 = SCBF 6 = EBF 2 = Seismic design capacity 1 = A
            2 = B 3 = C 4 = D 5 = E 6 = F 3 = Phi bending Value > 0 4 = Phi compression
            Value > 0 5 = Phi tension – yielding Value > 0 6 = Phi tension - fracture Value
            > 0 7 = Phi shear Value > 0 8 = Phi shear - torsion Value > 0 9 = Phi
            compression, angle Value > 0 10 = Ignore seismic code 0 = No Any other value =
            Yes 11 = Ignore special seismic code 0 = No Any other value = Yes 12 = Is
            doubler plate plug-welded 0 = No Any other value = Yes 13 = Consider deflection
            0 = No Any other value = Yes 14 = DL deflection limit, L/Value Value > 0 15 =
            SDL + LL deflection limit, L/Value Value > 0 16 = LL deflection limit, L/Value
            Value > 0 17 = Total deflection limit, L/Value Value > 0 18 = Total camber
            limit, L/Value Value > 0 19 = Pattern live load factor Value >= 0 20 = Demand
            capacity ratio limit Value > 0 21 = Multi-response case design 1 = Envelopes 2 =
            Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC_LRFD99.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 37, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Omega0 3 = Consider deflection 4
            = Deflection check type 5 = DL deflection limit, L/Value 6 = SDL + LL deflection
            limit, L/Value 7 = LL deflection limit, L/Value 8 = Total load deflection limit,
            L/Value 9 = Total camber limit, L/Value 10 = DL deflection limit, absolute 11 =
            SDL + LL deflection limit, absolute 12 = LL deflection limit, absolute 13 =
            Total load deflection limit, absolute 14 = Total camber limit, absolute 15 =
            Specified camber 16 = Net area to total area ratio 17 = Live load reduction
            factor 18 = Unbraced length ratio, Major 19 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 20 = Effective length factor, K Major 21 = Effective
            length factor, K Minor 22 = Moment coefficient, Cm Major 23 = Moment
            coefficient, Cm Minor 24 = Bending coefficient, Cb 25 = Non-sway moment factor,
            B1 Major 26 = Non-sway moment factor, B1 Minor 27 = Sway moment factor, B2 Major
            28 = Sway moment factor, B2 Minor 29 = Yield stress, Fy 30 = Expected to
            specified Fy ratio, Ry 31 = Compressive capacity, phi*Pnc 32 = Tensile capacity,
            phi*Pnt 33 = Major bending capacity, phi*Mn3 34 = Minor bending capacity,
            phi*Mn2 35 = Major shear capacity, phi*Vn2 36 = Minor shear capacity, phi*Vn3 37
            = Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = OMF 2 = IMF 3 = SMF 4 = OCBF 5 = SCBF 6 = EBF 2 = Omega0
            Value >= 0; 0 means use a program determined value. 3 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 4 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 5 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 6 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 7 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 8 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 9 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 10 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 11 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 12 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 13 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 14 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 15 =
            Specified camber Value >= 0. [L] 16 = Net area to total area ratio Value >= 0; 0
            means use program default value. 17 = Live load reduction factor Value >= 0; 0
            means use program determined value. 18 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 19 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 20
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 21 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 22 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 23 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 24 = Bending coefficient, Cb Value >= 0; 0 means
            use program determined value. 25 = Nonsway moment factor, B1 Major Value >= 0; 0
            means use program determined value. 26 = Nonsway moment factor, B1 Minor Value
            >= 0; 0 means use program determined value. 27 = Sway moment factor, B2 Major
            Value >= 0; 0 means use program determined value. 28 = Sway moment factor, B2
            Minor Value >= 0; 0 means use program determined value. 29 = Yield stress, Fy
            Value >= 0; 0 means use program determined value. [F/L 2 ] 30 = Expected to
            specified Fy ratio, Ry Value >= 0; 0 means use program determined value. 31 =
            Compressive capacity, phi*Pnc Value >= 0; 0 means use program determined value.
            [F] 32 = Tensile capacity, phi*Pnt Value >= 0; 0 means use program determined
            value. [F] 33 = Major bending capacity, phi*Mn3 Value >= 0; 0 means use program
            determined value. [FL] 34 = Minor bending capacity, phi*Mn2 Value >= 0; 0 means
            use program determined value. [FL] 35 = Major shear capacity, phi*Vn2 Value >=
            0; 0 means use program determined value. [F] 36 = Minor shear capacity, phi*Vn3
            Value >= 0; 0 means use program determined value. [F] 37 = Demand/capacity ratio
            limit Value >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC_LRFD99.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 21, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Seismic design capacity 3 = Phi
            bending 4 = Phi compression 5 = Phi tension - yielding 6 = Phi tension -
            fracture 7 = Phi shear 8 = Phi shear - torsion 9 = Phi compression, angle 10 =
            Ignore seismic code 11 = Ignore special seismic code 12 = Is doubler plate plug-
            welded 13 = Consider deflection 14 = DL deflection limit, L/Value 15 = SDL + LL
            deflection limit, L/Value 16 = LL deflection limit, L/Value 17 = Total
            deflection limit, L/Value 18 = Total camber limit, L/Value 19 = Pattern live
            load factor 20 = Demand capacity ratio limit 21 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            OMF 2 = IMF 3 = SMF 4 = OCBF 5 = SCBF 6 = EBF 2 = Seismic design capacity 1 = A
            2 = B 3 = C 4 = D 5 = E 6 = F 3 = Phi bending Value > 0 4 = Phi compression
            Value > 0 5 = Phi tension – yielding Value > 0 6 = Phi tension - fracture Value
            > 0 7 = Phi shear Value > 0 8 = Phi shear - torsion Value > 0 9 = Phi
            compression, angle Value > 0 10 = Ignore seismic code 0 = No Any other value =
            Yes 11 = Ignore special seismic code 0 = No Any other value = Yes 12 = Is
            doubler plate plug-welded 0 = No Any other value = Yes 13 = Consider deflection
            0 = No Any other value = Yes 14 = DL deflection limit, L/Value Value > 0 15 =
            SDL + LL deflection limit, L/Value Value > 0 16 = LL deflection limit, L/Value
            Value > 0 17 = Total deflection limit, L/Value Value > 0 18 = Total camber
            limit, L/Value Value > 0 19 = Pattern live load factor Value >= 0 20 = Demand
            capacity ratio limit Value > 0 21 = Multi-response case design 1 = Envelopes 2 =
            Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC_LRFD99.SetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]


class N_DesignSteel_AISC_LRFD93:
    """Wrapper para SapModel.DesignSteel.AISC_LRFD93."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 35, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, Cm Major 22 = Moment
            coefficient, Cm Minor 23 = Bending coefficient, Cb 24 = Non-sway moment factor,
            B1 Major 25 = Non-sway moment factor, B1 Minor 26 = Sway moment factor, B2 Major
            27 = Sway moment factor, B2 Minor 28 = Yield stress, Fy 29 = Compressive
            capacity, phi*Pnc 30 = Tensile capacity, phi*Pnt 31 = Major bending capacity,
            phi*Mn3 32 = Minor bending capacity, phi*Mn2 33 = Major shear capacity, phi*Vn2
            34 = Minor shear capacity, phi*Vn3 35 = Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 19
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 22 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 23 = Bending coefficient, Cb Value >= 0; 0 means
            use program determined value. 24 = Non-sway moment factor, B1 Major Value >= 0;
            0 means use program determined value. 25 = Non-sway moment factor, B1 Minor
            Value >= 0; 0 means use program determined value. 26 = Sway moment factor, B2
            Major Value >= 0; 0 means use program determined value. 27 = Sway moment factor,
            B2 Minor Value >= 0; 0 means use program determined value. 28 = Yield stress, Fy
            Value >= 0; 0 means use program determined value. [F/L 2 ] 29 = Compressive
            capacity, phi*Pnc Value >= 0; 0 means use program determined value. [F] 30 =
            Tensile capacity, phi*Pnt Value >= 0; 0 means use program determined value. [F]
            31 = Major bending capacity, phi*Mn3 Value >= 0; 0 means use program determined
            value. [FL] 32 = Minor bending capacity, phi*Mn2 Value >= 0; 0 means use program
            determined value. [FL] 33 = Major shear capacity, phi*Vn2 Value >= 0; 0 means
            use program determined value. [F] 34 = Minor shear capacity, phi*Vn3 Value >= 0;
            0 means use program determined value. [F] 35 = Demand/capacity ratio limit Value
            >= 0; 0 means use program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC_LRFD93.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 15, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Phi bending 3 = Phi compression
            4 = Phi tension 5 = Phi shear 6 = Phi compression, angle 7 = Consider deflection
            8 = DL deflection limit, L/Value 9 = SDL + LL deflection limit, L/Value 10 = LL
            deflection limit, L/Value 11 = Total deflection limit, L/Value 12 = Total camber
            limit, L/Value 13 = Pattern live load factor 14 = Demand/capacity ratio limit 15
            = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Phi bending Value > 0 3 = Phi compression
            Value > 0 4 = Phi tension Value > 0 5 = Phi shear Value > 0 6 = Phi compression,
            angle Value > 0 7 = Consider deflection 0 = No Any other value = Yes 8 = DL
            deflection limit, L/Value Value > 0 9 = SDL + LL deflection limit, L/Value Value
            > 0 10 = LL deflection limit, L/Value Value > 0 11 = Total deflection limit,
            L/Value Value > 0 12 = Total camber limit, L/Value Value > 0 13 = Pattern live
            load factor Value >= 0 14 = Demand/capacity ratio limit Value > 0 15 = Multi-
            response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes
            -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC_LRFD93.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 35, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Consider deflection 3 =
            Deflection check type 4 = DL deflection limit, L/Value 5 = SDL + LL deflection
            limit, L/Value 6 = LL deflection limit, L/Value 7 = Total load deflection limit,
            L/Value 8 = Total camber limit, L/Value 9 = DL deflection limit, absolute 10 =
            SDL + LL deflection limit, absolute 11 = LL deflection limit, absolute 12 =
            Total load deflection limit, absolute 13 = Total camber limit, absolute 14 =
            Specified camber 15 = Net area to total area ratio 16 = Live load reduction
            factor 17 = Unbraced length ratio, Major 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 19 = Effective length factor, K Major 20 = Effective
            length factor, K Minor 21 = Moment coefficient, Cm Major 22 = Moment
            coefficient, Cm Minor 23 = Bending coefficient, Cb 24 = Non-sway moment factor,
            B1 Major 25 = Non-sway moment factor, B1 Minor 26 = Sway moment factor, B2 Major
            27 = Sway moment factor, B2 Minor 28 = Yield stress, Fy 29 = Compressive
            capacity, phi*Pnc 30 = Tensile capacity, phi*Pnt 31 = Major bending capacity,
            phi*Mn3 32 = Minor bending capacity, phi*Mn2 33 = Major shear capacity, phi*Vn2
            34 = Minor shear capacity, phi*Vn3 35 = Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Consider deflection 0 =
            Program Determined 1 = No 2 = Yes 3 = Deflection check type 0 = Program default
            1 = Ratio 2 = Absolute 3 = Both 4 = DL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 5 = SDL + LL deflection limit, L/Value Value >= 0;
            0 means no check for this item. 6 = LL deflection limit, L/Value Value >= 0; 0
            means no check for this item. 7 = Total load deflection limit, L/Value Value >=
            0; 0 means no check for this item. 8 = Total camber limit, L/Value Value >= 0; 0
            means no check for this item. 9 = DL deflection limit, absolute Value >= 0; 0
            means no check for this item. [L] 10 = SDL + LL deflection limit, absolute Value
            >= 0; 0 means no check for this item. [L] 11 = LL deflection limit, absolute
            Value >= 0; 0 means no check for this item. [L] 12 = Total load deflection
            limit, absolute Value >= 0; 0 means no check for this item. [L] 13 = Total
            camber limit, absolute Value >= 0; 0 means no check for this item. [L] 14 =
            Specified camber Value >= 0. [L] 15 = Net area to total area ratio Value >= 0; 0
            means use program default value. 16 = Live load reduction factor Value >= 0; 0
            means use program determined value. 17 = Unbraced length ratio, Major Value >=
            0; 0 means use program determined value. 18 = Unbraced length ratio, Minor
            Lateral Torsional Buckling Value >= 0; 0 means use program determined value. 19
            = Effective length factor, K Major Value >= 0; 0 means use program determined
            value. 20 = Effective length factor, K Minor Value >= 0; 0 means use program
            determined value. 21 = Moment coefficient, Cm Major Value >= 0; 0 means use
            program determined value. 22 = Moment coefficient, Cm Minor Value >= 0; 0 means
            use program determined value. 23 = Bending coefficient, Cb Value >= 0; 0 means
            use program determined value. 24 = Nonsway moment factor, B1 Major Value >= 0; 0
            means use program determined value. 25 = Nonsway moment factor, B1 Minor Value
            >= 0; 0 means use program determined value. 26 = Sway moment factor, B2 Major
            Value >= 0; 0 means use program determined value. 27 = Sway moment factor, B2
            Minor Value >= 0; 0 means use program determined value. 28 = Yield stress, Fy
            Value >= 0; 0 means use program determined value. [F/L 2 ] 29 = Compressive
            capacity, phi*Pnc Value >= 0; 0 means use program determined value. [F] 30 =
            Tensile capacity, phi*Pnt Value >= 0; 0 means use program determined value. [F]
            31 = Major bending capacity, phi*Mn3 Value >= 0; 0 means use program determined
            value. [FL] 32 = Minor bending capacity, phi*Mn2 Value >= 0; 0 means use program
            determined value. [FL] 33 = Major shear capacity, phi*Vn2 Value >= 0; 0 means
            use program determined value. [F] 34 = Minor shear capacity, phi*Vn3 Value >= 0;
            0 means use program determined value. [F] 35 = Demand/capacity ratio limit Value
            >= 0; 0 means use program determined value.
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects= 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC_LRFD93.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 15, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Phi bending 3 = Phi compression
            4 = Phi tension 5 = Phi shear 6 = Phi compression, angle 7 = Consider deflection
            8 = DL deflection limit, L/Value 9 = SDL + LL deflection limit, L/Value 10 = LL
            deflection limit, L/Value 11 = Total deflection limit, L/Value 12 = Total camber
            limit, L/Value 13 = Pattern live load factor 14 = Demand/capacity ratio limit 15
            = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Phi bending Value > 0 3 = Phi compression
            Value > 0 4 = Phi tension Value > 0 5 = Phi shear Value > 0 6 = Phi compression,
            angle Value > 0 7 = Consider deflection 0 = No Any other value = Yes 8 = DL
            deflection limit, L/Value Value > 0 9 = SDL + LL deflection limit, L/Value Value
            > 0 10 = LL deflection limit, L/Value Value > 0 11 = Total deflection limit,
            L/Value Value > 0 12 = Total camber limit, L/Value Value > 0 13 = Pattern live
            load factor Value >= 0 14 = Demand/capacity ratio limit Value > 0 15 = Multi-
            response case design 1 = Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes
            -- All 5 = Step-by-step -- All
        """
        _r = self._raw.SetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.AISC_LRFD93.SetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]


class N_DesignSteel_UBC97_LRFD:
    """Wrapper para SapModel.DesignSteel.UBC97_LRFD."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 36, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Omega0 3 = Consider deflection 4
            = Deflection check type 5 = DL deflection limit, L/Value 6 = SDL + LL deflection
            limit, L/Value 7 = LL deflection limit, L/Value 8 = Total load deflection limit,
            L/Value 9 = Total camber limit, L/Value 10 = DL deflection limit, absolute 11 =
            SDL + LL deflection limit, absolute 12 = LL deflection limit, absolute 13 =
            Total load deflection limit, absolute 14 = Total camber limit, absolute 15 =
            Specified camber 16 = Net area to total area ratio 17 = Live load reduction
            factor 18 = Unbraced length ratio, Major 19 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 20 = Effective length factor, K Major 21 = Effective
            length factor, K Minor 22 = Moment coefficient, Cm Major 23 = Moment
            coefficient, Cm Minor 24 = Bending coefficient, Cb 25 = Non-sway moment factor,
            B1 Major 26 = Non-sway moment factor, B1 Minor 27 = Sway moment factor, B2 Major
            28 = Sway moment factor, B2 Minor 29 = Yield stress, Fy 30 = Compressive
            capacity, phi*Pnc 31 = Tensile capacity, phi*Pnt 32 = Major bending capacity,
            phi*Mn3 33 = Minor bending capacity, phi*Mn2 34 = Major shear capacity, phi*Vn2
            35 = Minor shear capacity, phi*Vn3 36 = Demand/capacity ratio limit
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Ordinary MRF 2 = Special MRF 3 = Braced Frame 4 = Special
            CBF 5 = EBF 2 = Omega0 Value >= 0; 0 means use a program determined value. 3 =
            Consider deflection 0 = Program Determined 1 = No 2 = Yes 4 = Deflection check
            type 0 = Program default 1 = Ratio 2 = Absolute 3 = Both 5 = DL deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 6 = SDL + LL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 7 = LL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 8 = Total
            load deflection limit, L/Value Value >= 0; 0 means no check for this item. 9 =
            Total camber limit, L/Value Value >= 0; 0 means no check for this item. 10 = DL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 11 =
            SDL + LL deflection limit, absolute Value >= 0; 0 means no check for this item.
            [L] 12 = LL deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 13 = Total load deflection limit, absolute Value >= 0; 0 means no
            check for this item. [L] 14 = Total camber limit, absolute Value >= 0; 0 means
            no check for this item. [L] 15 = Specified camber Value >= 0. [L] 16 = Net area
            to total area ratio Value >= 0; 0 means use program default value. 17 = Live
            load reduction factor Value >= 0; 0 means use program determined value. 18 =
            Unbraced length ratio, Major Value >= 0; 0 means use program determined value.
            19 = Unbraced length ratio, Minor Lateral Torsional Buckling Value >= 0; 0 means
            use program determined value. 20 = Effective length factor, K Major Value >= 0;
            0 means use program determined value. 21 = Effective length factor, K Minor
            Value >= 0; 0 means use program determined value. 22 = Moment coefficient, Cm
            Major Value >= 0; 0 means use program determined value. 23 = Moment coefficient,
            Cm Minor Value >= 0; 0 means use program determined value. 24 = Bending
            coefficient, Cb Value >= 0; 0 means use program determined value. 25 = Nonsway
            moment factor, B1 Major Value >= 0; 0 means use program determined value. 26 =
            Nonsway moment factor, B1 Minor Value >= 0; 0 means use program determined
            value. 27 = Sway moment factor, B2 Major Value >= 0; 0 means use program
            determined value. 28 = Sway moment factor, B2 Minor Value >= 0; 0 means use
            program determined value. 29 = Yield stress, Fy Value >= 0; 0 means use program
            determined value. [F/L 2 ] 30 = Compressive capacity, phi*Pnc Value >= 0; 0
            means use program determined value. [F] 31 = Tensile capacity, phi*Pnt Value >=
            0; 0 means use program determined value. [F] 32 = Major bending capacity,
            phi*Mn3 Value >= 0; 0 means use program determined value. [FL] 33 = Minor
            bending capacity, phi*Mn2 Value >= 0; 0 means use program determined value. [FL]
            34 = Major shear capacity, phi*Vn2 Value >= 0; 0 means use program determined
            value. [F] 35 = Minor shear capacity, phi*Vn3 Value >= 0; 0 means use program
            determined value. [F] 36 = Demand/capacity ratio limit Value >= 0; 0 means use
            program determined value.
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.UBC97_LRFD.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 12, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Importance factor 3 = Seismic
            zone 4 = Phi bending 5 = Phi compression 6 = Phi tension 7 = Phi shear 8 = Phi
            compression angle 9 = Consider deflection 10 = DL deflection limit, L/Value 11 =
            SDL + LL deflection limit, L/Value 12 = LL deflection limit, L/Value 13 = Total
            deflection limit, L/Value 14 = Total camber limit, L/Value 15 = Pattern live
            load factor 16 = Demand/capacity ratio limit 17 = Multi-response case design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Ordinary MRF 2 = Special MRF 3 = Braced Frame 4 = Special CBF 5 = EBF 2 =
            Importance factor Value > 0 3 = Seismic zone 1 = Zone 0 2 = Zone 1 3 = Zone 2 4
            = Zone 3 5 = Zone 4 3 = Lateral factor Value > 0 4 = Phi bending Value > 0 5 =
            Phi compression Value > 0 6 = Phi tension Value > 0 7 = Phi shear Value > 0 8 =
            Phi compression angle Value > 0 9 = Consider deflection 0 = No Any other value =
            Yes 10 = DL deflection limit, L/Value Value > 0 11 = SDL + LL deflection limit,
            L/Value Value > 0 12 = LL deflection limit, L/Value Value > 0 13 = Total
            deflection limit, L/Value Value > 0 14 = Total camber limit, L/Value Value > 0
            15 = Pattern live load factor Value >= 0 16 = Demand/capacity ratio limit Value
            > 0 17 = Multi-response case design 1 = Envelopes 2 = Step-by-step 3 = Last step
            4 = Envelopes -- All 5 = Step-by-step -- All
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.UBC97_LRFD.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 36, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Omega0 3 = Consider deflection 4
            = Deflection check type 5 = DL deflection limit, L/Value 6 = SDL + LL deflection
            limit, L/Value 7 = LL deflection limit, L/Value 8 = Total load deflection limit,
            L/Value 9 = Total camber limit, L/Value 10 = DL deflection limit, absolute 11 =
            SDL + LL deflection limit, absolute 12 = LL deflection limit, absolute 13 =
            Total load deflection limit, absolute 14 = Total camber limit, absolute 15 =
            Specified camber 16 = Net area to total area ratio 17 = Live load reduction
            factor 18 = Unbraced length ratio, Major 19 = Unbraced length ratio, Minor
            Lateral Torsional Buckling 20 = Effective length factor, K Major 21 = Effective
            length factor, K Minor 22 = Moment coefficient, Cm Major 23 = Moment
            coefficient, Cm Minor 24 = Bending coefficient, Cb 25 = Non-sway moment factor,
            B1 Major 26 = Non-sway moment factor, B1 Minor 27 = Sway moment factor, B2 Major
            28 = Sway moment factor, B2 Minor 29 = Yield stress, Fy 30 = Compressive
            capacity, phi*Pnc 31 = Tensile capacity, phi*Pnt 32 = Major bending capacity,
            phi*Mn3 33 = Minor bending capacity, phi*Mn2 34 = Major shear capacity, phi*Vn2
            35 = Minor shear capacity, phi*Vn3 36 = Demand/capacity ratio limit
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Ordinary MRF 2 = Special MRF 3 = Braced Frame 4 = Special
            CBF 5 = EBF 2 = Omega0 Value >= 0; 0 means use a program determined value. 3 =
            Consider deflection 0 = Program Determined 1 = No 2 = Yes 4 = Deflection check
            type 0 = Program default 1 = Ratio 2 = Absolute 3 = Both 5 = DL deflection
            limit, L/Value Value >= 0; 0 means no check for this item. 6 = SDL + LL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 7 = LL
            deflection limit, L/Value Value >= 0; 0 means no check for this item. 8 = Total
            load deflection limit, L/Value Value >= 0; 0 means no check for this item. 9 =
            Total camber limit, L/Value Value >= 0; 0 means no check for this item. 10 = DL
            deflection limit, absolute Value >= 0; 0 means no check for this item. [L] 11 =
            SDL + LL deflection limit, absolute Value >= 0; 0 means no check for this item.
            [L] 12 = LL deflection limit, absolute Value >= 0; 0 means no check for this
            item. [L] 13 = Total load deflection limit, absolute Value >= 0; 0 means no
            check for this item. [L] 14 = Total camber limit, absolute Value >= 0; 0 means
            no check for this item. [L] 15 = Specified camber Value >= 0. [L] 16 = Net area
            to total area ratio Value >= 0; 0 means use program default value. 17 = Live
            load reduction factor Value >= 0; 0 means use program determined value. 18 =
            Unbraced length ratio, Major Value >= 0; 0 means use program determined value.
            19 = Unbraced length ratio, Minor Lateral Torsional Buckling Value >= 0; 0 means
            use program determined value. 20 = Effective length factor, K Major Value >= 0;
            0 means use program determined value. 21 = Effective length factor, K Minor
            Value >= 0; 0 means use program determined value. 22 = Moment coefficient, Cm
            Major Value >= 0; 0 means use program determined value. 23 = Moment coefficient,
            Cm Minor Value >= 0; 0 means use program determined value. 24 = Bending
            coefficient, Cb Value >= 0; 0 means use program determined value. 25 = Nonsway
            moment factor, B1 Major Value >= 0; 0 means use program determined value. 26 =
            Nonsway moment factor, B1 Minor Value >= 0; 0 means use program determined
            value. 27 = Sway moment factor, B2 Major Value >= 0; 0 means use program
            determined value. 28 = Sway moment factor, B2 Minor Value >= 0; 0 means use
            program determined value. 29 = Yield stress, Fy Value >= 0; 0 means use program
            determined value. [F/L 2 ] 30 = Compressive capacity, phi*Pnc Value >= 0; 0
            means use program determined value. [F] 31 = Tensile capacity, phi*Pnt Value >=
            0; 0 means use program determined value. [F] 32 = Major bending capacity,
            phi*Mn3 Value >= 0; 0 means use program determined value. [FL] 33 = Minor
            bending capacity, phi*Mn2 Value >= 0; 0 means use program determined value. [FL]
            34 = Major shear capacity, phi*Vn2 Value >= 0; 0 means use program determined
            value. [F] 35 = Minor shear capacity, phi*Vn3 Value >= 0; 0 means use program
            determined value. [F] 36 = Demand/capacity ratio limit Value >= 0; 0 means use
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
            raise Sap2000ApiError("SapModel.DesignSteel.UBC97_LRFD.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 17, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Importance factor 3 = Seismic
            zone 4 = Phi bending 5 = Phi compression 6 = Phi tension 7 = Phi shear 8 = Phi
            compression angle 9 = Consider deflection 10 = DL deflection limit, L/Value 11 =
            SDL + LL limit, L/Value 12 = Live load limit, L/Value 13 = Total limit, L/Value
            14 = Total camber limit, L/Value 15 = Pattern live load factor 16 =
            Demand/capacity ratio limit 17 = Multi-response case design
        Value (input): The value of the considered preference item. 1 = Framing type 1 =
            Ordinary MRF 2 = Special MRF 3 = Braced Frame 4 = Special CBF 5 = EBF 2 =
            Importance factor Value > 0 3 = Seismic zone 1 = Zone 0 2 = Zone 1 3 = Zone 2 4
            = Zone 3 5 = Zone 4 3 = Lateral factor Value > 0 4 = Phi bending Value > 0 5 =
            Phi compression Value > 0 6 = Phi tension Value > 0 7 = Phi shear Value > 0 8 =
            Phi compression angle Value > 0 9 = Consider deflection 0 = No Any other value =
            Yes 10 = DL limit, L/Value Value > 0 11 = Super DL + LL limit, L/Value Value > 0
            12 = Live load limit, L/Value Value > 0 13 = Total limit, L/Value Value > 0 14 =
            Total camber limit, L/Value Value > 0 15 = Pattern live load factor Value >= 0
            16 = Demand/capacity ratio limit Value > 0 17 = Multi-response case design 1 =
            Envelopes 2 = Step-by-step 3 = Last step 4 = Envelopes -- All 5 = Step-by-step
            -- All
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.UBC97_LRFD.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignSteel_Italian_NTC_2018:
    """Wrapper para SapModel.DesignSteel.Italian_NTC_2018."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Name (input): The name of a frame object with a steel frame design procedure.
        Item (input): This is an integer between 1 and 49, inclusive, indicating the
            overwrite item considered. 1 = Current Design Section 2 = Framing type 3 =
            Consider deflection 4 = Deflection check type 5 = DL deflection limit, L/Value 6
            = SDL + LL deflection limit, L/Value 7 = LL deflection limit, L/Value 8 = Total
            load deflection limit, L/Value 9 = Total camber limit, L/Value 10 = DL
            deflection limit, absolute 11 = SDL + LL deflection limit, absolute 12 = LL
            deflection limit, absolute 13 = Total load deflection limit, absolute 14 = Total
            camber limit, absolute 15 = Specified camber 16 = Net area to total area ratio
            17 = Live load reduction factor 18 = Unbraced length ratio, Major 19 = Unbraced
            length ratio, Minor 20 = Effective length factor, K2 Major 21 = Effective length
            factor, K2 Minor 22 = Moment coefficient, kyy Major 23 = Moment coefficient, kzz
            Minor 24 = Bending coefficient, C1 25 = Moment coefficient, kzy 26 = Moment
            coefficient, kyz 27 = Yield stress, Fy 28 = Compressive capacity, Nc.Rd 29 =
            Tensile capacity, Nt.Rd 30 = Major bending capacity, Mc3.Rd 31 = Minor bending
            capacity, Mc2.Rd 32 = Buckling resistance moment, Mb.Rd 33 = Major shear
            capacity, V2.Rd 34 = Minor shear capacity, V3.RD 35 = Demand/capacity ratio
            limit 36 = Section class 37 = Column buckling curve, y-y 38 = Column buckling
            curve, z-z 39 = Buckling curve for LTB 40 = System overstrength factor, Omega 41
            = Is rolled section 42 = Unbraced length ratio, LTB 43 = Effective length factor
            braced, K1 Major 44 = Effective length factor braced, K1 Minor 45 = Effective
            length factor, K LTB 46 = Material overstrength factor, GammaRd 47 = Warping
            constant, Iw 48 = Elastic torsional buckling force, Ncr T 49 = Elastic
            torsional-flexural buckling force, Ncr TF
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, "", 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Italian_NTC_2018.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPreference(self, Item: int):
        """This function retrieves the value of a steel design preference item. The function returns
        zero if the item is successfully retrieved; otherwise, it returns a nonzero value.
    
        Item (input): This is an integer between 3 and 23, inclusive, indicating the
            preference item considered. 3 = Method Used for Buckling in P-M-M 4 = Framing
            type 5 = GammaM0 6 = GammeM1 7 = GammaM2 8 = Consider deflection 9 = DL
            deflection limit, L/Value 10 = SDL + LL deflection limit, L/Value 11 = LL
            deflection limit, L/Value 12 = Total deflection limit, L/Value 13 = Total camber
            limit, L/Value 14 = Pattern live load factor 15 = Demand/capacity ratio limit 16
            = Multi-Response Case Design 17 = Behavior Factor, q 0 18 = System Overstrength
            Factor, W 19 = Consider P-Delta 20 = Consider Torsion 21 = Ignore Seismic Code
            22 = Ignore Special Seismic Load 23 = Is Doubler Plate Plug-Welded
        """
        _r = self._raw.GetPreference(Item, "", 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Italian_NTC_2018.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetOverwrite(self, Name: str, Item: int, textValue: str, numericValue: float, ItemType: int = 0):
        """This function sets the value of a steel design overwrite item. The function returns zero if
        the item is successfully set; otherwise, it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 49, inclusive, indicating the
            overwrite item considered. 1 = Current Design Section 2 = Framing type 3 =
            Consider deflection 4 = Deflection check type 5 = DL deflection limit, L/Value 6
            = SDL + LL deflection limit, L/Value 7 = LL deflection limit, L/Value 8 = Total
            load deflection limit, L/Value 9 = Total camber limit, L/Value 10 = DL
            deflection limit, absolute 11 = SDL + LL deflection limit, absolute 12 = LL
            deflection limit, absolute 13 = Total load deflection limit, absolute 14 = Total
            camber limit, absolute 15 = Specified camber 16 = Net area to total area ratio
            17 = Live load reduction factor 18 = Unbraced length ratio, Major 19 = Unbraced
            length ratio, Minor 20 = Effective length factor, K2 Major 21 = Effective length
            factor, K2 Minor 22 = Moment coefficient, kyy Major 23 = Moment coefficient, kzz
            Minor 24 = Bending coefficient, C1 25 = Moment coefficient, kzy 26 = Moment
            coefficient, kyz 27 = Yield stress, Fy 28 = Compressive capacity, Nc.Rd 29 =
            Tensile capacity, Nt.Rd 30 = Major bending capacity, Mc3.Rd 31 = Minor bending
            capacity, Mc2.Rd 32 = Buckling resistance moment, Mb.Rd 33 = Major shear
            capacity, V2.Rd 34 = Minor shear capacity, V3.RD 35 = Demand/capacity ratio
            limit 36 = Section class 37 = Column buckling curve, y-y 38 = Column buckling
            curve, z-z 39 = Buckling curve for LTB 40 = System overstrength factor, Omega 41
            = Is rolled section 42 = Unbraced length ratio, LTB 43 = Effective length factor
            braced, K1 Major 44 = Effective length factor braced, K1 Minor 45 = Effective
            length factor, K LTB 46 = Material overstrength factor, GammaRd 47 = Warping
            constant, Iw 48 = Elastic torsional buckling force, Ncr T 49 = Elastic
            torsional-flexural buckling force, Ncr TF
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, textValue, numericValue, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Italian_NTC_2018.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, textValue: str, numericValue: float):
        """This function sets the value of a steel design preference item. The function returns zero if
        the item is successfully set; otherwise, it returns a nonzero value.
    
        Item (input): This is an integer between 3 and 23, inclusive, indicating the
            preference item considered. 3 = Method Used for Buckling in P-M-M 4 = Framing
            type 5 = GammaM0 6 = GammeM1 7 = GammaM2 8 = Consider deflection 9 = DL
            deflection limit, L/Value 10 = SDL + LL deflection limit, L/Value 11 = LL
            deflection limit, L/Value 12 = Total deflection limit, L/Value 13 = Total camber
            limit, L/Value 14 = Pattern live load factor 15 = Demand/capacity ratio limit 16
            = Multi-Response Case Design 17 = Behavior Factor, q 0 18 = System Overstrength
            Factor, W 19 = Consider P-Delta 20 = Consider Torsion 21 = Ignore Seismic Code
            22 = Ignore Special Seismic Load 23 = Is Doubler Plate Plug-Welded
        """
        _r = self._raw.SetPreference(Item, textValue, numericValue)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignSteel.Italian_NTC_2018.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


