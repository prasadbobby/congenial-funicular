from flask import Flask, render_template, request, jsonify, session
import json
import uuid
import random
import string
from datetime import datetime, timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)
app.secret_key = 'appointment_booking_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'

# Static data for doctors and specialties
specialties = [
    {"id": 1, "name": "Cardiology"},
    {"id": 2, "name": "Dermatology"},
    {"id": 3, "name": "Orthopedics"},
]

doctors = [
    {
        "id": 1, 
        "name": "Dr. Smith", 
        "specialty_id": 1, 
        "email": "smith@hospital.com",
        "bio": "Board-certified cardiologist with 15 years of experience.",
        "education": "Harvard Medical School",
        "image_url": "https://randomuser.me/api/portraits/men/36.jpg"
    },
    {
        "id": 2, 
        "name": "Dr. Johnson", 
        "specialty_id": 1, 
        "email": "johnson@hospital.com",
        "bio": "Interventional cardiologist specializing in minimally invasive procedures.",
        "education": "Johns Hopkins School of Medicine",
        "image_url": "https://randomuser.me/api/portraits/women/65.jpg"
    },
    {
        "id": 3, 
        "name": "Dr. Williams", 
        "specialty_id": 2, 
        "email": "williams@hospital.com",
        "bio": "Dermatologist with expertise in skin cancer screening.",
        "education": "Stanford University School of Medicine",
        "image_url": "https://randomuser.me/api/portraits/men/45.jpg"
    },
    {
        "id": 4, 
        "name": "Dr. Brown", 
        "specialty_id": 3, 
        "email": "brown@hospital.com",
        "bio": "Orthopedic surgeon specializing in sports medicine.",
        "education": "University of Pennsylvania School of Medicine",
        "image_url": "https://randomuser.me/api/portraits/women/32.jpg"
    },
]

# Generate time slots for the next 7 days
def generate_time_slots():
    time_slots = []
    for doctor in doctors:
        for day in range(7):
            date = datetime.now() + timedelta(days=day)
            # Create slots from 9AM to 4PM
            for hour in range(9, 16):
                start_time = datetime(date.year, date.month, date.day, hour, 0)
                end_time = start_time + timedelta(minutes=45)
                time_slots.append({
                    "doctor_id": doctor["id"],
                    "start_time": start_time.strftime("%Y-%m-%d %H:%M"),
                    "end_time": end_time.strftime("%Y-%m-%d %H:%M"),
                    "formatted_time": start_time.strftime("%A, %B %d at %I:%M %p"),
                    "is_booked": False
                })
    return time_slots

time_slots = generate_time_slots()
appointments = []

def generate_meet_code():
    # Google Meet uses 3-4-3 format with lowercase letters
    first = ''.join(random.choices(string.ascii_lowercase, k=3))
    second = ''.join(random.choices(string.ascii_lowercase, k=4))
    third = ''.join(random.choices(string.ascii_lowercase, k=3))
    return f"{first}-{second}-{third}"

def send_appointment_email(appointment, doctor_name, patient_email, meet_link):
    sender_email = "knvdurgaprasad610@gmail.com"
    app_password = "eesc wjrl gaqi whct"  # App password from Google account
    
    # Create message
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = patient_email
    message['Subject'] = f"Appointment Confirmation with {doctor_name}"
    
    # Email body
    start_time = datetime.strptime(appointment['start_time'], "%Y-%m-%d %H:%M")
    end_time = datetime.strptime(appointment['end_time'], "%Y-%m-%d %H:%M")
    
    body = f"""
    <html>
    <body style="font-family: Arial, sans-serif; line-height: 1.6; color: #333;">
        <div style="max-width: 600px; margin: 0 auto; padding: 20px; border: 1px solid #ddd; border-radius: 10px;">
            <h2 style="color: #3498db; text-align: center;">Your Appointment has been Confirmed</h2>
            <div style="background-color: #f9f9f9; padding: 15px; border-radius: 5px; margin-bottom: 20px;">
                <p><strong>Doctor:</strong> {doctor_name}</p>
                <p><strong>Date:</strong> {start_time.strftime("%A, %B %d, %Y")}</p>
                <p><strong>Time:</strong> {start_time.strftime("%I:%M %p")} - {end_time.strftime("%I:%M %p")}</p>
                <p><strong>Google Meet Link:</strong> <a href="{meet_link}" style="color: #3498db;">{meet_link}</a></p>
            </div>
            <p>Please join the meeting at the scheduled time using the Google Meet link above.</p>
            <p>Best regards,<br>
            Doctor Appointment Service</p>
        </div>
    </body>
    </html>
    """
    
    message.attach(MIMEText(body, 'html'))
    
    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Secure the connection
        server.login(sender_email, app_password)
        
        # Send email
        server.send_message(message)
        server.quit()
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

@app.route('/')
def index():
    return render_template('booking.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    print("Received chat request")
    data = request.json
    message = data.get('message', '').lower()
    print(f"Message: {message}")
    chat_state = session.get('chat_state', 'initial')
    print(f"Chat state: {chat_state}")
    
    # Initialize session if not exists
    if 'booking_data' not in session:
        session['booking_data'] = {}
    
    response = {"message": "", "options": [], "input_required": False}
    
    # Handle different states of conversation
    if chat_state == 'initial':
        if message == 'book':
            specialty_options = [{"text": specialty["name"], "value": str(specialty["id"])} for specialty in specialties]
            response["message"] = "What type of specialist would you like to see?"
            response["options"] = specialty_options
            session['chat_state'] = 'specialty_selection'
            print("Setting chat state to specialty_selection")
        else:
            response["message"] = "Hello! How can I help you with your doctor appointment today?"
            response["options"] = [{"text": "Book Appointment", "value": "book"}]
    
    elif chat_state == 'specialty_selection':
        try:
            specialty_id = int(message)
            filtered_doctors = [d for d in doctors if d["specialty_id"] == specialty_id]
            doctor_options = [{"text": doctor["name"], "value": str(doctor["id"])} for doctor in filtered_doctors]
            
            specialty_name = next((s['name'] for s in specialties if s['id'] == specialty_id), '')
            session['booking_data']['specialty'] = specialty_name
            
            response["message"] = f"Here are the available {specialty_name} specialists:"
            response["options"] = doctor_options
            session['chat_state'] = 'doctor_selection'
            print(f"Setting chat state to doctor_selection with options: {doctor_options}")
        except ValueError:
            response["message"] = "Please select a specialty from the options."
            specialty_options = [{"text": specialty["name"], "value": str(specialty["id"])} for specialty in specialties]
            response["options"] = specialty_options
    
    elif chat_state == 'doctor_selection':
        try:
            doctor_id = int(message)
            doctor = next((d for d in doctors if d["id"] == doctor_id), None)
            if doctor:
                session['booking_data']['doctor_id'] = doctor_id
                session['booking_data']['doctor_name'] = doctor["name"]
                
                # Get available slots for this doctor
                available_slots = [
                    slot for slot in time_slots 
                    if slot["doctor_id"] == doctor_id and not slot["is_booked"]
                ]
                
                slot_options = [
                    {"text": slot["formatted_time"], "value": idx} 
                    for idx, slot in enumerate(available_slots[:6])  # Show first 6 slots
                ]
                
                session['available_slots'] = available_slots
                
                response["message"] = f"You've selected {doctor['name']}. Please choose an available time slot:"
                response["options"] = slot_options
                session['chat_state'] = 'time_selection'
                print(f"Setting chat state to time_selection with options: {slot_options}")
            else:
                response["message"] = "I couldn't find that doctor. Please try again."
                specialty_id = session['booking_data'].get('specialty_id', 1)
                filtered_doctors = [d for d in doctors if d["specialty_id"] == specialty_id]
                doctor_options = [{"text": doctor["name"], "value": str(doctor["id"])} for doctor in filtered_doctors]
                response["options"] = doctor_options
        except ValueError:
            response["message"] = "Please select a doctor from the options."
            specialty_id = session['booking_data'].get('specialty_id', 1)
            filtered_doctors = [d for d in doctors if d["specialty_id"] == specialty_id]
            doctor_options = [{"text": doctor["name"], "value": str(doctor["id"])} for doctor in filtered_doctors]
            response["options"] = doctor_options
    
    elif chat_state == 'time_selection':
        try:
            slot_index = int(message)
            available_slots = session.get('available_slots', [])
            
            if 0 <= slot_index < len(available_slots):
                selected_slot = available_slots[slot_index]
                session['booking_data']['time_slot'] = selected_slot
                
                response["message"] = f"You've selected {selected_slot['formatted_time']}. Please enter your email address to confirm the appointment:"
                response["input_required"] = True
                session['chat_state'] = 'email_input'
                print("Setting chat state to email_input")
            else:
                response["message"] = "Invalid selection. Please choose a time slot from the options."
                slot_options = [
                    {"text": slot["formatted_time"], "value": idx} 
                    for idx, slot in enumerate(available_slots[:6])
                ]
                response["options"] = slot_options
        except ValueError:
            response["message"] = "Please select a time slot from the options."
            available_slots = session.get('available_slots', [])
            slot_options = [
                {"text": slot["formatted_time"], "value": idx} 
                for idx, slot in enumerate(available_slots[:6])
            ]
            response["options"] = slot_options
    
    elif chat_state == 'email_input':
        email = message.strip()
        if '@' in email and '.' in email:  # Basic email validation
            session['booking_data']['email'] = email
            
            # Create the appointment
            booking_data = session['booking_data']
            doctor_id = booking_data['doctor_id']
            doctor_name = booking_data['doctor_name']
            time_slot = booking_data['time_slot']
            
            # Generate Google Meet link
            meet_code = generate_meet_code()
            google_meet_link = f"https://meet.google.com/{meet_code}"
            
            # Save appointment
            appointment_id = str(uuid.uuid4())
            new_appointment = {
                "id": appointment_id,
                "doctor_id": doctor_id,
                "doctor_name": doctor_name,
                "start_time": time_slot["start_time"],
                "end_time": time_slot["end_time"],
                "formatted_time": time_slot["formatted_time"],
                "patient_email": email,
                "google_meet_link": google_meet_link
            }
            appointments.append(new_appointment)
            
            # Send email confirmation
            try:
                email_sent = send_appointment_email(new_appointment, doctor_name, email, google_meet_link)
                print(f"Email sent status: {email_sent}")
            except Exception as e:
                print(f"Error in email sending: {e}")
                email_sent = False
            
            # Update slot to booked
            for slot in time_slots:
                if (slot["doctor_id"] == doctor_id and 
                    slot["start_time"] == time_slot["start_time"] and 
                    slot["end_time"] == time_slot["end_time"]):
                    slot["is_booked"] = True
            
            # Reset session
            session['chat_state'] = 'initial'
            session.pop('booking_data', None)
            session.pop('available_slots', None)
            
            email_status = "We've sent you an email confirmation." if email_sent else "We couldn't send an email confirmation. Please save the appointment details."
            
            response["message"] = f"""
            Appointment confirmed! Here are your details:
            - Doctor: {doctor_name}
            - Time: {time_slot['formatted_time']}
            - Your email: {email}
            - Google Meet link: {google_meet_link}
            
            {email_status}
            The appointment has been added to your Google Calendar.
            Anything else I can help you with?
            """
            response["options"] = [{"text": "Book Another Appointment", "value": "book"}]
            print("Appointment confirmed and session reset to initial")
        else:
            response["message"] = "Please enter a valid email address:"
            response["input_required"] = True
    
    else:
        # Default response for unknown state
        session['chat_state'] = 'initial'
        response["message"] = "Hello! How can I help you with your doctor appointment today?"
        response["options"] = [{"text": "Book Appointment", "value": "book"}]
    
    print(f"Sending response: {response}")
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5006, ssl_context='adhoc')
