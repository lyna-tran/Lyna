import streamlit as st
# YOUR CODE HERE
st.title('Bé tập làm toán')
co1,co2,co3=st.columns(3)
with co1:
  a = st.number_input('a')
with co2:
  t = st.radio('Phép toán',('\+','\-','x',':'),horizontal=True)
with co3:
  b = st.number_input('b')
n = st.number_input('Nhập kết quả')
if st.button('Kiểm tra'):
  i=0
  if t =='/+':
    i=a+b
  elif t =='/-':
    i = a-b
  elif t=='x':
    i=a*b
  elif t ==':':
    i=a/b
    if i==n:
        st.text('Chính xác')
        st.balloon()
    else:
        st.write('Sai, đáp án đúng là',i)
        st.snow()