import streamlit as st
import time

def set_custom_css():
    """Set custom CSS for wider table, row borders, and hover effects."""
    st.markdown(
        """
        <style>
        .streamlit-expanderHeader {
            font-size: 0.2rem;
        }
        .block-container {
            max-width: 900px;
            padding: 0.2rem 0.2rem;
        }
        .stButton>button {
            width: 100%;
        }
        .table-header {
            display: flex;
            background-color: #f0f0f0;
            padding: 2px;
            font-weight: bold;
            border-bottom: 1px solid #ccc;
            margin-bottom: 2px;
        }
        .table-row {
            display: flex;
            padding: 0.2px;
            border: 1px solid lightgray;
            margin-bottom: 1px;
            transition: background-color 0.3s ease;
        }
        .table-row:hover {
            background-color: #f0f0f0;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# Define the correct passkey
correct_passkey = "class4vn"

def main():

    set_custom_css()
    
    # Create a state variable to keep track of whether the passkey has been validated
    if 'passkey_validated' not in st.session_state:
        st.session_state.passkey_validated = False

    # Define pages with their titles and file paths
    pages = {
        "Do Your Test": [
            ("List of all tests", "Do_Test/all_tests_list.py"),
        ],
        "Manage Your Test": [
            ("Edit current test", "Manage_Test/edit_test.py"),
            ("Backup tests data", "Manage_Test/backup_tests.py"),
        ]
    }

    # Sidebar navigation
    st.sidebar.title("Navigation")
    if st.sidebar.button('List of all tests'):
        st.session_state.page = 'test_list'
        st.session_state.url = 'Do_Test/all_tests_list.py'
        st.rerun()  
    if st.sidebar.button('Edit current test'):
        st.session_state.page  = 'input_passkey'
        st.rerun()
        # If passkey has not been validated, prompt the user to enter it
        # if st.session_state.passkey_validated == False:
        #     #st.session_state.page = None
        #     st.write("###Warning###")
        #     st.subheader("You need passkey to edit the test:")
        #     passkey = st.text_input('Enter passkey:',)
        #     if st.button('Submit'):
        #         if passkey.lower() == correct_passkey.lower():
        #             st.session_state.passkey_validated = True
        #             st.success("Passkey validated!")
        #             st.session_state.page = 'table'
        #             st.session_state.url = 'Manage_Test/edit_test.py'
        #             time.sleep(2)
        #             st.rerun()  # Reload the page to reflect the new selection
        #         else:
        #             st.session_state.passkey_validated = False
        #             st.warning("Wrong passkey. Please try again.")
        #             time.sleep(2)
        #             #st.session_state.page = 'test_list'
        #             #st.session_state.url = 'Do_Test/all_tests_list.py'
        #             #st.rerun()  # Reload the page to reflect the new selection
        
        # else:
        #     # If passkey has already been validated, process the request
        #     st.session_state.page = 'table'
        #     st.session_state.url = 'Manage_Test/edit_test.py'
        #     st.rerun()  # Reload the page to reflect the new selection
    
    if st.sidebar.button('Backup tests data'):
        st.session_state.page = 'backup'
        st.session_state.url = 'Manage_Test/backup_tests.py'
        st.rerun()  # Reload the page to reflect the new selection

    # Display the selected page
    if "page" in st.session_state:
        if st.session_state.page  == 'input_passkey':
            if st.session_state.passkey_validated == False:
                #st.session_state.page = None
                st.write("###Warning###")
                st.subheader("You need passkey to edit the test:")
                passkey = st.text_input('Enter passkey:')
                if st.button('Submit'):
                    if passkey.lower() == correct_passkey.lower():
                        st.session_state.passkey_validated = True
                        st.success("Passkey validated!")
                        st.session_state.page = 'table'
                        st.session_state.url = 'Manage_Test/edit_test.py'
                        time.sleep(2)
                        st.rerun()  # Reload the page to reflect the new selection
                else:
                    #st.session_state.passkey_validated = False
                    st.warning("Wrong passkey. Please try again.")
                    #time.sleep(2)
                    #st.session_state.page = 'test_list'
                    #st.session_state.url = 'Do_Test/all_tests_list.py'
                    #st.rerun()  # Reload the page to reflect the new selection
        
            else:
                # If passkey has already been validated, process the request
                st.session_state.page = 'table'
                st.session_state.url = 'Manage_Test/edit_test.py'
                st.rerun()  # Reload the page to reflect the new selection
        else:
            st.write(f"Selected Page: {st.session_state.page}") #IMPORTANT FOR DEBUG
            # Open the file with the correct encoding (usually UTF-8)
            with open(st.session_state.url, 'r', encoding='utf-8') as f:
                code = f.read()
            exec(code, globals())  # Execute the selected page
    else:
        st.session_state.page = 'test_list'
        st.session_state.url = 'Do_Test/all_tests_list.py'
        st.rerun()

if __name__ == "__main__":
    main()
