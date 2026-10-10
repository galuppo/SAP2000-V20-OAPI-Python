"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_DesignColdFormed:
    """Wrapper para SapModel.DesignColdFormed."""

    def __init__(self, raw):
        self._raw = raw

    def DeleteResults(self):
        """This function deletes all cold formed frame design results. The function returns zero if the
        results are successfully deleted; otherwise it returns a nonzero value.
        """
        _r = self._raw.DeleteResults()
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.DeleteResults falhou (ret={_r})".format(_r=_r))
        return None

    def GetCode(self):
        """This function retrieves the cold formed design code. The function returns zero if the code
        is successfully retrieved; otherwise it returns a nonzero value.
    
        CodeName (output): This is one of the following cold formed design code names. AISI-
            ASD96 AISI-LRFD96
        """
        _r = self._raw.GetCode("")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.GetCode falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetComboAutoGenerate(self, AutoGenerate: bool):
        """This function retrieves the value of the automatically generated code-based design load
        combinations option for cold formed frame design. The function returns zero if the
        options are successfully set; otherwise it returns a nonzero value.
    
        AutoGenerate (input): If this item is True, the option to automatically generate
            code-based design load combinations for cold formed frame design is turned on.
            If it is False, the option is turned off.
        """
        _r = self._raw.GetComboAutoGenerate(AutoGenerate)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.GetComboAutoGenerate falhou (ret={_r})".format(_r=_r))
        return None

    def GetComboDeflection(self):
        """This function retrieves the names of all load combinations selected as design combinations
        for cold formed deflection design. The function returns zero if the names are
        successfully retrieved; otherwise it returns a nonzero value.
    
        NumberItems (output): The number of load combinations selected as design
            combinations for cold formed deflection design.
        MyName (output): This is an array that includes the name of each response
            combination selected as a design combination for cold formed deflection design.
        """
        _r = self._raw.GetComboDeflection(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.GetComboDeflection falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetComboStrength(self):
        """This function retrieves the names of all load combinations selected as design combinations
        for cold formed strength design. The function returns zero if the names are
        successfully retrieved; otherwise it returns a nonzero value.
    
        NumberItems (output): The number of load combinations selected as design
            combinations for cold formed strength design.
        MyName (output): This is an array that includes the name of each response
            combination selected as a design combination for cold formed strength design.
        """
        _r = self._raw.GetComboStrength(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.GetComboStrength falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDesignSection(self, Name: str):
        """This function retrieves the design section for a specified cold formed frame object. The
        function returns zero if the section is successfully retrieved; otherwise it returns
        a nonzero value.
    
        Name (input): The name of a frame object with a cold formed frame design procedure.
        PropName (output): The name of the design section for the specified frame object.
        """
        _r = self._raw.GetDesignSection(Name, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.GetDesignSection falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetGroup(self):
        """This function retrieves the names of all groups selected for cold formed design. The
        function returns zero if the names are successfully retrieved; otherwise it returns
        a nonzero value.
    
        NumberItems (output): The number of groups selected for cold formed design.
        MyName (output): This is an array that includes the name of each group selected for
            cold formed design.
        """
        _r = self._raw.GetGroup(0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.GetGroup falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetResultsAvailable(self):
        """The function returns True if the cold formed frame design results are available, otherwise
        False.
        """
        _r = self._raw.GetResultsAvailable()
        return _r

    def GetSummaryResults(self, Name: str, ItemType: int = 0):
        """This function retrieves summary results for cold formed design. The function returns zero if
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
            raise Sap2000ApiError("SapModel.DesignColdFormed.GetSummaryResults falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def ResetOverwrites(self):
        """This function resets all cold formed frame design overwrites to default values. The function
        returns zero if the overwrites are successfully reset; otherwise it returns a
        nonzero value. The function will fail if no cold formed frame objects are present.
        """
        _r = self._raw.ResetOverwrites()
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.ResetOverwrites falhou (ret={_r})".format(_r=_r))
        return None

    def SetAutoSelectNull(self, Name: str, ItemType: int = 0):
        """This function removes the auto select section assignments from all specified frame objects
        that have a cold formed frame design procedure. The function returns zero if the
        auto select section assignments are successfully removed; otherwise it returns a
        nonzero value.
    
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
            raise Sap2000ApiError("SapModel.DesignColdFormed.SetAutoSelectNull falhou (ret={_r})".format(_r=_r))
        return None

    def SetCode(self, CodeName: str):
        """This function sets the cold formed design code. The function returns zero if the code is
        successfully set; otherwise it returns a nonzero value.
    
        CodeName (input): This is one of the following cold formed design code names. AISI-
            ASD96 AISI-LRFD96
        """
        _r = self._raw.SetCode(CodeName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.SetCode falhou (ret={_r})".format(_r=_r))
        return None

    def SetComboAutoGenerate(self, AutoGenerate: bool):
        """This function turns on or off the option to automatically generate code-based design load
        combinations for cold formed frame design. The function returns zero if the options
        are successfully set; otherwise it returns a nonzero value.
    
        AutoGenerate (input): If this item is True, the option to automatically generate
            code-based design load combinations for cold formed frame design is turned on.
            If it is False, the option is turned off.
        """
        _r = self._raw.SetComboAutoGenerate(AutoGenerate)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.SetComboAutoGenerate falhou (ret={_r})".format(_r=_r))
        return None

    def SetComboDeflection(self, Name: str, Selected: bool):
        """This function selects or deselects a load combination for cold formed deflection design. The
        function returns zero if the selection status is successfully set; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing load combination.
        Selected (input): If this item is True, the specified load combination is selected
            as a design combination for cold formed deflection design. If it is False, the
            combination is not selected for cold formed deflection design.
        """
        _r = self._raw.SetComboDeflection(Name, Selected)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.SetComboDeflection falhou (ret={_r})".format(_r=_r))
        return None

    def SetComboStrength(self, Name: str, Selected: bool):
        """This function selects or deselects a load combination for cold formed strength design. The
        function returns zero if the selection status is successfully set; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing load combination.
        Selected (input): If this item is True, the specified load combination is selected
            as a design combination for cold formed strength design. If it is False, the
            combination is not selected for cold formed strength design.
        """
        _r = self._raw.SetComboStrength(Name, Selected)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.SetComboStrength falhou (ret={_r})".format(_r=_r))
        return None

    def SetDesignSection(self, Name: str, PropName: str, LastAnalysis: bool, ItemType: int = 0):
        """This function modifies the design section for all specified frame objects that have a cold
        formed frame design procedure. The function returns zero if the design section is
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
            raise Sap2000ApiError("SapModel.DesignColdFormed.SetDesignSection falhou (ret={_r})".format(_r=_r))
        return None

    def SetGroup(self, Name: str, Selected: bool):
        """This function selects or deselects a group for cold formed design. The function returns zero
        if the selection status is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing group.
        Selected (input): If this item is True, the specified group is selected as a design
            group for cold formed design. If it is False, the group is not selected for cold
            formed design.
        """
        _r = self._raw.SetGroup(Name, Selected)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.SetGroup falhou (ret={_r})".format(_r=_r))
        return None

    def StartDesign(self):
        """This function starts the cold formed frame design. The function returns zero if the cold
        formed frame design is successfully started; otherwise it returns a nonzero value.
        The function will fail if no cold formed frame objects are present. It will also
        fail if analysis results are not available.
        """
        _r = self._raw.StartDesign()
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.StartDesign falhou (ret={_r})".format(_r=_r))
        return None

    def VerifyPassed(self):
        """This function retrieves the names of the frame objects that did not pass the design check or
        have not yet been checked, if any. The function returns zero if the names are
        successfully retrieved; otherwise it returns a nonzero value.
    
        NumberItems (output): The number of cold formed frame objects that did not pass the
            design check or have not yet been checked.
        n1 (output): The number of cold formed frame objects that did not pass the design
            check.
        n2 (output): The number of cold formed frame objects that have not yet been checked.
        MyName (output): This is an array that includes the name of each frame object that
            did not pass the design check or has not yet been checked.
        """
        _r = self._raw.VerifyPassed(0, 0, 0, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.VerifyPassed falhou (ret={_ret})".format(_ret=_ret))
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
            raise Sap2000ApiError("SapModel.DesignColdFormed.VerifySections falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    @cached_property
    def AISI_ASD96(self):
        return N_DesignColdFormed_AISI_ASD96(self._raw.AISI_ASD96)

    @cached_property
    def AISI_LRFD96(self):
        return N_DesignColdFormed_AISI_LRFD96(self._raw.AISI_LRFD96)


class N_DesignColdFormed_AISI_ASD96:
    """Wrapper para SapModel.DesignColdFormed.AISI_ASD96."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a cold formed design overwrite item. The function
        returns zero if the item is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of a frame object with a cold formed frame design procedure.
        Item (input): This is an integer between 1 and 27, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor and Lateral
            Torsional Buckling 5 = Effective length factor, K Major 6 = Effective length
            factor, K Minor 7 = Moment coefficient, Cm Major 8 = Moment coefficient, Cm
            Minor 9 = Moment coefficient, Ctf Major 10 = Moment coefficient, Ctf Minor 11 =
            Bending coefficient, Cb 12 = Moment factor, Alpha Major 13 = Moment factor,
            Alpha Minor 14 = Through fastened to deck 15 = Fastener eccentricity, a/b 16 =
            Hole diameter at top flange 17 = Hole diameter at bottom flange 18 = Hole
            diameter on web 19 = Yield stress, Fy 20 = Nominal compressive capacity, Pnc 21
            = Nominal tensile capacity, Pnt 22 = Nominal bending capacity for yielding, Mn33
            23 = Nominal bending capacity for yielding, Mn22 24 = Nominal bending capacity
            for lateral torsional buckling, Mn33 25 = Nominal bending capacity for lateral
            torsional buckling, Mn22 26 = Nominal shear capacity, Vn2 27 = Nominal shear
            capacity, Vn3
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Live load reduction factor
            Value >= 0; 0 means use a program determined value. 3 = Unbraced length ratio,
            Major Value >= 0; 0 means use program determined value. 4 = Unbraced length
            ratio, Minor and Lateral Torsional Buckling Value >= 0; 0 means use program
            determined value. 5 = Effective length factor, K Major Value >= 0; 0 means use
            program determined value. 6 = Effective length factor, K Minor Value >= 0; 0
            means use program determined value. 7 = Moment coefficient, Cm Major Value >= 0;
            0 means use program determined value. 8 = Moment coefficient, Cm Minor Value >=
            0; 0 means use program determined value. 9 = Moment coefficient, Ctf Major Value
            >= 0; 0 means use program determined value. 10 = Moment coefficient, Ctf Minor
            Value >= 0; 0 means use program determined value. 11 = Bending coefficient, Cb
            Value >= 0; 0 means use program determined value. 12 = Moment factor, Alpha
            Major Value >= 0; 0 means use program determined value. 13 = Moment factor,
            Alpha Minor Value >= 0; 0 means use program determined value. 14 = Through
            fastened to deck 0 = No. Any other value = Yes. 15 = Fastener eccentricity, a/b
            Value >= 0; 0 means use program determined value. [L] 16 = Hole diameter at top
            flange Value >= 0; 0 means use program determined value. [L] 17 = Hole diameter
            at bottom flange Value >= 0; 0 means use program determined value. [L] 18 = Hole
            diameter on web Value >= 0; 0 means use program determined value. [L] 19 = Yield
            stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 20 =
            Nominal compressive capacity, Pnc Value >= 0; 0 means use program determined
            value. [F] 21 = Nominal tensile capacity, Pnt Value >= 0; 0 means use program
            determined value. [F] 22 = Nominal bending capacity for yielding, Mn33 Value >=
            0; 0 means use program determined value. [FL] 23 = Nominal bending capacity for
            yielding, Mn22 Value >= 0; 0 means use program determined value. [FL] 24 =
            Nominal bending capacity for lateral torsional buckling, Mn33 Value >= 0; 0
            means use program determined value. [FL] 25 = Nominal bending capacity for
            lateral torsional buckling, Mn22 Value >= 0; 0 means use program determined
            value. [FL] 26 = Nominal shear capacity, Vn2 Value >= 0; 0 means use program
            determined value. [F] 27 = Nominal shear capacity, Vn3 Value >= 0; 0 means use
            program determined value. [F]
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.AISI_ASD96.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a cold formed design preference item. The function
        returns zero if the item is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Item (input): This is an integer between 1 and 10, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Demand/capacity ratio limit 3 =
            Omega bending stiffened 4 = Omega bending unstiffened 5 = Omega bending lateral
            torsional buckling 6 = Omega shear slender 7 = Omega shear nonslender 8 = Omega
            axial tension 9 = Omega axial compression 10 = Time history design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Demand/capacity ratio limit Value > 0 3 =
            Omega bending stiffened Value > 0 4 = Omega bending unstiffened Value > 0 5 =
            Omega bending lateral torsional buckling Value > 0 6 = Omega shear slender Value
            > 0 7 = Omega shear nonslender Value > 0 8 = Omega axial tension Value > 0 9 =
            Omega axial compression Value > 0 10 = Time history design 1 = Envelopes 2 =
            Step-by step
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.AISI_ASD96.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a cold formed design overwrite item. The function returns
        zero if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 27, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor and Lateral
            Torsional Buckling 5 = Effective length factor, K Major 6 = Effective length
            factor, K Minor 7 = Moment coefficient, Cm Major 8 = Moment coefficient, Cm
            Minor 9 = Moment coefficient, Ctf Major 10 = Moment coefficient, Ctf Minor 11 =
            Bending coefficient, Cb 12 = Moment factor, Alpha Major 13 = Moment factor,
            Alpha Minor 14 = Through fastened to deck 15 = Fastener eccentricity, a/b 16 =
            Hole diameter at top flange 17 = Hole diameter at bottom flange 18 = Hole
            diameter on web 19 = Yield stress, Fy 20 = Nominal compressive capacity, Pnc 21
            = Nominal tensile capacity, Pnt 22 = Nominal bending capacity for yielding, Mn33
            23 = Nominal bending capacity for yielding, Mn22 24 = Nominal bending capacity
            for lateral torsional buckling, Mn33 25 = Nominal bending capacity for lateral
            torsional buckling, Mn22 26 = Nominal shear capacity, Vn2 27 = Nominal shear
            capacity, Vn3
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Live load reduction factor
            Value >= 0; 0 means use a program determined value. 3 = Unbraced length ratio,
            Major Value >= 0; 0 means use program determined value. 4 = Unbraced length
            ratio, Minor and Lateral Torsional Buckling Value >= 0; 0 means use program
            determined value. 5 = Effective length factor, K Major Value >= 0; 0 means use
            program determined value. 6 = Effective length factor, K Minor Value >= 0; 0
            means use program determined value. 7 = Moment coefficient, Cm Major Value >= 0;
            0 means use program determined value. 8 = Moment coefficient, Cm Minor Value >=
            0; 0 means use program determined value. 9 = Moment coefficient, Ctf Major Value
            >= 0; 0 means use program determined value. 10 = Moment coefficient, Ctf Minor
            Value >= 0; 0 means use program determined value. 11 = Bending coefficient, Cb
            Value >= 0; 0 means use program determined value. 12 = Moment factor, Alpha
            Major Value >= 0; 0 means use program determined value. 13 = Moment factor,
            Alpha Minor Value >= 0; 0 means use program determined value. 14 = Through
            fastened to deck 0 = No. Any other value = Yes. 15 = Fastener eccentricity, a/b
            Value >= 0; 0 means use program determined value. [L] 16 = Hole diameter at top
            flange Value >= 0; 0 means use program determined value. [L] 17 = Hole diameter
            at bottom flange Value >= 0; 0 means use program determined value. [L] 18 = Hole
            diameter on web Value >= 0; 0 means use program determined value. [L] 19 = Yield
            stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 20 =
            Nominal compressive capacity, Pnc Value >= 0; 0 means use program determined
            value. [F] 21 = Nominal tensile capacity, Pnt Value >= 0; 0 means use program
            determined value. [F] 22 = Nominal bending capacity for yielding, Mn33 Value >=
            0; 0 means use program determined value. [FL] 23 = Nominal bending capacity for
            yielding, Mn22 Value >= 0; 0 means use program determined value. [FL] 24 =
            Nominal bending capacity for lateral torsional buckling, Mn33 Value >= 0; 0
            means use program determined value. [FL] 25 = Nominal bending capacity for
            lateral torsional buckling, Mn22 Value >= 0; 0 means use program determined
            value. [FL] 26 = Nominal shear capacity, Vn2 Value >= 0; 0 means use program
            determined value. [F] 27 = Nominal shear capacity, Vn3 Value >= 0; 0 means use
            program determined value. [F]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.AISI_ASD96.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a cold formed design preference item. The function returns
        zero if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 10, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Demand/capacity ratio limit 3 =
            Omega bending stiffened 4 = Omega bending unstiffened 5 = Omega bending lateral
            torsional buckling 6 = Omega shear slender 7 = Omega shear nonslender 8 = Omega
            axial tension 9 = Omega axial compression 10 = Time history design
        Value (input): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Demand/capacity ratio limit Value > 0 3 =
            Omega bending stiffened Value > 0 4 = Omega bending unstiffened Value > 0 5 =
            Omega bending lateral torsional buckling Value > 0 6 = Omega shear slender Value
            > 0 7 = Omega shear nonslender Value > 0 8 = Omega axial tension Value > 0 9 =
            Omega axial compression Value > 0 10 = Time history design 1 = Envelopes 2 =
            Step-by step
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.AISI_ASD96.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


class N_DesignColdFormed_AISI_LRFD96:
    """Wrapper para SapModel.DesignColdFormed.AISI_LRFD96."""

    def __init__(self, raw):
        self._raw = raw

    def GetOverwrite(self, Name: str, Item: int, ProgDet: bool):
        """This function retrieves the value of a cold formed design overwrite item. The function
        returns zero if the item is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of a frame object with a cold formed frame design procedure.
        Item (input): This is an integer between 1 and 27, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor and Lateral
            Torsional Buckling 5 = Effective length factor, K Major 6 = Effective length
            factor, K Minor 7 = Moment coefficient, Cm Major 8 = Moment coefficient, Cm
            Minor 9 = Moment coefficient, Ctf Major 10 = Moment coefficient, Ctf Minor 11 =
            Bending coefficient, Cb 12 = Moment factor, Alpha Major 13 = Moment factor,
            Alpha Minor 14 = Through fastened to deck 15 = Fastener eccentricity, a/b 16 =
            Hole diameter at top flange 17 = Hole diameter at bottom flange 18 = Hole
            diameter on web 19 = Yield stress, Fy 20 = Nominal compressive capacity, Pnc 21
            = Nominal tensile capacity, Pnt 22 = Nominal bending capacity for yielding, Mn33
            23 = Nominal bending capacity for yielding, Mn22 24 = Nominal bending capacity
            for lateral torsional buckling, Mn33 25 = Nominal bending capacity for lateral
            torsional buckling, Mn22 26 = Nominal shear capacity, Vn2 27 = Nominal shear
            capacity, Vn3
        Value (output): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Live load reduction factor
            Value >= 0; 0 means use a program determined value. 3 = Unbraced length ratio,
            Major Value >= 0; 0 means use program determined value. 4 = Unbraced length
            ratio, Minor and Lateral Torsional Buckling Value >= 0; 0 means use program
            determined value. 5 = Effective length factor, K Major Value >= 0; 0 means use
            program determined value. 6 = Effective length factor, K Minor Value >= 0; 0
            means use program determined value. 7 = Moment coefficient, Cm Major Value >= 0;
            0 means use program determined value. 8 = Moment coefficient, Cm Minor Value >=
            0; 0 means use program determined value. 9 = Moment coefficient, Ctf Major Value
            >= 0; 0 means use program determined value. 10 = Moment coefficient, Ctf Minor
            Value >= 0; 0 means use program determined value. 11 = Bending coefficient, Cb
            Value >= 0; 0 means use program determined value. 12 = Moment factor, Alpha
            Major Value >= 0; 0 means use program determined value. 13 = Moment factor,
            Alpha Minor Value >= 0; 0 means use program determined value. 14 = Through
            fastened to deck 0 = No. Any other value = Yes. 15 = Fastener eccentricity, a/b
            Value >= 0; 0 means use program determined value. [L] 16 = Hole diameter at top
            flange Value >= 0; 0 means use program determined value. [L] 17 = Hole diameter
            at bottom flange Value >= 0; 0 means use program determined value. [L] 18 = Hole
            diameter on web Value >= 0; 0 means use program determined value. [L] 19 = Yield
            stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 20 =
            Nominal compressive capacity, Pnc Value >= 0; 0 means use program determined
            value. [F] 21 = Nominal tensile capacity, Pnt Value >= 0; 0 means use program
            determined value. [F] 22 = Nominal bending capacity for yielding, Mn33 Value >=
            0; 0 means use program determined value. [FL] 23 = Nominal bending capacity for
            yielding, Mn22 Value >= 0; 0 means use program determined value. [FL] 24 =
            Nominal bending capacity for lateral torsional buckling, Mn33 Value >= 0; 0
            means use program determined value. [FL] 25 = Nominal bending capacity for
            lateral torsional buckling, Mn22 Value >= 0; 0 means use program determined
            value. [FL] 26 = Nominal shear capacity, Vn2 Value >= 0; 0 means use program
            determined value. [F] 27 = Nominal shear capacity, Vn3 Value >= 0; 0 means use
            program determined value. [F]
        ProgDet (input): If this item is True, the specified value is program determined.
        """
        _r = self._raw.GetOverwrite(Name, Item, 0.0, ProgDet)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.AISI_LRFD96.GetOverwrite falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetPreference(self, Item: int):
        """This function retrieves the value of a cold formed design preference item. The function
        returns zero if the item is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Item (input): This is an integer between 1 and 10, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Demand/capacity ratio limit 3 =
            Phi bending stiffened 4 = Phi bending unstiffened 5 = Phi bending lateral
            torsional buckling 6 = Phi shear slender 7 = Phi shear nonslender 8 = Phi axial
            tension 9 = Phi axial compression 10 = Time history design
        Value (output): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Demand/capacity ratio limit Value > 0 3 = Phi
            bending stiffened Value > 0 4 = Phi bending unstiffened Value > 0 5 = Phi
            bending lateral torsional buckling Value > 0 6 = Phi shear slender Value > 0 7 =
            Phi shear nonslender Value > 0 8 = Phi axial tension Value > 0 9 = Phi axial
            compression Value > 0 10 = Time history design 1 = Envelopes 2 = Step-by step
        """
        _r = self._raw.GetPreference(Item, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.AISI_LRFD96.GetPreference falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def SetOverwrite(self, Name: str, Item: int, Value: float, ItemType: int = 0):
        """This function sets the value of a cold formed design overwrite item. The function returns
        zero if the item is successfully set; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame object or group depending on the value
            of the ItemType item.
        Item (input): This is an integer between 1 and 27, inclusive, indicating the
            overwrite item considered. 1 = Framing type 2 = Live load reduction factor 3 =
            Unbraced length ratio, Major 4 = Unbraced length ratio, Minor and Lateral
            Torsional Buckling 5 = Effective length factor, K Major 6 = Effective length
            factor, K Minor 7 = Moment coefficient, Cm Major 8 = Moment coefficient, Cm
            Minor 9 = Moment coefficient, Ctf Major 10 = Moment coefficient, Ctf Minor 11 =
            Bending coefficient, Cb 12 = Moment factor, Alpha Major 13 = Moment factor,
            Alpha Minor 14 = Through fastened to deck 15 = Fastener eccentricity, a/b 16 =
            Hole diameter at top flange 17 = Hole diameter at bottom flange 18 = Hole
            diameter on web 19 = Yield stress, Fy 20 = Nominal compressive capacity, Pnc 21
            = Nominal tensile capacity, Pnt 22 = Nominal bending capacity for yielding, Mn33
            23 = Nominal bending capacity for yielding, Mn22 24 = Nominal bending capacity
            for lateral torsional buckling, Mn33 25 = Nominal bending capacity for lateral
            torsional buckling, Mn22 26 = Nominal shear capacity, Vn2 27 = Nominal shear
            capacity, Vn3
        Value (input): The value of the considered overwrite item. 1 = Framing type 0 =
            Program Default 1 = Moment Frame 2 = Braced Frame 2 = Live load reduction factor
            Value >= 0; 0 means use a program determined value. 3 = Unbraced length ratio,
            Major Value >= 0; 0 means use program determined value. 4 = Unbraced length
            ratio, Minor and Lateral Torsional Buckling Value >= 0; 0 means use program
            determined value. 5 = Effective length factor, K Major Value >= 0; 0 means use
            program determined value. 6 = Effective length factor, K Minor Value >= 0; 0
            means use program determined value. 7 = Moment coefficient, Cm Major Value >= 0;
            0 means use program determined value. 8 = Moment coefficient, Cm Minor Value >=
            0; 0 means use program determined value. 9 = Moment coefficient, Ctf Major Value
            >= 0; 0 means use program determined value. 10 = Moment coefficient, Ctf Minor
            Value >= 0; 0 means use program determined value. 11 = Bending coefficient, Cb
            Value >= 0; 0 means use program determined value. 12 = Moment factor, Alpha
            Major Value >= 0; 0 means use program determined value. 13 = Moment factor,
            Alpha Minor Value >= 0; 0 means use program determined value. 14 = Through
            fastened to deck 0 = No. Any other value = Yes. 15 = Fastener eccentricity, a/b
            Value >= 0; 0 means use program determined value. [L] 16 = Hole diameter at top
            flange Value >= 0; 0 means use program determined value. [L] 17 = Hole diameter
            at bottom flange Value >= 0; 0 means use program determined value. [L] 18 = Hole
            diameter on web Value >= 0; 0 means use program determined value. [L] 19 = Yield
            stress, Fy Value >= 0; 0 means use program determined value. [F/L 2 ] 20 =
            Nominal compressive capacity, Pnc Value >= 0; 0 means use program determined
            value. [F] 21 = Nominal tensile capacity, Pnt Value >= 0; 0 means use program
            determined value. [F] 22 = Nominal bending capacity for yielding, Mn33 Value >=
            0; 0 means use program determined value. [FL] 23 = Nominal bending capacity for
            yielding, Mn22 Value >= 0; 0 means use program determined value. [FL] 24 =
            Nominal bending capacity for lateral torsional buckling, Mn33 Value >= 0; 0
            means use program determined value. [FL] 25 = Nominal bending capacity for
            lateral torsional buckling, Mn22 Value >= 0; 0 means use program determined
            value. [FL] 26 = Nominal shear capacity, Vn2 Value >= 0; 0 means use program
            determined value. [F] 27 = Nominal shear capacity, Vn3 Value >= 0; 0 means use
            program determined value. [F]
        ItemType (input): This is one of the following items in the eItemType enumeration:
            Object = 0 Group = 1 SelectedObjects = 2 If this item is Object, the assignment
            is made to the frame object specified by the Name item. If this item is Group,
            the assignment is made to all frame objects in the group specified by the Name
            item. If this item is SelectedObjects, assignment is made to all selected frame
            objects, and the Name item is ignored.
        """
        _r = self._raw.SetOverwrite(Name, Item, Value, ItemType)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.AISI_LRFD96.SetOverwrite falhou (ret={_r})".format(_r=_r))
        return None

    def SetPreference(self, Item: int, Value: float):
        """This function sets the value of a cold formed design preference item. The function returns
        zero if the item is successfully set; otherwise it returns a nonzero value.
    
        Item (input): This is an integer between 1 and 10, inclusive, indicating the
            preference item considered. 1 = Framing type 2 = Demand/capacity ratio limit 3 =
            Phi bending stiffened 4 = Phi bending unstiffened 5 = Phi bending lateral
            torsional buckling 6 = Phi shear slender 7 = Phi shear nonslender 8 = Phi axial
            tension 9 = Phi axial compression 10 = Time history design
        Value (input): The value of the considered preference item. 1 = Framing type 1 =
            Moment Frame 2 = Braced Frame 2 = Demand/capacity ratio limit Value > 0 3 = Phi
            bending stiffened Value > 0 4 = Phi bending unstiffened Value > 0 5 = Phi
            bending lateral torsional buckling Value > 0 6 = Phi shear slender Value > 0 7 =
            Phi shear nonslender Value > 0 8 = Phi axial tension Value > 0 9 = Phi axial
            compression Value > 0 10 = Time history design 1 = Envelopes 2 = Step-by step
        """
        _r = self._raw.SetPreference(Item, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.DesignColdFormed.AISI_LRFD96.SetPreference falhou (ret={_r})".format(_r=_r))
        return None


