import streamlit as st
from streamlit_option_menu import option_menu
import snowflake.connector
from PIL import Image
import base64
from io import BytesIO
import io

# Function to handle page navigation
def navigate_to(page):
    st.session_state.current_page = page

def st_image_to_base64(img):
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_str = base64.b64encode(buffered.getvalue()).decode()
        return img_str
    
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


        # Convert the image to Base64
    # Navbar with links to scrollable sections and separate pages
    st.markdown("""
            <div class="navbar">
                <a href="#home">Home</a>
                <a href="#abouta">About Us</a>
                <a href="#services">Services</a>
                <a href="#contact">Contact</a>
                <a href="?page=signin">Sign In</a>
                <a href="?page=signup">Sign Up</a>
            </div>
            """, unsafe_allow_html=True)
    st.markdown("<div id='home' class='content'>", unsafe_allow_html=True)

    
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
         <section class="services" id="services">
        
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
    image_path = "images/blurimage.png"  # Update this path as needed
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
   
def login_as(username, password):
    conn_params = {
        'user': 'dheepika13',
        'password': 'Dheepika@13',
        'account': 'sx93925.ap-southeast-1',
        'warehouse': 'COMPUTE_WH',
        'database': 'LOGIN',
        'schema': 'logindetails'
    }
    
    try:
        conn = snowflake.connector.connect(**conn_params)
        cursor = conn.cursor()
        query = """
        SELECT * FROM users WHERE username=%s AND password=%s;
        """
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        return bool(result)
    except Exception as e:
        st.error(f"Error checking credentials: {e}")
        return False
    finally:
        cursor.close()
        conn.close()

# Function to get the user role from the database
def get_user_role(username):
    conn_params = {
        'user': 'dheepika13',
        'password': 'Dheepika@13',
        'account': 'sx93925.ap-southeast-1',
        'warehouse': 'COMPUTE_WH',
        'database': 'LOGIN',
        'schema': 'logindetails'
    }
    
    try:
        conn = snowflake.connector.connect(**conn_params)
        cursor = conn.cursor()
        query = "SELECT role FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()
        return result[0] if result else None
    except Exception as e:
        st.error(f"Error fetching user role: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

# Function to navigate to a specific page
def navigate_to(page):
    st.session_state.current_page = page

# Function to handle login
def login(username, password):
    if login_as(username, password):
        user_role = get_user_role(username)
        
        if user_role:
            if user_role == 'Nurse':
                navigate_to('nurse_login')
            elif user_role == 'Doctor':
                navigate_to('doctor_login')
            elif user_role == 'Admin':
                navigate_to('admin_login')
            else:
                st.error("Role not recognized!")
        else:
            st.error("User not found!")
    else:
        st.error("Invalid username or password!")

# Streamlit interface for the login page
def login_page():
    st.title("Login")
    
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    if st.button("Login"):
        login(username, password)

# Example login pages for different roles
def nurse_login_page():
    st.title("Nurse Login")

def doctor_login_page():
    st.title("Doctor Login")

def admin_login_page():
    st.title("Admin Login")

# Page navigation based on session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'login'

if st.session_state.current_page == 'login':
    login_page()
elif st.session_state.current_page == 'nurse_login':
    nurse_login_page()
elif st.session_state.current_page == 'doctor_login':
    doctor_login_page()
elif st.session_state.current_page == 'admin_login':
    admin_login_page()
    
        
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


# Get the current page from query parameters using st.query_params
page = st.query_params.get("page", "home")

# Routing logic to load the appropriate page
if page == "home":
    home_section()
    about_us_section()
    services_section()
    contact_page()
    footer()
elif page == "signin":
    login_as()
elif page == "signup":
    signup_page()
elif page == "forgot_password":
    forgot_password_page()
elif page == "reset_password":
    reset_password_page()
else:
    home_section()  # Default to home if no page is specified
    footer()
    
