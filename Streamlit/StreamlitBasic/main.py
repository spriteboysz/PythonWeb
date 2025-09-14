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
    # 1. streamlit write()
    st.write('# 1. st.write()')
    st.write(pd.DataFrame({
        '第一列': [1, 2, 3, 4],
        '第二列': [5, 6, 7, 8]
    }))

    # 2. st.line_chart()
    st.write('# 2. st.line_chart()')
    st.line_chart(pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    ))

    # 3. st.map()
    st.write('# 3. st.map()')
    st.map(pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [22.54, 114.05],
        columns=['lat', 'lon']
    ))

    # 4. st.slider()
    st.write('# 4. st.slider()')
    st.write(x := st.slider('x'), 'squared is ', x * x)

    # 5. st.text_input()
    st.write('# 5. st.text_input()')
    st.text_input('your name', key='name')
    st.write(f'you input: {st.session_state.name}')

    # 6. st.checkbox()
    st.write('# 6. st.checkbox()')
    if st.checkbox('show DateFrame'):
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c']
        )
        st.line_chart(chart_data)

    # 7. st.selectbox()
    st.write('# 7. st.selectbox()')
    option = st.selectbox(
        'which number do you like best?',
        pd.DataFrame({
            '第一列': [1, 2, 3, 4]
        })['第一列']
    )
    st.write(f'you select: {option}')


if __name__ == '__main__':
    func()
