import streamlit as st



st.title('User Registration Form')
if 'username' not in st.session_state:
    st.session_state.username=[]

form_one=st.form('Registration Form',clear_on_submit=True)
with form_one:
    
    username=st.text_input('Enter your username:')
    password=st.text_input('Enter your password:')
    gmail=st.text_input('Enter your mail-id:')
    age=st.number_input('Age:',max_value=50)
    gender=st.selectbox('Gender',['Male','Female'],None)
    college=st.selectbox('College Name',[ 
        "Indian Institute of Technology (IIT) Bombay",
        "Indian Institute of Technology (IIT) Delhi",
        "Indian Institute of Technology (IIT) Madras",
        "Indian Institute of Technology (IIT) Kharagpur",
        "Indian Institute of Technology (IIT) Kanpur",
        "National Institute of Technology (NIT) Trichy",
        "National Institute of Technology (NIT) Surathkal",
        "Birla Institute of Technology and Science (BITS) Pilani",
        "Vellore Institute of Technology (VIT)",
        "SRM Institute of Science and Technology"],None,accept_new_options=True)
    percentage_10=st.selectbox('Percentage %',[
        '90-100',
        '80-90',
        '70-80',
        '60-70',
        '50-60',
        'Below-60'
    ],None)
    rollno=st.text_input('Enter Your Register No of College:')

  
button=form_one.form_submit_button('Submit')
if username!='' and password!='' and age!=''and gender!=''and gmail!='' and college!='' and percentage_10!='' and rollno!='' :
    if button:
            st.write('Registration Successful!')
            x={
                'username':username,
                'password':password,
                'age':age,
                'gmail':gmail,
                'gender':gender,
                'college':college,
                'percentage_10':percentage_10,
                'rollno':rollno
            }
            # print(x)
            # st.write(x)

            if x:
                # st.session_state.username.append(x)
                if st.session_state.username:
                    exists=False
                    for i in st.session_state.username:
                         if i['username']==x['username']:
                            exists=True
                            break;

                    if exists:
                         st.write(f'{x['username']} already exists Try other!')

                    else:
                         st.session_state.username.append(x)
                        
                        #  st.write('Successfully Registered')
                else:
                    st.session_state.username.append(x)
                        
                    # st.write('Successfully Registered')
                                       
else:
    if button:
        st.write('Please fill all the fields')


st.write(st.session_state.username)

x={
'username':username,
'password':password,
'age':age,
'gmail':gmail,
'gender':gender,
'college':college,
'percentage_10':percentage_10,
'rollno':rollno               
}

st.dataframe(x)





