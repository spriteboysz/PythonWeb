#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2025-09-14 11:02
FileName: main01.py
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

    # 2. st.line_chart
    st.write('# 2. st.line_chart')
    st.line_chart(pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c']
    ))

    # 3. st.map
    st.write('# 3. st.map')
    st.map(pd.DataFrame(
        np.random.randn(1000, 2) / [50, 50] + [22.54, 114.05],
        columns=['lat', 'lon']
    ))

    # 4. st.slider
    st.write('# 4. st.slider')
    st.write(x := st.slider('x'), 'squared is ', x * x)

    # 5. st.text_input
    st.write('# 5. st.text_input')
    st.text_input('your name', key='name')
    st.write(f'you input: {st.session_state.name}')

    # 6. st.checkbox
    st.write('# 6. st.checkbox')
    if st.checkbox('show DateFrame'):
        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=['a', 'b', 'c']
        )
        st.line_chart(chart_data)

    # 7. st.selectbox
    st.write('# 7. st.selectbox')
    option = st.selectbox(
        'which number do you like best?',
        pd.DataFrame({
            '第一列': [1, 2, 3, 4]
        })['第一列']
    )
    st.write(f'you select: {option}')

    # 8. st.sidebar
    st.write('# 8. st.sidebar')
    add_select = st.sidebar.selectbox(
        '通信方式选项：',
        ('微信', 'QQ', 'Phone', 'Email')
    )
    st.write(f'下拉选项: {add_select}')

    add_slider = st.sidebar.slider(
        '选择一个范围值：',
        0.0, 100.0, (25.0, 75.0)
    )
    st.write(f'值的范围：{add_slider}')

    # 9. st.radio
    st.write('# 9. st.radio')
    left, right = st.columns(2)
    left.button('Press me')
    with right:
        chosen = st.radio(
            '手机品牌',
            ('苹果', '华为', '小米')
        )
        st.write(f'you choose: {chosen}')

    # 10. st.progress
    st.write('# 10. st.progress')
    import time
    st.write('模拟长时间计算：')
    lastest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        lastest_iteration.text(f'Iteration: {i}')
        bar.progress(i + 1)
        time.sleep(0.1)
    st.write('finish!')

    # 11. st.file_uploader
    st.write('# 11. st.file_uploader')
    st.file_uploader(
        '上传数据集csv文件'
    )


if __name__ == '__main__':
    func()
