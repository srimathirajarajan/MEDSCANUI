import streamlit as st
from streamlit_option_menu import option_menu
import snowflake.connector
from PIL import Image
import base64
from io import BytesIO

# Function to handle page navigation
def navigate_to(page):
    st.session_state.current_page = page
    
def st_image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

def st_image_to_base64(img):
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return img_str
    
# Convert PIL image to base64
def st_image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()
    
# Function to convert image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()
    
def set_bg_image(image_file):
    encoded_string = image_to_base64(image_file)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/png;base64,{encoded_string});
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Scrollable sections content
def home_section():
    
    bg_image_path = "images/sam.png"  # Update this path as needed
    bg_image = Image.open(bg_image_path)
    bg_image_base64 = st_image_to_base64(bg_image)  # Converts image to base64
    
    st.markdown(
    f"""
    <style>
    @import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css'); /* Font Awesome CDN */

    /* Navbar */
    .navbar {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #007bff;
        z-index: 100;  /* Ensures the navbar is above the hero section */
        color: white;
        padding: 8px 0;
        display: flex;
        justify-content: space-between;  /* Space between the logo and the links */
        align-items: center;
        max-height: 100vh; /* 100% of the viewport height */
        overflow-y: auto;  /* Enables vertical scrolling */
    }}

    .navbar .logo {{
        margin-left: 20px;
        font-size: 24px;
        font-weight: bold;
    }}

    .navbar .nav-links {{
        display: flex;
    }}

    .navbar a {{
        color: white;
        padding: 14px 20px;
        text-decoration: none;
        text-align: center;
        display: inline-block;
    }}

    .navbar a:hover {{
        background-color: white;
        color: black;
    }}

    #homea {{
        background-color: #027BB0 ;
        border-color: #060606; 
        border-radius: 20px;
    }}

    .hero-section {{
        background: url('data:image/png;base64,{bg_image_base64}') top right no-repeat; 
        height: 88vh; 
        width: 210vh; 
        top: 0;
        background-size: cover; 
        margin-right: 180px;
        margin-left: -410px;
        padding-left: 150px;
        display: flex;   
        margin-top: -300px;
    }}

    .hero-content {{
        margin-top: 150px;  /* Reset margin-top to keep the content centered */
        padding-right: 0; 
    }}

    .hero-title {{
        margin-right: 80px;
        font-size: 30px;
    }}

    .hero-subtitle {{
        font-size: 32px;
        margin-right: 80px;
        margin-top: 20px;
    }}

    .custom-button1 {{
        font-size: 25px;
        padding: 5px;
        margin-right: 180px;
        background-color: #00AEEF;
        border: none;
        border-radius: 30px;
        color: white;
        display: inline-flex;
        align-items: center;
        overflow: hidden;
        margin-top: 40px;
    }}

    .custom-button1 span {{
        padding: 10px 30px;
    }}

    .content {{
        padding-top: 250px; /* Space for the navbar */
        text-align: center;
    }}

    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}
    
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<div id='home' class='content'>", unsafe_allow_html=True)

    st.markdown(f"""
        <section id="homea">
            <div class="hero-section">
                <div class="hero-content">
                    <h3 class="hero-title">WELCOME TO MEDSCAN!</h3>
                    <h3 class="hero-subtitle">Unlocking Smarter Healthcare</h3>
                    <div>
                        <button class="custom-button1">
                            <span>Chat Interface</span>
                        </button>
                    </div>
                </div>
            </div>
        </section>
    """, unsafe_allow_html=True)

    st.markdown("""
        <div class="navbar">
            <div class="logo">MEDSCAN</div>
            <div class="nav-links">
                <a href="#home">Home</a>
                <a href="#about">About Us</a>
                <a href="#services">Services</a>
                <a href="#contact">Contact</a>
                <a href="?page=signin">Sign In</a>
                <a href="?page=signup">Sign Up</a>
            </div>
        </div>
    """, unsafe_allow_html=True)



    
def about_us_section():
    image_path = "images/left.jpg"
    uploaded_image = Image.open(image_path)
    img_base64 = st_image_to_base64(uploaded_image)  # Convert image to base64
    
    st.markdown(
        """
        <style>
        /* Full-page container */
        .about{
            
            border-radius:10px;
            width:1520px;
            margin-left:-410px;
        }
        
        .container {
            height: 100vh; /* Reduced height */
            display: flex;
            align-items: center;
            justify-content: center;
        }

        /* Custom border under "About Us" */
        .custom-border1 {
            width: 100px;
            right:20px;
        }

        /* Styles for the icon containers */
        .icon-container {
            text-align: center;
            background-color: #e7f3ff;
            border-radius: 50%;
            padding: 25px 15px;
            height: 140px;
            width: 140px;
            margin: 0 15px; /* Adjusted margin for spacing */
            color: #007bff;
            transition: background-color 0.3s, color 0.3s, transform 0.3s; /* Smooth transition */
        }

        .icon-container:hover {
            background-color: #e0f7fa; /* Light blue background on hover */
            color: #007bff; /* Change text color on hover */
            transform: scale(1.05); /* Slightly enlarge the icon container */
        }

        /* Center text inside icon containers */
        .icon-container h6 {
            font-size: 14px;
            margin: 10px 0 0 0;
        }

        /* Flexbox layout for image and text */
        .about-us-container {
            display: flex;
            align-items: center; /* Center align vertically */
            justify-content: space-between;
            gap: 20px; /* Adjust space between image and text */
        }

        .image-content-container {
            display: flex;
            align-items: center; /* Vertically center the content */
            gap: 20px; /* Space between the image and the content */
        }

        /* Image styling */
        .about-us-image {
            border-radius: 15px;
            width: 70%; /* Adjust width as needed */
            height: 60%; /* Maintain aspect ratio */
            object-fit: cover;
            margin-right:-200px;
            margin-left:50px;
        }

        /* Text and icons section */
        .about-us-text {
            width: 60vw;
            text-align: left;
            margin-top:-100px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # HTML content with base64 image
    st.markdown(
        f"""
        <section class="about" id="abouta">
        <div class="container">
            <div class="about-us-container">
                <div class="image-content-container">
                    <div class="about-us-image">
                        <img src="data:image/png;base64,{img_base64}" alt="About Us Image" class="about-us-image"/>
                    </div>
                    <div class="about-us-text">
                        <h4 class="custom-border1">About Us</h4>
                        <h2>Effortless Access, Better Care: Your Medical Records, Just a Query Away</h2>
                        <p style="color: black;">Key Benefits</p>
                        <div style="display: flex; justify-content: space-around;">
                            <div class="icon-container">
                                <svg xmlns="http://www.w3.org/2000/svg" width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <polygon points="13 2 3 14 12 14 11 22 21 10 13 10 13 2"></polygon>
                                </svg>
                                <h6>Instant<br><small style="color: #007bff;">Data Retrieval</small></h6>
                            </div>
                            <div class="icon-container">
                                <svg xmlns="http://www.w3.org/2000/svg" width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M9 2H7a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V4a2 2 0 0 0-2-2h-2"></path>
                                    <rect x="9" y="2" width="6" height="4" rx="1" ry="1"></rect>
                                    <line x1="9" y1="10" x2="15" y2="10"></line>
                                    <line x1="9" y1="14" x2="15" y2="14"></line>
                                    <line x1="9" y1="18" x2="15" y2="18"></line>
                                </svg>
                                <h6>Patient-Centric<br><small style="color: #007bff;">Summaries</small></h6>
                            </div>
                            <div class="icon-container">
                                <svg xmlns="http://www.w3.org/2000/svg" width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <rect x="3" y="3" width="7" height="9"></rect>
                                    <rect x="14" y="3" width="7" height="5"></rect>
                                    <rect x="14" y="12" width="7" height="9"></rect>
                                    <rect x="3" y="16" width="7" height="5"></rect>
                                </svg>
                                <h6>Dynamic Dashboard<br><small style="color: #007bff;">for Visulization</small></h6>
                            </div>
                            <div class="icon-container">
                                <svg xmlns="http://www.w3.org/2000/svg" width="38" height="38" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                    <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
                                </svg>
                                <h6>Secure Health<br><small style="color: #007bff;">Records Access</small></h6>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <section>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<div id='about' class='content'>", unsafe_allow_html=True)

def services_section():
    # Services section
    st.markdown("<div id='services' class='content'>", unsafe_allow_html=True)

    # Inject CSS for service boxes and "Our Services" text
    st.markdown(
        """
        <style>
        .services-container {
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-left:-400px;
            margin-right:-400px;
            justify-content: center;
        }

        .service-box {
            background-color: #f8f9fa;
            border-radius: 15px;
            padding: 20px;
            width: 250px;
            text-align: center;
            transition: transform 0.3s ease, background-color 0.3s ease;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            display: flex;
            flex-direction: column;
            align-items: center;
            position:relative;
            top:-400px;
        }

        .service-box:hover {
            background-color: #007bff;
            transform: translateY(-10px);
            color: white;
        }

        .service-icon {
            font-size: 40px;
            margin-bottom: 10px;
        }

        .icon-container:hover {
            background-color: #e0f7fa;
            color: #007bff;
            transform: scale(1.05);
            transition: background-color 0.3s, color 0.3s, transform 0.3s;
        }

    .custom-border {
    font-size: 36px;
    color: #007bff;
    text-align: center;
    border-bottom: 4px solid #007bff;
    margin-bottom: 30px;
    width: 300px;
    margin-left: auto;
    margin-right: auto;
    position: relative;
    top: -400px; /* Adjust this value to move the text closer to the top */
    }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display services in a grid layout
    st.markdown(
        """
        <section id="services">
        <h4 class="custom-border">Our Services</h4>
        <div class="services-container">
            <div class="service-box">
                <div class="service-icon"><i class="fas fa-chart-line"></i></div>
                <h4>Visualization</h4>
                <p>Dynamic visualization of patient reports.</p>
            </div>
            <div class="service-box">
                <div class="service-icon"><i class="fas fa-file-invoice"></i></div>
                <h4>Report Summarization</h4>
                <p>Summarizing patient records based on request.</p>
            </div>
            <div class="service-box">
                <div class="service-icon"><i class="fas fa-database"></i></div>
                <h4>Data Retrieval</h4>
                <p>Seamless access to patient records via secure portal.</p>
            </div>
            <div class="service-box">
                <div class="service-icon"><i class="fas fa-lock"></i></div>
                <h4>Prompt Injection</h4>
                <p>Manipulates inputs to control AI-generated content.</p>
            </div>
        </div>
        </section>
        """,
        unsafe_allow_html=True
    )

    
def contact_page():
    image_path = "images/contact.jpg"  # Update this path as needed
    bg_image = Image.open(image_path)
    bg_image_base64 = st_image_to_base64(bg_image)  # Convert image to base64

    st.markdown(
        f"""
        <style>
            .contact-section {{
                background: url('data:image/png;base64,{bg_image_base64}') top right no-repeat; 
                background-size: cover; /* Cover the entire section */
                padding: 50px;
                border-radius: 10px;
                color: black;
                margin-top: -100px;
                width: 100%; /* Use percentage width for responsiveness */
                box-sizing: border-box; /* Include padding in width calculation */
            }}
            .contact-box {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                color: black;
                margin: auto;
                padding: 20px;
                background: rgba(0, 0, 0, 0.5); /* Semi-transparent background inside the box */
                border-radius: 10px;
                box-shadow: 0px 4px 20px rgba(0, 0, 0, 0.2); /* Shadow for depth */
                max-width: 1200px; /* Set max-width for better layout */
                width: 100%; /* Use percentage width for responsiveness */
            }}
            .contact-info p {{
                font-size: 20px; /* Adjusted font size */
                margin-bottom: 20px;
                line-height: 1.5;
                color: white;
                margin-right: 50px;
            }}
            .contact-info h4 {{
                color: white;
                margin-right: 10px;
            }}
            .contact-form input, .contact-form textarea {{
                width: 100%;
                padding: 10px;
                margin: 10px 0;
                border: none;
                border-radius: 5px;
            }}
            .contact-form h4 {{
                color: white;
                margin-right: 10px;
            }}
            .contact-form button {{
                background-color: #027bb0;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                transition: background-color 0.3s ease;
            }}
            .contact-form button:hover {{
                background-color: #534bff; /* Hover effect for button */
            }}
            .contact-info-icons {{
                display: flex;
                gap: 10px;
                font-size: 18px;
            }}
        </style>
        <div id="contact" class="contact-section">
            <div class="contact-box">
                <div class="contact-info">
                    <h4>Get In Touch!</h4>
                    <p>"The thread that links us to vital assistance is woven through each carefully shared detail."</p>
                </div>
                <div class="contact-form">
                    <h4>Send us a Message</h4>
                    <input type="text" placeholder="Your Name">                                                                                                                          
                    <input type="email" placeholder="Your Email">
                    <textarea placeholder="Your Message"></textarea>
                    <button>Send Message</button>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
      
    
def signup_page():
    # Path to background image
    bg_image_path = "images/background_signup.jpg"  # Path to your uploaded image
    bg_image = Image.open(bg_image_path)
    bg_image_base64 = st_image_to_base64(bg_image)  # Converts image to base64

    # Apply background to the entire page
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url('data:image/png;base64,{bg_image_base64}');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: top right;
            position: fixed;
            width: 100%;
            height: 100%;
        }}
        .icon-nurse {{
        font-size: 24px;
        color: #007bff;
        padding-right: 10px;
        padding-top: 5px;
       }}
        .signup-container h1 {{
            margin-bottom: 1rem;
            font-size: 2rem;
            text-align: center;
            font-weight: bold;
            top: -100px;
        }}
        .signup-container input {{
            width: 100%;
            padding: 0.8rem;
            margin-bottom: 1rem;
            border-radius: 5px;
            border: 1px solid #ddd;
            font-size: 1rem;
        }}
        .signup-container select {{
            width: 100%;
            padding: 0.8rem;
            margin-bottom: 1rem;
            border-radius: 5px;
            border: 1px solid #ddd;
            font-size: 1rem;
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
            font-weight: bold;
        }}
        .signup-container button:hover {{
            background-color: blue;
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

    # Form for user input
    with st.form(key='signup_form'):
        st.markdown("<div class='signup-container'>", unsafe_allow_html=True)
        st.markdown("<h1>Sign Up</h1>", unsafe_allow_html=True)
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type='password')
        role = st.selectbox("Select Your Role", ["", "Nurse", "Doctor", "Admin"])
        submit_button = st.form_submit_button(label='Sign Up')
        st.markdown("</div>", unsafe_allow_html=True)

        if submit_button:
            if username and email and password and role:
                result = insert_user_to_snowflake(username, email, password, role)
                if "Error" in result:
                    st.markdown(f"<div class='message error'>{result}</div>", unsafe_allow_html=True)
                else:
                    st.markdown(f"<div class='message success'>{result}</div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='message error'>All fields are required.</div>", unsafe_allow_html=True)
                
def forgot_password_page():
    st.title("Forgot Password")
    st.write("Enter your email address to receive a password reset link.")
    
    email = st.text_input("Email")
    submit_button = st.button("Send Reset Link")
    
    if submit_button:
        # Add logic to send the reset link to the provided email
        send_reset_link(email)
        st.success("A password reset link has been sent to your email address.")

def send_reset_link(email):
    # Logic to generate a reset token, save it to the database, and send the email
    pass

def reset_password_page():
    token = st.experimental_get_query_params().get("token", [""])[0]
    
    if not token:
        st.error("Invalid or missing token.")
        return
    
    st.title("Reset Password")
    new_password = st.text_input("New Password", type='password')
    confirm_password = st.text_input("Confirm Password", type='password')
    submit_button = st.button("Reset Password")
    
    if submit_button:
        if new_password == confirm_password:
            # Add logic to verify the token and update the password in the database
            reset_password(token, new_password)
            st.success("Your password has been successfully reset.")
        else:
            st.error("Passwords do not match.")

def reset_password(token, new_password):
    # Logic to verify the token and update the password
    pass

# Helper function to convert image to base64 (used in the background image)
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

def display_login_as_page():
    st.title("Select Your Role")
    
    # Set the background image
    set_bg_image('images/background_login.jpg')  # Replace with the path to your background image
    
    # Create three columns for aligning buttons
    col1, col2, col3 = st.columns(3)

    # Buttons for each role
    with col1:
        st.image("images/nurse.png", use_column_width=True)
        if st.button("Sign in as Nurse"):   
           st.query_params.from_dict({"page": "role_selection", "role": "nurse"})

    with col2:
        st.image("images/doctor.png", use_column_width=True)
        if st.button("Sign in as Doctor"):
           st.query_params.from_dict({"page": "role_selection", "role": "doctor"})

    with col3:
        st.image("images/office assistant.png", use_column_width=True)
        if st.button("Sign in as Admin"):
           st.query_params.from_dict({"page": "role_selection", "role": "admin"})

    # Display the login form based on the selected role
    if "page" in st.session_state:
        if st.session_state.page == "nurse_login":
            display_nurse_login()
        elif st.session_state.page == "doctor_login":
            display_doctor_login()
        elif st.session_state.page == "admin_login":
            display_admin_login()
        else:
            st.write("Please select a role.")
            
# Function to set the background image
def set_bg_image(image_file):
    with open(image_file, "rb") as img_file:
        encoded_string = base64.b64encode(img_file.read()).decode()
        
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/jpeg;base64,{encoded_string});
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )


def check_user_credentials(username, password, role):
    snowflake_conn_params = {
        'user': 'dheepika13',
        'password': 'Dheepika@13',
        'account': 'sx93925.ap-southeast-1',
        'warehouse': 'COMPUTE_WH',
        'database': 'LOGIN',
        'schema': 'logindetails'
    }
    
    try:
        conn = snowflake.connector.connect(**snowflake_conn_params)
        cursor = conn.cursor()
        
        # Check role first
        role_query = """
        SELECT * FROM users WHERE username=%s AND role=%s;
        """
        cursor.execute(role_query, (username, role))
        role_result = cursor.fetchone()
        
        if not role_result:
            return "Role does not match or user does not exist."
        
        # Check credentials if role is valid
        credentials_query = """
        SELECT * FROM users WHERE username=%s AND password=%s AND role=%s;
        """
        cursor.execute(credentials_query, (username, password, role))
        credentials_result = cursor.fetchone()
        
        if credentials_result:
            return True
        else:
            return "Invalid credentials, please try again."
    except Exception as e:
        return f"Error checking credentials: {e}"
    finally:
        cursor.close()
        conn.close()

# Function to convert image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

def display_nurse_login():
    st.title("Nurse Login")
    
    # Load images
    bg_image_path = "images/background_log.jpg"
    icon_image_path = "images/nurse.png"

    # Ensure images exist at the provided paths
    try:
        bg_image = Image.open(bg_image_path)
        icon_image = Image.open(icon_image_path)
    except FileNotFoundError as e:
        st.error(f"Image file not found: {e}")
        return

    # Convert images to base64
    bg_image_base64 = image_to_base64(bg_image_path)
    nurse_icon_base64 = image_to_base64(icon_image_path)

    # Apply background to the entire page
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url('data:image/png;base64,{bg_image_base64}');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
            position: fixed;
            width: 100%;
            height: 100%;
        }}
        
        .icon {{
            display: flex;
            justify-content: center;
            width: 100%;
            margin-bottom: 1rem;
        }}
        .signin-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 2rem;
            background: rgba(255, 255, 255, 0.9); /* Slightly opaque white background for better readability */
            border-radius: 10px;
        }}
        .signin-container h1 {{
            margin-bottom: 1rem;
            font-size: 2rem;
            text-align: center;
            font-weight: bold;
        }}
        .signin-container input {{
            width: 100%;
            padding: 0.8rem;
            margin-bottom: 1rem;
            border-radius: 5px;
            border: 1px solid #ddd;
            font-size: 1rem;
        }}
        .signin-container select {{
            width: 100%;
            padding: 0.8rem;
            margin-bottom: 1rem;
            border-radius: 5px;
            border: 1px solid #ddd;
            font-size: 1rem;
        }}
        .signin-container button {{
            width: 100%;
            padding: 0.8rem;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
            font-weight: bold;
        }}
        .signin-container button:hover {{
            background-color: blue;
        }}
        .icon {{
            margin-bottom: 1rem;
        }}
        .icon img {{
            width: 100px; /* Adjust width as needed */
            height: auto; /* Maintain aspect ratio */
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
            SELECT * FROM users WHERE username=%(username)s AND password=%(password)s ;
            """
            cursor.execute(query, {'username': username, 'password': password, })
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
    if st.session_state.get("username") and st.session_state.get("password"):
        username = st.session_state["username"]
        password = st.session_state["password"]
        result = check_user_credentials(username, password)
        if result is True:
            st.session_state.current_page = "home"  # Navigate to home
        else:
            message = f"<div class='message error'>{result if isinstance(result, str) else 'Invalid credentials, please try again.'}</div>"
            
    # Sign in page layout
    with st.form(key='signin_form'):
        st.markdown("<div class='signin-container'>", unsafe_allow_html=True)
        st.markdown(f"<div class='icon'><img src='data:image/png;base64,{nurse_icon_base64}' alt='Doctor Icon'/></div>", unsafe_allow_html=True)
        username_input = st.text_input("Username", value=username)
        password_input = st.text_input("Password", type='password', value=password)
        
        # Add the "Forgot Password" link
        st.markdown("""
        <div class="forgot-password">
            <a href="?page=forgot_password">Forgot Password?</a>
        </div>
        """, unsafe_allow_html=True)
        submit_button = st.form_submit_button(label='Sign In')

        if submit_button:
            result = check_user_credentials(username_input, password_input)
            if result is True:
                st.session_state.current_page = "home"  # Navigate to home
                message = "<div class='message success'>Welcome back!</div>"
            else:
                message = f"<div class='message error'>{result if isinstance(result, str) else 'Invalid credentials, please try again.'}</div>"

        st.markdown("</div>", unsafe_allow_html=True)

    if message:
        st.markdown(message, unsafe_allow_html=True)


def display_doctor_login():
    st.title("Doctor Login")
    
    # Load images
    bg_image_path = "images/background_log.jpg"
    icon_image_path = "images/doctor.png"

    # Ensure images exist at the provided paths
    try:
        bg_image = Image.open(bg_image_path)
        icon_image = Image.open(icon_image_path)
    except FileNotFoundError as e:
        st.error(f"Image file not found: {e}")
        return

    # Convert images to base64
    bg_image_base64 = image_to_base64(bg_image_path)
    doctor_icon_base64 = image_to_base64(icon_image_path)

    # Apply background to the entire page
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url('data:image/png;base64,{bg_image_base64}');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: top right;
            position: fixed;
            width: 100%;
            height: 100%;
        }}
        .icon {{
            display: flex;
            justify-content: center;
            width: 100%;
            margin-bottom: 1rem;
        }}
        .icon img {{
            width: 120px; /* Adjust width as needed */
            height: auto; /* Maintain aspect ratio */
        }}
        .signin-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
            padding: 2rem;
            background: rgba(255, 255, 255, 0.9); /* Slightly opaque white background for better readability */
            border-radius: 10px;
        }}
        .signin-container h1 {{
            margin-bottom: 1rem;
            font-size: 2rem;
            text-align: center;
            font-weight: bold;
        }}
        .signin-container input {{
            width: 100%;
            padding: 0.8rem;
            margin-bottom: 1rem;
            border-radius: 5px;
            border: 1px solid #ddd;
            font-size: 1rem;
        }}
        .signin-container select {{
            width: 100%;
            padding: 0.8rem;
            margin-bottom: 1rem;
            border-radius: 5px;
            border: 1px solid #ddd;
            font-size: 1rem;
        }}
        .signin-container button {{
            width: 100%;
            padding: 0.8rem;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
            font-weight: bold;
        }}
        .signin-container button:hover {{
            background-color: blue;
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
            SELECT * FROM users WHERE username=%(username)s AND password=%(password)s ;
            """
            cursor.execute(query, {'username': username, 'password': password, })
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
    if st.session_state.get("username") and st.session_state.get("password"):
        username = st.session_state["username"]
        password = st.session_state["password"]
        result = check_user_credentials(username, password)
        if result is True:
            st.session_state.current_page = "home"  # Navigate to home
            st.experimental_rerun()  # Refresh the page to navigate
        else:
            message = f"<div class='message error'>{result if isinstance(result, str) else 'Invalid credentials, please try again.'}</div>"
            
    # Sign in page layout
    with st.form(key='signin_form'):
        st.markdown("<div class='signin-container'>", unsafe_allow_html=True)
        st.markdown(f"<div class='icon'><img src='data:image/png;base64,{doctor_icon_base64}' alt='Doctor Icon'/></div>", unsafe_allow_html=True)
        username_input = st.text_input("Username", value=username)
        password_input = st.text_input("Password", type='password', value=password)
        
        # Add the "Forgot Password" link
        st.markdown("""
        <div class="forgot-password">
            <a href="?page=forgot_password">Forgot Password?</a>
        </div>
        """, unsafe_allow_html=True)
        submit_button = st.form_submit_button(label='Sign In')

        if submit_button:
            result = check_user_credentials(username_input, password_input)
            if result is True:
                st.session_state.current_page = "home"  # Navigate to home
                message = "<div class='message success'>Welcome back!</div>"
                
            else:
                message = f"<div class='message error'>{result if isinstance(result, str) else 'Invalid credentials, please try again.'}</div>"

        st.markdown("</div>", unsafe_allow_html=True)

    if message:
        st.markdown(message, unsafe_allow_html=True)
        
def admin_choice():
    # Function to convert image to base64
    def image_to_base64(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    # Function to set background image
    def set_bg_image(image_file):
        encoded_string = image_to_base64(image_file)
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url(data:image/png;base64,{encoded_string});
                background-size: cover;
                background-repeat: no-repeat;
                background-attachment: fixed;
                background-position: center;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    # Set the background image
    set_bg_image("images/new_pic.jpg")

    # Main function for the app
    st.title("Dashboard and Chat Interface")

    # CSS for hover effect, text boxes, and buttons
    st.markdown(
        """
        <style>
        .hover-container {
            text-align: center;
            margin-top: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            background-color: #f0f0f0;
            padding: 10px;
            min-height: 300px; /* Ensure both containers have the same minimum height */
        }
        .hover-container:hover {
            opacity: 0.7;
            transition: opacity 0.3s ease-in-out;
        }
        .hover-container img {
            width: 100%;
            border-radius: 5px;
        }
        .hover-container p {
            margin: 0;
            font-size: 16px;
            font-weight: bold;
            padding: 5px;
        }
        .stButton>button {
            color: white;
            background-color: #007bff;
            border: none;
            border-radius: 3px;
            font-size: 12px;
            font-weight: bold;
            cursor: pointer;
            padding: 5px 10px;
            transition: background-color 0.3s ease-in-out, transform 0.3s ease-in-out; /* Add transition for hover effect */
        }
        .stButton>button:hover {
            background-color: #0056b3;
            transform: scale(1.05); /* Slightly enlarge the button on hover */
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Create two columns for the dashboard and chat interface
    col1, col2 = st.columns(2)

    # Use a container to group the images and their descriptions
    with st.container():
        # Dashboard column
        with col1:
            st.header("Dashboard")

            # Add dashboard image and text box with hover effect
            st.markdown(
                f"""
                <div class="hover-container">
                    <img src="data:image/png;base64,{image_to_base64("D:/CTS/dashboard.jpg")}" alt="Dashboard Image">
                    <p>Dashboard</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Add content below the box
            st.markdown(
                """
                <div>
                    <p>The Dashboard provides an overview of data visualizations.
                    It helps users monitor performance, track trends, and make informed decisions.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            # "More" button for the dashboard
            if st.button("Real-Time Insights ➜", key="dashboard"):
                st.write("More information about the Dashboard...")

        # Chat interface column
        with col2:
            st.header("Chat Interface")

            # Add chat image and text box with hover effect
            st.markdown(
                f"""
                <div class="hover-container">
                    <img src="data:image/png;base64,{image_to_base64("D:/CTS/chat.jpg")}" alt="Chat Interface Image">
                    <p>Chat Interface</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Add content below the box
            st.markdown(
                """
                <div>
                    <p>The Chat Interface enables real-time communication between users and the system.
                    It facilitates quick responses.</p>
                </div>
                """,
                unsafe_allow_html=True
            )

            # "More" button for the chat interface
            if st.button("Chat Interface ➜", key="chat"):
                st.write("More information about the Chat Interface...")


def display_admin_login():
    st.title("Admin Login")

    # Load images
    bg_image_path = "images/background_log.jpg"
    icon_image_path = "images/office assistant.png"
    
    bg_image = Image.open(bg_image_path)
    icon_image = Image.open(icon_image_path)

    # Convert images to base64
    bg_image_base64 = st_image_to_base64(bg_image)
    admin_icon_base64 = st_image_to_base64(icon_image)

    # Apply background to the entire page
    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url('data:image/png;base64,{bg_image_base64}');
            background-size: cover;
            background-repeat: no-repeat;
            background-position: top right;
            position: fixed;
            width: 100%;
            height: 100%;
        }}
        .icon {{
            display: flex;
            justify-content: center;
            width: 100%;
            margin-bottom: 1rem;
        }}
        .icon img {{
            width: 150px;  /* Set the width of the icon */
            height: auto;  /* Maintain the aspect ratio */
        }}
        .signin-container h1 {{
            margin-bottom: 1rem;
            font-size: 2rem;
            text-align: center;
            font-weight: bold;
        }}
        .signin-container input {{
            width: 100%;
            padding: 0.8rem;
            margin-bottom: 1rem;
            border-radius: 5px;
            border: 1px solid #ddd;
            font-size: 1rem;
        }}
        .signin-container select {{
            width: 100%;
            padding: 0.8rem;
            margin-bottom: 1rem;
            border-radius: 5px;
            border: 1px solid #ddd;
            font-size: 1rem;
        }}
        .signin-container button {{
            width: 100%;
            padding: 0.8rem;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
            font-weight: bold;
        }}
        .signin-container button:hover {{
            background-color: blue;
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
            SELECT * FROM users WHERE username=%(username)s AND password=%(password)s;
            """
            cursor.execute(query, {'username': username, 'password': password})
            result = cursor.fetchone()
            return bool(result)
        except Exception as e:
            raise Exception(f"Error checking credentials: {e}")
        finally:
            cursor.close()
            conn.close()

    # Retrieve the username and password from the URL parameters
    params = st.query_params
    username = params.get("username", [""])[0]
    password = params.get("password", [""])[0]

    # Initialize message
    message = ""
    
    # Handle sign-in logic if the form is submitted
    if st.session_state.get("username") and st.session_state.get("password"):
        username = st.session_state["username"]
        password = st.session_state["password"]
        try:
            result = check_user_credentials(username, password)
            if result:
                st.query_params.from_dict({"page": "admin_choice"})
                st.experimental_rerun()  # Refresh the page to navigate
                return "Login success"
            else:
                message = "<div class='message error'>Invalid credentials, please try again.</div>"
                return "Login failed"
        except Exception as e:
            message = f"<div class='message error'>{e}</div>"
            return "Login failed"
            
    # Sign in page layout
    # Form for user input
    with st.form(key='signin_form'):
        st.markdown("<div class='signin-container'>", unsafe_allow_html=True)
        st.markdown(f"<div class='icon'><img src='data:image/png;base64,{admin_icon_base64}' alt='Admin Icon'/></div>", unsafe_allow_html=True)
        username_input = st.text_input("Username", value=username)
        password_input = st.text_input("Password", type='password', value=password)
        # Add the "Forgot Password" link
        st.markdown("""
        <div class="forgot-password">
            <a href="?page=forgot_password">Forgot Password?</a>
        </div>
        """, unsafe_allow_html=True)
        submit_button = st.form_submit_button(label='Sign In')

        # Update the message after the form is submitted
        if submit_button:
            try:
                result = check_user_credentials(username_input, password_input)
                if result:
                    st.query_params.from_dict({"page": "admin_choice"})
                    st.experimental_rerun()  # Refresh the page to navigate
                    message = "<div class='message success'>Welcome back!</div>"
                    return "Login success"
                else:
                    message = "<div class='message error'>Invalid credentials, please try again.</div>"
                    return "Login failed"
            except Exception as e:
                message = f"<div class='message error'>{e}</div>"
                return "Login failed"

        st.markdown("</div>", unsafe_allow_html=True)

    # Display message if needed
    if message:
        st.markdown(message, unsafe_allow_html=True)

    # Return default message if no specific message is set
    return "No action taken"

if "page" not in st.session_state:
    st.session_state.page = ""

       
def footer():   
   # Footer page
   st.markdown("""
    <style>
    .footer {
    background-color: #027BB0;
    color: white;
    padding: 10px;
    position: relative;
    left: -420px;
    bottom: 0;
    text-align: center;
    margin-right:-870px;
    margin-bottom:-200px; 
    margin-top:100px;
    }
    .footer-columns {
    display: flex;
    justify-content: space-around;
    margin-bottom: 20px;
    }
    .footer-column {
    flex: 1;
    padding: 0 10px;
    }
    .footer-column h4 {
    border-bottom: 2px solid #00A9DF;
    padding-bottom: 10px;
    margin-bottom: 10px;
    }
    .footer-column a {
    color: white;
    text-decoration: none;
    display: block;
    margin: 5px 0;
    }
    .footer-column a:hover {
    color: #00A9DF;
    }
    .footer-newsletter input[type="email"] {
    padding: 8px;
    margin-right: 10px;
    border-radius: 4px;
    border: none;
    }
    .footer-newsletter button {
    background-color: #00A9DF;
    color: white;
    border: none;
    padding: 8px 16px;
    border-radius: 4px;
    cursor: pointer;
    }
    .footer-newsletter button:hover {
    background-color: #007799;
    }
    .footer-social-icons {
    display: flex;
    justify-content: center;
    gap: 10px;  /* Adjust this for spacing between icons */
    margin-top: 10px;
    }

    .footer-social-icons a {
        color: white;
        text-decoration: none;
        font-size: 24px;
    }

    .footer-social-icons a:hover {
        color: #00A9DF;
    }

    .footer-bottom {
        border-top: 1px solid #FFFFFF;
        padding-top: 10px;
    }
    </style>
    <div class="footer">
            <div class="footer-columns">
            <div class="footer-column">
                <h4>GET IN TOUCH</h4>
                <p>SRI MANAKULA VINAYAGAR ENGINEERING COLLEGE</p>
                <p>📍 Madagadipet </p>
                <p>📧 smvec@ac.in</p>
                <p>📞 +012 345 67890</p>
            </div>
            <div class="footer-column">
                <h4>QUICK LINKS</h4>
                <a href="#">Home</a>
                <a href="#">About Us</a>
                <a href="#">Our Services</a>
                <a href="#">Contact Us</a>
            </div>
            <div class="footer-column">
                <h4>POPULAR LINKS</h4>
                <a href="#">Home</a>
                <a href="#">About Us</a>
                <a href="#">Our Services</a>
                <a href="#">Contact Us</a>
            </div>
            <div class="footer-column">
                <h4>NEWSLETTER</h4>
                <form class="footer-newsletter">
                    <input type="email" placeholder="Your Email Address"><br>
                    <button type="submit">Sign Up</button>
                </form>
                <h4>Follow Us</h4>
                <div class="footer-social-icons">
                    <a href="#"><i class="fab fa-twitter"></i></a>
                    <a href="#"><i class="fab fa-facebook-f"></i></a>
                    <a href="#"><i class="fab fa-linkedin-in"></i></a>
                    <a href="#"><i class="fab fa-instagram"></i></a>
                </div>
            </div>
        </div>
        <div class="footer-bottom">
            <p>© MedScan. All Rights Reserved. Designed by <a href="#" style="color: #00A9DF;">Tech-Titans</a></p>
        </div>
        </div>
        """, unsafe_allow_html=True)  


query_params = st.query_params.to_dict()
page = query_params.get("page", "home")
role = query_params.get("role", "")

# Navigation logic based on query parameters
if page == "home":
    home_section()
    about_us_section()
    services_section()
    contact_page()
    footer()

elif page == "signin":
    display_login_as_page()  # Show login page with role options (e.g., Nurse, Doctor, Admin)

elif page == "role_selection" and role:
    # Automatically navigate to the corresponding role page
    if role == "nurse":
        st.query_params.from_dict({"page": "nurse"})
        display_nurse_login()
    elif role == "doctor":
        st.query_params.from_dict({"page": "doctor"})
        display_doctor_login()
    elif role == "admin":
        st.query_params.from_dict({"page": "admin"})
        display_admin_login()

# Role-specific pages
elif page == "nurse":
    display_nurse_login()

elif page == "doctor":
    display_doctor_login()

elif page == "admin":
    display_admin_login()

elif page == "admin_choice":
    admin_choice()

else:
    # Default to home if no page is specified
    st.query_params.from_dict({"page": "home"})
    home_section()
    footer()
