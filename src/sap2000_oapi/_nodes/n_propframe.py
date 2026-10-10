"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_PropFrame:
    """Wrapper para SapModel.PropFrame."""

    def __init__(self, raw):
        self._raw = raw

    def ChangeName(self, Name: str, NewName: str):
        """This function changes the name of an existing frame section property. The function returns
        zero if the new name is successfully applied; otherwise it returns a nonzero value.
    
        Name (input): The existing name of a defined frame section property.
        NewName (input): The new name for the frame section property.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self, PropType: int = None):
        """This function returns the total number of defined frame section properties in the model. If
        desired, counts can be returned for all frame section properties of a specified type
        in the model.
    
        PropType (input): This optional value is one of the following items in the
            eFramePropType enumeration. SECTION_I = 1 SECTION_CHANNEL = 2 SECTION_T = 3
            SECTION_ANGLE = 4 SECTION_DBLANGLE = 5 SECTION_BOX = 6 SECTION_PIPE = 7
            SECTION_RECTANGULAR = 8 SECTION_CIRCLE = 9 SECTION_GENERAL = 10
            SECTION_DBCHANNEL = 11 SECTION_AUTO = 12 SECTION_SD = 13 SECTION_VARIABLE = 14
            SECTION_JOIST = 15 SECTION_BRIDGE = 16 SECTION_COLD_C = 17 SECTION_COLD_2C = 18
            SECTION_COLD_Z = 19 SECTION_COLD_L = 20 SECTION_COLD_2L = 21 SECTION_COLD_HAT =
            22 SECTION_BUILTUP_I_COVERPLATE = 23 SECTION_PCC_GIRDER_I = 24
            SECTION_PCC_GIRDER_U = 25 SECTION_BUILTUP_I_HYBRID = 26 SECTION_BUILTUP_U_HYBRID
            = 27 If no value is input for PropType, a count is returned for all frame
            section properties in the model regardless of type.
        """
        _r = self._raw.Count(PropType)
        return _r

    def Delete(self, Name: str):
        """The function deletes a specified frame section property. The function returns zero if the
        frame section property is successfully deleted; otherwise it returns a nonzero
        value. It returns an error if the specified frame section property can not be
        deleted; for example, if it is being used by a frame object.
    
        Name (input): The name of an existing frame section property.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetAngle(self, Name: str, Color: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for an angle-type frame section. The
        function returns zero if the section property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property.
        FileName (output): If the section property was imported from a property file; this
            is the name of that file. If the section property was not imported; this item is
            blank.
        MatProp (output): The name of the material property for the section.
        t3 (output): The vertical leg depth. [L]
        t2 (output): The horizontal leg width. [L]
        tf (output): The horizontal leg thickness. [L]
        tw (output): The vertical leg thickness. [L]
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetAngle(Name, "", "", 0.0, 0.0, 0.0, 0.0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetAngle falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetAutoSelectAluminum(self, Name: str, NumberItems: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for a aluminum auto select lists. The
        function returns zero if the data is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing auto select section list-type frame section
            property.
        NumberItems (input): The number of frame section properties included in the auto
            select list.
        SectName (output): This is an array of the names of the frame section properties
            included in the auto select list.
        AutoStartSection (output): This is Median or the name of a frame section property in
            the SectName array. It is the starting section for the auto select list.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetAutoSelectAluminum(Name, NumberItems, [], "", Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetAutoSelectAluminum falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetAutoSelectColdFormed(self, Name: str, NumberItems: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for a cold formed auto select lists. The
        function returns zero if the data is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing auto select section list-type frame section
            property.
        NumberItems (input): The number of frame section properties included in the auto
            select list.
        SectName (output): This is an array of the names of the frame section properties
            included in the auto select list.
        AutoStartSection (output): This is Median or the name of a frame section property in
            the SectName array. It is the starting section for the auto select list.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetAutoSelectColdFormed(Name, NumberItems, [], "", Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetAutoSelectColdFormed falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetAutoSelectSteel(self, Name: str, NumberItems: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for a steel auto select lists. The
        function returns zero if the data is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing auto select section listtype frame section
            property.
        NumberItems (input): The number of frame section properties included in the auto
            select list.
        SectName (output): This is an array of the names of the frame section properties
            included in the auto select list.
        AutoStartSection (output): This is either Median or the name of a frame section
            property in the SectName array. It is the starting section for the auto select
            list.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetAutoSelectSteel(Name, NumberItems, [], "", Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetAutoSelectSteel falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetChannel(self, Name: str, Color: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for a channel-type frame section. The
        function returns zero if the section property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property.
        FileName (output): If the section property was imported from a property file, this
            is the name of that file. If the section property was not imported, this item is
            blank.
        MatProp (output): The name of the material property for the section.
        t3 (output): The section depth. [L]
        t2 (output): The flange width. [L]
        tf (output): The flange thickness. [L]
        tw (output): The web thickness. [L]
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetChannel(Name, "", "", 0.0, 0.0, 0.0, 0.0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetChannel falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetCircle(self, Name: str, Color: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for a circular frame section. The
        function returns zero if the section property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing circular frame section property.
        FileName (output): If the section property was imported from a property file, this
            is the name of that file. If the section property was not imported, this item is
            blank.
        MatProp (output): The name of the material property for the section.
        t3 (output): The section diameter. [L]
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetCircle(Name, "", "", 0.0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetCircle falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetColdC(self, Name: str, Color: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for a cold formed C-type frame section.
        The function returns zero if the section property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cold formed C-type frame section property.
        FileName (output): If the section property was imported from a property file, this
            is the name of that file. If the section property was not imported, this item is
            blank.
        MatProp (output): The name of the material property for the section.
        t3 (output): The section depth. [L]
        t2 (output): The section width. [L]
        Thickness (output): The section thickness. [L]
        Radius (output): The corner radius, if any. [L]
        LipDepth (output): The lip depth, if any. [L]
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetColdC(Name, "", "", 0.0, 0.0, 0.0, 0.0, 0.0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetColdC falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetColdHat(self, Name: str, Color: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for a cold formed hat-type frame
        section. The function returns zero if the section property data is successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cold formed hat-type frame section property.
        FileName (output): If the section property was imported from a property file, this
            is the name of that file. If the section property was not imported, this item is
            blank.
        MatProp (output): The name of the material property for the section.
        t3 (output): The section depth. [L]
        t2 (output): The section width. [L]
        Thickness (output): The section thickness. [L]
        Radius (output): The corner radius, if any. [L]
        LipDepth (output): The lip depth, if any. [L]
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetColdHat(Name, "", "", 0.0, 0.0, 0.0, 0.0, 0.0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetColdHat falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetColdZ(self, Name: str, Color: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for a cold formed Z-type frame section.
        The function returns zero if the section property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing cold formed Z-type frame section property.
        FileName (output): If the section property was imported from a property file, this
            is the name of that file. If the section property was not imported, this item is
            blank.
        MatProp (output): The name of the material property for the section.
        t3 (output): The section depth. [L]
        t2 (output): The section width. [L]
        Thickness (output): The section thickness. [L]
        Radius (output): The corner radius, if any. [L]
        LipDepth (output): The lip depth, if any. [L]
        LipAngle (output): The lip angle measured from horizontal (0 <= LipAngle <= 90).
            [deg]
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetColdZ(Name, "", "", 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetColdZ falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetCoverPlatedI(self, Name: str, FyTopFlange: float, FyWeb: float, FyBotFlange: float, Color: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for a tube-type frame section. The
        function returns zero if the section property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property.
        SectName (output): The name of an existing I-type frame section property that is
            used for the I-section portion of the coverplated I section.
        FyTopFlange (input): The yield strength of the top flange of the I-section. [F/L 2 ]
            If this item is 0, the yield strength of the I-section specified by the SectName
            item is used.
        FyWeb (input): The yield strength of the web of the I-section. [F/L 2 ] If this item
            is 0, the yield strength of the I-section specified by the SectName item is
            used.
        FyBotFlange (input): The yield strength of the bottom flange of the I-section. [F/L
            2 ] If this item is 0, the yield strength of the I-section specified by the
            SectName item is used.
        tc (output): The thickness of the top cover plate. [L] If the tc or the bc item is
            less than or equal to 0, no top cover plate exists.
        bc (output): The width of the top cover plate. [L] If the tc or the bc item is less
            than or equal to 0, no top cover plate exists.
        MatPropTop (output): The name of the material property for the top cover plate. This
            item applies only if both the tc and the bc items are greater than 0.
        tcb (output): The thickness of the bottom cover plate. [L] If the tcb or the bcb
            item is less than or equal to 0, no bottom cover plate exists.
        bcb (output): The width of the bottom cover plate. [L] If the tcb or the bcb item is
            less than or equal to 0, no bottom cover plate exists.
        MatPropBot (output): The name of the material property for the bottom cover plate.
            This item applies only if both the tcb and the bcb items are greater than 0.
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetCoverPlatedI(Name, "", FyTopFlange, FyWeb, FyBotFlange, 0.0, 0.0, "", 0.0, 0.0, "", Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetCoverPlatedI falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDblAngle(self, Name: str, Color: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for a double angle-type frame section.
        The function returns zero if the section property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property.
        FileName (output): If the section property was imported from a property file, this
            is the name of that file. If the section property was not imported, this item is
            blank.
        MatProp (output): The name of the material property for the section.
        t3 (output): The vertical leg depth. [L]
        t2 (output): The total width of the section, that is, the sum of the widths of each
            horizontal leg plus the back-to-back distance. [L]
        tf (output): The horizontal leg thickness. [L]
        tw (output): The vertical leg thickness. [L]
        dis (output): The back-to-back distance between the angles. [L]
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetDblAngle(Name, "", "", 0.0, 0.0, 0.0, 0.0, 0.0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetDblAngle falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDblChannel(self, Name: str, Color: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for a double channel-type frame section.
        The function returns zero if the section property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property.
        FileName (output): If the section property was imported from a property file, this
            is the name of that file. If the section property was not imported, this item is
            blank.
        MatProp (output): The name of the material property for the section.
        t3 (output): The section depth. [L]
        t2 (output): The total width of the section, that is, the sum of the widths of each
            flange plus the back-to-back distance. [L]
        tf (output): The flange thickness. [L]
        tw (output): The web thickness. [L]
        dis (output): The back-to-back distance between the channels. [L]
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetDblChannel(Name, "", "", 0.0, 0.0, 0.0, 0.0, 0.0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetDblChannel falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetGeneral(self, Name: str, Color: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for a general frame section. The
        function returns zero if the section property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property.
        FileName (output): If the section property was imported from a property file, this
            is the name of that file. If the section property was not imported, this item is
            blank.
        MatProp (output): The name of the material property for the section.
        t3 (output): The section depth. [L]
        t2 (output): The section width. [L]
        Area (output): The cross-sectional area. [L 2 ]
        As2 (output): The shear area for forces in the section local 2-axis direction. [L 2
            ]
        As3 (output): The shear area for forces in the section local 3-axis direction. [L 2
            ]
        Torsion (output): The torsional constant. [L 4 ]
        I22 (output): The moment of inertia for bending about the local 2 axis. [L 4 ]
        I33 (output): The moment of inertia for bending about the local 3 axis. [L 4 ]
        S22 (output): The section modulus for bending about the local 2 axis. [L 3 ]
        S33 (output): The section modulus for bending about the local 3 axis. [L 3 ]
        Z22 (output): The plastic modulus for bending about the local 2 axis. [L 3 ]
        Z33 (output): The plastic modulus for bending about the local 3 axis. [L 3 ]
        R22 (output): The radius of gyration about the local 2 axis. [L]
        R33 (output): The radius of gyration about the local 3 axis. [L]
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetGeneral(Name, "", "", 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetGeneral falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetHybridISection(self, name: str, GUID: str):
        """This function retrieves frame section property data for a steel hybrid I frame section. The
        function returns zero if the section property data is successfully retrieved,
        otherwise it returns a nonzero value.
    
        MatPropTopFlange (output): The name of the material property for the top flange.
        MatPropWeb (output): The name of the material property for the web.
        MatPropBotFlange (output): The name of the material property for the bottom flange.
        t3 (output): The height of the section. [L]
        t2 (output): The width of the top flange. [L]
        TF (output): The thickness of the top flange. [L]
        TW (output): The thickness of the web. [L]
        t2b (output): The width of the bottom flange. [L]
        tfb (output): The thickness of the bottom flange. [L]
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetHybridISection(name, "", "", "", 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0, "", GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetHybridISection falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetHybridUSection(self, name: str, GUID: str):
        """This function retrieves frame section property data for a steel hybrid U frame section. The
        function returns zero if the section property data is successfully retrieved,
        otherwise it returns a nonzero value.
    
        WebMaterial (output): The name of the material property for the webs.
        TopFlangeMaterial (output): The name of the material property for the top flanges.
        BotFlangeMaterial (output): The name of the material property for the bottom flange.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetHybridUSection(name, "", "", "", [], 0, "", GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetHybridUSection falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetISection(self, Name: str, Color: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for an I-type frame section. The
        function returns zero if the section property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing I-type frame section property.
        FileName (output): If the section property was imported from a property file, this
            is the name of that file. If the section property was not imported, this item is
            blank.
        MatProp (output): The name of the material property for the section.
        t3 (output): The section depth. [L]
        t2 (output): The top flange width. [L]
        tf (output): The top flange thickness. [L]
        tw (output): The web thickness. [L]
        t2b (output): The bottom flange width. [L]
        tfb (output): The bottom flange thickness. [L]
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetISection(Name, "", "", 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetISection falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetModifiers(self, Name: str):
        """This function retrieves the modifier assignments for a frame section property. The default
        value for all modifiers is one. The function returns zero if the modifier
        assignments are successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property.
        Value (output): This is an array of eight unitless modifiers. Value(0) = Cross
            sectional area modifier Value(1) = Shear area in local 2 direction modifier
            Value(2) = Shear area in local 3 direction modifier Value(3) = Torsional
            constant modifier Value(4) = Moment of inertia about local 2 axis modifier
            Value(5) = Moment of inertia about local 3 axis modifier Value(6) = Mass
            modifier Value(7) = Weight modifier
        """
        _r = self._raw.GetModifiers(Name, [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetModifiers falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetNameInPropFile(self, Name: str):
        """This function retrieves the names of the section property file from which an imported frame
        section originated, and it also retrieves the section name used in the property
        file. The function returns zero if the names are successfully retrieved; otherwise
        it returns nonzero. If the specified frame section property was not imported, blank
        strings are returned for NameInFile and FileName.
    
        Name (input): The name of an existing frame section property.
        NameInFile (output): The name of the specified frame section property in the frame
            section property file.
        FileName (output): The name of the frame section property file from which the
            specified frame section property was obtained.
        MatProp (output): The name of the material property for the section.
        PropType (output): This is one of the following items in the eFramePropType
            enumeration. SECTION_I = 1 SECTION_CHANNEL = 2 SECTION_T = 3 SECTION_ANGLE = 4
            SECTION_DBLANGLE = 5 SECTION_BOX = 6 SECTION_PIPE = 7 SECTION_RECTANGULAR = 8
            SECTION_CIRCLE = 9 SECTION_GENERAL = 10 SECTION_DBCHANNEL = 11 SECTION_AUTO = 12
            SECTION_SD = 13 SECTION_VARIABLE = 14 SECTION_JOIST = 15 SECTION_BRIDGE = 16
            SECTION_COLD_C = 17 SECTION_COLD_2C = 18 SECTION_COLD_Z = 19 SECTION_COLD_L = 20
            SECTION_COLD_2L = 21 SECTION_COLD_HAT = 22 SECTION_BUILTUP_I_COVERPLATE = 23
            SECTION_PCC_GIRDER_I = 24 SECTION_PCC_GIRDER_U = 25
        """
        _r = self._raw.GetNameInPropFile(Name, "", "", "", None)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetNameInPropFile falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNameList(self, PropType: int = None):
        """This function retrieves the names of all defined frame section properties of the specified
        type. The function returns zero if the names are successfully retrieved; otherwise
        it returns nonzero.
    
        NumberNames (output): The number of frame section property names retrieved by the
            program.
        MyName (output): This is a one-dimensional array of frame section property names.
            The MyName array is created as a dynamic, zero-based, array by the API user: Dim
            MyName() as String The array is dimensioned to (NumberNames - 1) inside the
            SAP2000 program, filled with the names, and returned to the API user.
        PropType (input): This optional value is one of the following items in the
            eFramePropType enumeration. SECTION_I = 1 SECTION_CHANNEL = 2 SECTION_T = 3
            SECTION_ANGLE = 4 SECTION_DBLANGLE = 5 SECTION_BOX = 6 SECTION_PIPE = 7
            SECTION_RECTANGULAR = 8 SECTION_CIRCLE = 9 SECTION_GENERAL = 10
            SECTION_DBCHANNEL = 11 SECTION_AUTO = 12 SECTION_SD = 13 SECTION_VARIABLE = 14
            SECTION_JOIST = 15 SECTION_BRIDGE = 16 SECTION_COLD_C = 17 SECTION_COLD_2C = 18
            SECTION_COLD_Z = 19 SECTION_COLD_L = 20 SECTION_COLD_2L = 21 SECTION_COLD_HAT =
            22 SECTION_BUILTUP_I_COVERPLATE = 23 SECTION_PCC_GIRDER_I = 24
            SECTION_PCC_GIRDER_U = 25 SECTION_BUILTUP_I_HYBRID = 26 SECTION_BUILTUP_U_HYBRID
            = 27 If no value is input for PropType, names are returned for all frame section
            properties in the model regardless of type.
        """
        _r = self._raw.GetNameList(0, [], PropType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNonPrismatic(self, Name: str, NumberItems: int, Color: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for nonprismatic (variable) sections.
        The function returns zero if the data is successfully retrieved; otherwise it
        returns a nonzero value.
    
        NumberItems (input): The number of segments assigned to the nonprismatic section.
        StartSec (output): This is an array of the names of the frame section properties at
            the start of each segment.
        EndSec (output): This is an array of the names of the frame section properties at
            the end of each segment.
        MyLength (output): This is an array that includes the length of each segment. The
            length may be variable or absolute as indicated by the MyType item. [L] when
            length is absolute
        MyType (output): This is an array of either 1 or 2, indicating the length type for
            each segment. 1 = Variable (relative length) 2 = Absolute
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetNonPrismatic(Name, NumberItems, [], [], [], [], [], [], Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetNonPrismatic falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPipe(self, Name: str, Color: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for a pipe-type frame section. The
        function returns zero if the section property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property.
        FileName (output): If the section property was imported from a property file, this
            is the name of that file. If the section property was not imported, this item is
            blank.
        MatProp (output): The name of the material property for the section.
        t3 (output): The outside diameter. [L]
        tw (output): The wall thickness. [L]
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetPipe(Name, "", "", 0.0, 0.0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetPipe falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPrecastI_1(self, Name: str, Color: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for a precast concrete I girder frame
        section. The function returns zero if the section property data is successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing precast concrete I girder frame section
            property.
        FileName (output): If the section property was imported from a property file, this
            is the name of that file. If the section property was not imported, this item is
            blank.
        MatProp (output): The name of the material property for the section.
        b (output): This is an array, dimensioned to 3, containing the horizontal section
            dimensions. [L] b(0) = B1 (> 0) b(1) = B2 (> 0) b(2) = B3 (>= 0) b(3) = B4 (>=
            0) Section dimensions B1 through B4 are defined on the precast concrete I girder
            definition form.
        d (output): This is an array, dimensioned to 5, containing the vertical section
            dimensions. [L] d(0) = D1 (> 0) d(1) = D2 (> 0) d(2) = D3 (>= 0) d(3) = D4 (>=
            0) d(4) = D5 (> 0) d(5) = D6 (>= 0) d(6) = D7 (>=0) Section dimensions D1
            through D7 are defined on the precast concrete I girder definition form.
        t (output): This is an array, dimensioned to 1, containing the web thickness
            dimensions. [L] T(0) = T1 (> 0) T(1) = T2 (> 0) Section dimensions T1 and T2 are
            defined on the precast I girder definition form.
        c (output): The bottom flange chamfer dimension, denoted as C1 on the precast
            concrete I girder definition form.
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetPrecastI_1(Name, "", "", [], [], [], 0.0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetPrecastI_1 falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPrecastU(self, Name: str, Color: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for a precast concrete U girder frame
        section. The function returns zero if the section property data is successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing precast concrete U girder frame section
            property.
        FileName (output): If the section property was imported from a property file, this
            is the name of that file. If the section property was not imported, this item is
            blank.
        MatProp (output): The name of the material property for the section.
        b (output): This is an array, dimensioned to 5, containing the horizontal section
            dimensions. [L] b(0) = B1 (> 0) b(1) = B2 (> 0) b(2) = B3 (> 0) b(3) = B4 (>= 0)
            b(4) = B5 (>= 0) b(5) = B6 (>= 0) Section dimensions B1 through B6 are defined
            on the precast concrete U girder definition form.
        d (output): This is an array, dimensioned to 6, containing the vertical section
            dimensions. [L] d(0) = D1 (> 0) d(1) = D2 (> 0) d(2) = D3 (>= 0) d(3) = D4 (>=
            0) d(4) = D5 (>= 0) d(5) = D6 (>= 0) d(6) = D7 (>= 0) Section dimensions D1
            through D7 are defined on the precast concrete U girder definition form.
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetPrecastU(Name, "", "", [], [], Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetPrecastU falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPropFileNameList(self, FileName: str, PropType: int = None):
        """This function retrieves the names of all defined frame section properties of a specified
        type in a specified frame section property file. The function returns zero if the
        names are successfully retrieved; otherwise it returns a nonzero value.
    
        FileName (input): The name of the frame section property file from which to get the
            name list. In most cases, inputting only the name of the property file (e.g.
            Sections8.pro) is required, and the program will be able to find it. In some
            cases, inputting the full path to the property file may be necessary.
        NumberNames (output): The number of frame section property names retrieved by the
            program.
        MyName (output): This is an array the includes the property names obtained from the
            frame section property file.
        PropType (input): This optional value is one of the following items in the
            eFramePropType enumeration. SECTION_I = 1 SECTION_CHANNEL = 2 SECTION_T = 3
            SECTION_ANGLE = 4 SECTION_DBLANGLE = 5 SECTION_BOX = 6 SECTION_PIPE = 7
            SECTION_RECTANGULAR = 8 SECTION_CIRCLE = 9 SECTION_GENERAL = 10
            SECTION_DBCHANNEL = 11 SECTION_AUTO = 12 SECTION_SD = 13 SECTION_VARIABLE = 14
            SECTION_JOIST = 15 SECTION_BRIDGE = 16 SECTION_COLD_C = 17 SECTION_COLD_2C = 18
            SECTION_COLD_Z = 19 SECTION_COLD_L = 20 SECTION_COLD_2L = 21 SECTION_COLD_HAT =
            22 SECTION_BUILTUP_I_COVERPLATE = 23 SECTION_PCC_GIRDER_I = 24
            SECTION_PCC_GIRDER_U = 25 SECTION_BUILTUP_I_HYBRID = 26 SECTION_BUILTUP_U_HYBRID
            = 27 If no value is input for PropType, names are returned for all frame section
            properties in the specified file regardless of type.
        """
        _r = self._raw.GetPropFileNameList(FileName, 0, [], [], PropType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetPropFileNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetRebarBeam(self, Name: str):
        """This function retrieves beam rebar data for frame sections. The function returns zero if the
        data is successfully retrieved; otherwise it returns a nonzero value. This function
        applies only to the following section types. Calling this function for any other
        type of frame section property returns an error. SECTION_T = 3 SECTION_ANGLE = 4
        SECTION_RECTANGULAR = 8 SECTION_CIRCLE = 9 The material assigned to the specified
        frame section property must be concrete or this function returns an error.
    
        Name (input): The name of an existing frame section property.
        MatPropLong (output): The name of the rebar material property for the longitudinal
            rebar.
        MatPropConfine (output): The name of the rebar material property for the confinement
            rebar.
        CoverTop (output): The distance from the top of the beam to the centroid of the top
            longitudinal reinforcement. [L]
        CoverBot (output): The distance from the bottom of the beam to the centroid of the
            bottom longitudinal reinforcement. [L]
        TopLeftArea (output): The total area of longitudinal reinforcement at the top left
            end of the beam. [L 2 ]
        TopRightArea (output): The total area of longitudinal reinforcement at the top right
            end of the beam. [L 2 ]
        BotLeftArea (output): The total area of longitudinal reinforcement at the bottom
            left end of the beam. [L 2 ]
        BotRightArea (output): The total area of longitudinal reinforcement at the bottom
            right end of the beam. [L 2 ]
        """
        _r = self._raw.GetRebarBeam(Name, "", "", 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetRebarBeam falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetRebarColumn(self, Name: str, ToBeDesigned: bool):
        """This function retrieves column rebar data for frame sections. The function returns zero if
        the data is successfully retrieved; otherwise it returns a nonzero value. This
        function applies only to the following section types. Calling this function for any
        other type of frame section property returns an error. SECTION_RECTANGULAR = 8
        SECTION_CIRCLE = 9 The material assigned to the specified frame section property
        must be concrete or else this function returns an error.
    
        Name (input): The name of an existing frame section property.
        MatPropLong (output): The name of the rebar material property for the longitudinal
            rebar.
        MatPropConfine (output): The name of the rebar material property for the confinement
            rebar.
        Pattern (output): This is either 1 or 2, indicating the rebar configuration. 1 =
            Rectangular 2 = Circular For circular frame section properties, this item must
            be 2; otherwise an error is returned.
        ConfineType (output): This is either 1 or 2, indicating the confinement bar type. 1
            = Ties 2 = Spiral This item applies only when Pattern = 2. If Pattern = 1, the
            confinement bar type is assumed to be ties.
        Cover (output): The clear cover for the confinement steel (ties). In the special
            case of circular reinforcement in a rectangular column, this is the minimum
            clear cover. [L]
        NumberCBars (output): This item applies to a circular rebar configuration, Pattern =
            2. It is the total number of longitudinal reinforcing bars in the column.
        NumberR3Bars (output): This item applies to a rectangular rebar configuration,
            Pattern = 1. It is the number of longitudinal bars (including the corner bar) on
            each face of the column that is parallel to the local 3-axis of the column.
        NumberR2Bars (output): This item applies to a rectangular rebar configuration,
            Pattern = 1. It is the number of longitudinal bars (including the corner bar) on
            each face of the column that is parallel to the local 2-axis of the column.
        RebarSize (output): The rebar name for the longitudinal rebar in the column.
        TieSize (output): The rebar name for the confinement rebar in the column.
        TieSpacingLongit (output): The longitudinal spacing of the confinement bars (ties).
            [L]
        Number2DirTieBars (output): This item applies to a rectangular reinforcing
            configuration, Pattern = 1. It is the number of confinement bars (tie legs)
            extending in the local 2-axis direction of the column.
        Number3DirTieBars (output): This item applies to a rectangular reinforcing
            configuration, Pattern = 1. It is the number of confinement bars (tie legs)
            extending in the local 3-axis direction of the column.
        ToBeDesigned (input): If this item is True, the column longitudinal rebar is to be
            designed; otherwise it is to be checked.
        """
        _r = self._raw.GetRebarColumn(Name, "", "", 0, 0, 0.0, 0, 0, 0, "", "", 0.0, 0, 0, ToBeDesigned)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetRebarColumn falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetRectangle(self, Name: str, Color: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for a rectangular frame section. The
        function returns zero if the section property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing rectangular frame section property.
        FileName (output): If the section property was imported from a property file, this
            is the name of that file. If the section property was not imported, this item is
            blank.
        MatProp (output): The name of the material property for the section.
        t3 (output): The section depth. [L]
        t2 (output): The section width. [L]
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetRectangle(Name, "", "", 0.0, 0.0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetRectangle falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSDSection(self, Name: str, Color: int, Notes: str, GUID: str):
        """This function retrieves section property data for a section designer section. The function
        returns zero if the section property data is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing section designer property.
        MatProp (output): The name of the base material property for the section.
        NumberItems (output): The number of shapes defined in the section designer section.
        ShapeName (output): This is an array that includes the name of each shape in the
            section designer section.
        MyType (output): This is an array that includes the type of each shape in the
            section designer section. 1 = I-section 2 = Channel 3 = Tee 4 = Angle 5 = Double
            Angle 6 = Box 7 = Pipe 8 = Plate 101 = Solid Rectangle 102 = Solid Circle 103 =
            Solid Segment 104 = Solid Sector 201 = Polygon 301 = Reinforcing Single 302 =
            Reinforcing Line 303 = Reinforcing Rectangle 304 = Reinforcing Circle 401 =
            Reference Line 402 = Reference Circle 501 = Caltrans Square 502 = Caltrans
            Circle 503 = Caltrans Hexagon 504 = Caltrans Octagon
        DesignType (output): This is 0, 1, 2 or 3, indicating the design option for the
            section. 0 = No design 1 = Design as general steel section 2 = Design as a
            concrete column; check the reinforcing 3 = Design as a concrete column; design
            the reinforcing
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetSDSection(Name, "", 0, [], [], 0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetSDSection falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSectProps(self, Name: str):
        """This function retrieves properties for frame section. The function returns zero if the
        property data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property.
        Area (output): The cross-sectional area. [L 2 ]
        As2 (output): The shear area for forces in the section local 2-axis direction. [L 2
            ]
        As3 (output): The shear area for forces in the section local 3-axis direction. [L 2
            ]
        Torsion (output): The torsional constant. [L 4 ]
        I22 (output): The moment of inertia for bending about the local 2 axis. [L 4 ]
        I33 (output): The moment of inertia for bending about the local 3 axis. [L 4 ]
        S22 (output): The section modulus for bending about the local 2 axis. [L 3 ]
        S33 (output): The section modulus for bending about the local 3 axis. [L 3 ]
        Z22 (output): The plastic modulus for bending about the local 2 axis. [L 3 ]
        Z33 (output): The plastic modulus for bending about the local 3 axis. [L 3 ]
        R22 (output): The radius of gyration about the local 2 axis. [L]
        R33 (output): The radius of gyration about the local 3 axis. [L]
        """
        _r = self._raw.GetSectProps(Name, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetSectProps falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTee(self, Name: str, Color: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for a tee-type frame section. The
        function returns zero if the section property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property.
        FileName (output): If the section property was imported from a property file, this
            is the name of that file. If the section property was not imported, this item is
            blank.
        MatProp (output): The name of the material property for the section.
        t3 (output): The section depth. [L]
        t2 (output): The flange width. [L]
        tf (output): The flange thickness. [L]
        tw (output): The web thickness. [L]
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetTee(Name, "", "", 0.0, 0.0, 0.0, 0.0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetTee falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTube(self, Name: str, Color: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for a tube-type frame section. The
        function returns zero if the section property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property.
        FileName (output): If the section property was imported from a property file, this
            is the name of that file. If the section property was not imported, this item is
            blank.
        MatProp (output): The name of the material property for the section.
        t3 (output): The section depth. [L]
        t2 (output): The section width. [L]
        tf (output): The flange thickness. [L]
        tw (output): The web thickness. [L]
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetTube(Name, "", "", 0.0, 0.0, 0.0, 0.0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetTube falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTypeRebar(self, Name: str):
        """This function retrieves the rebar design type for the specified frame section property. The
        function returns zero if the type is successfully retrieved; otherwise it returns
        nonzero. This function applies only to the following section property types. Calling
        this function for any other type of frame section property returns an error.
        SECTION_T = 3 SECTION_ANGLE = 4 SECTION_RECTANGULAR = 8 SECTION_CIRCLE = 9 A nonzero
        rebar type is returned only if the frame section property has a concrete material.
    
        Name (input): The name of an existing frame section property.
        """
        _r = self._raw.GetTypeRebar(Name, 0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetTypeRebar falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetTypeOAPI(self, Name: str):
        """This function retrieves the property type for the specified frame section property. The
        function returns zero if the type is successfully retrieved; otherwise it returns
        nonzero.
    
        Name (input): The name of an existing frame section property.
        PropType (output): This is one of the following items in the eFramePropType
            enumeration. SECTION_I = 1 SECTION_CHANNEL = 2 SECTION_T = 3 SECTION_ANGLE = 4
            SECTION_DBLANGLE = 5 SECTION_BOX = 6 SECTION_PIPE = 7 SECTION_RECTANGULAR = 8
            SECTION_CIRCLE = 9 SECTION_GENERAL = 10 SECTION_DBCHANNEL = 11 SECTION_AUTO = 12
            SECTION_SD = 13 SECTION_VARIABLE = 14 SECTION_JOIST = 15 SECTION_BRIDGE = 16
            SECTION_COLD_C = 17 SECTION_COLD_2C = 18 SECTION_COLD_Z = 19 SECTION_COLD_L = 20
            SECTION_COLD_2L = 21 SECTION_COLD_HAT = 22 SECTION_BUILTUP_I_COVERPLATE = 23
            SECTION_PCC_GIRDER_I = 24 SECTION_PCC_GIRDER_U = 25
        """
        _r = self._raw.GetTypeOAPI(Name, None)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetTypeOAPI falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def ImportProp(self, Name: str, MatProp: str, FileName: str, PropName: str, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function imports a frame section property from a property file. The function returns
        zero if the section property is successfully initialized; otherwise it returns a
        nonzero value. If the property file is not found, or the specified property name is
        not found in the property file, the section is set to be a general section with
        default properties.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added. This name does not need to be the same as the PropName item.
        MatProp (input): The name of the material property for the section.
        FileName (input): The name of the frame section property file from which to get the
            frame section property specified by the PropName item. In most cases you can
            input just the name of the property file (e.g. Sections8.pro) and the program
            will be able to find it. In some cases you may have to input the full path to
            the property file.
        PropName (input): The name of the frame section property, inside the property file
            specified by the FileName item, that is to be imported.
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.ImportProp(Name, MatProp, FileName, PropName, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.ImportProp falhou (ret={_r})".format(_r=_r))
        return None

    def SetAngle(self, Name: str, MatProp: str, t3: float, t2: float, tf: float, tw: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes an angle-type frame section property. If this function is called
        for an existing frame section property, all items for the section are reset to their
        default value. The function returns zero if the section property is successfully
        initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        MatProp (input): The name of the material property for the section.
        t3 (input): The vertical leg depth. [L]
        t2 (input): The horizontal leg width. [L]
        tf (input): The horizontal leg thickness. [L]
        tw (input): The vertical leg thickness. [L]
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section. GUID The GUID (global
            unique identifier), if any, assigned to the section. If this item is input as
            Default, then the program assigns a GUID to the section.
        """
        _r = self._raw.SetAngle(Name, MatProp, t3, t2, tf, tw, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetAngle falhou (ret={_r})".format(_r=_r))
        return None

    def SetAutoSelectAluminum(self, Name: str, NumberItems: int, SectName: list[str], AutoStartSection: str = 'Median', Notes: str = '', GUID: str = ''):
        """This function assigns frame section properties to an auto select list. If this function is
        called for an existing frame section property, all items for the section are reset
        to their default value. The function returns zero if the auto select list is
        successfully filled; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        NumberItems (input): The number of frame section properties included in the auto
            select list.
        SectName (input): This is an array of the names of the frame section properties
            included in the auto select list. Auto select lists and nonprismatic (variable)
            sections are not allowed in this array.
        AutoStartSection (input): This is Median or the name of a frame section property in
            the SectName array. It is the starting section for the auto select list.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetAutoSelectAluminum(Name, NumberItems, SectName, AutoStartSection, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetAutoSelectAluminum falhou (ret={_r})".format(_r=_r))
        return None

    def SetAutoSelectColdFormed(self, Name: str, NumberItems: int, SectName: list[str], AutoStartSection: str = 'Median', Notes: str = '', GUID: str = ''):
        """This function assigns frame section properties to an auto select list. If this function is
        called for an existing frame section property, all items for the section are reset
        to their default value. The function returns zero if the auto select list is
        successfully filled; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        NumberItems (input): The number of frame section properties included in the auto
            select list.
        SectName (input): This is an array of the names of the frame section properties
            included in the auto select list. Auto select lists and nonprismatic (variable)
            sections are not allowed in this array.
        AutoStartSection (input): This is Median or the name of a frame section property in
            the SectName array. It is the starting section for the auto select list.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetAutoSelectColdFormed(Name, NumberItems, SectName, AutoStartSection, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetAutoSelectColdFormed falhou (ret={_r})".format(_r=_r))
        return None

    def SetAutoSelectSteel(self, Name: str, NumberItems: int, SectName: list[str], AutoStartSection: str = 'Median', Notes: str = '', GUID: str = ''):
        """This function assigns frame section properties to an auto select list. If this function is
        called for an existing frame section property, all items for the section are reset
        to their default value. The function returns zero if the auto select list is
        successfully filled; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        NumberItems (input): The number of frame section properties included in the auto
            select list.
        SectName (input): This is an array of the names of the frame section properties
            included in the auto select list. Auto select lists and nonprismatic (variable)
            sections are not allowed in this array.
        AutoStartSection (input): This is either Median or the name of a frame section
            property in the SectName array. It is the starting section for the auto select
            list.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetAutoSelectSteel(Name, NumberItems, SectName, AutoStartSection, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetAutoSelectSteel falhou (ret={_r})".format(_r=_r))
        return None

    def SetChannel(self, Name: str, MatProp: str, t3: float, t2: float, tf: float, tw: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes a channel-type frame section property. If this function is called
        for an existing frame section property, all items for the section are reset to their
        default value. The function returns zero if the section property is successfully
        initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        MatProp (input): The name of the material property for the section.
        t3 (input): The section depth. [L]
        t2 (input): The flange width. [L]
        tf (input): The flange thickness. [L]
        tw (input): The web thickness. [L]
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetChannel(Name, MatProp, t3, t2, tf, tw, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetChannel falhou (ret={_r})".format(_r=_r))
        return None

    def SetCircle(self, Name: str, MatProp: str, t3: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes a solid circular frame section property. If this function is
        called for an existing frame section property, all items for the section are reset
        to their default value. The function returns zero if the section property is
        successfully initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        MatProp (input): The name of the material property for the section.
        t3 (input): The section diameter. [L]
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetCircle(Name, MatProp, t3, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetCircle falhou (ret={_r})".format(_r=_r))
        return None

    def SetColdC(self, Name: str, MatProp: str, t3: float, t2: float, Thickness: float, Radius: float, LipDepth: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes an cold formed C-type frame section property. If this function is
        called for an existing frame section property, all items for the section are reset
        to their default value. The function returns zero if the section property is
        successfully initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        MatProp (input): The name of the material property for the section.
        t3 (input): The section depth. [L]
        t2 (input): The section width. [L]
        Thickness (input): The section thickness. [L]
        Radius (input): The corner radius, if any. [L]
        LipDepth (input): The lip depth, if any. [L]
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetColdC(Name, MatProp, t3, t2, Thickness, Radius, LipDepth, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetColdC falhou (ret={_r})".format(_r=_r))
        return None

    def SetColdHat(self, Name: str, MatProp: str, t3: float, t2: float, Thickness: float, Radius: float, LipDepth: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes an cold formed hat-type frame section property. If this function
        is called for an existing frame section property, all items for the section are
        reset to their default value. The function returns zero if the section property is
        successfully initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        MatProp (input): The name of the material property for the section.
        t3 (input): The section depth. [L]
        t2 (input): The section width. [L]
        Thickness (input): The section thickness. [L]
        Radius (input): The corner radius, if any. [L]
        LipDepth (input): The lip depth, if any. [L]
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, then the program assigns a GUID to the
            section.
        """
        _r = self._raw.SetColdHat(Name, MatProp, t3, t2, Thickness, Radius, LipDepth, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetColdHat falhou (ret={_r})".format(_r=_r))
        return None

    def SetColdZ(self, Name: str, MatProp: str, t3: float, t2: float, Thickness: float, Radius: float, LipDepth: float, LipAngle: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes an cold formed Z-type frame section property. If this function is
        called for an existing frame section property, all items for the section are reset
        to their default value. The function returns zero if the section property is
        successfully initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property then that property is modified, otherwise, a new property is
            added.
        MatProp (input): The name of the material property for the section.
        t3 (input): The section depth. [L]
        t2 (input): The section width. [L]
        Thickness (input): The section thickness. [L]
        Radius (input): The corner radius, if any. [L]
        LipDepth (input): The lip depth, if any. [L]
        LipAngle (input): The lip angle measured from horizontal (0 <= LipAngle <= 90).
            [deg]
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetColdZ(Name, MatProp, t3, t2, Thickness, Radius, LipDepth, LipAngle, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetColdZ falhou (ret={_r})".format(_r=_r))
        return None

    def SetCoverPlatedI(self, Name: str, SectName: str, FyTopFlange: float, FyWeb: float, FyBotFlange: float, tc: float, bc: float, MatPropTop: str, tcb: float, bcb: float, MatPropBot: str, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes a cover plated I-type frame section property. If this function is
        called for an existing frame section property, all items for the section are reset
        to their default value. The function returns zero if the section property is
        successfully initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        SectName (input): The name of an existing I-type frame section property that is used
            for the I-section portion of the coverplated I section.
        FyTopFlange (input): The yield strength of the top flange of the I-section. [F/L 2 ]
            If this item is 0, the yield strength of the I-section specified by the SectName
            item is used.
        FyWeb (input): The yield strength of the web of the I-section. [F/L 2 ] If this item
            is 0, the yield strength of the I-section specified by the SectName item is
            used.
        FyBotFlange (input): The yield strength of the bottom flange of the I-section. [F/L
            2 ] If this item is 0, the yield strength of the I-section specified by the
            SectName item is used.
        tc (input): The thickness of the top cover plate. [L] If the tc or the bc item is
            less than or equal to 0, no top cover plate exists.
        bc (input): The width of the top cover plate. [L] If the tc or the bc item is less
            than or equal to 0, no top cover plate exists.
        MatPropTop (input): The name of the material property for the top cover plate. This
            item applies only if both the tc and the bc items are greater than 0.
        tcb (input): The thickness of the bottom cover plate. [L] If the tcb or the bcb item
            is less than or equal to 0, no bottom cover plate exists.
        bcb (input): The width of the bottom cover plate. [L] If the tcb or the bcb item is
            less than or equal to 0, no bottom cover plate exists.
        MatPropBot (input): The name of the material property for the bottom cover plate.
            This item applies only if both the tcb and the bcb items are greater than 0.
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetCoverPlatedI(Name, SectName, FyTopFlange, FyWeb, FyBotFlange, tc, bc, MatPropTop, tcb, bcb, MatPropBot, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetCoverPlatedI falhou (ret={_r})".format(_r=_r))
        return None

    def SetDblAngle(self, Name: str, MatProp: str, t3: float, t2: float, tf: float, tw: float, dis: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes a double angle-type frame section property. If this function is
        called for an existing frame section property, all items for the section are reset
        to their default value. The function returns zero if the section property is
        successfully initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        MatProp (input): The name of the material property for the section.
        t3 (input): The vertical leg depth. [L]
        t2 (input): The total width of the section, that is, the sum of the widths of each
            horizontal leg plus the back-to-back distance. [L]
        tf (input): The horizontal leg thickness. [L]
        tw (input): The vertical leg thickness. [L]
        dis (input): The back-to-back distance between the angles. [L]
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetDblAngle(Name, MatProp, t3, t2, tf, tw, dis, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetDblAngle falhou (ret={_r})".format(_r=_r))
        return None

    def SetDblChannel(self, Name: str, MatProp: str, t3: float, t2: float, tf: float, tw: float, dis: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes a double channel-type frame section property. If this function is
        called for an existing frame section property, all items for the section are reset
        to their default value. The function returns zero if the section property is
        successfully initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        MatProp (input): The name of the material property for the section.
        t3 (input): The section depth. [L]
        t2 (input): The total width of the section, that is, the sum of the widths of each
            flange plus the back-to-back distance. [L]
        tf (input): The flange thickness. [L]
        tw (input): The web thickness. [L]
        dis (input): The back-to-back distance between the channels. [L]
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetDblChannel(Name, MatProp, t3, t2, tf, tw, dis, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetDblChannel falhou (ret={_r})".format(_r=_r))
        return None

    def SetGeneral(self, Name: str, MatProp: str, t3: float, t2: float, Area: float, As2: float, As3: float, Torsion: float, I22: float, I33: float, S22: float, S33: float, Z22: float, Z33: float, R22: float, R33: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes a general frame section property. If this function is called for
        an existing frame section property, all items for the section are reset to their
        default value. The function returns zero if the section property is successfully
        initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        MatProp (input): The name of the material property for the section.
        t3 (input): The section depth. [L]
        t2 (input): The section width. [L]
        Area (input): The cross-sectional area. [L 2 ]
        As2 (input): The shear area for forces in the section local 2-axis direction. [L 2 ]
        As3 (input): The shear area for forces in the section local 3-axis direction. [L 2 ]
        Torsion (input): The torsional constant. [L 4 ]
        I22 (input): The moment of inertia for bending about the local 2 axis. [L 4 ]
        I33 (input): The moment of inertia for bending about the local 3 axis. [L 4 ]
        S22 (input): The section modulus for bending about the local 2 axis. [L 3 ]
        S33 (input): The section modulus for bending about the local 3 axis. [L 3 ]
        Z22 (input): The plastic modulus for bending about the local 2 axis. [L 3 ]
        Z33 (input): The plastic modulus for bending about the local 3 axis. [L 3 ]
        R22 (input): The radius of gyration about the local 2 axis. [L]
        R33 (input): The radius of gyration about the local 3 axis. [L]
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetGeneral(Name, MatProp, t3, t2, Area, As2, As3, Torsion, I22, I33, S22, S33, Z22, Z33, R22, R33, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetGeneral falhou (ret={_r})".format(_r=_r))
        return None

    def SetHybridISection(self, Name: str, MatPropTopFlange: str, MatPropWeb: str, MatPropBotFlange: str, t3: float, t2: float, TF: float, TW: float, t2b: float, tfb: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes a steel hybrid I frame section property. If this function is
        called for an existing frame section property then all items for the section are
        reset to their default value. The function returns zero if the section property is
        successfully initialized, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property then that property is modified, otherwise, a new property is
            added.
        MatPropTopFlange (input): The name of the material property for the top flange.
        MatPropWeb (input): The name of the material property for the web.
        MatPropBotFlange (input): The name of the material property for the bottom flange.
        t3 (input): The height of the section. [L]
        t2 (input): The width of the top flange. [L]
        TF (input): The thickness of the top flange. [L]
        TW (input): The thickness of the web. [L]
        t2b (input): The width of the bottom flange. [L]
        tfb (input): The thickness of the bottom flange. [L]
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, then the program assigns a GUID to the
            section.
        """
        _r = self._raw.SetHybridISection(Name, MatPropTopFlange, MatPropWeb, MatPropBotFlange, t3, t2, TF, TW, t2b, tfb, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetHybridISection falhou (ret={_r})".format(_r=_r))
        return None

    def SetHybridUSection(self, Name: str, WebMaterial: str, TopFlangeMaterial: str, BotFlangeMaterial: str, T: list[float], Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes a steel hybrid U frame section property. If this function is
        called for an existing frame section property then all items for the section are
        reset to their default value. The function returns zero if the section property is
        successfully initialized, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property then that property is modified, otherwise, a new property is
            added.
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, then the program assigns a GUID to the
            section.
        """
        _r = self._raw.SetHybridUSection(Name, WebMaterial, TopFlangeMaterial, BotFlangeMaterial, T, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetHybridUSection falhou (ret={_r})".format(_r=_r))
        return None

    def SetISection(self, Name: str, MatProp: str, t3: float, t2: float, tf: float, tw: float, t2b: float, tfb: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes an I-type frame section property. If this function is called for
        an existing frame section property, all items for the section are reset to their
        default value. The function returns zero if the section property is successfully
        initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        MatProp (input): The name of the material property for the section.
        t3 (input): The section depth. [L]
        t2 (input): The top flange width. [L]
        tf (input): The top flange thickness. [L]
        tw (input): The web thickness. [L]
        t2b (input): The bottom flange width. [L]
        tfb (input): The bottom flange thickness. [L]
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetISection(Name, MatProp, t3, t2, tf, tw, t2b, tfb, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetISection falhou (ret={_r})".format(_r=_r))
        return None

    def SetModifiers(self, Name: str, Value: list[float]):
        """This function assigns property modifiers to a frame section property. The default value for
        all modifiers is one. The function returns zero if the modifiers are successfully
        assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property.
        Value (input): This is an array of eight unitless modifiers. Value(0) = Cross
            sectional area modifier Value(1) = Shear area in local 2 direction modifier
            Value(2) = Shear area in local 3 direction modifier Value(3) = Torsional
            constant modifier Value(4) = Moment of inertia about local 2 axis modifier
            Value(5) = Moment of inertia about local 3 axis modifier Value(6) = Mass
            modifier Value(7) = Weight modifier
        """
        _r = self._raw.SetModifiers(Name, Value)
        if _r[1] != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetModifiers falhou (ret={_r})".format(_r=_r))
        return None

    def SetNonPrismatic(self, Name: str, NumberItems: int, StartSec: list[str], EndSec: list[str], MyLength: list[float], MyType: list[int], EI33: list[int], EI22: list[int], Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function assigns data to a nonprismatic frame section property. The function returns
        zero if the data is successfully filled; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        NumberItems (input): The number of segments assigned to the nonprismatic section.
        StartSec (input): This is an array of the names of the frame section properties at
            the start of each segment. Auto select lists and nonprismatic sections are not
            allowed in this array.
        EndSec (input): This is an array of the names of the frame section properties at the
            end of each segment. Auto select lists and nonprismatic sections are not allowed
            in this array.
        MyLength (input): This is an array that includes the length of each segment. The
            length may be variable or absolute as indicated by the MyType item. [L] when
            length is absolute
        MyType (input): This is an array of either 1 or 2, indicating the length type for
            each segment. 1 = Variable (relative length) 2 = Absolute
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetNonPrismatic(Name, NumberItems, StartSec, EndSec, MyLength, MyType, EI33, EI22, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetNonPrismatic falhou (ret={_r})".format(_r=_r))
        return None

    def SetPipe(self, Name: str, MatProp: str, t3: float, tw: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes a pipe-type frame section property. If this function is called for
        an existing frame section property, all items for the section are reset to their
        default value. The function returns zero if the section property is successfully
        initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        MatProp (input): The name of the material property for the section.
        t3 (input): The outside diameter. [L]
        tw (input): The wall thickness. [L]
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetPipe(Name, MatProp, t3, tw, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetPipe falhou (ret={_r})".format(_r=_r))
        return None

    def SetPrecastI_1(self, Name: str, MatProp: str, b: list[float], d: list[float], t: list[float], c: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes a precast concrete I girder frame section property. If this
        function is called for an existing frame section property, all items for the section
        are reset to their default value. The function returns zero if the section property
        is successfully initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        MatProp (input): The name of the material property for the section.
        b (input): This is an array, dimensioned to 3, containing the horizontal section
            dimensions. [L] b(0) = B1 (> 0) b(1) = B2 (> 0) b(2) = B3 (>= 0) b(3) = B4 (>=
            0) Section dimensions B1 through B4 are defined on the precast concrete I girder
            definition form.
        d (input): This is an array, dimensioned to 5, containing the vertical section
            dimensions. [L] d(0) = D1 (> 0) d(1) = D2 (> 0) d(2) = D3 (>= 0) d(3) = D4 (>=
            0) d(4) = D5 (> 0) d(5) = D6 (>= 0) d(6) = D7 (>=0) Section dimensions D1
            through D7 are defined on the precast concrete I girder definition form.
        t (input): This is an array, dimensioned to 1, containing the web thickness
            dimensions. [L] T(0) = T1 (> 0) T(1) = T2 (> 0) Section dimensions T1 and T2 are
            defined on the precast I girder definition form.
        c (input): The bottom flange chamfer dimension, denoted as C1 on the precast
            concrete I girder definition form.
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetPrecastI_1(Name, MatProp, b, d, t, c, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetPrecastI_1 falhou (ret={_r})".format(_r=_r))
        return None

    def SetPrecastU(self, Name: str, MatProp: str, b: list[float], d: list[float], Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes a precast concrete U girder frame section property. If this
        function is called for an existing frame section property, all items for the section
        are reset to their default value. The function returns zero if the section property
        is successfully initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        MatProp (input): The name of the material property for the section.
        b (input): This is an array, dimensioned to 5, containing the horizontal section
            dimensions. [L] b(0) = B1 (> 0) b(1) = B2 (> 0) b(2) = B3 (> 0) b(3) = B4 (>= 0)
            b(4) = B5 (>= 0) b(5) = B6 (>= 0) Section dimensions B1 through B6 are defined
            on the precast concrete U girder definition form.
        d (input): This is an array, dimensioned to 6, containing the vertical section
            dimensions. [L] d(0) = D1 (> 0) d(1) = D2 (> 0) d(2) = D3 (>= 0) d(3) = D4 (>=
            0) d(4) = D5 (>= 0) d(5) = D6 (>= 0) d(6) = D7 (>= 0) Section dimensions D1
            through D7 are defined on the precast concrete U girder definition form.
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetPrecastU(Name, MatProp, b, d, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetPrecastU falhou (ret={_r})".format(_r=_r))
        return None

    def SetRebarBeam(self, Name: str, MatPropLong: str, MatPropConfine: str, CoverTop: float, CoverBot: float, TopLeftArea: float, TopRightArea: float, BotLeftArea: float, BotRightArea: float):
        """This function assigns beam rebar data to frame sections. The function returns zero if the
        rebar data is successfully assigned; otherwise it returns a nonzero value. This
        function applies only to the following section types. Calling this function for any
        other type of frame section property returns an error. SECTION_T = 3 SECTION_ANGLE =
        4 SECTION_RECTANGULAR = 8 SECTION_CIRCLE = 9 The material assigned to the specified
        frame section property must be concrete or this function returns an error.
    
        Name (input): The name of an existing frame section property.
        MatPropLong (input): The name of the rebar material property for the longitudinal
            rebar.
        MatPropConfine (input): The name of the rebar material property for the confinement
            rebar.
        CoverTop (input): The distance from the top of the beam to the centroid of the top
            longitudinal reinforcement. [L]
        CoverBot (input): The distance from the bottom of the beam to the centroid of the
            bottom longitudinal reinforcement. [L]
        TopLeftArea (input): The total area of longitudinal reinforcement at the top left
            end of the beam. [L 2 ]
        TopRightArea (input): The total area of longitudinal reinforcement at the top right
            end of the beam. [L 2 ]
        BotLeftArea (input): The total area of longitudinal reinforcement at the bottom left
            end of the beam. [L 2 ]
        BotRightArea (input): The total area of longitudinal reinforcement at the bottom
            right end of the beam. [L 2 ]
        """
        _r = self._raw.SetRebarBeam(Name, MatPropLong, MatPropConfine, CoverTop, CoverBot, TopLeftArea, TopRightArea, BotLeftArea, BotRightArea)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetRebarBeam falhou (ret={_r})".format(_r=_r))
        return None

    def SetRebarColumn(self, Name: str, MatPropLong: str, MatPropConfine: str, Pattern: int, ConfineType: int, Cover: float, NumberCBars: int, NumberR3Bars: int, NumberR2Bars: int, RebarSize: str, TieSize: str, TieSpacingLongit: float, Number2DirTieBars: int, Number3DirTieBars: int, ToBeDesigned: bool):
        """This function assigns column rebar data to frame sections. The function returns zero if the
        rebar data is successfully assigned; otherwise it returns a nonzero value. This
        function applies only to the following section types. Calling this function for any
        other type of frame section property returns an error. SECTION_RECTANGULAR = 8
        SECTION_CIRCLE = 9 The material assigned to the specified frame section property
        must be concrete or else this function returns an error.
    
        Name (input): The name of an existing frame section property.
        MatPropLong (input): The name of the rebar material property for the longitudinal
            rebar.
        MatPropConfine (input): The name of the rebar material property for the confinement
            rebar.
        Pattern (input): This is either 1 or 2, indicating the rebar configuration. 1 =
            Rectangular 2 = Circular For circular frame section properties this item must be
            2; otherwise an error is returned.
        ConfineType (input): This is either 1 or 2, indicating the confinement bar type. 1 =
            Ties 2 = Spiral This item applies only when Pattern = 2. If Pattern = 1, the
            confinement bar type is assumed to be ties.
        Cover (input): The clear cover for the confinement steel (ties). In the special case
            of circular reinforcement in a rectangular column, this is the minimum clear
            cover. [L]
        NumberCBars (input): This item applies to a circular rebar configuration, Pattern =
            2. It is the total number of longitudinal reinforcing bars in the column.
        NumberR3Bars (input): This item applies to a rectangular rebar configuration,
            Pattern = 1. It is the number of longitudinal bars (including the corner bar) on
            each face of the column that is parallel to the local 3-axis of the column.
        NumberR2Bars (input): This item applies to a rectangular rebar configuration,
            Pattern = 1. It is the number of longitudinal bars (including the corner bar) on
            each face of the column that is parallel to the local 2-axis of the column.
        RebarSize (input): The rebar name for the longitudinal rebar in the column.
        TieSize (input): The rebar name for the confinement rebar in the column.
        TieSpacingLongit (input): The longitudinal spacing of the confinement bars (ties).
            [L]
        Number2DirTieBars (input): This item applies to a rectangular reinforcing
            configuration, Pattern = 1. It is the number of confinement bars (tie legs)
            running in the local 2-axis direction of the column.
        Number3DirTieBars (input): This item applies to a rectangular reinforcing
            configuration, Pattern = 1. It is the number of confinement bars (tie legs)
            running in the local 3-axis direction of the column.
        ToBeDesigned (input): If this item is True, the column longitudinal rebar is to be
            designed; otherwise it is to be checked.
        """
        _r = self._raw.SetRebarColumn(Name, MatPropLong, MatPropConfine, Pattern, ConfineType, Cover, NumberCBars, NumberR3Bars, NumberR2Bars, RebarSize, TieSize, TieSpacingLongit, Number2DirTieBars, Number3DirTieBars, ToBeDesigned)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetRebarColumn falhou (ret={_r})".format(_r=_r))
        return None

    def SetRectangle(self, Name: str, MatProp: str, t3: float, t2: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes a solid rectangular frame section property. If this function is
        called for an existing frame section property, all items for the section are reset
        to their default value. The function returns zero if the section property is
        successfully initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        MatProp (input): The name of the material property for the section.
        t3 (input): The section depth. [L]
        t2 (input): The section width. [L]
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetRectangle(Name, MatProp, t3, t2, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetRectangle falhou (ret={_r})".format(_r=_r))
        return None

    def SetSDSection(self, Name: str, MatProp: str, DesignType: int = 0, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes a section designer property. The function returns zero if the
        section property is successfully initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        MatProp (input): The name of the base material property for the section.
        DesignType (input): This is 0, 1, 2 or 3, indicating the design option for the
            section. 0 = No design 1 = Design as general steel section 2 = Design as a
            concrete column; check the reinforcing 3 = Design as a concrete column; design
            the reinforcing When DesignType = 1 is assigned, the material property specified
            by the MatProp item must be a steel material; otherwise the program sets
            DesignType = 0. Similarly, when DesignType = 2 or DesignType = 3 is assigned,
            the material property specified by the MatProp item must be a concrete material;
            otherwise the program sets DesignType = 0.
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetSDSection(Name, MatProp, DesignType, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetSDSection falhou (ret={_r})".format(_r=_r))
        return None

    def SetTee(self, Name: str, MatProp: str, t3: float, t2: float, tf: float, tw: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes a tee-type frame section property. If this function is called for
        an existing frame section property, all items for the section are reset to their
        default value. The function returns zero if the section property is successfully
        initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        MatProp (input): The name of the material property for the section.
        t3 (input): The section depth. [L]
        t2 (input): The flange width. [L]
        tf (input): The flange thickness. [L]
        tw (input): The web thickness. [L]
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetTee(Name, MatProp, t3, t2, tf, tw, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetTee falhou (ret={_r})".format(_r=_r))
        return None

    def SetTube(self, Name: str, MatProp: str, t3: float, t2: float, tf: float, tw: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes a tube-type frame section property. If this function is called for
        an existing frame section property, all items for the section are reset to their
        default value. The function returns zero if the section property is successfully
        initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        MatProp (input): The name of the material property for the section.
        t3 (input): The section depth. [L]
        t2 (input): The section width. [L]
        tf (input): The flange thickness. [L]
        tw (input): The web thickness. [L]
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetTube(Name, MatProp, t3, t2, tf, tw, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetTube falhou (ret={_r})".format(_r=_r))
        return None

    def GetNotionalSize(self, Name: str):
        """This function retrieves the method to determine the notional size of a frame section for the
        creep and shrinkage calculations. This function is currently worked for the
        steel/aluminum sections - I/Wide Flange, Channel, Tee, Angle, Double Angle, Double
        Channel, Pipe and Tube sections, and all the concrete sections - Rectangular,
        Circular, Pipe, Tube, Precast I. The function returns zero if the parameters are
        successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property.
        stype (output): The type to define the notional size of a section. It can be: "Auto"
            = Program will determine the notional size based on the average thickness of an
            area element. "User" = The notional size is based on the user-defined value.
            "None" = Notional size will not be considered. In other words, the time-
            dependent effect of this section will not be considered.
        Value (output): For stype is "Auto", the Value represents for the scale factor to
            the program - determined notional size; for stype is User, the Value represents
            for the user-defined notional size [L]; for stype is None, the Value will not be
            used and can be set to 1.
        """
        _r = self._raw.GetNotionalSize(Name, "", 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetNotionalSize falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTrapezoidal(self, Name: str, Color: int, Notes: str, GUID: str):
        """This function retrieves frame section property data for a trapezoidal frame section. The
        function returns zero if the section property is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing trapezoidal frame section property.
        FileName (output): If the section property was imported from a property file, this
            is the name of that file. If the section property was not imported, this item is
            blank.
        MatProp (output): The name of the material property for the section.
        t3 (output): The section depth. [L]
        t2 (output): The section top width. [L]
        t2b (output): The section bottom width. [L]
        Color (input): The display color assigned to the section.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
        """
        _r = self._raw.GetTrapezoidal(Name, "", "", 0.0, 0.0, 0.0, Color, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.GetTrapezoidal falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetNotionalSize(self, Name: str, stype: str, Value: float):
        """This function assigns the method to determine the notional size of a frame section for the
        creep and shrinkage calculations. This function is currently worked for the
        steel/aluminum sections - I/Wide Flange, Channel, Tee, Angle, Double Angle, Double
        Channel, Pipe and Tube sections, and all the concrete sections - Rectangular,
        Circular, Pipe, Tube, Precast I. The function returns zero if the parameters are
        successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property.
        stype (input): The type to define the notional size of a section. It can be: "Auto"
            = Program will determine the notional size based on the average thickness of an
            area element. "User" = The notional size is based on the user-defined value.
            "None" = Notional size will not be considered. In other words, the time-
            dependent effect of this section will not be considered.
        Value (input): For stype is "Auto", the Value represents for the scale factor to the
            program - determined notional size; for stype is User, the Value represents for
            the user-defined notional size [L]; for stype is None, the Value will not be
            used and can be set to 1.
        """
        _r = self._raw.SetNotionalSize(Name, stype, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetNotionalSize falhou (ret={_r})".format(_r=_r))
        return None

    def SetTrapezoidal(self, Name: str, MatProp: str, t3: float, t2: float, t2b: float, Color: int = -1, Notes: str = '', GUID: str = ''):
        """This function initializes a solid trapezoidal frame section property. If this function is
        called for an existing frame section property, all items for the section are reset
        to their default value. The function returns zero if the section property is
        successfully initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new frame section property. If this is an
            existing property, that property is modified; otherwise, a new property is
            added.
        MatProp (input): The name of the material property for the section.
        t3 (input): The section depth. [L]
        t2 (input): The section top width. [L]
        t2b (input): The section bottom width. [L]
        Color (input): The display color assigned to the section. If Color is specified as
            -1, the program will automatically assign a color.
        Notes (input): The notes, if any, assigned to the section.
        GUID (input): The GUID (global unique identifier), if any, assigned to the section.
            If this item is input as Default, the program assigns a GUID to the section.
        """
        _r = self._raw.SetTrapezoidal(Name, MatProp, t3, t2, t2b, Color, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SetTrapezoidal falhou (ret={_r})".format(_r=_r))
        return None

    @cached_property
    def SDShape(self):
        return N_PropFrame_SDShape(self._raw.SDShape)


class N_PropFrame_SDShape:
    """Wrapper para SapModel.PropFrame.SDShape."""

    def __init__(self, raw):
        self._raw = raw

    def Delete(self, Name: str, ShapeName: str, All: bool = False):
        """This function deletes shapes from a section designer property. The function returns zero if
        the shape is successfully deleted; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing shape in a section designer property. If
            the All item is True, this item may be specified as a blank string.
        All (input): If this item is True, all shapes in the section designer property
            specified by the Name item are deleted.
        """
        _r = self._raw.Delete(Name, ShapeName, All)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetAngle(self, Name: str, ShapeName: str, Color: int):
        """This function retrieves property data for an Angle shape in a section designer section. The
        function returns zero if the property data is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing Angle shape in the specified frame
            section property.
        MatProp (output): The name of the material property for the shape.
        PropName (output): This is a blank string or the name of a defined Angle property
            that has been imported from a section property file. If it is the name of a
            defined Angle property, the section dimensions are taken from that property.
        Color (input): The fill color assigned to the shape.
        XCenter (output): The X-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        YCenter (output): The Y-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        h (output): The section depth. [L]
        bf (output): The flange width. [L]
        tf (output): The flange thickness. [L]
        tw (output): The web thickness. [L]
        Rotation (output): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        """
        _r = self._raw.GetAngle(Name, ShapeName, "", "", Color, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetAngle falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetChannel(self, Name: str, ShapeName: str, Color: int):
        """This function retrieves property data for a Channel shape in a section designer section. The
        function returns zero if the property data is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing Channel shape in the specified frame
            section property.
        MatProp (output): The name of the material property for the shape.
        PropName (output): This is a blank string or the name of a defined Channel property
            that has been imported from a section property file. If it is the name of a
            defined Channel property, the section dimensions are taken from that property.
        Color (input): The fill color assigned to the shape.
        XCenter (output): The X-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        YCenter (output): The Y-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        h (output): The section depth. [L]
        bf (output): The flange width. [L]
        tf (output): The flange thickness. [L]
        tw (output): The web thickness. [L]
        Rotation (output): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        """
        _r = self._raw.GetChannel(Name, ShapeName, "", "", Color, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetChannel falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDblAngle(self, Name: str, ShapeName: str, Color: int):
        """This function retrieves property data for a Double Angle shape in a section designer
        section. The function returns zero if the property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing Double Angle shape in the specified frame
            section property.
        MatProp (output): The name of the material property for the shape.
        PropName (output): This is a blank string or the name of a defined Double Angle
            property that has been imported from a section property file. If it is the name
            of a defined Double Angle property, then the section dimensions are taken from
            that property.
        Color (input): The fill color assigned to the shape.
        XCenter (output): The X-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        YCenter (output): The Y-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        h (output): The section depth. [L]
        w (output): The flange width. [L]
        tf (output): The flange thickness. [L]
        tw (output): The web thickness. [L]
        dis (output): Separation between the two flanges that are parallel. [L]
        Rotation (output): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        """
        _r = self._raw.GetDblAngle(Name, ShapeName, "", "", Color, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetDblAngle falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetISection(self, Name: str, ShapeName: str, Color: int):
        """This function retrieves property data for an I-section shape in a section designer section.
        The function returns zero if the property data is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing I-section shape in the specified frame
            section property.
        MatProp (output): The name of the material property for the shape.
        PropName (output): This is a blank string or the name of a defined I-section
            property that has been imported from a section property file. If it is the name
            of a defined I-section property, the section dimensions are taken from that
            property.
        Color (input): The fill color assigned to the shape.
        XCenter (output): The X-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        YCenter (output): The Y-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        h (output): The section depth. [L]
        bf (output): The top flange width. [L]
        tf (output): The top flange thickness. [L]
        tw (output): The web thickness. [L]
        bfb (output): The bottom flange width. [L]
        tfb (output): The bottom flange thickness. [L]
        Rotation (output): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        """
        _r = self._raw.GetISection(Name, ShapeName, "", "", Color, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetISection falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPipe(self, Name: str, ShapeName: str, Color: int):
        """This function retrieves property data for a Pipe shape in a section designer section. The
        function returns zero if the property data is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing Pipe shape in the specified frame section
            property.
        MatProp (output): The name of the material property for the shape.
        PropName (output): This is a blank string or the name of a defined Pipe property
            that has been imported from a section property file. If it is the name of a
            defined Pipe property, the section dimensions are taken from that property.
        Color (input): The fill color assigned to the shape.
        XCenter (output): The X-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        YCenter (output): The Y-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        diameter (output): The outer diameter of the Pipe. [L]
        thickness (output): The wall thickness of the Pipe. [L]
        """
        _r = self._raw.GetPipe(Name, ShapeName, "", "", Color, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetPipe falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPlate(self, Name: str, ShapeName: str, Color: int):
        """This function retrieves property data for an Plate shape in a section designer section. The
        function returns zero if the property data is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing Plate shape in the specified frame
            section property.
        MatProp (output): The name of the material property for the shape.
        Color (input): The fill color assigned to the shape.
        XCenter (output): The X-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        YCenter (output): The Y-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        thickness (output): The thickness of the plate. [L]
        w (output): The width of the Plate. [L]
        Rotation (output): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        """
        _r = self._raw.GetPlate(Name, ShapeName, "", Color, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetPlate falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPolygon(self, Name: str, ShapeName: str, SSOverwrite: str, Color: int, Reinf: bool):
        """This function retrieves property data for a polygon shape in a section designer section. The
        function returns zero if the property data is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing polygon shape in the specified frame
            section property.
        MatProp (output): The name of the material property for the shape.
        SSOverwrite (input): This is a blank string, Default, or the name of a defined
            stress-strain curve. If this item is a blank string or Default, the shape
            stress-strain curve is based on the assigned material property.
        NumberPoints (output): The number of point coordinates used to define the polygon.
        X (output): This is an array that contains the X-coordinates of the polygon points.
            [L]
        Y (output): This is an array that contains the Y-coordinates of the polygon points.
            [L]
        Radius (output): This is an array that contains the radius to be applied at each of
            the polygon points. [L]
        Color (input): The fill color assigned to the shape.
        Reinf (input): This item is True when there is edge and corner reinforcing steel
            associated with the shape. The MatProp item must refer to a concrete material
            for this item to be True.
        MatRebar (output): The material property for the edge and corner reinforcing steel
            associated with the shape. This item applies only when the MatProp item is a
            concrete material and the Reinf item is True.
        """
        _r = self._raw.GetPolygon(Name, ShapeName, "", SSOverwrite, 0, [], [], [], Color, Reinf, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetPolygon falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetRefCircle(self, Name: str, ShapeName: str):
        """This function retrieves property data for a reference circle shape in a section designer
        section. The function returns zero if the property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing or new shape in a section designer
            property. If this is an existing shape, that shape is modified; otherwise, a new
            shape is added. This item may be input as a blank string, in which case the
            program will assign a shape name to the shape and return that name in the
            ShapeName variable.
        XCenter (output): The X-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        YCenter (output): The Y-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        Diameter (output): The diameter of the circular shape. [L]
        """
        _r = self._raw.GetRefCircle(Name, ShapeName, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetRefCircle falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetRefLine(self, Name: str, ShapeName: str):
        """This function retrieves property data for a reference line shape in a section designer
        section. The function returns zero if the property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of a reference line shape in the section designer
            section.
        X1 (output): The section designer X coordinate of the first drawn end point of the
            line pattern reinforcing. [L]
        Y1 (output): The section designer Y coordinate of the first drawn end point of the
            line pattern reinforcing. [L]
        X2 (output): The section designer X coordinate of the second drawn end point of the
            line pattern reinforcing. [L]
        Y2 (output): The section designer Y coordinate of the second drawn end point of the
            line pattern reinforcing. [L]
        """
        _r = self._raw.GetRefLine(Name, ShapeName, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetRefLine falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetReinfCircle(self, Name: str, ShapeName: str):
        """This function retrieves property data for a circular reinforcing shape in a section designer
        section. The function returns zero if the property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of a circular reinforcing shape in the section designer
            section.
        XCenter (output): The X-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        YCenter (output): The Y-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        Diameter (output): The diameter of the circular shape. [L]
        Rotation (output): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        MatRebar (output): The material property for the reinforcing steel.
        """
        _r = self._raw.GetReinfCircle(Name, ShapeName, 0.0, 0.0, 0.0, 0, 0.0, "", "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetReinfCircle falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetReinfCorner(self, Name: str, ShapeName: str):
        """This function retrieves corner point reinforcing data for solid rectangle, circle and
        polygon shapes in a section designer property. The function returns zero if the
        property data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing solid rectangle shape in the specified
            frame section property.
        NumberItems (output): The number of edges in the shape.
        PointNum (output): This is an array that includes the corner point number in the
            shape.
        RebarSize (output): This is an array that includes None or the name of a defined
            rebar, indicating the rebar assignment to the considered corner point.
        """
        _r = self._raw.GetReinfCorner(Name, ShapeName, 0, [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetReinfCorner falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetReinfEdge(self, Name: str, ShapeName: str):
        """This function retrieves edge reinforcing data for solid rectangle, circle, polygon, and
        rectangular reinforcing shapes in a section designer property. The function returns
        zero if the property data is successfully retrieved; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing solid rectangle shape in the specified
            frame section property.
        NumberItems (output): The number of edges in the shape.
        EdgeNum (output): This is an array that includes the edge number in the shape.
        RebarSize (output): This is an array that includes None or the name of a defined
            rebar, indicating the rebar assignment to the considered edge.
        Spacing (output): This is an array that includes the rebar maximum center-to-center
            along the considered edge. [L]
        Cover (output): This is an array that includes the rebar clear cover along the
            considered edge. [L]
        """
        _r = self._raw.GetReinfEdge(Name, ShapeName, 0, [], [], [], [])
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetReinfEdge falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetReinfLine(self, Name: str, ShapeName: str, EndBars: bool):
        """This function retrieves property data for a line reinforcing shape in a section designer
        section. The function returns zero if the property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of a line reinforcing shape in the section designer
            section.
        X1 (output): The section designer X coordinate of the first drawn end point of the
            line reinforcing. [L]
        Y1 (output): The section designer Y coordinate of the first drawn end point of the
            line reinforcing. [L]
        X2 (output): The section designer X coordinate of the second drawn end point of the
            line reinforcing. [L]
        Y2 (output): The section designer Y coordinate of the second drawn end point of the
            line reinforcing. [L]
        Spacing (output): The center-to-center spacing of the bars in the line pattern
            shape. [L]
        EndBars (input): This item is True when there are bars at the end points of the line
            reinforcing.
        MatRebar (output): The material property for the reinforcing steel.
        """
        _r = self._raw.GetReinfLine(Name, ShapeName, 0.0, 0.0, 0.0, 0.0, 0.0, "", EndBars, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetReinfLine falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetReinfRectangular(self, Name: str, ShapeName: str):
        """This function retrieves property data for a rectangular reinforcing shape in a section
        designer section. The function returns zero if the property data is successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of a rectangular reinforcing shape in the section
            designer section.
        XCenter (output): The X-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        YCenter (output): The Y-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        h (output): The section depth. [L]
        w (output): The top flange width. [L]
        Rotation (output): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        MatRebar (output): The material property for the reinforcing steel.
        """
        _r = self._raw.GetReinfRectangular(Name, ShapeName, 0.0, 0.0, 0.0, 0.0, 0.0, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetReinfRectangular falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetReinfSingle(self, Name: str, ShapeName: str):
        """This function retrieves property data for a single bar reinforcing shape in a section
        designer section. The function returns zero if the property data is successfully
        retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of a single bar reinforcing shape in the section
            designer section.
        XCenter (output): The X-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        YCenter (output): The Y-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        MatRebar (output): The material property for the reinforcing steel.
        """
        _r = self._raw.GetReinfSingle(Name, ShapeName, 0.0, 0.0, "", "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetReinfSingle falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSolidCircle(self, Name: str, ShapeName: str, SSOverwrite: str, Color: int):
        """This function retrieves property data for a solid circle shape in a section designer
        section. The function returns zero if the property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing solid circle shape in the specified frame
            section property.
        MatProp (output): The name of the material property for the shape.
        SSOverwrite (input): This is a blank string, Default, or the name of a defined
            stress-strain curve. If this item is a blank string or Default, the shape
            stress-strain curve is based on the assigned material property.
        Color (input): The fill color assigned to the shape.
        XCenter (output): The X-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        YCenter (output): The Y-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        Diameter (output): The diameter of the circle.[L]
        Rotation (output): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        MatRebar (output): The material property for the edge and corner reinforcing steel
            associated with the shape. This item applies only when the MatProp item is a
            concrete material and the Reinf item is True.
        """
        _r = self._raw.GetSolidCircle(Name, ShapeName, "", SSOverwrite, Color, 0.0, 0.0, 0.0, 0.0, 0.0, "", "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetSolidCircle falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSolidRect(self, Name: str, ShapeName: str, SSOverwrite: str, Color: int, Reinf: bool):
        """This function retrieves property data for a solid rectangular shape in a section designer
        section. The function returns zero if the property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing solid rectangle shape in the specified
            frame section property.
        MatProp (output): The name of the material property for the shape.
        SSOverwrite (input): This is a blank string, Default, or the name of a defined
            stress-strain curve. If this item is a blank string or Default, the shape
            stress-strain curve is based on the assigned material property.
        Color (input): The fill color assigned to the shape.
        XCenter (output): The X-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        YCenter (output): The Y-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        h (output): The section depth. [L]
        w (output): The section width. [L]
        Rotation (output): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        Reinf (input): This item is True when there is edge and corner reinforcing steel
            associated with the shape. The MatProp item must refer to a concrete material
            for this item to be True.
        MatRebar (output): The material property for the edge and corner reinforcing steel
            associated with the shape. This item applies only when the MatProp item is a
            concrete material and the Reinf item is True.
        """
        _r = self._raw.GetSolidRect(Name, ShapeName, "", SSOverwrite, Color, 0.0, 0.0, 0.0, 0.0, 0.0, Reinf, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetSolidRect falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSolidSector(self, Name: str, ShapeName: str, Color: int):
        """This function retrieves property data for a solid sector shape in a section designer
        section. The function returns zero if the property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing solid sector shape in the specified frame
            section property.
        MatProp (output): The name of the material property for the shape.
        Color (input): The fill color assigned to the shape.
        XCenter (output): The X-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        YCenter (output): The Y-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        Angle (output): The angle between the two radii that define the circular sector.
            [deg]
        Rotation (output): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        Radius (output): The radius of the circle defining the Sector. [L]
        """
        _r = self._raw.GetSolidSector(Name, ShapeName, "", Color, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetSolidSector falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSolidSegment(self, Name: str, ShapeName: str, Color: int):
        """This function retrieves property data for a solid segment shape in a section designer
        section. The function returns zero if the property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing solid segment shape in the specified
            frame section property.
        MatProp (output): The name of the material property for the shape.
        Color (input): The fill color assigned to the shape.
        XCenter (output): The X-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        YCenter (output): The Y-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        Angle (output): The angle between lines drawn from the center of the circle to the
            end points of the chord tat defines the segment. [deg]
        Rotation (output): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        Radius (output): The radius of the circle defining the segment.
        """
        _r = self._raw.GetSolidSegment(Name, ShapeName, "", Color, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetSolidSegment falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTee(self, Name: str, ShapeName: str, Color: int):
        """This function retrieves property data for a Tee shape in a section designer section. The
        function returns zero if the property data is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing Tee shape in the specified frame section
            property.
        MatProp (output): The name of the material property for the shape.
        PropName (output): This is a blank string or the name of a defined Tee property that
            has been imported from a section property file. If it is the name of a defined
            Tee property, the section dimensions are taken from that property.
        Color (input): The fill color assigned to the shape.
        XCenter (output): The X-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        YCenter (output): The Y-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        h (output): The section depth. [L]
        bf (output): The section width. [L]
        tf (output): The flange thickness. [L]
        tw (output): The web thickness. [L]
        Rotation (output): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        """
        _r = self._raw.GetTee(Name, ShapeName, "", "", Color, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetTee falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTube(self, Name: str, ShapeName: str, Color: int):
        """This function retrieves property data for a Tube shape in a section designer section. The
        function returns zero if the property data is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing Tube shape in the specified frame section
            property.
        MatProp (output): The name of the material property for the shape.
        PropName (output): This is a blank string or the name of a defined Tube property
            that has been imported from a section property file. If it is the name of a
            defined Tube property, the section dimensions are taken from that property.
        Color (input): The fill color assigned to the shape.
        XCenter (output): The X-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        YCenter (output): The Y-coordinate of the center of the shape in the section
            designer coordinate system. [L]
        h (output): The section height. [L]
        w (output): The section width. [L]
        tf (output): The flange thickness. [L]
        tw (output): The web thickness. [L]
        Rotation (output): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        """
        _r = self._raw.GetTube(Name, ShapeName, "", "", Color, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.GetTube falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetAngle(self, Name: str, ShapeName: str, MatProp: str, PropName: str, XCenter: float, YCenter: float, Rotation: float, Color: int = -1, h: float = 24, bf: float = 24, tf: float = 2.4, tw: float = 2.4):
        """This function adds a new Angle shape or modifies an existing shape to be an Angle shape in a
        section designer property. The function returns zero if the shape is successfully
        added or modified; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing or new shape in a section designer
            property. If this is an existing shape, that shape is modified; otherwise, a new
            shape is added. This item may be input as a blank string, in which case the
            program will assign a shape name to the shape and return that name in the
            ShapeName variable.
        MatProp (input): The name of the material property for the shape.
        PropName (input): This is a blank string or the name of a defined Angle property
            that has been imported from a section property file. If this item is a blank
            string, the section dimensions are taken from the values input in this function.
            If this item is the name of a defined Angle property that has been imported from
            a section property file, the section dimensions are taken from the specified
            Angle property. If this item is not blank, and the specified property name is
            not an Angle that was imported from a section property file, an error is
            returned.
        XCenter (input): The X-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        YCenter (input): The Y-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        Rotation (input): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        Color (input): The fill color assigned to the shape. If Color is specified as -1,
            the program will automatically assign the default fill color.
        h (input): The section depth. [L]
        bf (input): The flange width. [L]
        tf (input): The flange thickness. [L]
        tw (input): The web thickness. [L]
        """
        _r = self._raw.SetAngle(Name, ShapeName, MatProp, PropName, XCenter, YCenter, Rotation, Color, h, bf, tf, tw)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetAngle falhou (ret={_r})".format(_r=_r))
        return None

    def SetChannel(self, Name: str, ShapeName: str, MatProp: str, PropName: str, XCenter: float, YCenter: float, Rotation: float, Color: int = -1, h: float = 24, bf: float = 24, tf: float = 2.4, tw: float = 2.4):
        """This function adds a new Channel shape or modifies an existing shape to be a Channel shape
        in a section designer property. The function returns zero if the shape is
        successfully added or modified; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing or new shape in a section designer
            property. If this is an existing shape, that shape is modified; otherwise, a new
            shape is added. This item may be input as a blank string, in which case the
            program will assign a shape name to the shape and return that name in the
            ShapeName variable.
        MatProp (input): The name of the material property for the shape.
        PropName (input): This is a blank string or the name of a defined Channel property
            that has been imported from a section property file. If this item is a blank
            string, the section dimensions are taken from the values input in this function.
            If this item is the name of a defined Channel property that has been imported
            from a section property file, the section dimensions are taken from the
            specified Channel property. If this item is not blank, and the specified
            property name is not an Channel that was imported from a section property file,
            an error is returned.
        XCenter (input): The X-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        YCenter (input): The Y-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        Rotation (input): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        Color (input): The fill color assigned to the shape. If Color is specified as -1,
            the program will automatically assign the default fill color.
        h (input): The section depth. [L]
        bf (input): The flange width. [L]
        tf (input): The flange thickness. [L]
        tw (input): The web thickness. [L]
        """
        _r = self._raw.SetChannel(Name, ShapeName, MatProp, PropName, XCenter, YCenter, Rotation, Color, h, bf, tf, tw)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetChannel falhou (ret={_r})".format(_r=_r))
        return None

    def SetDblAngle(self, Name: str, ShapeName: str, MatProp: str, PropName: str, XCenter: float, YCenter: float, Rotation: float, Color: int = -1, h: float = 24, w: float = 24, tf: float = 2.4, tw: float = 2.4, dis: float = 1.2):
        """This function adds a new Double Angle shape or modifies an existing shape to be an Double
        Angle shape in a section designer property. The function returns zero if the shape
        is successfully added or modified; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing or new shape in a section designer
            property. If this is an existing shape, that shape is modified; otherwise, a new
            shape is added. This item may be input as a blank string, in which case the
            program will assign a shape name to the shape and return that name in the
            ShapeName variable.
        MatProp (input): The name of the material property for the shape.
        PropName (input): This is a blank string or the name of a defined DblAngle property
            that has been imported from a section property file. If this item is a blank
            string, the section dimensions are taken from the values input in this function.
            If this item is the name of a defined DblAngle property that has been imported
            from a section property file, the section dimensions are taken from the
            specified DblAngle property. If this item is not blank and the specified
            property name is not an DblAngle that was imported from a section property file,
            an error is returned.
        XCenter (input): The X-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        YCenter (input): The Y-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        Rotation (input): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        Color (input): The fill color assigned to the shape. If Color is specified as -1,
            the program will automatically assign the default fill color.
        h (input): The section depth. [L]
        w (input): The flange width. [L]
        tf (input): The flange thickness. [L]
        tw (input): The web thickness. [L]
        dis (input): Separation between the two flanges that are parallel. [L]
        """
        _r = self._raw.SetDblAngle(Name, ShapeName, MatProp, PropName, XCenter, YCenter, Rotation, Color, h, w, tf, tw, dis)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetDblAngle falhou (ret={_r})".format(_r=_r))
        return None

    def SetISection(self, Name: str, ShapeName: str, MatProp: str, PropName: str, XCenter: float, YCenter: float, Rotation: float, Color: int = -1, h: float = 24, bf: float = 24, tf: float = 2.4, tw: float = 2.4, bfb: float = 24, tfb: float = 2.4):
        """This function adds a new I-section shape or modifies an existing shape to be an I-section
        shape in a section designer property. The function returns zero if the shape is
        successfully added or modified; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing or new shape in a section designer
            property. If this is an existing shape, that shape is modified; otherwise, a new
            shape is added. This item may be input as a blank string, in which case the
            program will assign a shape name to the shape and return that name in the
            ShapeName variable.
        MatProp (input): The name of the material property for the shape.
        PropName (input): This is a blank string or the name of a defined I-section property
            that has been imported from a section property file. If this item is a blank
            string, the section dimensions are taken from the values input in this function.
            If this item is the name of a defined I-section property that has been imported
            from a section property file, the section dimensions are taken from the
            specified I-section property. If this item is not blank, and the specified
            property name is not an I-section that was imported from a section property
            file, an error is returned.
        XCenter (input): The X-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        YCenter (input): The Y-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        Rotation (input): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        Color (input): The fill color assigned to the shape. If Color is specified as -1,
            the program will automatically assign the default fill color.
        h (input): The section depth. [L]
        bf (input): The top flange width. [L]
        tf (input): The top flange thickness. [L]
        tw (input): The web thickness. [L]
        bfb (input): The bottom flange width. [L]
        tfb (input): The bottom flange thickness. [L]
        """
        _r = self._raw.SetISection(Name, ShapeName, MatProp, PropName, XCenter, YCenter, Rotation, Color, h, bf, tf, tw, bfb, tfb)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetISection falhou (ret={_r})".format(_r=_r))
        return None

    def SetPipe(self, Name: str, ShapeName: str, MatProp: str, PropName: str, XCenter: float, YCenter: float, Color: int = -1, diameter: float = 24, thickness: float = 2.4):
        """This function adds a new Pipe shape or modifies an existing shape to be a Pipe shape in a
        section designer property. The function returns zero if the shape is successfully
        added or modified; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing or new shape in a section designer
            property. If this is an existing shape, that shape is modified; otherwise, a new
            shape is added. This item may be input as a blank string, in which case the
            program will assign a shape name to the shape and return that name in the
            ShapeName variable.
        MatProp (input): The name of the material property for the shape.
        PropName (input): This is a blank string or the name of a defined Pipe property that
            has been imported from a section property file. If this item is a blank string,
            the section dimensions are taken from the values input in this function. If this
            item is the name of a defined Pipe property that has been imported from a
            section property file, the section dimensions are taken from the specified Pipe
            property. If this item is not blank and the specified property name is not a
            Pipe that was imported from a section property file, an error is returned.
        XCenter (input): The X-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        YCenter (input): The Y-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        Color (input): The fill color assigned to the shape. If Color is specified as -1,
            the program will automatically assign the default fill color.
        diameter (input): The outer diameter of the Pipe. [L]
        thickness (input): The wall thickness of the Pipe. [L]
        """
        _r = self._raw.SetPipe(Name, ShapeName, MatProp, PropName, XCenter, YCenter, Color, diameter, thickness)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetPipe falhou (ret={_r})".format(_r=_r))
        return None

    def SetPlate(self, Name: str, ShapeName: str, MatProp: str, XCenter: float, YCenter: float, Rotation: float, Color: int = -1, thickness: float = 2.4, w: float = 24):
        """This function adds a new Plate shape or modifies an existing shape to be a Plate shape in a
        section designer property. The function returns zero if the shape is successfully
        added or modified; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing or new shape in a section designer
            property. If this is an existing shape,n that shape is modified; otherwise, a
            new shape is added. This item may be input as a blank string, in which case the
            program will assign a shape name to the shape and return that name in the
            ShapeName variable.
        MatProp (input): The name of the material property for the shape.
        XCenter (input): The X-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        YCenter (input): The Y-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        Rotation (input): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        Color (input): The fill color assigned to the shape. If Color is specified as -1,
            the program will automatically assign the default fill color.
        thickness (input): The thickness of the plate. [L]
        w (input): The width of the Plate. [L]
        """
        _r = self._raw.SetPlate(Name, ShapeName, MatProp, XCenter, YCenter, Rotation, Color, thickness, w)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetPlate falhou (ret={_r})".format(_r=_r))
        return None

    def SetPolygon(self, Name: str, ShapeName: str, MatProp: str, SSOverwrite: str, NumberPoints: int, X: list[float], Y: list[float], Radius: list[float], Color: int = -1, Reinf: bool = False, MatRebar: str = ''):
        """This function adds a new polygon shape or modifies an existing shape to be a polygon shape
        in a section designer property. The polygon points must be defined in order around
        the polygon, otherwise the shape will be created incorrectly or the creation of the
        shape will fail. The function returns zero if the shape is successfully added or
        modified; otherwise it returns a nonzero val .
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing or new shape in a section designer
            property. If this is an existing shape, that shape is modified; otherwise, a new
            shape is added. This item may be input as a blank string, in which case the
            program will assign a shape name to the shape and return that name in the
            ShapeName variable.
        MatProp (input): The name of the material property for the shape.
        SSOverwrite (input): This is a blank string, Default, or the name of a defined
            stress-strain curve. If this item is a blank string or Default, the shape
            stress-strain curve is based on the assigned material property.
        NumberPoints (input): The number of point coordinates used to define the polygon.
        X (input): This is an array that contains the X-coordinates of the polygon points.
            [L]
        Y (input): This is an array that contains the Y-coordinates of the polygon points.
            [L]
        Radius (input): This is an array that contains the radius to be applied at each of
            the polygon points. [L]
        Color (input): The fill color assigned to the shape. If Color is specified as -1,
            the program will automatically assign the default fill color.
        Reinf (input): This item is True when there is edge and corner reinforcing steel
            associated with the shape. If the MatProp item is not a concrete material, this
            item is always assumed to be False.
        MatRebar (input): The material property for the edge and corner reinforcing steel
            associated with the shape. This item applies only when the MatProp item is a
            concrete material and the Reinf item is True.
        """
        _r = self._raw.SetPolygon(Name, ShapeName, MatProp, SSOverwrite, NumberPoints, X, Y, Radius, Color, Reinf, MatRebar)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetPolygon falhou (ret={_r})".format(_r=_r))
        return None

    def SetRefCircle(self, Name: str, ShapeName: str, XCenter: float, YCenter: float, Diameter: float):
        """This function adds a new reference circle shape or modifies an existing shape to be a
        reference circle shape in a section designer property. The function returns zero if
        the shape is successfully added or modified; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing or new shape in a section designer
            property. If this is an existing shape, that shape is modified; otherwise, a new
            shape is added. This item may be input as a blank string, in which case the
            program will assign a shape name to the shape and return that name in the
            ShapeName variable.
        XCenter (input): The X-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        YCenter (input): The Y-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        Diameter (input): The diameter of the circular shape. [L]
        """
        _r = self._raw.SetRefCircle(Name, ShapeName, XCenter, YCenter, Diameter)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetRefCircle falhou (ret={_r})".format(_r=_r))
        return None

    def SetRefLine(self, Name: str, ShapeName: str, X1: float, Y1: float, X2: float, Y2: float):
        """This function adds a new reference line shape or modifies an existing shape to be a
        reference line shape in a section designer property. The function returns zero if
        the shape is successfully added or modified; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing or new shape in a section designer
            property. If this is an existing shape, that shape is modified; otherwise, a new
            shape is added. This item may be input as a blank string, in which case the
            program will assign a shape name to the shape and return that name in the
            ShapeName variable.
        X1 (input): The section designer X coordinate of the first drawn end point of the
            line pattern reinforcing. [L]
        Y1 (input): The section designer Y coordinate of the first drawn end point of the
            line pattern reinforcing. [L]
        X2 (input): The section designer X coordinate of the second drawn end point of the
            line pattern reinforcing. [L]
        Y2 (input): The section designer Y coordinate of the second drawn end point of the
            line pattern reinforcing. [L]
        """
        _r = self._raw.SetRefLine(Name, ShapeName, X1, Y1, X2, Y2)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetRefLine falhou (ret={_r})".format(_r=_r))
        return None

    def SetReinfCircle(self, Name: str, ShapeName: str, XCenter: float, YCenter: float, Diameter: float, Numberbars: int, Rotation: float, RebarSize: float, MatRebar: str = ''):
        """This function adds a new circular reinforcing shape or modifies an existing shape to be an
        circular reinforcing shape in a section designer property. The function returns zero
        if the shape is successfully added or modified; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing or new shape in a section designer
            property. If this is an existing shape, that shape is modified; otherwise, a new
            shape is added. This item may be input as a blank string, in which case the
            program will assign a shape name to the shape and return that name in the
            ShapeName variable.
        XCenter (input): The X-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        YCenter (input): The Y-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        Diameter (input): The diameter of the circular shape. [L]
        Rotation (input): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        MatRebar (input): The material property for the reinforcing steel.
        """
        _r = self._raw.SetReinfCircle(Name, ShapeName, XCenter, YCenter, Diameter, Numberbars, Rotation, RebarSize, MatRebar)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetReinfCircle falhou (ret={_r})".format(_r=_r))
        return None

    def SetReinfCorner(self, Name: str, ShapeName: str, PointNum: int, RebarSize: str, All: bool = False):
        """This function specifies corner reinforcing in solid rectangle, circle and polygon shapes in
        a section designer property. The function returns zero if the reinforcing is
        successfully specified; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing solid rectangle, circle or polygon shape
            in the specified section.
        PointNum (input): An corner point number in the shape. This item is ignored if the
            All item is True.
        RebarSize (input): This is None or the name of a defined rebar, indicating the rebar
            assignment to the specified corner.
        All (input): If this item is True, the specified rebar data applies to all corners
            in the shape.
        """
        _r = self._raw.SetReinfCorner(Name, ShapeName, PointNum, RebarSize, All)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetReinfCorner falhou (ret={_r})".format(_r=_r))
        return None

    def SetReinfEdge(self, Name: str, ShapeName: str, EdgeNum: int, RebarSize: str, Spacing: float, Cover: float, All: bool = False):
        """This function specifies edge reinforcing in solid rectangle, circle, polygon and rectangular
        reinforcing shapes in a section designer property. The function returns zero if the
        reinforcing is successfully specified; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing solid rectangle, circle or polygon shape
            in the specified section.
        EdgeNum (input): An edge number in the shape. This item is ignored if the All item
            is True.
        RebarSize (input): This is None or the name of a defined rebar, indicating the rebar
            assignment to the specified edge.
        Spacing (input): This is the rebar maximum center-to-center along the specified
            edge. [L]
        Cover (input): This is the rebar clear cover along the specified edge. [L]
        All (input): If this item is True, the specified rebar data applies to all edges in
            the shape.
        """
        _r = self._raw.SetReinfEdge(Name, ShapeName, EdgeNum, RebarSize, Spacing, Cover, All)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetReinfEdge falhou (ret={_r})".format(_r=_r))
        return None

    def SetReinfLine(self, Name: str, ShapeName: str, X1: float, Y1: float, X2: float, Y2: float, Spacing: float = 6, RebarSize: str = '', EndBars: bool = False, MatRebar: str = None):
        """This function adds a new line reinforcing shape or modifies an existing shape to be a line
        reinforcing shape in a section designer property. The function returns zero if the
        shape is successfully added or modified; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing or new shape in a section designer
            property. If this is an existing shape, that shape is modified; otherwise, a new
            shape is added. This item may be input as a blank string, in which case the
            program will assign a shape name to the shape and return that name in the
            ShapeName variable.
        X1 (input): The section designer X coordinate of the first drawn end point of the
            line reinforcing. [L]
        Y1 (input): The section designer Y coordinate of the first drawn end point of the
            line reinforcing. [L]
        X2 (input): The section designer X coordinate of the second drawn end point of the
            line reinforcing. [L]
        Y2 (input): The section designer Y coordinate of the second drawn end point of the
            line reinforcing. [L]
        Spacing (input): The center-to-center spacing of the bars in the line pattern shape.
            [L]
        EndBars (input): This item is True when there are bars at the end points of the line
            reinforcing.
        MatRebar (input): The material property for the reinforcing steel.
        """
        if MatRebar is None:
            raise TypeError("SapModel.PropFrame.SDShape.SetReinfLine: MatRebar é obrigatório (a doc original o lista após um parâmetro opcional, algo que o VB6 permite e o Python não - por isso tem um default aparente, mas precisa ser informado).")
        _r = self._raw.SetReinfLine(Name, ShapeName, X1, Y1, X2, Y2, Spacing, RebarSize, EndBars, MatRebar)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetReinfLine falhou (ret={_r})".format(_r=_r))
        return None

    def SetReinfRectangular(self, Name: str, ShapeName: str, XCenter: float, YCenter: float, Rotation: float, h: float, w: float, MatRebar: str = ''):
        """This function adds a new rectangular reinforcing shape or modifies an existing shape to be a
        rectangular reinforcing shape in a section designer property. The function returns
        zero if the shape is successfully added or modified; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing or new shape in a section designer
            property. If this is an existing shape, that shape is modified; otherwise, a new
            shape is added. This item may be input as a blank string, in which case the
            program will assign a shape name to the shape and return that name in the
            ShapeName variable.
        XCenter (input): The X-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        YCenter (input): The Y-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        Rotation (input): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        h (input): The section depth. [L]
        w (input): The top flange width. [L]
        MatRebar (input): The material property for the reinforcing steel.
        """
        _r = self._raw.SetReinfRectangular(Name, ShapeName, XCenter, YCenter, Rotation, h, w, MatRebar)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetReinfRectangular falhou (ret={_r})".format(_r=_r))
        return None

    def SetReinfSingle(self, Name: str, ShapeName: str, XCenter: float, YCenter: float, RebarSize: str = '', MatRebar: str = ''):
        """This function adds a new single bar reinforcing shape or modifies an existing shape to be a
        single bar reinforcing shape in a section designer property. The function returns
        zero if the shape is successfully added or modified; otherwise it returns a nonzero
        value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing or new shape in a section designer
            property. If this is an existing shape, that shape is modified; otherwise, a new
            shape is added. This item may be input as a blank string, in which case the
            program will assign a shape name to the shape and return that name in the
            ShapeName variable.
        XCenter (input): The X-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        YCenter (input): The Y-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        MatRebar (input): The material property for the reinforcing steel.
        """
        _r = self._raw.SetReinfSingle(Name, ShapeName, XCenter, YCenter, RebarSize, MatRebar)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetReinfSingle falhou (ret={_r})".format(_r=_r))
        return None

    def SetSolidCircle(self, Name: str, MatProp: str, SSOverwrite: str, XCenter: float, YCenter: float, diameter: float = 24, color: int = -1, Reinf: bool = False, NumberBars: int = 8, Rotation: float = None, Cover: float = 2, RebarSize: str = '', MatRebar: str = ''):
        """This function adds a new solid circle shape or modifies an existing shape to be a solid
        circle shape in a section designer property. The function returns zero if the shape
        is successfully added or modified; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        MatProp (input): The name of the material property for the shape.
        SSOverwrite (input): This is a blank string, Default, or the name of a defined
            stress-strain curve. If this item is a blank string or Default, the shape
            stress-strain curve is based on the assigned material property.
        XCenter (input): The X-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        YCenter (input): The Y-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        Reinf (input): This item is True when there is edge and corner reinforcing steel
            associated with the shape. If the MatProp item is not a concrete material, this
            item is always assumed to be False.
        Rotation (input): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        MatRebar (input): The material property for the edge and corner reinforcing steel
            associated with the shape. This item applies only when the MatProp item is a
            concrete material and the Reinf item is True.
        """
        if Rotation is None:
            raise TypeError("SapModel.PropFrame.SDShape.SetSolidCircle: Rotation é obrigatório (a doc original o lista após um parâmetro opcional, algo que o VB6 permite e o Python não - por isso tem um default aparente, mas precisa ser informado).")
        _r = self._raw.SetSolidCircle(Name, MatProp, SSOverwrite, XCenter, YCenter, diameter, color, Reinf, NumberBars, Rotation, Cover, RebarSize, MatRebar)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetSolidCircle falhou (ret={_r})".format(_r=_r))
        return None

    def SetSolidRect(self, Name: str, ShapeName: str, MatProp: str, SSOverwrite: str, XCenter: float, YCenter: float, h: float, w: float, Rotation: float, color: int = -1, Reinf: bool = False, MatRebar: str = ''):
        """This function adds a new solid rectangle shape or modifies an existing shape to be an solid
        rectangle shape in a section designer property. The function returns zero if the
        shape is successfully added or modified; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing or new shape in a section designer
            property. If this is an existing shape, that shape is modified; otherwise, a new
            shape is added. This item may be input as a blank string, in which case the
            program will assign a shape name to the shape and return that name in the
            ShapeName variable.
        MatProp (input): The name of the material property for the shape.
        SSOverwrite (input): This is a blank string, Default, or the name of a defined
            stress-strain curve. If this item is a blank string or Default, the shape
            stress-strain curve is based on the assigned material property.
        XCenter (input): The X-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        YCenter (input): The Y-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        h (input): The section depth. [L]
        w (input): The section width. [L]
        Rotation (input): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        Reinf (input): This item is True when there is edge and corner reinforcing steel
            associated with the shape. If the MatProp item is not a concrete material, this
            item is always assumed to be False.
        MatRebar (input): The material property for the edge and corner reinforcing steel
            associated with the shape. This item applies only when the MatProp item is a
            concrete material and the Reinf item is True.
        """
        _r = self._raw.SetSolidRect(Name, ShapeName, MatProp, SSOverwrite, XCenter, YCenter, h, w, Rotation, color, Reinf, MatRebar)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetSolidRect falhou (ret={_r})".format(_r=_r))
        return None

    def SetSolidSector(self, Name: str, ShapeName: str, MatProp: str, XCenter: float, YCenter: float, Angle: float, Rotation: float, Radius: float, Color: int = -1):
        """This function adds a new solid sector shape or modifies an existing shape to be a solid
        sector shape in a section designer property. The function returns zero if the shape
        is successfully added or modified; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing or new shape in a section designer
            property. If this is an existing shape, that shape is modified; otherwise, a new
            shape is added. This item may be input as a blank string, in which case the
            program will assign a shape name to the shape and return that name in the
            ShapeName variable.
        MatProp (input): The name of the material property for the shape.
        XCenter (input): The X-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        YCenter (input): The Y-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        Angle (input): The angle between the two radii that define the circular sector.
            [deg]
        Rotation (input): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        Radius (input): The radius of the circle defining the Sector. [L]
        Color (input): The fill color assigned to the shape. If Color is specified as -1,
            the program will automatically assign the default fill color.
        """
        _r = self._raw.SetSolidSector(Name, ShapeName, MatProp, XCenter, YCenter, Angle, Rotation, Radius, Color)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetSolidSector falhou (ret={_r})".format(_r=_r))
        return None

    def SetSolidSegment(self, Name: str, ShapeName: str, MatProp: str, XCenter: float, YCenter: float, Angle: float, Rotation: float, Radius: float, Color: int = -1):
        """This function adds a new solid segment shape or modifies an existing shape to be a solid
        segment shape in a section designer property. The function returns zero if the shape
        is successfully added or modified; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing or new shape in a section designer
            property. If this is an existing shape, that shape is modified; otherwise, a new
            shape is added. This item may be input as a blank string, in which case the
            program will assign a shape name to the shape and return that name in the
            ShapeName variable.
        MatProp (input): The name of the material property for the shape.
        XCenter (input): The X-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        YCenter (input): The Y-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        Angle (input): The angle between lines drawn from the center of the circle to the
            end points of the chord tat defines the segment. [deg]
        Rotation (input): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        Radius (input): The radius of the circle defining the segment.
        Color (input): The fill color assigned to the shape. If Color is specified as -1,
            the program will automatically assign the default fill color.
        """
        _r = self._raw.SetSolidSegment(Name, ShapeName, MatProp, XCenter, YCenter, Angle, Rotation, Radius, Color)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetSolidSegment falhou (ret={_r})".format(_r=_r))
        return None

    def SetTee(self, Name: str, ShapeName: str, MatProp: str, PropName: str, XCenter: float, YCenter: float, Rotation: float, Color: int = -1, h: float = 24, bf: float = 24, tf: float = 2.4, tw: float = 2.4):
        """This function adds a new Tee shape or modifies an existing shape to be a Tee shape in a
        section designer property. The function returns zero if the shape is successfully
        added or modified; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing or new shape in a section designer
            property. If this is an existing shape, that shape is modified; otherwise, a new
            shape is added. This item may be input as a blank string, in which case the
            program will assign a shape name to the shape and return that name in the
            ShapeName variable.
        MatProp (input): The name of the material property for the shape.
        PropName (input): This is a blank string or the name of a defined Tee property that
            has been imported from a section property file. If this item is a blank string,
            the section dimensions are taken from the values input in this function. If this
            item is the name of a defined Tee property that has been imported from a section
            property file, the section dimensions are taken from the specified Tee property.
            If this item is not blank, and the specified property name is not a Tee that was
            imported from a section property file, an error is returned.
        XCenter (input): The X-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        YCenter (input): The Y-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        Rotation (input): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        Color (input): The fill color assigned to the shape. If Color is specified as -1,
            the program will automatically assign the default fill color.
        h (input): The section depth. [L]
        bf (input): The section width. [L]
        tf (input): The flange thickness. [L]
        tw (input): The web thickness. [L]
        """
        _r = self._raw.SetTee(Name, ShapeName, MatProp, PropName, XCenter, YCenter, Rotation, Color, h, bf, tf, tw)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetTee falhou (ret={_r})".format(_r=_r))
        return None

    def SetTube(self, Name: str, ShapeName: str, MatProp: str, PropName: str, XCenter: float, YCenter: float, Rotation: float, Color: int = -1, h: float = 24, w: float = 24, tf: float = 2.4, tw: float = 2.4):
        """This function adds a new Tube shape or modifies an existing shape to be a Tube shape in a
        section designer property. The function returns zero if the shape is successfully
        added or modified; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing frame section property that is a section
            designer section.
        ShapeName (input): The name of an existing or new shape in a section designer
            property. If this is an existing shape, that shape is modified; otherwise, a new
            shape is added. This item may be input as a blank string, in which case the
            program will assign a shape name to the shape and return that name in the
            ShapeName variable.
        MatProp (input): The name of the material property for the shape.
        PropName (input): This is a blank string or the name of a defined Tube property that
            has been imported from a section property file. If this item is a blank string,
            the section dimensions are taken from the values input in this function. If this
            item is the name of a defined Tube property that has been imported from a
            section property file, the section dimensions are taken from the specified Tube
            property. If this item is not blank and the specified property name is not an
            Tube that was imported from a section property file, an error is returned.
        XCenter (input): The X-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        YCenter (input): The Y-coordinate of the center of the shape in the section designer
            coordinate system. [L]
        Rotation (input): The counter clockwise rotation of the shape from its default
            orientation. [deg]
        Color (input): The fill color assigned to the shape. If Color is specified as -1,
            the program will automatically assign the default fill color.
        h (input): The section height. [L]
        w (input): The section width. [L]
        tf (input): The flange thickness. [L]
        tw (input): The web thickness. [L]
        """
        _r = self._raw.SetTube(Name, ShapeName, MatProp, PropName, XCenter, YCenter, Rotation, Color, h, w, tf, tw)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropFrame.SDShape.SetTube falhou (ret={_r})".format(_r=_r))
        return None


