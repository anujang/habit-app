
# Habitual – A Habit & Reminder Tracker (React + Python + AWS)

A full-stack habit and reminder tracker built with:

- React + Tailwind CSS (frontend)
- Python (serverless backend via AWS Lambda)
- AWS Cognito for authentication
- AWS DynamoDB for data storage
- AWS SNS/SES for optional SMS or email reminders
- PWA support (installable on mobile)
- Hosted entirely on AWS Free Tier (S3 + CloudFront + Lambda + DynamoDB)

---

## Features

- User login and signup (Cognito)
- Create habits with custom frequency
- View and check off completed habits daily
- See history of completed tasks
- Optional SMS/email reminders
- Installable as a Progressive Web App (PWA)
- (Optional future step: Publish as Android app via TWA)

---

## Tech Stack

| Layer       | Tech                    |
|-------------|-------------------------|
| Frontend    | React, Tailwind CSS, Vite, PWA Plugin |
| Backend     | Python (AWS Lambda + API Gateway) |
| Database    | DynamoDB                |
| Auth        | AWS Cognito             |
| Notifications | AWS SNS or SES        |
| Hosting     | S3 + CloudFront         |
| Dev Tools   | GitHub Actions, Serverless Framework |

---

## Getting Started (Dev Plan)

1. `npm create vite@latest habitual` → Setup frontend
2. Set up Tailwind + React Router + auth UI
3. Configure Cognito for signup/login
4. Write Python Lambda for habit CRUD
5. Use API Gateway to expose endpoints
6. Store data in DynamoDB (users, habits, logs)
7. Add reminder Lambda to trigger SNS/SES
8. Configure PWA manifest + service worker
9. Deploy frontend to S3 + backend via Serverless

---

## Status
Currently in development  
First milestone: core CRUD + auth  
Future milestone: PWA + reminder notifications

---

## Credits

Made by Anujan — to stay sharp & build something useful ❤️
