import streamlit as st
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
bg_image_path = "D:/CTS/background_signup.jpg"  # Update this path as needed
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
    .signup-container {{
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
    .signup-container h1 {{
        margin-bottom: 1rem;
        font-size: 2rem;
        text-align: center;
    }}
    .signup-container input {{
        width: 100%;
        padding: 0.8rem;
        margin-bottom: 1rem;
        border-radius: 5px;
        border: 1px solid #ddd;
    }}
    .signup-container select {{
        width: 100%;
        padding: 0.8rem;
        margin-bottom: 1rem;
        border-radius: 5px;
        border: 1px solid #ddd;
    }}
    .signup-container button {{
        width: 100%;
        padding: 0.8rem;
        background-color: #007bff;
        color: white;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1rem;
    }}
    .signup-container button:hover {{
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

def insert_user_to_snowflake(username, email, password, role):
    try:
        conn = snowflake.connector.connect(**snowflake_conn_params)
        cursor = conn.cursor()
        query = """
        INSERT INTO users (username, email, password, role)
        VALUES (%s, %s, %s, %s);
        """
        cursor.execute(query, (username, email, password, role))
        conn.commit()
        return "User registered successfully!"
    except Exception as e:
        return f"Error inserting user: {e}"
    finally:
        cursor.close()
        conn.close()

# Retrieve the username, email, password, and role from the URL parameters
params = st.query_params
username = params.get("username", [""])[0]
email = params.get("email", [""])[0]
password = params.get("password", [""])[0]
role = params.get("role", [""])[0]

message = ""

# Handle sign-up logic if the form is submitted
if username and email and password and role:
    result = insert_user_to_snowflake(username, email, password, role)
    if "Error" in result:
        message = f"<div class='message error'>{result}</div>"
    else:
        message = f"<div class='message success'>{result}</div>"

# Sign Up page layout
st.markdown(f"""
    <div class="signup-container">
        <h1>Sign Up</h1>
        <form action="/" method="get">
            <input type="text" name="username" placeholder="Create a Username" required/>
            <input type="email" name="email" placeholder="Email Address" required/>
            <input type="password" name="password" placeholder="Create a Password" required/>
            <select name="role" required>
                <option value="">Select Your Role</option>
                <option value="Patient">Patient</option>
                <option value="Doctor">Doctor</option>
                <option value="Admin">Admin</option>
            </select>
            <button type="submit">Sign Up</button>
        </form>
        {message}  <!-- Display the message here -->
    </div>
""", unsafe_allow_html=True)
