# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 19:53:10 2021

@author: SUDHA
"""
import language_tool_python
def check(text):
    tool = language_tool_python.LanguageTool('en-US')
    matches = tool.check(st)
    return matches







