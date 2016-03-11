#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author:  Dominik Gresch <greschd@gmx.ch>
# Date:    20.02.2016 10:10:06 MST
# File:    test_move_convergence.py

from z2pack._core.surface._control import MoveConvergence
from z2pack._core._control_base import SurfaceControl

from monkeypatch_data import *

import z2pack
import pytest
import numpy as np

def test_base(test_ctrl_base):
    test_ctrl_base(MoveConvergence)
    assert issubclass(MoveConvergence, SurfaceControl)

@pytest.fixture(params=np.linspace(0.1, 0.5, 11))
def move_tol(request):
    return request.param

def test_single_update(move_tol, patch_max_move, patch_surface_data):
    mc = MoveConvergence(move_tol=move_tol)
    vals = [0.1, 0.2, 0.3, 0.4]
    #~ mc.update(TrivialSurfaceData(vals))
    mc.update(SurfaceData(vals))
    conv = [min(v1, v2) < move_tol for v1, v2 in zip(vals[:-1], vals[1:])]
    assert mc.converged == conv
