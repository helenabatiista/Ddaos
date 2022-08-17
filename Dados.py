import pandas as pd
import streamlit as st
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

# Titulo
st.write("""
temperatura do mar\n
App que utiliza machine Learning para prever possível temperatura do mar.\n
Fonte: PIMA - INDIA (Kaggle)
""")

#dataset
df = pd.read_csv("/content/Temperatura do Mar .csv")

#Cabecalho
st.subheader('Informações dos dados')


#Nome do usuario
user_input = st.sidebar.text_input('digite seu nome')


#dados de entrada
X = df. drop(['Outcome'])
Y = df[' Outcome: ],1)

#Esepara dados e treinamento e teste
X_train, X_test, y_train, y_test = train_test_split(x, Y, test size

#dados com a funcão
def get_user_dataO:
agosto  =st.sidebar.stider('temperatura' ,14.3,16.75)
setembro =st.sidebar.stider('temperatura',14.4,16.65)
outrobro =st.sidebar.slider('temperatura'13.1, 14.65)
novembro =st.sidebar.slider('temperatura'11.85,13.35 )
dezembro =st.sidebar.slider('temperatura' 10.1, 11.9)
janeiro =st.sidebar.slider('temperatura' 9.75, 10.35)
fevereiro =st.sidebar.slider('temperatura'9.2,19.3 )
março =st.sidebar.slider('temperatura' 8.6, 13.05)
abril =st.sidebar.slider('temperatura'9.6, 12.45)
maio =st.sidebar.slider('temperatura'10.5, 12.85)
junho =st.sidebar.slider('temperatura'10.55,13.9 )
julho =st.sidebar.slider('temperatura'12.4,17.4 )
agosto =st.sidebar.slider('temperatura'15.4 ,16.95)

      fatures = pd.DataFrane (user data, Index=(•])
      return features

user_input _variables = get_user data()

#Grafico
graf=st.bar_chart(user_input_variables)

st. subheader ('Dados')
st.write(user_input_variables)

dtc = DecisionTreeCtassiffer(eriterion='entropy', max_depht=3)
dtc.fit(X_train,y_train)


#Acuracia do modelo
st.subheader("Acuráciadonodelo")
st.write(accuracy_score(y_test,ate.predict(X_test))+180)


#aprevisao
prediction = dte.prediet(user_input_variables)

st. subheader ('Previsad':)
st.arite(prediction)