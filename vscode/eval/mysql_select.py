import streamlit as st
import pymysql
import pandas as pd
# streamlit run hello.py


con = pymysql.connect(host='localhost', user='llm', password='1111133333',
                      db='llm', charset='utf8', # 한글처리 (charset = 'utf8')
                      autocommit=True, # 결과 DB 반영 (Insert or update)
                      cursorclass=pymysql.cursors.DictCursor) # DB조회시 컬럼명을 동시에 보여줌


cur = con.cursor()
sql = "SELECT * FROM st_info" # customers 테이블 전체를 불러옴
cur.execute(sql)
rows = cur.fetchall()
con.close() # DB 연결 종료
# print(rows)                      
st_df = pd.DataFrame(rows)

st.table(st_df.head())            
st.write('Hello world!')


