TWO FINAL FEATURES FOR GOALPATH AI

FEATURE 1: FILE STORAGE & LIBRARY

GoalPath already has file upload in AI Tutor. Extend this to include persistent storage.

REQUIREMENTS:

1. SAVE UPLOADED FILES
- When user uploads file (image, PDF, doc) in AI Tutor, give option to save it
- Checkbox: "💾 Save to My Files" (optional, not forced)
- If checked, store file in database or file system
- Track: filename, upload_date, file_type, file_size, goal_plan_id (if applicable)
2. FILE LIBRARY
- Add new section: "📁 My Files" (in sidebar or main menu)
- Display all saved files in a list/grid:
  * File name
  * Upload date
  * File type (image/PDF/doc)
  * Size
  * Associated goal (if any)
- Search/filter files by name or date
3. FILE RETRIEVAL
- Click file to view/download
- For images: Display inline
- For PDFs: Show in viewer or download
- For docs: Download option
- Delete button per file
4. STORAGE MANAGEMENT
- Show total storage used
- Optional: Set storage limit (e.g., 100MB max)
- Warn if approaching limit
5. ORGANIZATION (OPTIONAL)
- Tag files (e.g., "profile", "reference", "notes")
- Associate file with specific goal plan
- Simple folder structure

IMPLEMENTATION:

- Store files in: /uploaded_files/ directory OR database BLOB
- Track metadata in new database table: user_files
- Use secure filename handling (prevent path traversal)
- Limit file types: images (png, jpg), PDFs, docs (txt, docx)
- Max file size: 10MB per file

FEATURE 2: MOBILE SECURITY IMPROVEMENTS

Add security tweaks specifically for mobile use and public WiFi exposure.

REQUIREMENTS:

1. CONFIGURABLE SESSION TIMEOUT
- Add to .env: SESSION_TIMEOUT_HOURS (default: 4 for mobile)
- Cookie expires after X hours of initial login
- Display "Session expires in: X hours" on screen
- When expired: User must login again
2. AUTO-LOGOUT ON INACTIVITY
- Track last activity timestamp
- If no interaction for 30 minutes → auto logout
- Show warning at 25 minutes: "Session will expire in 5 minutes"
- Reset timer on any user action
3. ENHANCED PASSWORD VALIDATION
- When setting APP_PASSWORD, validate strength:
  * Minimum 12 characters
  * At least 1 uppercase
  * At least 1 lowercase  
  * At least 1 number
  * At least 1 special character
- Show password strength indicator when logging in
- Reject weak passwords with helpful message
4. HTTPS ENFORCEMENT
- Add check: If deployed and not using HTTPS, show warning
- Redirect HTTP to HTTPS if possible
- Display security badge: "🔒 Secure Connection" when HTTPS active
5. REMEMBER ME OPTION (OPTIONAL)
- Add "Remember Me" checkbox on login
- If unchecked: Session timeout = 4 hours
- If checked: Session timeout = 24 hours (only for trusted devices)
- Default: Unchecked for security
6. SECURITY NOTIFICATIONS
- On login: "Last login: [date/time]" (helps detect unauthorized access)
- On logout: "You have been logged out. Session ended."
- On session expiry: "Session expired for security. Please login again."
7. FILE UPLOAD SECURITY
- Validate file types (whitelist: png, jpg, jpeg, pdf, txt, docx)
- Scan file size (reject > 10MB)
- Sanitize filenames (remove special characters, prevent ../attacks)
- Store with unique IDs (don't expose original names in URLs)

IMPLEMENTATION NOTES:

- Use environment variables for timeouts (configurable)
- Store session activity in streamlit session_state
- Use secure cookie flags (HttpOnly, Secure, SameSite)
- Add middleware for inactivity checking
- Password validation function in utils/auth.py

GOAL:
Make GoalPath AI secure enough for mobile use on public WiFi while keeping it simple and not over-engineering.

These are the FINAL two features. After this, GoalPath AI is complete.
