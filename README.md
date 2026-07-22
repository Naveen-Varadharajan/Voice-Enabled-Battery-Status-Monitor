# 🔋 Voice-Enabled Battery Status Monitor

A simple **console-based Python application** that retrieves your system's battery information and announces it using offline text-to-speech. The application displays the current battery percentage and charging status in the terminal while audibly speaking the battery status.

This project demonstrates the use of Python for **system monitoring**, **automation**, and **accessibility**.

## ✨ Features

- 🔋 Retrieves the current battery percentage
- ⚡ Detects whether the battery is charging or discharging
- 🗣️ Announces battery status using offline text-to-speech
- 💻 Displays battery information in the console
- 🌐 Works without an internet connection

## 🛠️ Technologies Used

- **Python**
- **psutil** – Retrieves real-time battery information
- **pyttsx3** – Offline text-to-speech engine


## ▶️ Usage

Run the application:

```bash
python battery_status.py
```

The application will:

- Display the current battery percentage in the console.
- Show whether the system is charging or on battery power.
- Announce the battery status using voice output.

## 📌 Sample Output

```text
Battery Percentage: 78%
Status: Charging

Speaking...
"Battery is at 78 percent and is currently charging."
```

## 📚 What I Learned

- Accessing system battery information with `psutil`
- Implementing offline text-to-speech using `pyttsx3`
- Building console-based automation tools in Python
- Working with system utilities and accessibility features

## 🚀 Future Enhancements

- 🔔 Add desktop notifications
- 🔄 Run automatically in the background on startup
- 📊 Display battery history and usage statistics
- 🤖 AI-based battery usage prediction

## ⭐ Acknowledgement

This project was built as part of my journey in learning **Python system utilities, automation, and accessibility-focused applications**.


---

⭐ If you found this project helpful, consider giving it a star on GitHub!
