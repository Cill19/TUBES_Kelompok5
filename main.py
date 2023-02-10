#import library streamlit
import streamlit as st
#import streamlit option menu
from streamlit_option_menu import option_menu
#import pandas library
import streamlit.components as stc
import random
from itertools import cycle
from itertools import repeat
from itertools import count
import numpy as np
import itertools
import pandas as pd
import operator
from itertools import chain
from itertools import combinations
from itertools import permutations
from functools import reduce
#import plotly-express
import plotly.express as px
#import image
from PIL import Image

# horizontal Menu
selected2 = option_menu(None, ["Home","Materi","Terapan","Video","Referensi"],
    icons=["house-fill","book-half","lightbulb-fill","youtube", "journal-bookmark-fill"], menu_icon="cast", default_index=0, orientation="horizontal")

#selected case home
if (selected2 == 'Home') : 
    st.title('TUGAS BESAR PEMROGRAMAN FUNGSIONAL - WEB PEMBELAJARAN DASAR')
    st.header('KELOMPOK 5')
    st.image('ppgrup.jpeg')
    tab_titles = [
        "Ketua",
        "Anggota 1",
        "Anggota 2",
        "Anggota 3",
        ]
    tabs = st.tabs(tab_titles)
    
    with tabs[0]:
        st.markdown(":star: Nama : M. Nur Aqil Bahri")
        st.markdown(":fish: NIM : :blue[21102144]")
        st.image("Aqil.jpeg")

    with tabs[1]:
        st.markdown(":star: Nama : Rizal Adiyaksa Abdul Malik")
        st.markdown(":fish: NIM : :blue[21102312]")
        st.image("rizal.jpeg")

    with tabs[2]:
        st.markdown(":star: Nama : Deo Septry Wengy")
        st.markdown(":fish: NIM : :blue[21102146]")
        st.image("DEO.jpeg")

    with tabs[3]:
        st.markdown(":star: Nama : Ikhmal Bayu Pamungkas")
        st.markdown(":fish: NIM : :blue[21102129]")
        st.image("ikhmal.jpeg")

#selected case materi 
if (selected2 == 'Materi') : 
    st.header ('Materi Infinite Itertools - Count')
    
    st.markdown('Count() adalah fungsi python untuk     mengembalikan jumlah total elemen yang diberikan dalam sebuah string. perhitungan dimulai dari awal string sampai akhir. Dimungkinkan juga untuk menentukan indeks awal dan akhir dari tempat Anda ingin memulai pencarian.')

    st.text('Berikut contoh codingnya :')
#write the code
    code = '''iterator = (count(start  = 0, step = 2))

            print('Even LIst:',
                 list(next(iterator) for _ in range(5)))
        
        iterator = (count(start = 1, step = 2))

        print('Odd list:',
                 list(next(iterator)for _ in range(5)))'''
    st.code(code, language='python')
    code = '''Output :'''
    st.code(code, language='python')

    iterator = (count(start  = 0, step = 2))
    st.write('Even List:',
             list(next(iterator)for _ in range(5)))
    iterator = (count(start=1, step = 2))
    st.write('Odd list:',
             list(next(iterator)for _ in range(5)))

#materi
    st.header ('Materi Infinite Iterators - Cycle')    
    st.markdown('Cycle() adalah fungsi python yang akan mengulangi siklus nilai.')

#write the code
    code = '''from itertools import cycle
c=0
for i in cycle(‘Codespeedy’):
    print(i,end=’-’)
c+=1
if(c>15):
    break'''
    st.code(code,language='python')
    code ='''Output : 
C-o-d-e-s-p-e-e-d-y-C-o-d-e-s-p'''
    st.code(code,language='python')

#materi
    st.header ('Materi Infinite Iterators - Repeat')
    
    st.markdown('Fungsi repeat mengulang sebuah object, baik secara tak terbatas atau sebuah jumlah tertentu.')

#write the code
    code = '''import itertools    
print (list(itertools.repeat(25, 4)))'''
    st.code(code,language='python')
    code = '''Output :'''
    st.code(code,language='python')
    st.write(list(itertools.repeat(25,4)))
    

#materi
    st.header('Materi Finite Iterators - Accumulate')
    st.markdown('Fungsi ini mengembalikan urutan pengurangan :red[input iterable]. fungsi ini merupakan _higher-order functions_ dan dapat melakukan berbagai macam perhitungan')

#write the code
    code = '''import itertools
import operator
GFG = [1,2,3,4,5]
result = itertools.accumulate(GFG, operator.mul)
for each in result :
    print(each)'''
    
    st.code(code, language='python')
    code = '''Output'''
    st.code(code, language='python')

    GFG = [1,2,3,4,5]
    result = itertools.accumulate(GFG, operator.mul)
    for each in result :
        st.write(each)

#materi
    st.header('Materi Finite Iterators - Compress')
    st.markdown('funsgi ini :red[menyaring satu iterable] berdasarkan pada :red[kedua iterable] dengan nilai :red[_Boolean_]')

#write the code
    code = '''import itertools
impport operator
    
codes = ['C', 'C++', 'Java', 'Python']
selectors = [false, false, false, true]
    
best_Programing = itertools.compress(codes, selectors)
    
for each in best_Programing :
    print(each)'''
    
    st.code(code, language='python')

    code = '''Outputnya :'''
    st.code(code, language='python')

    codes = ['C', 'C++', 'Java', 'Python']
    selectors = [False, False, False, True]

    best_programing = itertools.compress(codes, selectors)
    for each in best_programing:
        st.write(each)


#materi
    st.header('Materi Finite Iterators - Chain')
    st.markdown('Fungsi ini menggabungkan beberapa iterable secara :red[Seriall]')

#write the code
    code = '''from itertools import chain
    odd = [1,3,5,7,9]
    even = [2,4,6,8,10]
    numbers = list(chain(odd, even))
    print(numbers)'''

    st.code(code, language='python')

    code = '''outputnya :'''

    st.code(code, language='python')

    odd = [1,3,5,7,9]
    even = [2,4,6,8,10]
    numbers = list(chain(odd, even))
    st.write(numbers)    
    
#materi
    st.header('Materi Infinite Iterators - Combinations')
    st.markdown('Fungsi _Combinations_ menerima argumen list dan sebuah bilangan r, dan mengembalikan daftar tuple dari semua kombinasi dengan panjang r yang mungkin')

    code = '''from itertools import combinations
letters = "Aqil"

a = combinations(letters, 3)
y = [''.join(i) for i in a]

print(y)'''

    st.code(code, language='python')

    code = '''Outputnya :'''

    st.code(code, language='python')

    letters = 'Aqil'
    a = combinations(letters, 3)
    y = [''.join(i) for i in a]
    st.write(y)

#materi
    st.header('Materi Infinite Iterators - Permutations')
    st.markdown('Untuk dapat melakukan permutasi di Python kita harus mengimpor fungsi permutations dari paket itertools. Fungsi permutasi ini menerima argumen list sebagai input dan mengembalikan sebuah list berisi semua permutasi yang mungkin')

    code = '''from itertools import permutations
a = "Aqil"
p = permutations(a)
 
for j in list(p):
  print(j)'''

    st.code(code, language='python')

    code = '''Outputnya :'''

    st.code(code, language='python')

    a = "Aqil"
    p = permutations(a)
    for j in list(p):
        st.write(j)
#materi
    st.header('Materi Infinite Iterators - Groupby')
    st.markdown('Fungsi ini mmenggunakan fungsi untuk menguraikan :red[satu iterable] ke urutan :red[iterable] diatas subset dari data inputan')

    code = '''import itertools
L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]
  
key_func = lambda x: x[0]
  
for key, group in itertools.groupby(L, key_func):
    print(key + " :", list(group))'''

    st.code(code, language='python')

    code = '''Outputnya :'''

    st.code(code, language='python')

    L = [("a", 1), ("a", 2), ("b", 3), ("b", 4)]
    key_func = lambda x: x[0]
    
    for key, group in itertools.groupby(L, key_func) :
        st.write(key + ": ", list(group))

#materi
    st.header('Materi Function Tools Partial')

    st.text('contoh coding')
    code = '''from functools import partial
    def func_multiply (x,y) :
        return x+y
    func_multiply (3,4)'''
    st.code(code, language='python')
    st.text('multiply 3,4 = 12')
    code = '''#membuat fungsi parsial
    partial_multiply = partial (func_multiply, 4)
    partial_multiply (4)'''
    st.code(code,language='python')
    st.text('nilai partial_multiply = 4,  partial_multiply,4 = 16')
    
    code = '''partial_multiply (3)'''
    st.code(code, language='python')
    code = '''outputnya : 
12'''
    st.code(code, language='python')
    

#materi
    st.header('Materi Function Tools Reduce')
    st.text('contoh coding')
    code = '''from functools import reduce
    
    data = [2,3,5,7,11,13,17,19,23,29]
    multiplier = lambda x,y : x*y
    reduce (multiplier, data)
    '''
    st.code(code, language='python')
    code = '''6469693230'''
    st.code(code, language='python')
    code = '''product = 1
    for x in data :
        product = product * x
    product'''
    st.code(code, language='python')
    code = '''6469693230'''
    st.code(code, language='python')
    code = '''form functools import reduce
    number = [[99, 47, 11, 6, 42, 102, 13, 9]
    f =  lambda a,b : a if a > b else b
    max_value = reduce (f, numbers)
    print (max_value)'''
    st.code(code, language='python')
    code = '''outputnya adalah : 
102'''
    st.code(code, language='python')


#selected case implementasi
if (selected2 == 'Terapan') : 

    #sidebar
    with st.sidebar :
        selected = option_menu ('Pilih materi',['Groupby Data Excel','Game Tebak Angka'],
        default_index=0)
    
    if(selected == 'Groupby Data Excel') :
        st.title('Implementasi Materi Groupby')
        st.text('Contoh Implementasi')

        st.text('download file excel dibawah untuk dimasukan di kolom upload')
        st.markdown('https://drive.google.com/drive/folders/1XgHGGBPw7H1AEsN_UQuCzsunlyMg5sBo?usp=sharing')
        st.text('Masukan File Excel untuk diurutkan dengan Groupby')

        uploaded_file = st.file_uploader('Upload disini', type='xlsx')
        if uploaded_file:
            st.markdown('-----')
            df = pd.read_excel(uploaded_file, engine='openpyxl')
            st.dataframe(df)
            groupby_column = st.selectbox(
                'apa yang mau di urutkan?',
                ('NAMA', 'KOTA ASAL'),
            )
            output_column = ['NAMA', 'KOTA ASAL']
            df_grouped = df.groupby(by=[groupby_column], as_index=False)[output_column].sum()
            st.dataframe(df_grouped)
          
    if(selected == 'Game Tebak Angka') :
        st.title('Implementasi Materi Cycle')
        st.text('')
        

if (selected2 == 'Video'):
    st.header('Video Pembelajaran')
    st.markdown('Berikut Video-video pembelajaran yang kami buat untuk mendukung pemahaman materi')
    st.markdown('<iframe width="560" height="315" src="https://www.youtube.com/embed/8SOM9GCCgRU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>',unsafe_allow_html=True)

    st.markdown('<iframe width="560" height="315" src="https://www.youtube.com/embed/WrWV090fUF8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>', unsafe_allow_html=True)

#selected Case Referensi
if (selected2 == 'Referensi') : 
    st.header ('Sumber Referensi')
    st.markdown('Berikut Video-video yang menjadi sumber referensi pembuatan web ini')
    st.markdown('<iframe width="560" height="315" src="https://www.youtube.com/embed/5Q1dgmogOMc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>',unsafe_allow_html=True)
    st.markdown('<iframe width="560" height="315" src="https://www.youtube.com/embed/0PBpAEGuNHM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>', unsafe_allow_html=True)