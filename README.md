# 🏫 College Event Management System

A complete, production-ready full-stack web application for managing college events, registrations, and user roles. Built with modern technologies and best practices.

---

## 🚀 Features

### Core Functionality
* 🔐 **JWT-based Authentication** - Secure login/signup system
* 👨‍💼 **Role-Based Access Control** - Admin and Student/User roles
* 🎯 **Event Management** - Complete CRUD operations for events
* 📝 **Event Registration** - Students can register for events
* 📈 **Dashboard Analytics** - Real-time statistics for admins
* 🔍 **Search & Filter** - Find events easily
* 🖼️ **Image Upload** - Cloudinary integration for event images
* 🔔 **In-App Notifications** - Success alerts using Sonner

### Admin Capabilities
* Create, edit, and delete events
* View all registrations
* Manage users and events
* Dashboard with key metrics (total events, users, registrations)

### Student/User Capabilities
* Browse and search events
* Register for events
* View registered events (upcoming and past)
* Personal dashboard

---

## 🛠️ Tech Stack

### Frontend
* **Framework**: React 19
* **Styling**: Tailwind CSS with custom design system
* **UI Components**: Shadcn/UI (Radix UI primitives)
* **Routing**: React Router DOM v7
* **HTTP Client**: Axios
* **Notifications**: Sonner
* **Icons**: Lucide React
* **Date Handling**: date-fns

### Backend
* **Framework**: FastAPI (Python)
* **Database**: MongoDB with Motor (async driver)
* **Authentication**: JWT tokens with python-jose
* **Password Hashing**: Passlib with bcrypt
* **Image Storage**: Cloudinary
* **CORS**: Enabled for cross-origin requests

---

## 📚 Project Structure

```
college-event-management-system/
├── backend/                 # FastAPI backend
│   ├── models/              # Pydantic models
│   │   ├── user.py
│   │   ├── event.py
│   │   └── registration.py
│   ├── routes/              # API endpoints
│   │   ├── auth.py
│   │   ├── events.py
│   │   ├── registrations.py
│   │   ├── admin.py
│   │   └── cloudinary.py
│   ├── middleware/          # Auth middleware
│   │   └── auth.py
│   ├── database.py          # MongoDB connection
│   ├── server.py            # Main FastAPI app
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # Environment variables
│
├── frontend/                # React frontend
│   ├── src/
│   │   ├── components/      # Reusable components
│   │   │   ├── ui/          # Shadcn UI components
│   │   │   ├── Navbar.js
│   │   │   ├── Footer.js
│   │   │   ├── EventCard.js
│   │   │   └── ProtectedRoute.js
│   │   ├── context/         # React Context
│   │   │   └── AuthContext.js
│   │   ├── pages/           # Page components
│   │   │   ├── Login.js
│   │   │   ├── Signup.js
│   │   │   ├── Events.js
│   │   │   ├── UserDashboard.js
│   │   │   ├── AdminDashboard.js
│   │   │   └── EventForm.js
│   │   ├── services/        # API services
│   │   │   └── api.js
│   │   ├── App.js           # Main app component
│   │   ├── App.css
│   │   └── index.css        # Global styles
│   ├── public/
│   ├── package.json         # Node dependencies
│   └── .env                 # Environment variables
│
├── README.md
└── .gitignore
```

---

## ⚡ Installation & Setup

### Prerequisites
* Python 3.11+
* Node.js 18+
* MongoDB (local or Atlas)
* Cloudinary account (for image uploads)

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/vikrantproject/college-event-management-system.git
cd college-event-management-system
```

### 2️⃣ Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file (see Backend Environment Variables below)
cp .env.example .env
# Edit .env with your actual values

# Run the server
uvicorn server:app --host 0.0.0.0 --port 8001 --reload
```

**Backend Environment Variables** (`.env`)
```env
MONGO_URL="mongodb://localhost:27017"
DB_NAME="college_events_db"
CORS_ORIGINS="*"
JWT_SECRET="your-secret-key-change-in-production"
CLOUDINARY_CLOUD_NAME="your_cloud_name"
CLOUDINARY_API_KEY="your_api_key"
CLOUDINARY_API_SECRET="your_api_secret"
```

### 3️⃣ Frontend Setup

```bash
cd ../frontend

# Install dependencies
yarn install  # or npm install

# Create .env file (see Frontend Environment Variables below)
cp .env.example .env
# Edit .env with your backend URL

# Run the development server
yarn start  # or npm start
```

**Frontend Environment Variables** (`.env`)
```env
REACT_APP_BACKEND_URL=http://localhost:8001
```

### 4️⃣ Get Cloudinary Credentials

1. Go to [https://cloudinary.com](https://cloudinary.com)
2. Sign up or log in
3. Go to Dashboard
4. Copy your:
   - **Cloud Name**
   - **API Key**
   - **API Secret**
5. Add them to `backend/.env`

---

## 🖥️ Usage

### Access the Application

* **Frontend**: http://localhost:3000
* **Backend API**: http://localhost:8001
* **API Docs**: http://localhost:8001/docs (FastAPI Swagger UI)

### Create Admin Account

1. Go to http://localhost:3000/signup
2. Fill in details
3. Select **"Admin"** as Account Type
4. Click "Create Account"

### Create Student Account

1. Go to http://localhost:3000/signup
2. Fill in details
3. Select **"Student/User"** as Account Type
4. Click "Create Account"

### Admin Workflow

1. Login as admin
2. Go to Admin Dashboard
3. Click "Create Event"
4. Fill event details and upload image
5. Submit to create event
6. View all events in the management table
7. Edit or delete events as needed

### Student Workflow

1. Login as student
2. Browse events on Events page
3. Use search to find specific events
4. Click "Register Now" on event cards
5. View registered events in "My Dashboard"

---

## 🔌 API Endpoints

### Authentication
* `POST /api/auth/signup` - Create new account
* `POST /api/auth/login` - Login to account

### Events
* `GET /api/events` - Get all events (with search & pagination)
* `GET /api/events/{id}` - Get event by ID
* `POST /api/events` - Create event (admin only)
* `PUT /api/events/{id}` - Update event (admin only)
* `DELETE /api/events/{id}` - Delete event (admin only)

### Registrations
* `POST /api/registrations` - Register for event
* `GET /api/registrations/user/{user_id}` - Get user's registrations
* `DELETE /api/registrations/{id}` - Cancel registration

### Admin
* `GET /api/admin/stats` - Get dashboard statistics
* `GET /api/admin/registrations` - Get all registrations

### Cloudinary
* `GET /api/cloudinary/signature` - Get signed upload parameters

---

## 🎨 Design System

The application follows a **Swiss & High-Contrast** design archetype:

* **Primary Color**: International Klein Blue (#002FA7)
* **Typography**: Work Sans (headings), IBM Plex Sans (body)
* **Layout**: Clean, structured dashboard with crisp borders
* **Components**: Shadcn/UI for consistency and accessibility
* **Interactions**: Smooth transitions and hover states
* **Responsive**: Mobile-first design approach

---

## 🔒 Security Features

* JWT token-based authentication
* Password hashing with bcrypt
* Role-based access control
* Protected API routes
* Signed Cloudinary uploads
* CORS configuration
* Environment variable protection

---

## 📦 Database Schema

### Users Collection
```json
{
  "id": "uuid",
  "name": "string",
  "email": "string",
  "hashed_password": "string",
  "role": "admin | user",
  "created_at": "ISO datetime"
}
```

### Events Collection
```json
{
  "id": "uuid",
  "title": "string",
  "description": "string",
  "date": "string",
  "location": "string",
  "image_url": "string (optional)",
  "created_by": "user_id",
  "created_at": "ISO datetime"
}
```

### Registrations Collection
```json
{
  "id": "uuid",
  "user_id": "string",
  "event_id": "string",
  "registered_at": "ISO datetime"
}
```

---

## 🚀 Deployment

### Backend Deployment (e.g., Railway, Render)

1. Push code to GitHub
2. Connect your repo to the platform
3. Set environment variables
4. Deploy backend service

### Frontend Deployment (e.g., Netlify, Vercel)

1. Build the project: `yarn build`
2. Connect your repo to the platform
3. Set `REACT_APP_BACKEND_URL` to your deployed backend URL
4. Deploy

### MongoDB Atlas (Cloud Database)

1. Create account at [https://mongodb.com/atlas](https://mongodb.com/atlas)
2. Create cluster
3. Get connection string
4. Update `MONGO_URL` in backend `.env`

---

## 🧑‍💻 Development

### Code Quality

* Well-commented code
* Modular architecture
* Reusable components
* Error handling
* Type safety with Pydantic

### Best Practices Followed

* Environment variables for configuration
* JWT for stateless authentication
* Async/await for database operations
* Component composition in React
* Custom hooks for reusability
* Protected routes
* Responsive design
* Accessibility features

---

---

## ✨ Why Choose This System?

### Advantages Over Alternatives

1. **Modern Tech Stack** - Built with cutting-edge technologies (FastAPI, React 19)
2. **Production-Ready** - Complete authentication, authorization, and error handling
3. **Scalable Architecture** - Modular design allows easy feature additions
4. **Beautiful UI** - Custom design system with professional aesthetics
5. **Real Cloud Integration** - Cloudinary for reliable image hosting
6. **Role-Based Access** - Proper separation of admin and user capabilities
7. **Search & Filter** - Users can easily find relevant events
8. **Responsive Design** - Works perfectly on mobile, tablet, and desktop
9. **Type Safety** - Pydantic models ensure data validation
10. **Developer Experience** - Clean code, good documentation, easy to maintain

### Perfect For

* Final year college projects
* Portfolio showcase
* Learning full-stack development
* Starting point for commercial systems
* Interview preparation
* Educational institutions

### Future Enhancement Ideas

* Email notifications (SendGrid/Resend integration)
* Event categories and tags
* Event capacity limits
* QR code for event check-ins
* Calendar view of events
* Social sharing features
* Rating and reviews system
* Payment integration for paid events
* Analytics dashboard with charts
* Export registrations to CSV/Excel

---

## 📝 License

MIT License - Feel free to use this project for learning, personal use, or commercial applications.

---

## 👤 Author

**Vikrant**

Built as a complete, production-ready college project demonstrating modern full-stack development practices.

---

## 🙏 Acknowledgments

* FastAPI for the excellent Python framework
* React team for the powerful UI library
* Shadcn for beautiful UI components
* Cloudinary for image hosting
* MongoDB for flexible database
* All open-source contributors

---

## 📞 Support

For questions or issues:
* Open an issue on GitHub
* Email: vikrantranahome@gmail.com

---

**Made with ❤️ using FastAPI, React, and MongoDB**
