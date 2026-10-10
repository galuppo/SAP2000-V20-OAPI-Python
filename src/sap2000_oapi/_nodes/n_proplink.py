"""Módulo gerado automaticamente a partir da documentação da OAPI
do SAP2000 v20 (CSI_OAPI_Documentation.chm). Não editar à mão -
reexecute tools/generate.py se precisar regenerar.
"""

from __future__ import annotations

from functools import cached_property

from ..errors import Sap2000ApiError


class N_PropLink:
    """Wrapper para SapModel.PropLink."""

    def __init__(self, raw):
        self._raw = raw

    def ChangeName(self, Name: str, NewName: str):
        """This function changes the name of an existing link property. The function returns zero if
        the new name is successfully applied; otherwise it returns a nonzero value.
    
        Name (input): The existing name of a defined link property.
        NewName (input): The new name for the link property.
        """
        _r = self._raw.ChangeName(Name, NewName)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.ChangeName falhou (ret={_r})".format(_r=_r))
        return None

    def Count(self, PropType: int = None):
        """This function returns the total number of defined link properties in the model. If desired,
        counts can be returned for all link properties of a specified type in the model.
    
        PropType (input): This optional value is one of the following items in the
            eLinkPropType enumeration. NLPROP_LINEAR = 1 NLPROP_DAMPER = 2 NLPROP_GAP = 3
            NLPROP_HOOK = 4 NLPROP_PLASTIC_WEN = 5 NLPROP_ISOLATOR1 = 6 (Rubber isolator)
            NLPROP_ISOLATOR2 = 7 (Friction isolator) NLPROP_MULTILINEAR_ELASTIC = 8
            NLPROP_MULTILINEAR_PLASTIC = 9 NLPROP_ISOLATOR3 = 10 (T/C Friction isolator) If
            no value is input for PropType, a count is returned for all link properties in
            the model regardless of type.
        """
        _r = self._raw.Count(PropType)
        return _r

    def Delete(self, Name: str):
        """The function deletes a specified link property. The function returns zero if the link
        property is successfully deleted; otherwise it returns a nonzero value. It returns
        an error if the specified link property can not be deleted, for example, if it is
        being used by an existing link object.
    
        Name (input): The name of an existing link property.
        """
        _r = self._raw.Delete(Name)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.Delete falhou (ret={_r})".format(_r=_r))
        return None

    def GetDamper(self, Name: str):
        """This function retrieves link property data for an exponential damper-type link property. The
        function returns zero if the property data is successfully retrieved; otherwise it
        returns a nonzero value.
        """
        _r = self._raw.GetDamper(Name, [], [], [], [], [], [], [], [], 0.0, 0.0, "", "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetDamper falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDamperBilinear(self, Name: str, dj2: float, dj3: float, Notes: str = '', GUID: str = ''):
        """This function retrieves link property data for a bilinear damper-type link property. The
        function returns zero if the property data is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing bilinear damper-type link property.
        DOF (output): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (output): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained.) Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (output): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1 has nonlinear properties
            NonLinear(4) = R2 has nonlinear properties NonLinear(5) = R3 has nonlinear
            properties The term NonLinear(n) applies only when DOF(n) = True and Fixed(n) =
            False.
        Ke (output): This is an array of effective stiffness terms for the link property.
            The effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (output): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        k (output): This is an array of initial stiffness terms for the link property. The
            initial stiffness applies for nonlinear analyses. k(0) = U1 [F/L] k(1) = U2
            [F/L] k(2) = U3 [F/L] k(3) = R1 [FL] k(4) = R2 [FL] k(5) = R3 [FL] The term k(n)
            only applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        c (output): This is an array of nonlinear initial damping coefficient terms for the
            link property. The nonlinear initial damping coefficient applies for nonlinear
            analyses. c(0) = U1 [F/L] c(1) = U2 [F/L] c(2) = U3 [F/L] c(3) = R1 [FL] c(4) =
            R2 [FL] c(5) = R3 [FL] The term c(n) applies only when DOF(n) = True, Fixed(n) =
            False and NonLinear(n) = True.
        cy (output): This is an array of nonlinear yielded damping coefficient terms for the
            link property. The nonlinear yielded damping coefficient applies for nonlinear
            analyses. cy(0) = U1 [F/L] cy(1) = U2 [F/L] cy(2) = U3 [F/L] cy(3) = R1 [FL]
            cy(4) = R2 [FL] cy(5) = R3 [FL] The term cy(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        ForceLimit (output): This is an array of nonlinear linear force limit terms for the
            link property. The linear force limit applies for nonlinear analyses.
            ForceLimit(0) = U1 [F] ForceLimit(1) = U2 [F] ForceLimit(2) = U3 [F]
            ForceLimit(3) = R1 [FL] ForceLimit(4) = R2 [FL] ForceLimit(5) = R3 [FL] The term
            ForceLimit(n) applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n)
            = True.
        dj2 (input): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (input): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, the program assigns a GUID to the property.
        """
        _r = self._raw.GetDamperBilinear(Name, [], [], [], [], [], [], [], [], [], dj2, dj3, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetDamperBilinear falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDamperLinearExponential(self, Name: str, Notes: str):
        """This function retrieves link property data for a linear exponential damper-type link
        property. The function returns zero if the property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing linear exponential damper-type link property.
        DOF (output): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (output): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained.) Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (output): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1 has nonlinear properties
            NonLinear(4) = R2 has nonlinear properties NonLinear(5) = R3 has nonlinear
            properties The term NonLinear(n) applies only when DOF(n) = True and Fixed(n) =
            False.
        Ke (output): This is an array of effective stiffness terms for the link property.
            The effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (output): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        k (output): This is an array of initial stiffness terms for the link property. The
            initial stiffness applies for nonlinear analyses. k(0) = U1 [F/L] k(1) = U2
            [F/L] k(2) = U3 [F/L] k(3) = R1 [FL] k(4) = R2 [FL] k(5) = R3 [FL] The term k(n)
            only applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        c (output): This is an array of nonlinear damping coefficient terms for the link
            property. The nonlinear damping coefficient applies for nonlinear analyses. c(0)
            = U1 [F/(L^cexp)] c(1) = U2 [F/(L^cexp)] c(2) = U3 [F/(L^cexp)] c(3) = R1 [FL]
            c(4) = R2 [FL] c(5) = R3 [FL] The term c(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        cexp (output): This is an array of the nonlinear damping exponent terms. The
            nonlinear damping exponent applies for nonlinear analyses. It is applied to the
            velocity across the damper in the equation of motion. cexp(0) = U1 cexp(1) = U2
            cexp(2) = U3 cexp(3) = R1 cexp(4) = R2 cexp(5) = R3 The term cexp(n) applies
            only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        ForceLimit (output): This is an array of nonlinear linear force limit terms for the
            link property. The linear force limit applies for nonlinear analyses.
            ForceLimit(0) = U1 [F] ForceLimit(1) = U2 [F] ForceLimit(2) = U3 [F]
            ForceLimit(3) = R1 [FL] ForceLimit(4) = R2 [FL] ForceLimit(5) = R3 [FL] The term
            ForceLimit(n) applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n)
            = True.
        dj2 (output): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (output): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (output): The GUID (global unique identifier), if any, assigned to the
            property. If this item is input as Default, the program assigns a GUID to the
            property.
        """
        _r = self._raw.GetDamperLinearExponential(Name, [], [], [], [], [], [], [], [], [], 0.0, 0.0, Notes, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetDamperLinearExponential falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetDamperFrictionSpring(self, Name: str, Notes: str):
        """This function retrieves link property data for a friction spring damper-type link property.
        The function returns zero if the property data is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing friction spring damper-type link property.
        DOF (output): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (output): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained.) Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (output): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1 has nonlinear properties
            NonLinear(4) = R2 has nonlinear properties NonLinear(5) = R3 has nonlinear
            properties The term NonLinear(n) applies only when DOF(n) = True and Fixed(n) =
            False.
        Ke (output): This is an array of effective stiffness terms for the link property.
            The effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (output): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        k (output): This is an array of initial (nonslipping) stiffness terms for the link
            property. The initial stiffness applies for nonlinear analyses. k(0) = U1 [F/L]
            k(1) = U2 [F/L] k(2) = U3 [F/L] k(3) = R1 [FL] k(4) = R2 [FL] k(5) = R3 [FL] The
            term k(n) only applies only when DOF(n) = True, Fixed(n) = False and
            NonLinear(n) = True.
        k1 (output): This is an array of slipping stiffness when loading terms for the link
            property. The slipping stiffness when loading applies for nonlinear analyses.
            k1(0) = U1 [F/L] k1(1) = U2 [F/L] k1(2) = U3 [F/L] k1(3) = R1 [FL] k1 (4) = R2
            [FL] k1(5) = R3 [FL] The term k1(n) applies only when DOF(n) = True, Fixed(n) =
            False and NonLinear(n) = True.
        k2 (output): This is an array of slipping stiffness when unloading terms for the
            link property. The slipping stiffness when unloading applies for nonlinear
            analyses. k2(0) = U1 [F/L] k2(1) = U2 [F/L] k2(2) = U3 [F/L] k2(3) = R1 [FL]
            k2(4) = R2 [FL] k2(5) = R3 [FL] The term k2(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        u0 (output): This is an array of precompression displacement terms for the link
            property. The nonlinear precompression displacement applies for nonlinear
            analyses. u0(0) = U1 [L] u0(1) = U2 [L] u0(2) = U3 [L] u0(3) = R1 u0(4) = R2
            u0(5) = R3 The term u0(n) applies only when DOF(n) = True, Fixed(n) = False and
            NonLinear(n) = True.
        us (output): This is an array of stop displacement terms for the link property. The
            nonlinear stop displacement applies for nonlinear analyses. us(0) = U1 [L] us(1)
            = U2 [L] us(2) = U3 [L] us(3) = R1 us(4) = R2 us(5) = R3 The term us(n) applies
            only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        dj2 (output): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (output): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (output): The GUID (global unique identifier), if any, assigned to the
            property. If this item is input as Default, the program assigns a GUID to the
            property.
        """
        _r = self._raw.GetDamperFrictionSpring(Name, [], [], [], [], [], [], [], [], [], [], [], 0.0, 0.0, Notes, "")
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetDamperFrictionSpring falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetFrictionIsolator(self, Name: str, Notes: str, GUID: str):
        """This function retrieves link property data for a friction isolator-type link property. The
        function returns zero if the property data is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing friction isolator-type link property.
        DOF (output): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (output): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (output): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1, Not Used NonLinear(4) = R2, Not
            Used NonLinear(5) = R3, Not Used Note that this item is applicable only for
            degrees of freedom U1, U2 and U3. For those degrees of freedom, the term
            NonLinear(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ke (output): This is an array of effective stiffness terms for the link property.
            The effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (output): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        k (output): This is an array of initial stiffness terms for the link property. The
            initial stiffness applies for nonlinear analyses. k(0) = U1 [F/L] k(1) = U2
            [F/L] k(2) = U3 [F/L] k(3) = R1, Not Used k(4) = R2, Not Used k(5) = R3, Not
            Used Note that this item is applicable only for degrees of freedom U1, U2 and
            U3. For those degrees of freedom, the term k(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        Slow (output): This is an array of the friction coefficient at zero velocity terms
            for the link property. This coefficient applies for nonlinear analyses. Slow(0)
            = U1, Not Used Slow(1) = U2 Slow(2) = U3 Slow(3) = R1, Not Used Slow(4) = R2,
            Not Used Slow(5) = R3, Not Used Note that this item is applicable only for
            degrees of freedom U2 and U3. For those degrees of freedom, the term Slow(n)
            applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        Fast (output): This is an array of the friction coefficient at fast velocity terms
            for the link property. This coefficient applies for nonlinear analyses. Fast(0)
            = U1, Not Used Fast(1) = U2 Fast(2) = U3 Fast(3) = R1, Not Used Fast(4) = R2,
            Not Used Fast(5) = R3, Not Used Note that this item is applicable only for
            degrees of freedom U2 and U3. For those degrees of freedom, the term Fast(n)
            applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        Rate (output): This is an array of the inverse of the characteristic sliding
            velocity terms for the link property. This item applies for nonlinear analyses.
            Rate(0) = U1, Not Used Rate(1) = U2 [s/L] Rate(2) = U3 [s/L] Rate(3) = R1, Not
            Used Rate(4) = R2, Not Used Rate(5) = R3, Not Used Note that this item is
            applicable only for degrees of freedom U2 and U3. For those degrees of freedom,
            the term Rate(n) applies only when DOF(n) = True, Fixed(n) = False and
            NonLinear(n) = True.
        Radius (output): This is an array of the radius of the sliding contact surface terms
            for the link property. Inputting 0 means there is an infinite radius, that is,
            the slider is flat. This item applies for nonlinear analyses. Radius(0) = U1,
            Not Used Radius(1) = U2 [L] Radius(2) = U3 [L] Radius(3) = R1, Not Used
            Radius(4) = R2, Not Used Radius(5) = R3, Not Used Note that this item is
            applicable only for degrees of freedom U2 and U3. For those degrees of freedom,
            the term Radius(n) applies only when DOF(n) = True, Fixed(n) = False and
            NonLinear(n) = True.
        Damping (output): This is the nonlinear damping coefficient used for the axial
            translational degree of freedom, U1. This item applies for nonlinear analyses.
            [F/L]
        dj2 (output): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (output): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
        """
        _r = self._raw.GetFrictionIsolator(Name, [], [], [], [], [], [], [], [], [], [], 0.0, 0.0, 0.0, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetFrictionIsolator falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetGap(self, Name: str, Notes: str, GUID: str):
        """This function retrieves link property data for a gap-type link property. The function
        returns zero if the property data is retrieved successfully; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing gap-type link property.
        DOF (output): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (output): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (output): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1 has nonlinear properties
            NonLinear(4) = R2 has nonlinear properties NonLinear(5) = R3 has nonlinear
            properties The term NonLinear(n) applies only when DOF(n) = True and Fixed(n) =
            False.
        Ke (output): This is an array of effective stiffness terms for the link property.
            The effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (output): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        k (output): This is an array of initial stiffness terms for the link property. The
            initial stiffness applies for nonlinear analyses. k(0) = U1 [F/L] k(1) = U2
            [F/L] k(2) = U3 [F/L] k(3) = R1 [FL] k(4) = R2 [FL] k(5) = R3 [FL] The term k(n)
            applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        dis (output): This is an array of initial gap opening terms for the link property.
            The initial gap opening applies for nonlinear analyses. dis(0) = U1 [L] dis(1) =
            U2 [L] dis(2) = U3 [L] dis(3) = R1 [rad] dis(4) = R2 [rad] dis(5) = R3 [rad] The
            term dis(n) applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) =
            True.
        dj2 (output): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (output): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
        """
        _r = self._raw.GetGap(Name, [], [], [], [], [], [], [], 0.0, 0.0, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetGap falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetHook(self, Name: str, Notes: str, GUID: str):
        """This function retrieves link property data for a hook-type link property. The function
        returns zero if the property data is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing hook-type link property.
        DOF (output): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (output): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (output): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1 has nonlinear properties
            NonLinear(4) = R2 has nonlinear properties NonLinear(5) = R3 has nonlinear
            properties The term NonLinear(n) applies only when DOF(n) = True and Fixed(n) =
            False.
        Ke (output): This is an array of effective stiffness terms for the link property.
            The effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (output): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        k (output): This is an array of initial stiffness terms for the link property. The
            initial stiffness applies for nonlinear analyses. k(0) = U1 [F/L] k(1) = U2
            [F/L] k(2) = U3 [F/L] k(3) = R1 [FL] k(4) = R2 [FL] k(5) = R3 [FL] The term k(n)
            applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        dis (output): This is an array of initial hook opening terms for the link property.
            The initial hook opening applies for nonlinear analyses. c(0) = U1 [L] c(1) = U2
            [L] c(2) = U3 [L] c(3) = R1 [rad] c(4) = R2 [rad] c(5) = R3 [rad] The term
            dis(n) applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) =
            True.
        dj2 (output): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (output): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
        """
        _r = self._raw.GetHook(Name, [], [], [], [], [], [], [], 0.0, 0.0, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetHook falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetLinear(self, Name: str, KeCoupled: bool, CeCoupled: bool, Notes: str, GUID: str):
        """This function retrieves link property data for a linear-type link property. The function
        returns zero if the property data is successfully retrieved; otherwise it returns a
        nonzero value.
    
        Name (input): The name of an existing linear-type link property.
        DOF (output): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (output): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity if
            DOF(0) = True Fixed(1) = U2 fixity if DOF(1) = True Fixed(2) = U3 fixity if
            DOF(2) = True Fixed(3) = R1 fixity if DOF(3) = True Fixed(4) = R2 fixity if
            DOF(4) = True Fixed(5) = R3 fixity if DOF(5) = True
        Ke (output): This is an array of stiffness terms for the link property. There are 6
            terms in the array if the stiffness is uncoupled and 21 if it is coupled. The
            KeCoupled item indicates if the stiffness is coupled. If the stiffness is
            uncoupled: Ke(0) = U1 [F/L] Ke(1) = U2 [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL]
            Ke(4) = R2 [FL] Ke(5) = R3 [FL] If the stiffness is coupled: Ke(0) = U1U1 [F/L]
            Ke(1) = U1U2 [F/L] Ke(2) = U2U2 [F/L] Ke(3) = U1U3 [F/L] Ke(4) = U2U3 [F/L]
            Ke(5) = U3U3 [F/L] Ke(6) = U1R1 [F] Ke(7) = U2R1 [F] Ke(8) = U3R1 [F] Ke(9) =
            R1R1 [FL] Ke(10) = U1R2 [F] Ke(11) = U2R2 [F] Ke(12) = U3R2 [F] Ke(13) = R1R2
            [FL] Ke(14) = R2R2 [FL] Ke(15) = U1R3 [F] Ke(16) = U2R3 [F] Ke(17) = U3R3 [F]
            Ke(18) = R1R3 [FL] Ke(19) = R2R3 [FL] Ke(20) = R3R3 [FL]
        Ce (output): This is an array of damping terms for the link property. There are 6
            terms in the array if the damping is uncoupled and 21 if it is coupled. The
            CeCoupled item indicates if the damping is coupled. If the damping is uncoupled:
            Ce(0) = U1 [F/L] Ce(1) = U2 [F/L] Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2
            [FL] Ce(5) = R3 [FL] If the damping is coupled: Ce(0) = U1U1 [F/L] Ce(1) = U1U2
            [F/L] Ce(2) = U2U2 [F/L] Ce(3) = U1U3 [F/L] Ce(4) = U2U3 [F/L] Ce(5) = U3U3
            [F/L] Ce(6) = U1R1 [F] Ce(7) = U2R1 [F] Ce(8) = U3R1 [F] Ce(9) = R1R1 [FL]
            Ce(10) = U1R2 [F] Ce(11) = U2R2 [F] Ce(12) = U3R2 [F] Ce(13) = R1R2 [FL] Ce(14)
            = R2R2 [FL] Ce(15) = U1R3 [F] Ce(16) = U2R3 [F] Ce(17) = U3R3 [F] Ce(18) = R1R3
            [FL] Ce(19) = R2R3 [FL] Ce(20) = R3R3 [FL]
        dj2 (output): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (output): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        KeCoupled (input): This item is True if the link stiffness, Ke, is coupled. There
            are 21 terms in the Ke array if Ke is coupled; otherwise there are 6 terms.
        CeCoupled (input): This item is True if the link damping, Ce, is coupled. There are
            21 terms in the Ce array if Ce is coupled; otherwise there are 6 terms.
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
        """
        _r = self._raw.GetLinear(Name, [], [], [], [], 0.0, 0.0, KeCoupled, CeCoupled, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetLinear falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetMultiLinearElastic(self, Name: str, Notes: str, GUID: str):
        """This function retrieves link property data for a multilinear elastic-type link property. The
        function returns zero if the property data is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing multilinear elastic-type link property.
        DOF (output): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (output): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (output): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1 has nonlinear properties
            NonLinear(4) = R2 has nonlinear properties NonLinear(5) = R3 has nonlinear
            properties The term NonLinear(n) applies only when DOF(n) = True and Fixed(n) =
            False.
        Ke (output): This is an array of effective stiffness terms for the link property.
            The effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (output): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies pnly when DOF(n) = True and Fixed(n) = False.
        dj2 (output): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (output): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
        """
        _r = self._raw.GetMultiLinearElastic(Name, [], [], [], [], [], 0.0, 0.0, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetMultiLinearElastic falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetMultiLinearPlastic(self, Name: str, Notes: str, GUID: str):
        """This function retrieves link property data for a multilinear plastic-type link property. The
        function returns zero if the property data is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing multilinear plastic-type link property.
        DOF (output): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (output): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (output): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1 has nonlinear properties
            NonLinear(4) = R2 has nonlinear properties NonLinear(5) = R3 has nonlinear
            properties The term NonLinear(n) applies only when DOF(n) = True and Fixed(n) =
            False.
        Ke (output): This is an array of effective stiffness terms for the link property.
            The effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (output): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        dj2 (output): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (output): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
        """
        _r = self._raw.GetMultiLinearPlastic(Name, [], [], [], [], [], 0.0, 0.0, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetMultiLinearPlastic falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetMultiLinearPoints(self, Name: str, DOF: int):
        """This function retrieves the force-deformation data for a specified degree of freedom in
        multilinear elastic and multilinear plastic link properties. The function returns
        zero if the data is successfully retrieved; otherwise it returns a nonzero value. To
        successfully retrieve this data from the indicated link property, the following
        conditions must be met: 1. The link property must be multilinear elastic or
        multilinear plastic. 2. The specified DOF must be active. 3. The specified DOF must
        not be fixed. 4. The specified DOF must be nonlinear.
    
        Name (input): The name of an existing multilinear elastic or multilinear plastic
            link property.
        DOF (input): This is 1, 2, 3, 4, 5 or 6, indicating the degree of freedom to which
            the multilinear points apply. 1 = U1 2 = U2 3 = U3 4 = R1 5 = R2 6 = R3
        NumberPoints (output): The number of foce-defomation points for the specified degree
            of freedom.
        F (output): This is an array, dimensioned to NumberPoints - 1, that includes the
            force at each point. When DOF is U1, U2 or U3, this is a force. When DOF is R1,
            R2 or R3, this is a moment. [F] if DOF <= 3, and [FL} if DOF > 3
        D (output): This is an array, dimensioned to NumberPoints - 1, that includes the
            displacement at each point. When DOF is U1, U2 or U3, this is a translation.
            When DOF is R1, R2 or R3, this is a rotation. [L] if DOF <= 3, and [rad] if DOF
            > 3
        MyType (output): This item applies only to multilinear plastic link properties. It
            is 1, 2 or 3, indicating the hysteresis type. 1 = Kinematic 2 = Takeda 3 = Pivot
        a1 (output): This item only applies to multilinear plastic link properties that have
            a pivot hysteresis type (MyType = 3). It is the Alpha1 hysteresis parameter.
        a2 (output): This item applies only to multilinear plastic link properties that have
            a pivot hysteresis type (MyType = 3). It is the Alpha2 hysteresis parameter.
        b1 (output): This item applies only to multilinear plastic link properties that have
            a pivot hysteresis type (MyType = 3). It is the Beta1 hysteresis parameter.
        b2 (output): This item applies only to multilinear plastic link properties that have
            a pivot hysteresis type (MyType = 3). It is the Beta2 hysteresis parameter.
        eta (output): This item applies only to multilinear plastic link properties that
            have a pivot hysteresis type (MyType = 3). It is the Eta hysteresis parameter.
        """
        _r = self._raw.GetMultiLinearPoints(Name, DOF, 0, [], [], 0, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetMultiLinearPoints falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetNameList(self, PropType: int = None):
        """This function retrieves the names of all defined link properties of the specified type. The
        function returns zero if the names are successfully retrieved; otherwise it returns
        nonzero.
    
        NumberNames (output): The number of link property names retrieved by the program.
        MyName (output): This is a one-dimensional array of link property names. The MyName
            array is created as a dynamic, zero-based, array by the API user: Dim MyName()
            as String The array is dimensioned to (NumberNames - 1) inside the SAP2000
            program, filled with the names, and returned to the API user.
        PropType (input): This optional value is one of the following items in the
            eLinkPropType enumeration. NLPROP_LINEAR = 1 NLPROP_DAMPER = 2 NLPROP_GAP = 3
            NLPROP_HOOK = 4 NLPROP_PLASTIC_WEN = 5 NLPROP_ISOLATOR1 = 6 (Rubber isolator)
            NLPROP_ISOLATOR2 = 7 (Friction isolator) NLPROP_MULTILINEAR_ELASTIC = 8
            NLPROP_MULTILINEAR_PLASTIC = 9 NLPROP_ISOLATOR3 = 10 (T/C Friction isolator) If
            no value is input for PropType, names are returned for all link properties in
            the model regardless of type.
        """
        _r = self._raw.GetNameList(0, [], PropType)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetNameList falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPDelta(self, Name: str):
        """This function retrieves P-delta parameters for a link property. The function returns zero if
        the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link property.
        """
        _r = self._raw.GetPDelta(Name, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetPDelta falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetPlasticWen(self, Name: str, Notes: str, GUID: str):
        """This function retrieves link property data for a plastic Wen-type link property. The
        function returns zero if the property data is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing plastic Wen-type link property.
        DOF (output): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (output): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (output): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1 has nonlinear properties
            NonLinear(4) = R2 has nonlinear properties NonLinear(5) = R3 has nonlinear
            properties The term NonLinear(n) applies only when DOF(n) = True and Fixed(n) =
            False.
        Ke (output): This is an array of effective stiffness terms for the link property.
            The effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (output): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        k (output): This is an array of initial stiffness terms for the link property. The
            initial stiffness applies for nonlinear analyses. k(0) = U1 [F/L] k(1) = U2
            [F/L] k(2) = U3 [F/L] k(3) = R1 [FL] k(4) = R2 [FL] k(5) = R3 [FL] The term k(n)
            applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        Yield (output): This is an array of yield force terms for the link property. The
            yield force applies for nonlinear analyses. Yield(0) = U1 [F] Yield(1) = U2 [F]
            Yield(2) = U3 [F] Yield(3) = R1 [FL] Yield(4) = R2 [FL] Yield(5) = R3 [FL] The
            term Yield(n) applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n)
            = True.
        Ratio (output): This is an array of post-yield stiffness ratio terms for the link
            property. The post-yield stiffness ratio applies for nonlinear analyses. It is
            the post-yield stiffness divided by the initial stiffness. Ratio(0) = U1
            Ratio(1) = U2 Ratio(2) = U3 Ratio(3) = R1 Ratio(4) = R2 Ratio(5) = R3 The term
            Ratio(n) applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) =
            True.
        exp (output): This is an array of yield exponent terms for the link property. The
            yield exponent applies for nonlinear analyses. The yielding exponent that
            controls the sharpness of the transition from the initial stiffness to the
            yielded stiffness. exp(0) = U1 exp(1) = U2 exp(2) = U3 exp(3) = R1 exp(4) = R2
            exp(5) = R3 The term exp(n) applies only when DOF(n) = True, Fixed(n) = False
            and NonLinear(n) = True.
        dj2 (output): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (output): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
        """
        _r = self._raw.GetPlasticWen(Name, [], [], [], [], [], [], [], [], [], 0.0, 0.0, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetPlasticWen falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetRubberIsolator(self, Name: str, Notes: str, GUID: str):
        """This function retrieves link property data for a rubber isolator-type link property. The
        function returns zero if the property data is successfully retrieved; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing rubber isolator-type link property.
        DOF (output): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (output): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (output): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1,
            Not Used NonLinear(1) = U2 has nonlinear properties NonLinear(2) = U3 has
            nonlinear properties NonLinear(3) = R1, Not Used NonLinear(4) = R2, Not Used
            NonLinear(5) = R3, Not Used Note that this item is applicable only for degrees
            of freedom U2 and U3. For those degrees of freedom, the term NonLinear(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        Ke (output): This is an array of effective stiffness terms for the link property.
            The effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (output): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        k (output): This is an array of initial stiffness terms for the link property. The
            initial stiffness applies for nonlinear analyses. k(0) = U1, Not Used k(1) = U2
            [F/L] k(2) = U3 [F/L] k(3) = R1, Not Used k(4) = R2, Not Used k(5) = R3, Not
            Used Note that this item is applicable only for degrees of freedom U2 and U3.
            For those degrees of freedom, the term k(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        Yield (output): This is an array of yield force terms for the link property. The
            yield force applies for nonlinear analyses. Yield(0) = U1, Not Used Yield(1) =
            U2 [F] Yield(2) = U3 [F] Yield(3) = R1, Not Used Yield(4) = R2, Not Used
            Yield(5) = R3, Not Used The term Yield(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        Ratio (output): This is an array of post-yield stiffness ratio terms for the link
            property. The post-yield stiffness ratio applies for nonlinear analyses. It is
            the post-yield stiffness divided by the initial stiffness. Ratio(0) = U1, Not
            Used Ratio(1) = U2 Ratio(2) = U3 Ratio(3) = R1, Not Used Ratio(4) = R2, Not Used
            Ratio(5) = R3, Not Used The term Ratio(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        dj2 (output): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (output): The distance from the J-End of the link to the U3 shear spring. This
            item applies pnly when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
        """
        _r = self._raw.GetRubberIsolator(Name, [], [], [], [], [], [], [], [], 0.0, 0.0, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetRubberIsolator falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetSpringData(self, Name: str):
        """This function retrieves length and area values for a link property that are used if the link
        property is specified in line and area spring assignments. The function returns zero
        if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link property.
        DefinedForThisLength (output): The link property is defined for this length in a
            line (frame) spring. [L]
        DefinedForThisArea (output): The link property is defined for this area in an area
            spring. [L 2 ]
        """
        _r = self._raw.GetSpringData(Name, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetSpringData falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTCFrictionIsolator(self, Name: str, Notes: str, GUID: str):
        """This function retrieves link property data for a T/C friction isolator-type link property.
        The function returns zero if the property data is successfully retrieved; otherwise
        it returns a nonzero value.
    
        Name (input): The name of an existing T/C friction isolator-type link property.
        DOF (output): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (output): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies pnly when DOF(n) = True.
        NonLinear (output): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1, Not Used NonLinear(4) = R2, Not
            Used NonLinear(5) = R3, Not Used Note that this item is applicable only for
            degrees of freedom U1, U2 and U3. For those degrees of freedom, the term
            NonLinear(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ke (output): This is an array of effective stiffness terms for the link property.
            The effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (output): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        k (output): This is an array of initial stiffness terms for the link property. The
            initial stiffness applies for nonlinear analyses. k(0) = U1 [F/L] k(1) = U2
            [F/L] k(2) = U3 [F/L] k(3) = R1, Not Used k(4) = R2, Not Used k(5) = R3, Not
            Used Note that this item is applicable only for degrees of freedom U1, U2 and
            U3. For those degrees of freedom, the term k(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        Slow (output): This is an array of the friction coefficient at zero velocity terms
            when U1 is in compression for the link property. This coefficient applies for
            nonlinear analyses. Slow(0) = U1, Not Used Slow(1) = U2 Slow(2) = U3 Slow(3) =
            R1, Not Used Slow(4) = R2, Not Used Slow(5) = R3, Not Used Note that this item
            is applicable only for degrees of freedom U2 and U3. For those degrees of
            freedom, the term Slow(n) applies only when DOF(n) = True, Fixed(n) = False and
            NonLinear(n) = True.
        Fast (output): This is an array of the friction coefficient at fast velocity terms
            when U1 is in compression for the link property. This coefficient applies for
            nonlinear analyses. Fast(0) = U1, Not Used Fast(1) = U2 Fast(2) = U3 Fast(3) =
            R1, Not Used Fast(4) = R2, Not Used Fast(5) = R3, Not Used Note that this item
            is applicable only for degrees of freedom U2 and U3. For those degrees of
            freedom, the term Fast(n) applies only when DOF(n) = True, Fixed(n) = False and
            NonLinear(n) = True.
        Rate (output): This is an array of the inverse of the characteristic sliding
            velocity terms when U1 is in compression for the link property. This item
            applies for nonlinear analyses. Rate(0) = U1, Not Used Rate(1) = U2 [s/L]
            Rate(2) = U3 [s/L] Rate(3) = R1, Not Used Rate(4) = R2, Not Used Rate(5) = R3,
            Not Used Note that this item is applicable only for degrees of freedom U2 and
            U3. For those degrees of freedom, the term Rate(n) applies only when DOF(n) =
            True, Fixed(n) = False and NonLinear(n) = True.
        Radius (output): This is an array of the radius of the sliding contact surface terms
            for the link property. Inputting 0 means there is an infinite radius, that is,
            the slider is flat. This item applies for nonlinear analyses. Radius(0) = U1,
            Not Used Radius(1) = U2 [L] Radius(2) = U3 [L] Radius(3) = R1, Not Used
            Radius(4) = R2, Not Used Radius(5) = R3, Not Used Note that this item is
            applicable only for degrees of freedom U2 and U3. For those degrees of freedom,
            the term Radius(n) applies only when DOF(n) = True, Fixed(n) = False and
            NonLinear(n) = True.
        SlowT (output): This is an array of the friction coefficient at zero velocity terms
            when U1 is in tension for the link property. This coefficient applies for
            nonlinear analyses. SlowT(0) = U1, Not Used SlowT(1) = U2 SlowT(2) = U3 SlowT(3)
            = R1, Not Used SlowT(4) = R2, Not Used SlowT(5) = R3, Not Used Note that this
            item is applicable only for degrees of freedom U2 and U3. For those degrees of
            freedom, the term SlowT(n) applies only when DOF(n) = True, Fixed(n) = False and
            NonLinear(n) = True.
        FastT (output): This is an array of the friction coefficient at fast velocity terms
            when U1 is in tension for the link property. This coefficient applies for
            nonlinear analyses. FastT(0) = U1, Not Used FastT(1) = U2 FastT(2) = U3 FastT(3)
            = R1, Not Used FastT(4) = R2, Not Used FastT(5) = R3, Not Used Note that this
            item is applicable only for degrees of freedom U2 and U3. For those degrees of
            freedom, the term FastT(n) applies only when DOF(n) = True, Fixed(n) = False and
            NonLinear(n) = True.
        RateT (output): This is an array of the inverse of the characteristic sliding
            velocity terms when U1 is in tension for the link property. This item applies
            for nonlinear analyses. RateT(0) = U1, Not Used RateT(1) = U2 [s/L] RateT(2) =
            U3 [s/L] RateT(3) = R1, Not Used RateT(4) = R2, Not Used RateT(5) = R3, Not Used
            Note that this item is applicable only for degrees of freedom U2 and U3. For
            those degrees of freedom, the term RateT(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        kt (output): The axial translational tension stiffness for the U1 degree of freedom.
            This item applies for nonlinear analyses. [F/L]
        dis (output): The U1 degree of freedom gap opening for compression. This item
            applies for nonlinear analyses. [L]
        dist (output): The U1 degree of freedom gap opening for tension. This item applies
            for nonlinear analyses. [L]
        Damping (output): The nonlinear damping coefficient used for the axial translational
            degree of freedom, U1. This item applies for nonlinear analyses. [F/L]
        dj2 (output): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (output): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
        """
        _r = self._raw.GetTCFrictionIsolator(Name, [], [], [], [], [], [], [], [], [], [], [], [], [], 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetTCFrictionIsolator falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTriplePendulumIsolator(self, Name: str, Notes: str, GUID: str):
        """This function retrieves link property data for a Triple Pendulum Isolator type link
        property. The function returns zero if the property data is successfully retrieved;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing Triple Pendulum Isolator type link property.
        Fixed (output): This is a Boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) only applies when DOF(n) = True.
        Ke (output): This is an array of effective stiffness terms for the link property.
            The effective stiffness applies for linear analyses, and also for nonlinear
            analysis for those DOF for which NonLinear(n) = False. Ke(0) = U1 [F/L] Ke(1) =
            U2 [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The
            term Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (output): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        K1 (output): This is the axial compression stiffness for the U1 degree of freedom.
            This item applies for nonlinear analyses. [F/L]
        Damping (output): This is the nonlinear damping coefficient for the axial degree of
            freedom, U1, when it is in compression. This item applies for nonlinear
            analyses. [F/L]
        K (output): This is an array, dimensioned to 3, of initial nonlinear stiffness
            (before sliding) for each sliding surface. K(0) = for the outer top sliding
            surface [F/L] K(1) = for the outer bottom sliding surface [F/L] K(2) = for the
            inner top sliding surface [F/L] K(3) = for the inner bottom sliding surface
            [F/L] Note that this item is applicable for degrees of freedom U2 and U3 only.
            For those degrees of freedom, the term k(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        Slow (output): This is an array, dimensioned to 3, of the friction coefficient at
            zero velocity for each sliding surface when U1 is in compression. Slow(0) = for
            the outer top sliding surface Slow(1) = for the outer bottom sliding surface
            Slow(2) = for the inner top sliding surface Slow(3) = for the inner bottom
            sliding surface Note that this item is applicable for degrees of freedom U2 and
            U3 only. For those degrees of freedom, the term Slow(n) applies only when DOF(n)
            = True, Fixed(n) = False and NonLinear(n) = True.
        Fast (output): This is an array, dimensioned to 3, of the friction coefficient at
            fast velocity for each sliding surface when U1 is in compression. Fast(0) = for
            the outer top sliding surface Fast(1) = for the outer bottom sliding surface
            Fast(2) = for the inner top sliding surface Fast(3) = for the inner bottom
            sliding surface Note that this item is applicable for degrees of freedom U2 and
            U3 only. For those degrees of freedom, the term Fast(n) applies only when DOF(n)
            = True, Fixed(n) = False and NonLinear(n) = True.
        Rate (output): This is an array, dimensioned to 3, of the inverse of the
            characteristic sliding velocity for the Slow and Fast friction coefficients for
            each sliding surface. This item applies for nonlinear analyses. Rate(0) = for
            the outer top sliding surface [s/L] Rate(1) = for the outer bottom sliding
            surface [s/L] Rate(2) = for the inner top sliding surface [s/L] Rate(3) = for
            the inner bottom sliding surface [s/L] Note that this item is applicable for
            degrees of freedom U2 and U3 only. For those degrees of freedom, the term
            Rate(n) applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) =
            True.
        Radius (output): This is an array, dimensioned to 3, of the radius for each sliding
            surface. Inputting 0 means there is an infinite radius, that is, the slider is
            flat. This item applies for nonlinear analyses. Radius(0) = for the outer top
            sliding surface [L] Radius(1) = for the outer bottom sliding surface [L]
            Radius(2) = for the inner top sliding surface [L] Radius(3) = for the inner
            bottom sliding surface [L] Note that this item is applicable for degrees of
            freedom U2 and U3 only. For those degrees of freedom, the term Radius(n) applies
            only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        StopDist (output): This is an array, dimensioned to 3, of the amount of displacement
            allowed before hitting a stiff limit for each sliding surface. Inputting 0 means
            there is no stop. This item applies for nonlinear analyses. StopDist(0) = for
            the outer top sliding surface [L] StopDist(1) = for the outer bottom sliding
            surface [L] StopDist(2) = for the inner top sliding surface [L] StopDist(3) =
            for the inner bottom sliding surface [L] Note that this item is applicable for
            degrees of freedom U2 and U3 only. For those degrees of freedom, the term
            StopDist(n) applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) =
            True.
        HeightOut (output): This is the height (distance) between the outer sliding surfaces
            at zero displacement. [L] Note that this item is applicable for degrees of
            freedom U2 and U3 only. For those degrees of freedom, the term applies only when
            DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        HeightIn (output): This is the height (distance) between the inner sliding surfaces.
            [L] Note that this item is applicable for degrees of freedom U2 and U3 only. For
            those degrees of freedom, the term applies only when DOF(n) = True, Fixed(n) =
            False and NonLinear(n) = True.
        dj2 (output): The distance from the J-End of the link to the U2 shear spring, that
            is, the center of the isolator. This item applies only when DOF(2) = True. [L]
        dj3 (output): The distance from the J-End of the link to the U3 shear spring, that
            is, the center of the isolator. This item applies only when DOF(3) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
        """
        _r = self._raw.GetTriplePendulumIsolator(Name, [], [], [], [], [], 0.0, 0.0, [], [], [], [], [], [], 0.0, 0.0, 0.0, 0.0, Notes, GUID)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetTriplePendulumIsolator falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def GetTypeOAPI(self, Name: str):
        """This function retrieves the property type for the specified link property. The function
        returns zero if the type is successfully retrieved; otherwise it returns nonzero.
    
        Name (input): The name of an existing link property.
        PropType (output): This is one of the following items in the eLinkPropType
            enumeration. NLPROP_LINEAR = 1 NLPROP_DAMPER = 2 NLPROP_GAP = 3 NLPROP_HOOK = 4
            NLPROP_PLASTIC_WEN = 5 NLPROP_ISOLATOR1 = 6 (Rubber isolator) NLPROP_ISOLATOR2 =
            7 (Friction isolator) NLPROP_MULTILINEAR_ELASTIC = 8 NLPROP_MULTILINEAR_PLASTIC
            = 9 NLPROP_ISOLATOR3 = 10 (T/C Friction isolator)
        """
        _r = self._raw.GetTypeOAPI(Name, None)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetTypeOAPI falhou (ret={_ret})".format(_ret=_ret))
        return _outs[0]

    def GetWeightAndMass(self, Name: str):
        """This function retrieves weight and mass data for a link property. The function returns zero
        if the data is successfully retrieved; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link property.
        w (output): The weight of the link. [F]
        m (output): The translational mass of the link. [M]
        R1 (output): The rotational inertia of the link about its local 1 axis. [ML 2 ]
        R2 (output): The rotational inertia of the link about its local 2 axis. [ML 2 ]
        R3 (output): The rotational inertia of the link about its local 3 axis. [ML 2 ]
        """
        _r = self._raw.GetWeightAndMass(Name, 0.0, 0.0, 0.0, 0.0, 0.0)
        *_outs, _ret = _r
        if _ret != 0:
            raise Sap2000ApiError("SapModel.PropLink.GetWeightAndMass falhou (ret={_ret})".format(_ret=_ret))
        return tuple(_outs)

    def SetDamper(self, Name: str, DOF: list[bool], Fixed: list[bool], NonLinear: list[bool], Ke: list[float], Ce: list[float], k: list[float], c: list[float], cexp: list[float], dj2: float, dj3: float, Notes: str = '', GUID: str = ''):
        """This function initializes an exponential damper-type link property. If this function is
        called for an existing link property, all items for the property are reset to their
        default values. The function returns zero if the property is successfully
        initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new link property. If this is an existing
            property, that property is modified; otherwise, a new property is added.
        DOF (input): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (input): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (input): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1 has nonlinear properties
            NonLinear(4) = R2 has nonlinear properties NonLinear(5) = R3 has nonlinear
            properties The term NonLinear(n) applies only when DOF(n) = True and Fixed(n) =
            False.
        Ke (input): This is an array of effective stiffness terms for the link property. The
            effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (input): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        k (input): This is an array of initial stiffness terms for the link property. The
            initial stiffness applies for nonlinear analyses. k(0) = U1 [F/L] k(1) = U2
            [F/L] k(2) = U3 [F/L] k(3) = R1 [FL] k(4) = R2 [FL] k(5) = R3 [FL] The term k(n)
            only applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        c (input): This is an array of nonlinear damping coefficient terms for the link
            property. The nonlinear damping coefficient applies for nonlinear analyses. c(0)
            = U1 [F/(L^cexp)] c(1) = U2 [F/(L^cexp)] c(2) = U3 [F/(L^cexp)] c(3) = R1 [FL]
            c(4) = R2 [FL] c(5) = R3 [FL] The term c(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        cexp (input): This is an array of the nonlinear damping exponent terms. The
            nonlinear damping exponent applies for nonlinear analyses. It is applied to the
            velocity across the damper in the equation of motion. cexp(0) = U1 cexp(1) = U2
            cexp(2) = U3 cexp(3) = R1 cexp(4) = R2 cexp(5) = R3 The term cexp(n) applies
            only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        dj2 (input): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (input): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, the program assigns a GUID to the property.
        """
        _r = self._raw.SetDamper(Name, DOF, Fixed, NonLinear, Ke, Ce, k, c, cexp, dj2, dj3, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.SetDamper falhou (ret={_r})".format(_r=_r))
        return None

    def SetDamperBilinear(self, Name: str, DOF: list[bool], Fixed: list[bool], NonLinear: list[bool], Ke: list[float], Ce: list[float], k: list[float], c: list[float], cy: list[float], ForceLimit: list[float], dj2: float, dj3: float, Notes: str = '', GUID: str = ''):
        """This function initializes a bilinear damper-type link property. If this function is called
        for an existing link property, all items for the property are reset to their default
        values. The function returns zero if the property is successfully initialized;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new link property. If this is an existing
            property, that property is modified; otherwise, a new property is added.
        DOF (input): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (input): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained.) Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (input): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1 has nonlinear properties
            NonLinear(4) = R2 has nonlinear properties NonLinear(5) = R3 has nonlinear
            properties The term NonLinear(n) applies only when DOF(n) = True and Fixed(n) =
            False.
        Ke (input): This is an array of effective stiffness terms for the link property. The
            effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (input): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        k (input): This is an array of initial stiffness terms for the link property. The
            initial stiffness applies for nonlinear analyses. k(0) = U1 [F/L] k(1) = U2
            [F/L] k(2) = U3 [F/L] k(3) = R1 [FL] k(4) = R2 [FL] k(5) = R3 [FL] The term k(n)
            only applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        c (input): This is an array of nonlinear initial damping coefficient terms for the
            link property. The nonlinear initial damping coefficient applies for nonlinear
            analyses. c(0) = U1 [F/L] c(1) = U2 [F/L] c(2) = U3 [F/L] c(3) = R1 [FL] c(4) =
            R2 [FL] c(5) = R3 [FL] The term c(n) applies only when DOF(n) = True, Fixed(n) =
            False and NonLinear(n) = True.
        cy (input): This is an array of nonlinear yielded damping coefficient terms for the
            link property. The nonlinear yielded damping coefficient applies for nonlinear
            analyses. cy(0) = U1 [F/L] cy(1) = U2 [F/L] cy(2) = U3 [F/L] cy(3) = R1 [FL]
            cy(4) = R2 [FL] cy(5) = R3 [FL] The term cy(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        ForceLimit (input): This is an array of nonlinear linear force limit terms for the
            link property. The linear force limit applies for nonlinear analyses.
            ForceLimit(0) = U1 [F] ForceLimit(1) = U2 [F] ForceLimit(2) = U3 [F]
            ForceLimit(3) = R1 [FL] ForceLimit(4) = R2 [FL] ForceLimit(5) = R3 [FL] The term
            ForceLimit(n) applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n)
            = True.
        dj2 (input): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (input): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, the program assigns a GUID to the property.
        """
        _r = self._raw.SetDamperBilinear(Name, DOF, Fixed, NonLinear, Ke, Ce, k, c, cy, ForceLimit, dj2, dj3, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.SetDamperBilinear falhou (ret={_r})".format(_r=_r))
        return None

    def SetDamperFrictionSpring(self, Name: str, DOF: list[bool], Fixed: list[bool], NonLinear: list[bool], Ke: list[float], Ce: list[float], k: list[float], k1: list[float], k2: list[float], u0: list[float], us: list[float], dir: list[int], dj2: float, dj3: float, Notes: str = '', GUID: str = ''):
        """This function initializes a friction spring damper-type link property. If this function is
        called for an existing link property, all items for the property are reset to their
        default values. The function returns zero if the property is successfully
        initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new link property. If this is an existing
            property, that property is modified; otherwise, a new property is added.
        DOF (input): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (input): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained.) Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (input): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1 has nonlinear properties
            NonLinear(4) = R2 has nonlinear properties NonLinear(5) = R3 has nonlinear
            properties The term NonLinear(n) applies only when DOF(n) = True and Fixed(n) =
            False.
        Ke (input): This is an array of effective stiffness terms for the link property. The
            effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (input): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        k (input): This is an array of initial (nonslipping) stiffness terms for the link
            property. The initial stiffness applies for nonlinear analyses. k(0) = U1 [F/L]
            k(1) = U2 [F/L] k(2) = U3 [F/L] k(3) = R1 [FL] k(4) = R2 [FL] k(5) = R3 [FL] The
            term k(n) only applies only when DOF(n) = True, Fixed(n) = False and
            NonLinear(n) = True.
        k1 (input): This is an array of slipping stiffness when loading terms for the link
            property. The slipping stiffness when loading applies for nonlinear analyses.
            k1(0) = U1 [F/L] k1(1) = U2 [F/L] k1(2) = U3 [F/L] k1(3) = R1 [FL] k1 (4) = R2
            [FL] k1(5) = R3 [FL] The term k1(n) applies only when DOF(n) = True, Fixed(n) =
            False and NonLinear(n) = True.
        k2 (input): This is an array of slipping stiffness when unloading terms for the link
            property. The slipping stiffness when unloading applies for nonlinear analyses.
            k2(0) = U1 [F/L] k2(1) = U2 [F/L] k2(2) = U3 [F/L] k2(3) = R1 [FL] k2(4) = R2
            [FL] k2(5) = R3 [FL] The term k2(n) applies only when DOF(n) = True, Fixed(n) =
            False and NonLinear(n) = True.
        u0 (input): This is an array of precompression displacement terms for the link
            property. The nonlinear precompression displacement applies for nonlinear
            analyses. u0(0) = U1 [L] u0(1) = U2 [L] u0(2) = U3 [L] u0(3) = R1 u0(4) = R2
            u0(5) = R3 The term u0(n) applies only when DOF(n) = True, Fixed(n) = False and
            NonLinear(n) = True.
        us (input): This is an array of stop displacement terms for the link property. The
            nonlinear stop displacement applies for nonlinear analyses. us(0) = U1 [L] us(1)
            = U2 [L] us(2) = U3 [L] us(3) = R1 us(4) = R2 us(5) = R3 The term us(n) applies
            only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        dj2 (input): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (input): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, the program assigns a GUID to the property.
        """
        _r = self._raw.SetDamperFrictionSpring(Name, DOF, Fixed, NonLinear, Ke, Ce, k, k1, k2, u0, us, dir, dj2, dj3, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.SetDamperFrictionSpring falhou (ret={_r})".format(_r=_r))
        return None

    def SetDamperLinearExponential(self, Name: str, DOF: list[bool], Fixed: list[bool], NonLinear: list[bool], Ke: list[float], Ce: list[float], k: list[float], c: list[float], cexp: list[float], ForceLimit: list[float], dj2: float, dj3: float, Notes: str = '', GUID: str = ''):
        """This function initializes a linear exponential damper-type link property. If this function
        is called for an existing link property, all items for the property are reset to
        their default values. The function returns zero if the property is successfully
        initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new link property. If this is an existing
            property, that property is modified; otherwise, a new property is added.
        DOF (input): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (input): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained.) Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (input): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1 has nonlinear properties
            NonLinear(4) = R2 has nonlinear properties NonLinear(5) = R3 has nonlinear
            properties The term NonLinear(n) applies only when DOF(n) = True and Fixed(n) =
            False.
        Ke (input): This is an array of effective stiffness terms for the link property. The
            effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (input): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        k (input): This is an array of initial stiffness terms for the link property. The
            initial stiffness applies for nonlinear analyses. k(0) = U1 [F/L] k(1) = U2
            [F/L] k(2) = U3 [F/L] k(3) = R1 [FL] k(4) = R2 [FL] k(5) = R3 [FL] The term k(n)
            only applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        c (input): This is an array of nonlinear damping coefficient terms for the link
            property. The nonlinear damping coefficient applies for nonlinear analyses. c(0)
            = U1 [F/(L^cexp)] c(1) = U2 [F/(L^cexp)] c(2) = U3 [F/(L^cexp)] c(3) = R1 [FL]
            c(4) = R2 [FL] c(5) = R3 [FL] The term c(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        cexp (input): This is an array of the nonlinear damping exponent terms. The
            nonlinear damping exponent applies for nonlinear analyses. It is applied to the
            velocity across the damper in the equation of motion. cexp(0) = U1 cexp(1) = U2
            cexp(2) = U3 cexp(3) = R1 cexp(4) = R2 cexp(5) = R3 The term cexp(n) applies
            only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        ForceLimit (input): This is an array of nonlinear linear force limit terms for the
            link property. The linear force limit applies for nonlinear analyses.
            ForceLimit(0) = U1 [F] ForceLimit(1) = U2 [F] ForceLimit(2) = U3 [F]
            ForceLimit(3) = R1 [FL] ForceLimit(4) = R2 [FL] ForceLimit(5) = R3 [FL] The term
            ForceLimit(n) applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n)
            = True.
        dj2 (input): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (input): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, the program assigns a GUID to the property.
        """
        _r = self._raw.SetDamperLinearExponential(Name, DOF, Fixed, NonLinear, Ke, Ce, k, c, cexp, ForceLimit, dj2, dj3, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.SetDamperLinearExponential falhou (ret={_r})".format(_r=_r))
        return None

    def SetFrictionIsolator(self, Name: str, DOF: list[bool], Fixed: list[bool], NonLinear: list[bool], Ke: list[float], Ce: list[float], k: list[float], Slow: list[float], Fast: list[float], Rate: list[float], Radius: list[float], Damping: float, dj2: float, dj3: float, Notes: str = '', GUID: str = ''):
        """This function initializes a friction isolator-type link property. If this function is called
        for an existing link property, all items for the property are reset to their default
        value. The function returns zero if the property is successfully initialized;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new link property. If this is an existing
            property, that property is modified; otherwise, a new property is added.
        DOF (input): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (input): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (input): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1, Not Used NonLinear(4) = R2, Not
            Used NonLinear(5) = R3, Not Used Note that this item is applicable only for
            degrees of freedom U1, U2 and U3. For those degrees of freedom, the term
            NonLinear(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ke (input): This is an array of effective stiffness terms for the link property. The
            effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (input): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        k (input): This is an array of initial stiffness terms for the link property. The
            initial stiffness applies for nonlinear analyses. k(0) = U1 [F/L] k(1) = U2
            [F/L] k(2) = U3 [F/L] k(3) = R1, Not Used k(4) = R2, Not Used k(5) = R3, Not
            Used Note that this item is applicable only for degrees of freedom U1, U2 and
            U3. For those degrees of freedom, the term k(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        Slow (input): This is an array of the friction coefficient at zero velocity terms
            for the link property. This coefficient applies for nonlinear analyses. Slow(0)
            = U1, Not Used Slow(1) = U2 Slow(2) = U3 Slow(3) = R1, Not Used Slow(4) = R2,
            Not Used Slow(5) = R3, Not Used Note that this item is applicable only for
            degrees of freedom U2 and U3. For those degrees of freedom, the term Slow(n)
            applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        Fast (input): This is an array of the friction coefficient at fast velocity terms
            for the link property. This coefficient applies for nonlinear analyses. Fast(0)
            = U1, Not Used Fast(1) = U2 Fast(2) = U3 Fast(3) = R1, Not Used Fast(4) = R2,
            Not Used Fast(5) = R3, Not Used Note that this item is applicable only for
            degrees of freedom U2 and U3. For those degrees of freedom, the term Fast(n)
            applies pnly when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        Rate (input): This is an array of the inverse of the characteristic sliding velocity
            terms for the link property. This item applies for nonlinear analyses. Rate(0) =
            U1, Not Used Rate(1) = U2 [s/L] Rate(2) = U3 [s/L] Rate(3) = R1, Not Used
            Rate(4) = R2, Not Used Rate(5) = R3, Not Used Note that this item is applicable
            only for degrees of freedom U2 and U3. For those degrees of freedom, the term
            Rate(n) applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) =
            True.
        Radius (input): This is an array of the radius of the sliding contact surface terms
            for the link property. Inputting 0 means there is an infinite radius, that is,
            the slider is flat. This item applies for nonlinear analyses. Radius(0) = U1,
            Not Used Radius(1) = U2 [L] Radius(2) = U3 [L] Radius(3) = R1, Not Used
            Radius(4) = R2, Not Used Radius(5) = R3, Not Used Note that this item is
            applicable only for degrees of freedom U2 and U3. For those degrees of freedom,
            the term Radius(n) applies only when DOF(n) = True, Fixed(n) = False and
            NonLinear(n) = True.
        Damping (input): This is the nonlinear damping coefficient used for the axial
            translational degree of freedom, U1. This item applies for nonlinear analyses.
            [F/L]
        dj2 (input): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (input): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, the program assigns a GUID to the property.
        """
        _r = self._raw.SetFrictionIsolator(Name, DOF, Fixed, NonLinear, Ke, Ce, k, Slow, Fast, Rate, Radius, Damping, dj2, dj3, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.SetFrictionIsolator falhou (ret={_r})".format(_r=_r))
        return None

    def SetGap(self, Name: str, DOF: list[bool], Fixed: list[bool], NonLinear: list[bool], Ke: list[float], Ce: list[float], k: list[float], dis: list[float], dj2: float, dj3: float, Notes: str = '', GUID: str = ''):
        """This function initializes a gap-type link property. If this function is called for an
        existing link property, all items for the property are reset to their default value.
        The function returns zero if the property is successfully initialized; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing or new link property. If this is an existing
            property then that property is modified; otherwise, a new property is added.
        DOF (input): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (input): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (input): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1 has nonlinear properties
            NonLinear(4) = R2 has nonlinear properties NonLinear(5) = R3 has nonlinear
            properties The term NonLinear(n) applies only when DOF(n) = True and Fixed(n) =
            False.
        Ke (input): This is an array of effective stiffness terms for the link property. The
            effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (input): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        k (input): This is an array of initial stiffness terms for the link property. The
            initial stiffness applies for nonlinear analyses. k(0) = U1 [F/L] k(1) = U2
            [F/L] k(2) = U3 [F/L] k(3) = R1 [FL] k(4) = R2 [FL] k(5) = R3 [FL] The term k(n)
            applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        dis (input): This is an array of initial gap opening terms for the link property.
            The initial gap opening applies for nonlinear analyses. dis(0) = U1 [L] dis(1) =
            U2 [L] dis(2) = U3 [L] dis(3) = R1 [rad] dis(4) = R2 [rad] dis(5) = R3 [rad] The
            term dis(n) applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) =
            True.
        dj2 (input): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (input): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, the program assigns a GUID to the property.
        """
        _r = self._raw.SetGap(Name, DOF, Fixed, NonLinear, Ke, Ce, k, dis, dj2, dj3, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.SetGap falhou (ret={_r})".format(_r=_r))
        return None

    def SetHook(self, Name: str, DOF: list[bool], Fixed: list[bool], NonLinear: list[bool], Ke: list[float], Ce: list[float], k: list[float], dis: list[float], dj2: float, dj3: float, Notes: str = '', GUID: str = ''):
        """This function initializes a hook-type link property. If this function is called for an
        existing link property, all items for the property are reset to their default value.
        The function returns zero if the property is successfully initialized; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing or new link property. If this is an existing
            property then that property is modified; otherwise, a new property is added.
        DOF (input): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (input): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (input): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1 has nonlinear properties
            NonLinear(4) = R2 has nonlinear properties NonLinear(5) = R3 has nonlinear
            properties The term NonLinear(n) applies only when DOF(n) = True and Fixed(n) =
            False.
        Ke (input): This is an array of effective stiffness terms for the link property. The
            effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (input): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        k (input): This is an array of initial stiffness terms for the link property. The
            initial stiffness applies for nonlinear analyses. k(0) = U1 [F/L] k(1) = U2
            [F/L] k(2) = U3 [F/L] k(3) = R1 [FL] k(4) = R2 [FL] k(5) = R3 [FL] The term k(n)
            applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        dis (input): This is an array of initial hook opening terms for the link property.
            The initial hook opening applies for nonlinear analyses. c(0) = U1 [L] c(1) = U2
            [L] c(2) = U3 [L] c(3) = R1 [rad] c(4) = R2 [rad] c(5) = R3 [rad] The term
            dis(n) applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) =
            True.
        dj2 (input): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (input): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, the program assigns a GUID to the property.
        """
        _r = self._raw.SetHook(Name, DOF, Fixed, NonLinear, Ke, Ce, k, dis, dj2, dj3, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.SetHook falhou (ret={_r})".format(_r=_r))
        return None

    def SetLinear(self, Name: str, DOF: list[bool], Fixed: list[bool], Ke: list[float], Ce: list[float], dj2: float, dj3: float, KeCoupled: bool = False, CeCoupled: bool = False, Notes: str = '', GUID: str = ''):
        """This function initializes a linear-type link property. If this function is called for an
        existing link property, all items for the property are reset to their default value.
        The function returns zero if the property is successfully initialized; otherwise it
        returns a nonzero value.
    
        Name (input): The name of an existing or new link property. If this is an existing
            property, that property is modified; otherwise, a new property is added.
        DOF (input): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (input): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity if
            DOF(0) = True Fixed(1) = U2 fixity if DOF(1) = True Fixed(2) = U3 fixity if
            DOF(2) = True Fixed(3) = R1 fixity if DOF(3) = True Fixed(4) = R2 fixity if
            DOF(4) = True Fixed(5) = R3 fixity if DOF(5) = True
        Ke (input): This is an array of stiffness terms for the link property. There are 6
            terms in the array if the stiffness is uncoupled and 21 if it is coupled. The
            KeCoupled item indicates if the stiffness is coupled. If the stiffness is
            uncoupled: Ke(0) = U1 [F/L] Ke(1) = U2 [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL]
            Ke(4) = R2 [FL] Ke(5) = R3 [FL] If the stiffness is coupled: Ke(0) = U1U1 [F/L]
            Ke(1) = U1U2 [F/L] Ke(2) = U2U2 [F/L] Ke(3) = U1U3 [F/L] Ke(4) = U2U3 [F/L]
            Ke(5) = U3U3 [F/L] Ke(6) = U1R1 [F] Ke(7) = U2R1 [F] Ke(8) = U3R1 [F] Ke(9) =
            R1R1 [FL] Ke(10) = U1R2 [F] Ke(11) = U2R2 [F] Ke(12) = U3R2 [F] Ke(13) = R1R2
            [FL] Ke(14) = R2R2 [FL] Ke(15) = U1R3 [F] Ke(16) = U2R3 [F] Ke(17) = U3R3 [F]
            Ke(18) = R1R3 [FL] Ke(19) = R2R3 [FL] Ke(20) = R3R3 [FL]
        Ce (input): This is an array of damping terms for the link property. There are 6
            terms in the array if the damping is uncoupled and 21 if it is coupled. The
            CeCoupled item indicates if the damping is coupled. If the damping is uncoupled:
            Ce(0) = U1 [F/L] Ce(1) = U2 [F/L] Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2
            [FL] Ce(5) = R3 [FL] If the damping is coupled: Ce(0) = U1U1 [F/L] Ce(1) = U1U2
            [F/L] Ce(2) = U2U2 [F/L] Ce(3) = U1U3 [F/L] Ce(4) = U2U3 [F/L] Ce(5) = U3U3
            [F/L] Ce(6) = U1R1 [F] Ce(7) = U2R1 [F] Ce(8) = U3R1 [F] Ce(9) = R1R1 [FL]
            Ce(10) = U1R2 [F] Ce(11) = U2R2 [F] Ce(12) = U3R2 [F] Ce(13) = R1R2 [FL] Ce(14)
            = R2R2 [FL] Ce(15) = U1R3 [F] Ce(16) = U2R3 [F] Ce(17) = U3R3 [F] Ce(18) = R1R3
            [FL] Ce(19) = R2R3 [FL] Ce(20) = R3R3 [FL]
        dj2 (input): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (input): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        KeCoupled (input): This item is True if the link stiffness, Ke, is coupled. There
            are 21 terms in the Ke array if Ke is coupled; otherwise there are 6 terms.
        CeCoupled (input): This item is True if the link damping, Ce, is coupled. There are
            21 terms in the Ce array if Ce is coupled; otherwise there are 6 terms.
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, the program assigns a GUID to the property.
        """
        _r = self._raw.SetLinear(Name, DOF, Fixed, Ke, Ce, dj2, dj3, KeCoupled, CeCoupled, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.SetLinear falhou (ret={_r})".format(_r=_r))
        return None

    def SetMultiLinearElastic(self, Name: str, DOF: list[bool], Fixed: list[bool], NonLinear: list[bool], Ke: list[float], Ce: list[float], dj2: float, dj3: float, Notes: str = '', GUID: str = ''):
        """This function initializes a multilinear elastic-type link property. If this function is
        called for an existing link property, all items for the property are reset to their
        default value. The function returns zero if the property is successfully
        initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new link property. If this is an existing
            property then. that property is modified; otherwise, a new property is added.
        DOF (input): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (input): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (input): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1 has nonlinear properties
            NonLinear(4) = R2 has nonlinear properties NonLinear(5) = R3 has nonlinear
            properties The term NonLinear(n) applies only when DOF(n) = True and Fixed(n) =
            False.
        Ke (input): This is an array of effective stiffness terms for the link property. The
            effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (input): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        dj2 (input): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (input): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, the program assigns a GUID to the property.
        """
        _r = self._raw.SetMultiLinearElastic(Name, DOF, Fixed, NonLinear, Ke, Ce, dj2, dj3, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.SetMultiLinearElastic falhou (ret={_r})".format(_r=_r))
        return None

    def SetMultiLinearPlastic(self, Name: str, DOF: list[bool], Fixed: list[bool], NonLinear: list[bool], Ke: list[float], Ce: list[float], dj2: float, dj3: float, Notes: str = '', GUID: str = ''):
        """This function initializes a multilinear plastic-type link property. If this function is
        called for an existing link property, all items for the property are reset to their
        default values. The function returns zero if the property is successfully
        initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new link property. If this is an existing
            property, that property is modified; otherwise, a new property is added.
        DOF (input): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (input): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (input): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1 has nonlinear properties
            NonLinear(4) = R2 has nonlinear properties NonLinear(5) = R3 has nonlinear
            properties The term NonLinear(n) applies only when DOF(n) = True and Fixed(n) =
            False.
        Ke (input): This is an array of effective stiffness terms for the link property. The
            effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (input): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        dj2 (input): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (input): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, the program assigns a GUID to the property.
        """
        _r = self._raw.SetMultiLinearPlastic(Name, DOF, Fixed, NonLinear, Ke, Ce, dj2, dj3, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.SetMultiLinearPlastic falhou (ret={_r})".format(_r=_r))
        return None

    def SetMultiLinearPoints(self, Name: str, DOF: int, NumberPoints: int, F: list[float], D: list[float], MyType: int = 1, a1: float = 0, a2: float = 0, b1: float = 0, b2: float = 0, eta: float = 0):
        """This function sets the force-deformation data for a specified degree of freedom in
        multilinear elastic and multilinear plastic link properties. The function returns
        zero if the data is successfully assigned; otherwise it returns a nonzero value. To
        successfully apply this data to the indicated link property, the following
        conditions must be met: 1. The link property must be multilinear elastic or
        multilinear plastic. 2. The specified DOF must be active. 3. The specified DOF must
        not be fixed. 4. The specified DOF must be nonlinear.
    
        Name (input): The name of an existing multilinear elastic or multilinear plastic
            link property.
        DOF (input): This is 1, 2, 3, 4, 5 or 6, indicating the degree of freedom to which
            the multilinear points apply. 1 = U1 2 = U2 3 = U3 4 = R1 5 = R2 6 = R3
        NumberPoints (input): The number of foce-defomation points for the specified degree
            of freedom.
        F (input): This is an array, dimensioned to NumberPoints - 1, that includes the
            force at each point. When DOF is U1, U2 or U3, this is a force. When DOF is R1,
            R2 or R3. this is a moment. [F] if DOF <= 3, and [FL} if DOF > 3
        D (input): This is an array, dimensioned to NumberPoints - 1, that includes the
            displacement at each point. When DOF is U1, U2 or U3, this is a translation.
            When DOF is R1, R2 or R3, this is a rotation. [L] if DOF <= 3, and [rad] if DOF
            > 3
        MyType (input): This item applies only to multilinear plastic link properties. It is
            1, 2 or 3, indicating the hysteresis type. 1 = Kinematic 2 = Takeda 3 = Pivot
        a1 (input): This item applies only to multilinear plastic link properties that have
            a pivot hysteresis type (MyType = 3). It is the Alpha1 hysteresis parameter.
        a2 (input): This item applies only to multilinear plastic link properties that have
            a pivot hysteresis type (MyType = 3). It is the Alpha2 hysteresis parameter.
        b1 (input): This item applies only to multilinear plastic link properties that have
            a pivot hysteresis type (MyType = 3). It is the Beta1 hysteresis parameter.
        b2 (input): This item applies only to multilinear plastic link properties that have
            a pivot hysteresis type (MyType = 3). It is the Beta2 hysteresis parameter.
        eta (input): This item applies only to multilinear plastic link properties that have
            a pivot hysteresis type (MyType = 3). It is the Eta hysteresis parameter.
        """
        _r = self._raw.SetMultiLinearPoints(Name, DOF, NumberPoints, F, D, MyType, a1, a2, b1, b2, eta)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.SetMultiLinearPoints falhou (ret={_r})".format(_r=_r))
        return None

    def SetPDelta(self, Name: str, Value: list[float]):
        """This function assigns P-delta parameters to a link property. The function returns zero if
        the values are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link property.
        Value (input): This is an array of P-delta parameters. Value(0) = M2 P-delta to
            I-end of link as moment, M2I Value(1) = M2 P-delta to J-end of link as moment,
            M2J Value(2) = M3 P-delta to I-end of link as moment, M3I Value(3) = M3 P-delta
            to J-end of link as moment, M3J
        """
        _r = self._raw.SetPDelta(Name, Value)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.SetPDelta falhou (ret={_r})".format(_r=_r))
        return None

    def SetPlasticWen(self, Name: str, DOF: list[bool], Fixed: list[bool], NonLinear: list[bool], Ke: list[float], Ce: list[float], k: list[float], Yield: list[float], Ratio: list[float], exp: list[float], dj2: float, dj3: float, Notes: str = '', GUID: str = ''):
        """This function initializes a plastic Wen-type link property. If this function is called for
        an existing link property, all items for the property are reset to their default
        values. The function returns zero if the property is successfully initialized;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new link property. If this is an existing
            property, that property is modified; otherwise, a new property is added.
        DOF (input): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (input): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (input): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1 has nonlinear properties
            NonLinear(4) = R2 has nonlinear properties NonLinear(5) = R3 has nonlinear
            properties The term NonLinear(n) applies only when DOF(n) = True and Fixed(n) =
            False.
        Ke (input): This is an array of effective stiffness terms for the link property. The
            effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (input): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        k (input): This is an array of initial stiffness terms for the link property. The
            initial stiffness applies for nonlinear analyses. k(0) = U1 [F/L] k(1) = U2
            [F/L] k(2) = U3 [F/L] k(3) = R1 [FL] k(4) = R2 [FL] k(5) = R3 [FL] The term k(n)
            applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        Yield (input): This is an array of yield force terms for the link property. The
            yield force applies for nonlinear analyses. Yield(0) = U1 [F] Yield(1) = U2 [F]
            Yield(2) = U3 [F] Yield(3) = R1 [FL] Yield(4) = R2 [FL] Yield(5) = R3 [FL] The
            term Yield(n) applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n)
            = True.
        Ratio (input): This is an array of post-yield stiffness ratio terms for the link
            property. The post-yield stiffness ratio applies for nonlinear analyses. It is
            the post-yield stiffness divided by the initial stiffness. Ratio(0) = U1
            Ratio(1) = U2 Ratio(2) = U3 Ratio(3) = R1 Ratio(4) = R2 Ratio(5) = R3 The term
            Ratio(n) applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) =
            True.
        exp (input): This is an array of yield exponent terms for the link property. The
            yield exponent applies for nonlinear analyses. The yielding exponent that
            controls the sharpness of the transition from the initial stiffness to the
            yielded stiffness. exp(0) = U1 exp(1) = U2 exp(2) = U3 exp(3) = R1 exp(4) = R2
            exp(5) = R3 The term exp(n) applies only when DOF(n) = True, Fixed(n) = False
            and NonLinear(n) = True.
        dj2 (input): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (input): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, the program assigns a GUID to the property.
        """
        _r = self._raw.SetPlasticWen(Name, DOF, Fixed, NonLinear, Ke, Ce, k, Yield, Ratio, exp, dj2, dj3, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.SetPlasticWen falhou (ret={_r})".format(_r=_r))
        return None

    def SetRubberIsolator(self, Name: str, DOF: list[bool], Fixed: list[bool], NonLinear: list[bool], Ke: list[float], Ce: list[float], k: list[float], Yield: list[float], Ratio: list[float], dj2: float, dj3: float, Notes: str = '', GUID: str = ''):
        """This function initializes a rubber isolator-type link property. If this function is called
        for an existing link property, all items for the property are reset to their default
        value. The function returns zero if the property is successfully initialized;
        otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new link property. If this is an existing
            property, that property is modified; otherwise, a new property is added.
        DOF (input): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (input): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (input): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1,
            Not Used NonLinear(1) = U2 has nonlinear properties NonLinear(2) = U3 has
            nonlinear properties NonLinear(3) = R1, Not Used NonLinear(4) = R2, Not Used
            NonLinear(5) = R3, Not Used Note that this item is applicable only for degrees
            of freedom U2 and U3. For those degrees of freedom, the term NonLinear(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        Ke (input): This is an array of effective stiffness terms for the link property. The
            effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (input): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        k (input): This is an array of initial stiffness terms for the link property. The
            initial stiffness applies for nonlinear analyses. k(0) = U1, Not Used k(1) = U2
            [F/L] k(2) = U3 [F/L] k(3) = R1, Not Used k(4) = R2, Not Used k(5) = R3, Not
            Used Note that this item is applicable only for degrees of freedom U2 and U3.
            For those degrees of freedom, the term k(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        Yield (input): This is an array of yield force terms for the link property. The
            yield force applies for nonlinear analyses. Yield(0) = U1, Not Used Yield(1) =
            U2 [F] Yield(2) = U3 [F] Yield(3) = R1, Not Used Yield(4) = R2, Not Used
            Yield(5) = R3, Not Used The term Yield(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        Ratio (input): This is an array of post-yield stiffness ratio terms for the link
            property. The post-yield stiffness ratio applies for nonlinear analyses. It is
            the post-yield stiffness divided by the initial stiffness. Ratio(0) = U1, Not
            Used Ratio(1) = U2 Ratio(2) = U3 Ratio(3) = R1, Not Used Ratio(4) = R2, Not Used
            Ratio(5) = R3, Not Used The term Ratio(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        dj2 (input): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (input): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, the program assigns a GUID to the property.
        """
        _r = self._raw.SetRubberIsolator(Name, DOF, Fixed, NonLinear, Ke, Ce, k, Yield, Ratio, dj2, dj3, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.SetRubberIsolator falhou (ret={_r})".format(_r=_r))
        return None

    def SetSpringData(self, Name: str, DefinedForThisLength: float, DefinedForThisArea: float):
        """This function assigns length and area values to a link property that are used if the link
        property is specified in line and area spring assignments. The function returns zero
        if the values are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link property.
        DefinedForThisLength (input): The link property is defined for this length in a line
            (frame) spring. [L]
        DefinedForThisArea (input): The link property is defined for this area in an area
            spring. [L 2 ]
        """
        _r = self._raw.SetSpringData(Name, DefinedForThisLength, DefinedForThisArea)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.SetSpringData falhou (ret={_r})".format(_r=_r))
        return None

    def SetTCFrictionIsolator(self, Name: str, DOF: list[bool], Fixed: list[bool], NonLinear: list[bool], Ke: list[float], Ce: list[float], k: list[float], Slow: list[float], Fast: list[float], Rate: list[float], Radius: list[float], SlowT: list[float], FastT: list[float], RateT: list[float], kt: float, dis: float, dist: float, Damping: float, dj2: float, dj3: float, Notes: str = '', GUID: str = ''):
        """This function initializes a T/C friction isolator-type link property. If this function is
        called for an existing link property, all items for the property are reset to their
        default value. The function returns zero if the property is successfully
        initialized; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new link property. If this is an existing
            property, that property is modified; otherwise, a new property is added.
        DOF (input): This is a boolean array, dimensioned to 5, indicating if properties
            exist for a specified degree of freedom. DOF(0) = U1 DOF(1) = U2 DOF(2) = U3
            DOF(3) = R1 DOF(4) = R2 DOF(5) = R3
        Fixed (input): This is a boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        NonLinear (input): This is a boolean array, dimensioned to 5, indicating if
            nonlinear properties exist for a specified degree of freedom. NonLinear(0) = U1
            has nonlinear properties NonLinear(1) = U2 has nonlinear properties NonLinear(2)
            = U3 has nonlinear properties NonLinear(3) = R1, Not Used NonLinear(4) = R2, Not
            Used NonLinear(5) = R3, Not Used Note that this item is applicable only for
            degrees of freedom U1, U2 and U3. For those degrees of freedom, the term
            NonLinear(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ke (input): This is an array of effective stiffness terms for the link property. The
            effective stiffness applies for linear analyses. Ke(0) = U1 [F/L] Ke(1) = U2
            [F/L] Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term
            Ke(n) applies only when DOF(n) = True and Fixed(n) = False.
        Ce (input): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        k (input): This is an array of initial stiffness terms for the link property. The
            initial stiffness applies for nonlinear analyses. k(0) = U1 [F/L] k(1) = U2
            [F/L] k(2) = U3 [F/L] k(3) = R1, Not Used k(4) = R2, Not Used k(5) = R3, Not
            Used Note that this item is applicable only for degrees of freedom U1, U2 and
            U3. For those degrees of freedom, the term k(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        Slow (input): This is an array of the friction coefficient at zero velocity terms
            when U1 is in compression for the link property. This coefficient applies for
            nonlinear analyses. Slow(0) = U1, Not Used Slow(1) = U2 Slow(2) = U3 Slow(3) =
            R1, Not Used Slow(4) = R2, Not Used Slow(5) = R3, Not Used Note that this item
            is applicable only for degrees of freedom U2 and U3. For those degrees of
            freedom, the term Slow(n) applies only when DOF(n) = True, Fixed(n) = False and
            NonLinear(n) = True.
        Fast (input): This is an array of the friction coefficient at fast velocity terms
            when U1 is in compression for the link property. This coefficient applies for
            nonlinear analyses. Fast(0) = U1, Not Used Fast(1) = U2 Fast(2) = U3 Fast(3) =
            R1, Not Used Fast(4) = R2, Not Used Fast(5) = R3, Not Used Note that this item
            is applicable only for degrees of freedom U2 and U3. For those degrees of
            freedom, the term Fast(n) applies only when DOF(n) = True, Fixed(n) = False and
            NonLinear(n) = True.
        Rate (input): This is an array of the inverse of the characteristic sliding velocity
            terms when U1 is in compression for the link property. This item applies for
            nonlinear analyses. Rate(0) = U1, Not Used Rate(1) = U2 [s/L] Rate(2) = U3 [s/L]
            Rate(3) = R1, Not Used Rate(4) = R2, Not Used Rate(5) = R3, Not Used Note that
            this item is applicable only for degrees of freedom U2 and U3. For those degrees
            of freedom, the term Rate(n) applies only when DOF(n) = True, Fixed(n) = False
            and NonLinear(n) = True.
        Radius (input): This is an array of the radius of the sliding contact surface terms
            for the link property. Inputting 0 means there is an infinite radius, that is,
            the slider is flat. This item applies for nonlinear analyses. Radius(0) = U1,
            Not Used Radius(1) = U2 [L] Radius(2) = U3 [L] Radius(3) = R1, Not Used
            Radius(4) = R2, Not Used Radius(5) = R3, Not Used Note that this item is
            applicable only for degrees of freedom U2 and U3. For those degrees of freedom,
            the term Radius(n) applies only when DOF(n) = True, Fixed(n) = False and
            NonLinear(n) = True.
        SlowT (input): This is an array of the friction coefficient at zero velocity terms
            when U1 is in tension for the link property. This coefficient applies for
            nonlinear analyses. SlowT(0) = U1, Not Used SlowT(1) = U2 SlowT(2) = U3 SlowT(3)
            = R1, Not Used SlowT(4) = R2, Not Used SlowT(5) = R3, Not Used Note that this
            item is applicable only for degrees of freedom U2 and U3. For those degrees of
            freedom, the term SlowT(n) applies only when DOF(n) = True, Fixed(n) = False and
            NonLinear(n) = True.
        FastT (input): This is an array of the friction coefficient at fast velocity terms
            when U1 is in tension for the link property. This coefficient applies for
            nonlinear analyses. FastT(0) = U1, Not Used FastT(1) = U2 FastT(2) = U3 FastT(3)
            = R1, Not Used FastT(4) = R2, Not Used FastT(5) = R3, Not Used Note that this
            item is applicable only for degrees of freedom U2 and U3. For those degrees of
            freedom, the term FastT(n) applies only when DOF(n) = True, Fixed(n) = False and
            NonLinear(n) = True.
        RateT (input): This is an array of the inverse of the characteristic sliding
            velocity terms when U1 is in tension for the link property. This item applies
            for nonlinear analyses. RateT(0) = U1, Not Used RateT(1) = U2 [s/L] RateT(2) =
            U3 [s/L] RateT(3) = R1, Not Used RateT(4) = R2, Not Used RateT(5) = R3, Not Used
            Note that this item is applicable only for degrees of freedom U2 and U3. For
            those degrees of freedom, the term RateT(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        kt (input): The axial translational tension stiffness for the U1 degree of freedom.
            This item applies for nonlinear analyses. [F/L]
        dis (input): The U1 degree of freedom gap opening for compression. This item applies
            for nonlinear analyses. [L]
        dist (input): The U1 degree of freedom gap opening for tension. This item applies
            for nonlinear analyses. [L]
        Damping (input): The nonlinear damping coefficient used for the axial translational
            degree of freedom, U1. This item applies for nonlinear analyses. [F/L]
        dj2 (input): The distance from the J-End of the link to the U2 shear spring. This
            item applies only when DOF(1) = True. [L]
        dj3 (input): The distance from the J-End of the link to the U3 shear spring. This
            item applies only when DOF(2) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, the program assigns a GUID to the property.
        """
        _r = self._raw.SetTCFrictionIsolator(Name, DOF, Fixed, NonLinear, Ke, Ce, k, Slow, Fast, Rate, Radius, SlowT, FastT, RateT, kt, dis, dist, Damping, dj2, dj3, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.SetTCFrictionIsolator falhou (ret={_r})".format(_r=_r))
        return None

    def SetTriplePendulumIsolator(self, Name: str, dof: list[bool], Fixed: list[bool], Nonlinear: list[bool], Ke: list[float], Ce: list[float], K1: float, Damping: float, K: list[float], Slow: list[float], Fast: list[float], Rate: list[float], Radius: list[float], StopDist: list[float], HeightOut: float, HeightIn: float, dj2: float, dj3: float, Notes: str = '', GUID: str = ''):
        """This function initializes a Triple Pendulum Isolator type link property. If this function is
        called for an existing link property, then all items for the property are reset to
        their default value. The function returns zero if the property is successfully
        initialized, otherwise it returns a nonzero value.
    
        Name (input): The name of an existing or new link property. If this is an existing
            property, that property is modified; otherwise, a new property is added.
        Fixed (input): This is a Boolean array, dimensioned to 5, indicating if the
            specified degree of freedom is fixed (restrained). Fixed(0) = U1 fixity Fixed(1)
            = U2 fixity Fixed(2) = U3 fixity Fixed(3) = R1 fixity Fixed(4) = R2 fixity
            Fixed(5) = R3 fixity The term Fixed(n) applies only when DOF(n) = True.
        Ke (input): This is an array of effective stiffness terms for the link property. The
            effective stiffness applies for linear analyses, and also for nonlinear analysis
            for those DOF for which NonLinear(n) = False. Ke(0) = U1 [F/L] Ke(1) = U2 [F/L]
            Ke(2) = U3 [F/L] Ke(3) = R1 [FL] Ke(4) = R2 [FL] Ke(5) = R3 [FL] The term Ke(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        Ce (input): This is an array of effective damping terms for the link property. The
            effective damping applies for linear analyses. Ce(0) = U1 [F/L] Ce(1) = U2 [F/L]
            Ce(2) = U3 [F/L] Ce(3) = R1 [FL] Ce(4) = R2 [FL] Ce(5) = R3 [FL] The term Ce(n)
            applies only when DOF(n) = True and Fixed(n) = False.
        K1 (input): This is the axial compression stiffness for the U1 degree of freedom.
            This item applies for nonlinear analyses. [F/L]
        Damping (input): This is the nonlinear damping coefficient for the axial degree of
            freedom, U1, when it is in compression. This item applies for nonlinear
            analyses. [F/L]
        K (input): This is an array, dimensioned to 3, of initial nonlinear stiffness
            (before sliding) for each sliding surface. K(0) = for the outer top sliding
            surface [F/L] K(1) = for the outer bottom sliding surface [F/L] K(2) = for the
            inner top sliding surface [F/L] K(3) = for the inner bottom sliding surface
            [F/L] Note that this item is applicable for degrees of freedom U2 and U3 only.
            For those degrees of freedom, the term k(n) applies only when DOF(n) = True,
            Fixed(n) = False and NonLinear(n) = True.
        Slow (input): This is an array, dimensioned to 3, of the friction coefficient at
            zero velocity for each sliding surface when U1 is in compression. Slow(0) = for
            the outer top sliding surface Slow(1) = for the outer bottom sliding surface
            Slow(2) = for the inner top sliding surface Slow(3) = for the inner bottom
            sliding surface Note that this item is applicable for degrees of freedom U2 and
            U3 only. For those degrees of freedom, the term Slow(n) only applies when DOF(n)
            = True, Fixed(n) = False and NonLinear(n) = True.
        Fast (input): This is an array, dimensioned to 3, of the friction coefficient at
            fast velocity for each sliding surface when U1 is in compression. Fast(0) = for
            the outer top sliding surface Fast(1) = for the outer bottom sliding surface
            Fast(2) = for the inner top sliding surface Fast(3) = for the inner bottom
            sliding surface Note that this item is applicable for degrees of freedom U2 and
            U3 only. For those degrees of freedom, the term Fast(n) applies only when DOF(n)
            = True, Fixed(n) = False and NonLinear(n) = True.
        Rate (input): This is an array, dimensioned to 3, of the inverse of the
            characteristic sliding velocity for the Slow and Fast friction coefficients for
            each sliding surface. This item applies for nonlinear analyses. Rate(0) = for
            the outer top sliding surface [s/L] Rate(1) = for the outer bottom sliding
            surface [s/L] Rate(2) = for the inner top sliding surface [s/L] Rate(3) = for
            the inner bottom sliding surface [s/L] Note that this item is applicable for
            degrees of freedom U2 and U3 only. For those degrees of freedom, the term
            Rate(n) applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) =
            True.
        Radius (input): This is an array, dimensioned to 3, of the radius for each sliding
            surface. Inputting 0 means there is an infinite radius, that is, the slider is
            flat. This item applies for nonlinear analyses. Radius(0) = for the outer top
            sliding surface [L] Radius(1) = for the outer bottom sliding surface [L]
            Radius(2) = for the inner top sliding surface [L] Radius(3) = for the inner
            bottom sliding surface [L] Note that this item is applicable for degrees of
            freedom U2 and U3 only. For those degrees of freedom, the term Radius(n) applies
            only when DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        StopDist (input): This is an array, dimensioned to 3, of the amount of displacement
            allowed before hitting a stiff limit for each sliding surface. Inputting 0 means
            there is no stop. This item applies for nonlinear analyses. StopDist(0) = for
            the outer top sliding surface [L] StopDist(1) = for the outer bottom sliding
            surface [L] StopDist(2) = for the inner top sliding surface [L] StopDist(3) =
            for the inner bottom sliding surface [L] Note that this item is applicable for
            degrees of freedom U2 and U3 only . For those degrees of freedom, the term
            StopDist(n) applies only when DOF(n) = True, Fixed(n) = False and NonLinear(n) =
            True.
        HeightOut (input): This is the height (distance) between the outer sliding surfaces
            at zero displacement. [L] Note that this item is applicable for degrees of
            freedom U2 and U3 only. For those degrees of freedom, the term applies only when
            DOF(n) = True, Fixed(n) = False and NonLinear(n) = True.
        HeightIn (input): This is the height (distance) between the inner sliding surfaces.
            [L] Note that this item is applicable for degrees of freedom U2 and U3 only. For
            those degrees of freedom, the term applies only when DOF(n) = True, Fixed(n) =
            False and NonLinear(n) = True.
        dj2 (input): The distance from the J-End of the link to the U2 shear spring, that
            is, the center of the isolator. This item applies only when DOF(2) = True. [L]
        dj3 (input): The distance from the J-End of the link to the U3 shear spring, that
            is, the center of the isolator. This item applies only when DOF(3) = True. [L]
        Notes (input): The notes, if any, assigned to the property.
        GUID (input): The GUID (global unique identifier), if any, assigned to the property.
            If this item is input as Default, then the program assigns a GUID to the
            property.
        """
        _r = self._raw.SetTriplePendulumIsolator(Name, dof, Fixed, Nonlinear, Ke, Ce, K1, Damping, K, Slow, Fast, Rate, Radius, StopDist, HeightOut, HeightIn, dj2, dj3, Notes, GUID)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.SetTriplePendulumIsolator falhou (ret={_r})".format(_r=_r))
        return None

    def SetWeightAndMass(self, Name: str, w: float, m: float, R1: float, R2: float, R3: float):
        """This function assigns weight and mass values to a link property. The function returns zero
        if the values are successfully assigned; otherwise it returns a nonzero value.
    
        Name (input): The name of an existing link property.
        w (input): The weight of the link. [F]
        m (input): The translational mass of the link. [M]
        R1 (input): The rotational inertia of the link about its local 1 axis. [ML 2 ]
        R2 (input): The rotational inertia of the link about its local 2 axis. [ML 2 ]
        R3 (input): The rotational inertia of the link about its local 3 axis. [ML 2 ]
        """
        _r = self._raw.SetWeightAndMass(Name, w, m, R1, R2, R3)
        if _r != 0:
            raise Sap2000ApiError("SapModel.PropLink.SetWeightAndMass falhou (ret={_r})".format(_r=_r))
        return None


