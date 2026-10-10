"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_DesignAluminum:
    """Wrapper para SapModel.DesignAluminum."""

    def __init__(self, raw):
        self._raw = raw

    def DeleteResults(self):
        """This function deletes all aluminum frame design results. The function returns zero if the
        results are successfully deleted; otherwise it returns a nonzero value.
        """
        _r = self._raw.DeleteResults()
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.DeleteResults falhou (ret={_r})".format(_r=_r))
        return None

    def GetCode(self):
        """This function retrieves the aluminum design code. The function returns zero if the code is
        successfully retrieved; otherwise it returns a nonzero value.
    
        CodeName (output): This is one of the following aluminum design code names. AA-ASD
            2000 AA-LRFD 2000
        """
        _r = self._raw.GetCode("")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.GetCode falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetComboAutoGenerate(self, AutoGenerate: bool):
        """This function retrieves the value of the automatically generated code-based design load
        combinations option for aluminum frame design. The function returns zero if the
        options are successfully set; otherwise it returns a nonzero value.
    
        AutoGenerate (input): If this item is True, the option to automatically generate
            code-based design load combinations for aluminum frame design is turned on. If
            it is False, the option is turned off.
        """
        _r = self._raw.GetComboAutoGenerate(AutoGenerate)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.GetComboAutoGenerate falhou (ret={_r})".format(_r=_r))
        return None

    def GetComboDeflection(self):
        """This function retrieves the names of all load combinations selected as design combinations
        for aluminum deflection design. The function returns zero if the names are
        successfully retrieved; otherwise it returns a nonzero value.
    
        NumberItems (output): The number of load combinations selected as design
            combinations for aluminum deflection design.
        MyName (output): This is an array that includes the name of each response
            combination selected as a design combination for aluminum deflection design.
        """
        _r = self._raw.GetComboDeflection(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.GetComboDeflection falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetComboStrength(self):
        """This function retrieves the names of all load combinations selected as design combinations
        for aluminum strength design. The function returns zero if the names are
        successfully retrieved; otherwise it returns a nonzero value.
    
        NumberItems (output): The number of load combinations selected as design
            combinations for aluminum strength design.
        MyName (output): This is an array that includes the name of each response
            combination selected as a design combination for aluminum strength design.
        """
        _r = self._raw.GetComboStrength(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.GetComboStrength falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDesignSection(self, Name: str):
        """This function retrieves the design section for a specified aluminum frame object. The
        function returns zero if the section is successfully retrieved; otherwise it returns
        a nonzero value.
    
        Name (input): The name of a frame object with a aluminum frame design procedure.
        PropName (output): The name of the design section for the specified frame object.
        """
        _r = self._raw.GetDesignSection(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.GetDesignSection falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetGroup(self):
        """This function retrieves the names of all groups selected for aluminum design. The function
        returns zero if the names are successfully retrieved; otherwise it returns a nonzero
        value.
    
        NumberItems (output): The number of groups selected for aluminum design.
        MyName (output): This is an array that includes the name of each group selected for
            aluminum design.
        """
        _r = self._raw.GetGroup(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.GetGroup falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetResultsAvailable(self):
        """The function returns True if the aluminum frame design results are available, otherwise
        False.
        """
        _r = self._raw.GetResultsAvailable()
        return _r

    def GetSummaryResults(self, Name: str, ItemType: int = 0):
        """This function retrieves summary results for aluminum design. The function returns zero if
        the results are successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        NumberItems (output): The number of frame objects for which results are obtained.
        FrameName (output): This is an array that includes each frame object name for which
            results are obtained.
        Ratio (output): This is an array that includes the controlling stress or capacity
            ratio for each frame object.
        RatioType (output): This is an array that includes 1, 3 or 4, indicating the
            controlling stress or capacity ratio type for each frame object. 1 = PMM 3 =
            Major shear 4 = Minor shear
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
            raise Sap2000ApiError("SapModel.DesignAluminum.GetSummaryResults falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def ResetOverwrites(self):
        """This function resets all aluminum frame design overwrites to default values. The function
        returns zero if the overwrites are successfully reset; otherwise it returns a
        nonzero value. The function will fail if no aluminum frame objects are present.
        """
        _r = self._raw.ResetOverwrites()
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.ResetOverwrites falhou (ret={_r})".format(_r=_r))
        return None

    def SetAutoSelectNull(self, Name: str, ItemType: int = 0):
        """This function removes the auto select section assignments from all specified frame objects
        that have a aluminum frame design procedure. The function returns zero if the auto
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
            raise Sap2000ApiError("SapModel.DesignAluminum.SetAutoSelectNull falhou (ret={_r})".format(_r=_r))
        return None

    def SetCode(self, CodeName: str):
        """This function sets the aluminum design code. The function returns zero if the code is
        successfully set; otherwise it returns a nonzero value.
    
        CodeName (input): This is one of the following aluminum design code names. AA-ASD
            2000 AA-LRFD 2000
        """
        _r = self._raw.SetCode(CodeName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.SetCode falhou (ret={_r})".format(_r=_r))
        return None

    def SetComboAutoGenerate(self, AutoGenerate: bool):
        """This function turns on or off the option to automatically generate code-based design load
        combinations for aluminum frame design. The function returns zero if the options are
        successfully set; otherwise it returns a nonzero value.
    
        AutoGenerate (input): If this item is True, the option to automatically generate
            code-based design load combinations for aluminum frame design is turned on. If
            it is False, the option is turned off.
        """
        _r = self._raw.SetComboAutoGenerate(AutoGenerate)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.SetComboAutoGenerate falhou (ret={_r})".format(_r=_r))
        return None

    def SetComboDeflection(self, Name: str, Selected: bool):
        """This function selects or deselects a load combination for aluminum deflection design. The
        function returns zero if the selection status is successfully set; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing load combination.
        Selected (input): If this item is True, the specified load combination is selected
            as a design combination for aluminum deflection design. If it is False, the
            combination is not selected for aluminum deflection design.
        """
        _r = self._raw.SetComboDeflection(Name, Selected)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.SetComboDeflection falhou (ret={_r})".format(_r=_r))
        return None

    def SetComboStrength(self, Name: str, Selected: bool):
        """This function selects or deselects a load combination for aluminum strength design. The
        function returns zero if the selection status is successfully set; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing load combination.
        Selected (input): If this item is True, the specified load combination is selected
            as a design combination for aluminum strength design. If it is False, the
            combination is not selected for aluminum strength design.
        """
        _r = self._raw.SetComboStrength(Name, Selected)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.SetComboStrength falhou (ret={_r})".format(_r=_r))
        return None

    def SetDesignSection(self, Name: str, PropName: str, LastAnalysis: bool, ItemType: int = 0):
        """This function modifies the design section for all specified frame objects that have a
        aluminum frame design procedure. The function returns zero if the design section is
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
            raise Sap2000ApiError("SapModel.DesignAluminum.SetDesignSection falhou (ret={_r})".format(_r=_r))
        return None

    def SetGroup(self, Name: str, Selected: bool):
        """This function selects or deselects a group for aluminum design. The function returns zero if
        the selection status is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing group.
        Selected (input): If this item is True, the specified group is selected as a design
            group for aluminum design. If it is False, the group is not selected for
            aluminum design.
        """
        _r = self._raw.SetGroup(Name, Selected)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.SetGroup falhou (ret={_r})".format(_r=_r))
        return None

    def StartDesign(self):
        """This function starts the aluminum frame design. The function returns zero if the aluminum
        frame design is successfully started; otherwise it returns a nonzero value. The
        function will fail if no aluminum frame objects are present. It will also fail if
        analysis results are not available.
        """
        _r = self._raw.StartDesign()
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.StartDesign falhou (ret={_r})".format(_r=_r))
        return None

    def VerifyPassed(self):
        """This function retrieves the names of the frame objects that did not pass the design check or
        have not yet been checked, if any. The function returns zero if the names are
        successfully retrieved; otherwise it returns a nonzero value.
    
        NumberItems (output): The number of aluminum frame objects that did not pass the
            design check or have not yet been checked.
        n1 (output): The number of aluminum frame objects that did not pass the design
            check.
        n2 (output): The number of aluminum frame objects that have not yet been checked.
        MyName (output): This is an array that includes the name of each frame object that
            did not pass the design check or has not yet been checked.
        """
        _r = self._raw.VerifyPassed(0, 0, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.VerifyPassed falhou (ret={_ret})".format(_ret=_ret))
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
            raise Sap2000ApiError("SapModel.DesignAluminum.VerifySections falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    @cached_property
    def AA_ASD_2000(self):
        return N_DesignAluminum_AA_ASD_2000(self._raw.AA_ASD_2000)

    @cached_property
    def AA_LRFD_2000(self):
        return N_DesignAluminum_AA_LRFD_2000(self._raw.AA_LRFD_2000)


class N_DesignAluminum_AA_ASD_2000:
    """Wrapper para SapModel.DesignAluminum.AA_ASD_2000."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of an aluminum design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a aluminum frame design procedure.
        Item (input): This is an integer between 1 and 23, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor and Lateral
            Torsional Buckling 5 = Effective length factor, K Major 6 = Effective length
            factor, K Minor 7 = Moment coefficient, Cm Major 8 = Moment coefficient, Cm
            Minor 9 = Bending coefficient, Cb 10 = Buckling constant for compression, k1 11
            = Buckling constant for compression, k2 12 = Buckling constant for bending, k1
            13 = Buckling constant for bending, k2 14 = Safety coefficient, kt 15 = Bending
            coefficient, C1 16 = Bending coefficient, C2 17 = Yield stress, Fy 18 =
            Compressive stress, Fa 19 = Tensile stress, Ft 20 = Major bending stress, Fb3 21
            = Minor bending stress, Fb2 22 = Major shear stress, Fs2 23 = Minor shear
            stress, Fs3
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Live load reduction factor
            Value >= 0; 0 means use a program determined value. 3 = Unbraced length ratio,
            Major Value >= 0; 0 means use program determined value. 4 = Unbraced length
            ratio, Minor and Lateral Torsional Buckling Value >= 0; 0 means use program
            determined value. 5 = Effective length factor, K Major Value >= 0; 0 means use
            program determined value. 6 = Effective length factor, K Minor Value >= 0; 0
            means use program determined value. 7 = Moment coefficient, Cm Major Value >= 0;
            0 means use program determined value. 8 = Moment coefficient, Cm Minor Value >=
            0; 0 means use program determined value. 9 = Bending coefficient, Cb Value >= 0;
            0 means use program determined value. 10 = Buckling constant for compression, k1
            Value >= 0; 0 means use program determined value. 11 = Buckling constant for
            compression, k2 Value >= 0; 0 means use program determined value. 12 = Buckling
            constant for bending, k1 Value >= 0; 0 means use program determined value. 13 =
            Buckling constant for bending, k2 Value >= 0; 0 means use program determined
            value. 14 = Safety coefficient, kt Value >= 0; 0 means use program determined
            value. 15 = Bending coefficient, C1 Value >= 0; 0 means use program determined
            value. 16 = Bending coefficient, C2 Value >= 0; 0 means use program determined
            value. 17 = Yield stress, Fy Value >= 0; 0 means use program determined value.
            [F/L 2 ] 18 = Compressive stress, Fa Value >= 0; 0 means use program determined
            value. [F/L 2 ] 19 = Tensile stress, Ft Value >= 0; 0 means use program
            determined value. [F/L 2 ] 20 = Major bending stress, Fb3 Value >= 0; 0 means
            use program determined value. [F/L 2 ] 21 = Minor bending stress, Fb2 Value >=
            0; 0 means use program determined value. [F/L 2 ] 22 = Major shear stress, Fs2
            Value >= 0; 0 means use program determined value. [F/L 2 ] 23 = Minor shear
            stress, Fs3 Value >= 0; 0 means use program determined value. [F/L 2 ]
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.AA_ASD_2000.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of an aluminum design preference item. The function
        returns zero if the item is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Item (input): This is an integer between 1 and 6, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Demand/capacity ratio limit 3 =
            Lateral factor 4 = Use lateral factor 5 = Bridge type structure 6 = Time history
            design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Demand/capacity ratio limit Value > 0 3 =
            Lateral factor Value > 0 4 = Use lateral factor 0 = No Any other value = Yes 5 =
            Bridge type structure 0 = No Any other value = Yes 6 = Time history design 1 =
            Envelopes 2 = Step-by step
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.AA_ASD_2000.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of an aluminum design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 23, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor and Lateral
            Torsional Buckling 5 = Effective length factor, K Major 6 = Effective length
            factor, K Minor 7 = Moment coefficient, Cm Major 8 = Moment coefficient, Cm
            Minor 9 = Bending coefficient, Cb 10 = Buckling constant for compression, k1 11
            = Buckling constant for compression, k2 12 = Buckling constant for bending, k1
            13 = Buckling constant for bending, k2 14 = Safety coefficient, kt 15 = Bending
            coefficient, C1 16 = Bending coefficient, C2 17 = Yield stress, Fy 18 =
            Compressive stress, Fa 19 = Tensile stress, Ft 20 = Major bending stress, Fb3 21
            = Minor bending stress, Fb2 22 = Major shear stress, Fs2 23 = Minor shear
            stress, Fs3
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Live load reduction factor
            Value >= 0; 0 means use a program determined value. 3 = Unbraced length ratio,
            Major Value >= 0; 0 means use program determined value. 4 = Unbraced length
            ratio, Minor and Lateral Torsional Buckling Value >= 0; 0 means use program
            determined value. 5 = Effective length factor, K Major Value >= 0; 0 means use
            program determined value. 6 = Effective length factor, K Minor Value >= 0; 0
            means use program determined value. 7 = Moment coefficient, Cm Major Value >= 0;
            0 means use program determined value. 8 = Moment coefficient, Cm Minor Value >=
            0; 0 means use program determined value. 9 = Bending coefficient, Cb Value >= 0;
            0 means use program determined value. 10 = Buckling constant for compression, k1
            Value >= 0; 0 means use program determined value. 11 = Buckling constant for
            compression, k2 Value >= 0; 0 means use program determined value. 12 = Buckling
            constant for bending, k1 Value >= 0; 0 means use program determined value. 13 =
            Buckling constant for bending, k2 Value >= 0; 0 means use program determined
            value. 14 = Safety coefficient, kt Value >= 0; 0 means use program determined
            value. 15 = Bending coefficient, C1 Value >= 0; 0 means use program determined
            value. 16 = Bending coefficient, C2 Value >= 0; 0 means use program determined
            value. 17 = Yield stress, Fy Value >= 0; 0 means use program determined value.
            [F/L 2 ] 18 = Compressive stress, Fa Value >= 0; 0 means use program determined
            value. [F/L 2 ] 19 = Tensile stress, Ft Value >= 0; 0 means use program
            determined value. [F/L 2 ] 20 = Major bending stress, Fb3 Value >= 0; 0 means
            use program determined value. [F/L 2 ] 21 = Minor bending stress, Fb2 Value >=
            0; 0 means use program determined value. [F/L 2 ] 22 = Major shear stress, Fs2
            Value >= 0; 0 means use program determined value. [F/L 2 ] 23 = Minor shear
            stress, Fs3 Value >= 0; 0 means use program determined value. [F/L 2 ]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.AA_ASD_2000.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of an aluminum design preference item. The function returns
        zero if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 6, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Demand/capacity ratio limit 3 =
            Lateral factor 4 = Use lateral factor 5 = Bridge type structure 6 = Time history
            design
        Value (input): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Demand/capacity ratio limit Value > 0 3 =
            Lateral factor Value > 0 4 = Use lateral factor 0 = No Any other value = Yes 5 =
            Bridge type structure 0 = No Any other value = Yes 6 = Time history design 1 =
            Envelopes 2 = Step-by step
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.AA_ASD_2000.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignAluminum_AA_LRFD_2000:
    """Wrapper para SapModel.DesignAluminum.AA_LRFD_2000."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of an aluminum design overwrite item. The function returns
        zero if the item is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of a frame object with a aluminum frame design procedure.
        Item (input): This is an integer between 1 and 23, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor and Lateral
            Torsional Buckling 5 = Effective length factor, K Major 6 = Effective length
            factor, K Minor 7 = Moment coefficient, Cm Major 8 = Moment coefficient, Cm
            Minor 9 = Bending coefficient, Cb 10 = Buckling constant for compression, k1 11
            = Buckling constant for compression, k2 12 = Buckling constant for bending, k1
            13 = Buckling constant for bending, k2 14 = Safety coefficient, kt 15 = Bending
            coefficient, C1 16 = Bending coefficient, C2 17 = Yield stress, Fy 18 =
            Compressive stress, Fa 19 = Tensile stress, Ft 20 = Major bending stress, Fb3 21
            = Minor bending stress, Fb2 22 = Major shear stress, Fs2 23 = Minor shear
            stress, Fs3
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Live load reduction factor
            Value >= 0; 0 means use a program determined value. 3 = Unbraced length ratio,
            Major Value >= 0; 0 means use program determined value. 4 = Unbraced length
            ratio, Minor and Lateral Torsional Buckling Value >= 0; 0 means use program
            determined value. 5 = Effective length factor, K Major Value >= 0; 0 means use
            program determined value. 6 = Effective length factor, K Minor Value >= 0; 0
            means use program determined value. 7 = Moment coefficient, Cm Major Value >= 0;
            0 means use program determined value. 8 = Moment coefficient, Cm Minor Value >=
            0; 0 means use program determined value. 9 = Bending coefficient, Cb Value >= 0;
            0 means use program determined value. 10 = Buckling constant for compression, k1
            Value >= 0; 0 means use program determined value. 11 = Buckling constant for
            compression, k2 Value >= 0; 0 means use program determined value. 12 = Buckling
            constant for bending, k1 Value >= 0; 0 means use program determined value. 13 =
            Buckling constant for bending, k2 Value >= 0; 0 means use program determined
            value. 14 = Safety coefficient, kt Value >= 0; 0 means use program determined
            value. 15 = Bending coefficient, C1 Value >= 0; 0 means use program determined
            value. 16 = Bending coefficient, C2 Value >= 0; 0 means use program determined
            value. 17 = Yield stress, Fy Value >= 0; 0 means use program determined value.
            [F/L 2 ] 18 = Compressive stress, Fa Value >= 0; 0 means use program determined
            value. [F/L 2 ] 19 = Tensile stress, Ft Value >= 0; 0 means use program
            determined value. [F/L 2 ] 20 = Major bending stress, Fb3 Value >= 0; 0 means
            use program determined value. [F/L 2 ] 21 = Minor bending stress, Fb2 Value >=
            0; 0 means use program determined value. [F/L 2 ] 22 = Major shear stress, Fs2
            Value >= 0; 0 means use program determined value. [F/L 2 ] 23 = Minor shear
            stress, Fs3 Value >= 0; 0 means use program determined value. [F/L 2 ]
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.AA_LRFD_2000.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of an aluminum design preference item. The function
        returns zero if the item is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Item (input): This is an integer between 1 and 6, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Demand/capacity ratio limit 3 =
            Phiy resistance factor 4 = Phib resistance factor 5 = Phic resistance factor 6 =
            Phiu resistance factor 7 = Phicc resistance factor 8 = Phicp resistance factor 9
            = Phiv resistance factor 10 = Phivp resistance factor 11 = Phiw resistance
            factor 12 = Time history design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Demand/capacity ratio limit Value > 0 3 = Phiy
            resistance factor Value > 0 4 = Phib resistance factor Value > 0 5 = Phic
            resistance factor Value > 0 6 = Phiu resistance factor Value > 0 7 = Phicc
            resistance factor Value > 0 8 = Phicp resistance factor Value > 0 9 = Phiv
            resistance factor Value > 0 10 = Phivp resistance factor Value > 0 11 = Phiw
            resistance factor Value > 0 12 = Time history design 1 = Envelopes 2 = Step-by
            step
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.AA_LRFD_2000.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of an aluminum design overwrite item. The function returns zero
        if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group, depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 23, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor and Lateral
            Torsional Buckling 5 = Effective length factor, K Major 6 = Effective length
            factor, K Minor 7 = Moment coefficient, Cm Major 8 = Moment coefficient, Cm
            Minor 9 = Bending coefficient, Cb 10 = Buckling constant for compression, k1 11
            = Buckling constant for compression, k2 12 = Buckling constant for bending, k1
            13 = Buckling constant for bending, k2 14 = Safety coefficient, kt 15 = Bending
            coefficient, C1 16 = Bending coefficient, C2 17 = Yield stress, Fy 18 =
            Compressive stress, Fa 19 = Tensile stress, Ft 20 = Major bending stress, Fb3 21
            = Minor bending stress, Fb2 22 = Major shear stress, Fs2 23 = Minor shear
            stress, Fs3
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Live load reduction factor
            Value >= 0; 0 means use a program determined value. 3 = Unbraced length ratio,
            Major Value >= 0; 0 means use program determined value. 4 = Unbraced length
            ratio, Minor and Lateral Torsional Buckling Value >= 0; 0 means use program
            determined value. 5 = Effective length factor, K Major Value >= 0; 0 means use
            program determined value. 6 = Effective length factor, K Minor Value >= 0; 0
            means use program determined value. 7 = Moment coefficient, Cm Major Value >= 0;
            0 means use program determined value. 8 = Moment coefficient, Cm Minor Value >=
            0; 0 means use program determined value. 9 = Bending coefficient, Cb Value >= 0;
            0 means use program determined value. 10 = Buckling constant for compression, k1
            Value >= 0; 0 means use program determined value. 11 = Buckling constant for
            compression, k2 Value >= 0; 0 means use program determined value. 12 = Buckling
            constant for bending, k1 Value >= 0; 0 means use program determined value. 13 =
            Buckling constant for bending, k2 Value >= 0; 0 means use program determined
            value. 14 = Safety coefficient, kt Value >= 0; 0 means use program determined
            value. 15 = Bending coefficient, C1 Value >= 0; 0 means use program determined
            value. 16 = Bending coefficient, C2 Value >= 0; 0 means use program determined
            value. 17 = Yield stress, Fy Value >= 0; 0 means use program determined value.
            [F/L 2 ] 18 = Compressive stress, Fa Value >= 0; 0 means use program determined
            value. [F/L 2 ] 19 = Tensile stress, Ft Value >= 0; 0 means use program
            determined value. [F/L 2 ] 20 = Major bending stress, Fb3 Value >= 0; 0 means
            use program determined value. [F/L 2 ] 21 = Minor bending stress, Fb2 Value >=
            0; 0 means use program determined value. [F/L 2 ] 22 = Major shear stress, Fs2
            Value >= 0; 0 means use program determined value. [F/L 2 ] 23 = Minor shear
            stress, Fs3 Value >= 0; 0 means use program determined value. [F/L 2 ]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.AA_LRFD_2000.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of an aluminum design preference item. The function returns
        zero if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 6, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Demand/capacity ratio limit 3 =
            Phiy resistance factor 4 = Phib resistance factor 5 = Phic resistance factor 6 =
            Phiu resistance factor 7 = Phicc resistance factor 8 = Phicp resistance factor 9
            = Phiv resistance factor 10 = Phivp resistance factor 11 = Phiw resistance
            factor 12 = Time history design
        Value (input): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Demand/capacity ratio limit Value > 0 3 = Phiy
            resistance factor Value > 0 4 = Phib resistance factor Value > 0 5 = Phic
            resistance factor Value > 0 6 = Phiu resistance factor Value > 0 7 = Phicc
            resistance factor Value > 0 8 = Phicp resistance factor Value > 0 9 = Phiv
            resistance factor Value > 0 10 = Phivp resistance factor Value > 0 11 = Phiw
            resistance factor Value > 0 12 = Time history design 1 = Envelopes 2 = Step-by
            step
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignAluminum.AA_LRFD_2000.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


