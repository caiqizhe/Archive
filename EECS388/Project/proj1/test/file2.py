#!/usr/bin/python
# -*- coding: utf-8 -*-
blob = """
           f��ΐJ|���;�@�L/6BDjQ4Nz�K��� ��N+���Sͽ�.�I��@=n��	��*q�l�V״�o����;3��Qe��~�*l	��K�E��d��f����k�ҿI+��`w~��R�@X[���"""
from hashlib import sha256
print sha256(blob).hexdigest()
