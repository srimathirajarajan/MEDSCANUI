import streamlit as st
from streamlit_option_menu import option_menu
import snowflake.connector
from PIL import Image
import base64
from io import BytesIO

# Helper function to convert image to base64
def st_image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return img_str

# Set page configuration as the first Streamlit command
st.set_page_config(layout="wide")

# Path to background image
bg_image_path = "D:/CTS/background_log.jpg"  # Update this path as needed
bg_image = Image.open(bg_image_path)
bg_image_base64 = st_image_to_base64(bg_image)  # Converts image to base64

# Apply background to the entire page
st.markdown(f"""
    <style>
    .stApp {{
        background-image: url('data:image/png;base64,{bg_image_base64}');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;
    }}
    .login-container {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        background: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        max-width: 400px;
        width: 100%;
        z-index: 1;
    }}
    .login-container h1 {{
        margin-bottom: 1rem;
        font-size: 2rem;
        text-align: center;
    }}
    .login-container input {{
        width: 100%;
        padding: 0.8rem;
        margin-bottom: 1rem;
        border-radius: 5px;
        border: 1px solid #ddd;
    }}
    .login-container button {{
        width: 100%;
        padding: 0.8rem;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1rem;
    }}
    .login-container button:hover {{
        background-color: #0056b3;
    }}
    .message {{
        text-align: center;
        margin-top: 1rem;
        font-size: 1rem;
    }}
    .success {{
        color: green;
    }}
    .error {{
        color: red;
    }}
    </style>
""", unsafe_allow_html=True)

# Snowflake connection details
snowflake_conn_params = {
    'user': 'dheepika13',
    'password': 'Dheepika@13',
    'account': 'sx93925.ap-southeast-1',
    'warehouse': 'COMPUTE_WH',
    'database': 'LOGIN',
    'schema': 'logindetails'
}

def check_user_credentials(username, password):
    try:
        conn = snowflake.connector.connect(**snowflake_conn_params)
        cursor = conn.cursor()
        query = """
        SELECT * FROM users WHERE username=%s AND password=%s;
        """
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        return bool(result)
    except Exception as e:
        return f"Error checking credentials: {e}"
    finally:
        cursor.close()
        conn.close()

# Retrieve the username and password from the URL parameters
params = st.query_params
username = params.get("username", [""])[0]
password = params.get("password", [""])[0]

message = ""

# Handle sign-in logic if the form is submitted
if username and password:
    result = check_user_credentials(username, password)
    if result is True:
        message = "<div class='message success'>Welcome back!</div>"
    else:
        message = f"<div class='message error'>{result if isinstance(result, str) else 'Invalid credentials, please try again.'}</div>"

# Sign in page layout
st.markdown(f"""
    <div class="login-container">
        <h1>Sign In</h1>
        <form action="/" method="get">
            <input type="text" name="username" placeholder="Username" required/>
            <input type="password" name="password" placeholder="Password" required/>
            <button type="submit">Sign In</button>
        </form>
        {message}  <!-- Display the message here -->
    </div>
""", unsafe_allow_html=True)
