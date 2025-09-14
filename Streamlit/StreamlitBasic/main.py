#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-09-14 11:02
FileName: main.py
Description:
"""

import streamlit as st
import pandas as pd
import numpy as np


def func():
    # 1. streamlit write
    st.write('# 1. st.write')
    st.write(pd.DataFrame({
        '第一列': [1, 2, 3, 4],
        '第二列': [5, 6, 7, 8]
    }))

    st.write('# 2. st.line_chart')
    chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    )
    st.line_chart(chart_data)


if __name__ == '__main__':
    func()
