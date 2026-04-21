╔══════════════════════════════════════════════════════════════════════════════╗
║                    DOCUMENTATION PDF - INSTRUCTIONS                          ║
╚══════════════════════════════════════════════════════════════════════════════╝

📄 HOW TO ADD YOUR DOCUMENTATION PDF
═══════════════════════════════════════════════════════════════════════════════

1. Place your PDF file in this folder
2. Rename it to: documentation.pdf
3. The button on the home page will automatically link to it

📁 FILE LOCATION
═══════════════════════════════════════════════════════════════════════════════

Put your PDF here:
    sepik_fresh/static/docs/documentation.pdf

🔗 BUTTON LOCATION
═══════════════════════════════════════════════════════════════════════════════

The green "View Documentation" button appears on:
    Home page (http://localhost:5000/)
    Below "Get Started" and "Learn More" buttons

🎨 BUTTON STYLE
═══════════════════════════════════════════════════════════════════════════════

✓ Green background (#2a7a30)
✓ White text
✓ PDF icon included
✓ Opens in new tab
✓ Hover effect (darker green)
✓ Responsive (mobile-friendly)

📝 TO CHANGE PDF NAME
═══════════════════════════════════════════════════════════════════════════════

If you want to use a different filename:

1. Open: sepik_fresh/templates/home.html
2. Find: href="/static/docs/documentation.pdf"
3. Change to: href="/static/docs/YOUR_FILENAME.pdf"

💡 TIPS
═══════════════════════════════════════════════════════════════════════════════

• Keep PDF filename simple (no spaces)
• Recommended size: Under 10MB
• Test the link after adding PDF
• PDF opens in new browser tab

✅ VERIFY IT WORKS
═══════════════════════════════════════════════════════════════════════════════

1. Add your PDF to this folder
2. Start application: python app.py
3. Open: http://localhost:5000
4. Click "View Documentation" button
5. PDF should open in new tab

═══════════════════════════════════════════════════════════════════════════════
