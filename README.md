# smart_log_analyzer
A Python-based log analyzer that processes user activity logs to extract insights like user activity count, error tracking, and session anomalies.

(Python)
--

## 📌 Overview
This project analyzes user activity logs and extracts useful insights such as:
- Total actions per user
- Most active users
- Error count
- Users with incomplete sessions

## 🛠️ Technologies Used
- Python 3

## 📂 Input Format
Each log entry:
<timestamp> <user_id> <action>

Example:
2026-03-18T10:15:30 user1 LOGIN

## ▶️ How to Run
1. Create a log file (log.txt)
2. Run:
python main.py

## 📊 Output
- Action count per user
- Most active user
- Error count
- Users without logout

## 💡 Future Improvements
- Add GUI dashboard
- Real-time log streaming
